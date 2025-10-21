from crud.certbot_wrapper import CertbotWrapper
from crud.panos_tools import PanosTools
from crud.cert_tools import CertTools
from models.config import CertBot, Panos


certbot_cfg = CertBot()
panos_cfg = Panos()


certbotWrapper = CertbotWrapper(certbot_cfg)

# Run Certbot
wrapper.run_certbot(dry_run=True)

#
