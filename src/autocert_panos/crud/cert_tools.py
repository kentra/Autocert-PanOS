from cryptography.hazmat.primitives.serialization import (
    pkcs12,
    BestAvailableEncryption,
)
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography import x509
import os
from pydantic_settings import BaseSettings
from OpenSSL import crypto
from datetime import datetime


class CertTools:
    def __init__(self, certbot_cfg: BaseSettings) -> None:
        self.private_key_path = (
            f"{certbot_cfg.CONFIG_DIR}/live/{certbot_cfg.CERT_NAME}/privkey.pem"
        )
        self.cert_path = (
            f"{certbot_cfg.CONFIG_DIR}/live/{certbot_cfg.CERT_NAME}/cert.pem"
        )
        self.ca_chain_path = (
            f"{certbot_cfg.CONFIG_DIR}/live/{certbot_cfg.CERT_NAME}/fullchain.pem"
        )
        self.pfx_path = certbot_cfg.PFX_DIR
        self.pfx_name = certbot_cfg.PFX_NAME
        self.pfx_pw = certbot_cfg.PFX_PW.get_secret_value()

    def convert_pem_to_pkcs12(self) -> None:
        """
        Creates a PKCS#12 (.pfx) file equivalent to:
        openssl pkcs12 -export -out out.pfx -inkey privkey.pem -in cert.pem -certfile cert.pem -passout pass:<password>

        :param privkey_path: Path to the private key PEM file
        :param cert_path: Path to the certificate PEM file
        :param ca_chain_path: Path to CA cert bundle (can be same as cert_path if no chain)
        :param output_path: Path to write the .pfx file
        :param password: Export password (string)
        """

        # Load private key
        with open(self.private_key_path, "rb") as f:
            private_key = load_pem_private_key(f.read(), password=None)

        # Load certificate
        with open(self.cert_path, "rb") as f:
            cert = x509.load_pem_x509_certificate(f.read())

        # Load CA chain (can be empty or same as cert)
        additional_certs = []
        if self.ca_chain_path:
            with open(self.ca_chain_path, "rb") as f:
                for cert_data in f.read().split(b"-----END CERTIFICATE-----"):
                    cert_data = cert_data.strip()
                    if cert_data:
                        cert_data += b"\n-----END CERTIFICATE-----\n"
                        additional_certs.append(
                            x509.load_pem_x509_certificate(cert_data)
                        )

        # Serialize into PKCS#12
        pfx_data = pkcs12.serialize_key_and_certificates(
            name=bytes(self.pfx_name, encoding="utf-8"),  # Friendly name
            key=private_key,
            cert=cert,
            cas=additional_certs if additional_certs else None,
            encryption_algorithm=BestAvailableEncryption(self.pfx_pw.encode("utf-8")),
        )

        # Write to file
        with open(f"{self.pfx_path}/{self.pfx_name}", "wb") as f:
            f.write(pfx_data)

    def get_cert_expiry_from_file(self):
        with open(self.cert_path, "rb") as f:
            cert_data = f.read()

        cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_data)
        expiry_bytes = cert.get_notAfter()  # e.g. b'20251231235959Z'
        expiry_str = expiry_bytes.decode("ascii")
        expiry_date = datetime.strptime(expiry_str, "%Y%m%d%H%M%SZ")
        return expiry_date

    # cert_file = "mycert.pem"
    # expiry = get_cert_expiry_from_file(cert_file)
    # print(f"Certificate expires on: {expiry}")
    # print(f"Days remaining: {(expiry - datetime.utcnow()).days}")
