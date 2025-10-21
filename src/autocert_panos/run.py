from crud.certbot_wrapper import CertbotWrapper
from models.config import Panos, CertBot

certbot = CertbotWrapper(certbot_cfg=CertBot(), domeneshop_cfg=Pa)

certbot.run_certbot()
