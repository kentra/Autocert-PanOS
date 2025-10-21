from cryptography.hazmat.primitives.serialization import (
    pkcs12,
    BestAvailableEncryption,
)
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography import x509
import os


class CertTools:
    def __init__(self) -> None:
        None

    def pem_to_pkcs12(
        private_key_path: str,
        cert_path: str,
        ca_chain_path: str,
        output_path: str,
        password: str = os.urandom(16).hex(),
    ) -> None:
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
        with open(private_key_path, "rb") as f:
            private_key = load_pem_private_key(f.read(), password=None)

        # Load certificate
        with open(cert_path, "rb") as f:
            cert = x509.load_pem_x509_certificate(f.read())

        # Load CA chain (can be empty or same as cert)
        additional_certs = []
        if ca_chain_path:
            with open(ca_chain_path, "rb") as f:
                for cert_data in f.read().split(b"-----END CERTIFICATE-----"):
                    cert_data = cert_data.strip()
                    if cert_data:
                        cert_data += b"\n-----END CERTIFICATE-----\n"
                        additional_certs.append(
                            x509.load_pem_x509_certificate(cert_data)
                        )

        # Serialize into PKCS#12
        pfx_data = pkcs12.serialize_key_and_certificates(
            name=b"letsencrypt",  # Friendly name
            key=private_key,
            cert=cert,
            cas=additional_certs if additional_certs else None,
            encryption_algorithm=BestAvailableEncryption(password.encode("utf-8")),
        )

        # Write to file
        with open(output_path, "wb") as f:
            f.write(pfx_data)
