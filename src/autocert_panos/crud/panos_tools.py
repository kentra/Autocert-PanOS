from panos import firewall, network, device
from app.models.config import Panos
import httpx


# /config/shared/ssl-tls-service-profile/entry[@name='$TLS_PROFILE']"


class PanosTools:
    def __init__(self, hostname: str, api_key: str):
        self.hostname = hostname
        self.api_key = api_key
        self.fw = firewall.Firewall(hostname=hostname, api_key=api_key)

    def upload_certificate(
        self, cert_name: str, cert_path: str, cert_password: str
    ) -> httpx.Response:

        with open(cert_path, "rb") as file:
            certificate = {
                "file": ("LetsEncrptPKCS12.pfx", file, "application/x-pkcs12")
            }

            with httpx.Client(verify=False) as client:
                url = f"https://{self.hostname}/api"
                params = {
                    "type": "import",
                    "category": "certificate",
                    "certificate-name": cert_name,
                    "format": "pkcs12",
                    "passphrase": cert_password,
                    "key": self.api_key,
                }

                response = client.post(url, params=params, files=certificate)

        return response

    def commit_config(self) -> None:
        self.fw.commit()


if __name__ == "__main__":
    config = Panos()
    fw = firewall.Firewall(
        hostname=config.MGMT, api_key=config.API_KEY.get_secret_value()
    )
    dev = device.CertificateProfile
    # fw.commit()
