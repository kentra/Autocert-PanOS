from panos import firewall, device
from models.config import Panos
import httpx
import xmltodict
from models.palo_xml_api import Certficate
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class PanosTools:
    def __init__(self, panos_cfg: BaseSettings, certbot_cfg: BaseSettings) -> None:
        self.hostname = panos_cfg.HOST
        self.api_key = panos_cfg.API_KEY
        self.certbot_cfg = certbot_cfg
        self.fw = firewall.Firewall(hostname=self.hostname, api_key=self.api_key)

    def __xml_to_pydantic(self, xml: str) -> Certficate:
        d = xmltodict.parse(xml)
        # time = d["response"]["result"]["entry"]["not-valid-after"]["@time"]
        return Certficate(**d)

    def upload_certificate(self) -> httpx.Response:

        with open(
            f"{self.certbot_cfg.PFX_DIR}/{self.certbot_cfg.PFX_NAME}", "rb"
        ) as file:
            certificate = {
                "file": ("LetsEncrptPKCS12.pfx", file, "application/x-pkcs12")
            }

            with httpx.Client(verify=False) as client:
                url = f"https://{self.hostname}/api"
                params = {
                    "type": "import",
                    "category": "certificate",
                    "certificate-name": self.certbot_cfg.PFX_NAME,
                    "format": "pkcs12",
                    "passphrase": self.certbot_cfg.PFX_PW.get_secret_value(),
                    "key": self.api_key,
                }

                response = client.post(url, params=params, files=certificate)
        return response

    def get_certificate(self, cert_name) -> Certficate:
        params = {
            "type": "config",
            "action": "get",
            "xpath": "/config/shared/certificate/entry[@name='kentra.org']",
            "key": self.api_key,
        }
        # xmltodict.parse(a.content)

        with httpx.Client(verify=False) as client:
            url = f"https://{self.hostname}/api"
            response = client.get(url, params=params)

        if response.status_code == 200:
            return self.__xml_to_pydantic(xml=response.content)

    def commit_config(self) -> None:
        self.fw.commit()


if __name__ == "__main__":
    config = Panos()
    fw = firewall.Firewall(
        hostname=config.HOST, api_key=config.API_KEY.get_secret_value()
    )
    dev = device.CertificateProfile
    # fw.commit()
