from panos import firewall, device
from models.config import Panos
import httpx
import xmltodict
from models.palo_xml_api import Certficate


class PanosTools:
    def __init__(self, hostname: str, api_key: str):
        self.hostname = hostname
        self.api_key = api_key
        self.fw = firewall.Firewall(hostname=hostname, api_key=api_key)

    def __xml_to_pydantic(self, xml: str) -> dict:
        d = xmltodict.parse(xml)
        # time = d["response"]["result"]["entry"]["not-valid-after"]["@time"]
        return Certficate(**d)

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

    def find_cert(self, cert_name):
        """
                /config/shared/certificate/entry[@name='kentra.org']
                /api/?type=config&action=get&xpath=/config/readonly
        https://palo.kentra.org/api/?REST_API_TOKEN=1479228100&type=config&action=get&xpath=%2Fconfig%2Fshared%2Fcertificate%2Fentry%5B%40name%3D%27kentra.org%27%5D
        https://10.217.3.2/api?type=config&action=get&xpath=%2Fconfig%2Fshared%2Fcertificate%2Fentry%5B%40name%3D%27kentra.org%27%5D&key=%2A%2A%2A%2A%2A%2A%2A%2A%2A%2A
                Args:
                    cert_name (_type_): _description_

                Returns:
                    _type_: _description_
        """
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
            return self.__fix_xml_cert(xml=response.content)

    def commit_config(self) -> None:
        self.fw.commit()


if __name__ == "__main__":
    config = Panos()
    fw = firewall.Firewall(
        hostname=config.MGMT, api_key=config.API_KEY.get_secret_value()
    )
    dev = device.CertificateProfile
    # fw.commit()
