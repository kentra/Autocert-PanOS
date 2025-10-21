from crud.certbot_wrapper import CertbotWrapper
from crud.panos_tools import PanosTools
from crud.cert_tools import CertTools
from models.config import CertBot, Panos
from log_handler import logger
from models.palo_xml_api import Certficate

logger.info("🚀 Getting things ready for takeoff!")
certbot_cfg = CertBot()
panos_cfg = Panos()

# Initialize the tools
certbotWrapper = CertbotWrapper(certbot_cfg=certbot_cfg)
certTools = CertTools(certbot_cfg=certbot_cfg)
panosTools = PanosTools(panos_cfg=panos_cfg, certbot_cfg=certbot_cfg)

# Run Certbot
logger.info("🌍 Hang on! Searching for certificate..(tqdm?)")
certbotWrapper.run_certbot(dry_run=False)
logger.success(
    "🎉 WOW! We are still on! Awesome! Well, let's compare the timestamp on both certs."
)
paloCert = panosTools.get_certificate(cert_name=certbot_cfg.CERT_NAME)
if type(paloCert) is Certficate:
    # paloResp = paloCert.response.result.entry.not_valid_after.text
    logger.info(
        f"❤️‍🔥 Palo's certificate expires {paloCert.response.result.entry.not_valid_after.text} (expiry epoch: {paloCert.response.result.entry.expiry_epoch.text})"
    )
else:
    logger.error("Well shit.. Something went wrong..")
logger.info("😎 Lets test the converting job PAM to PKCS12")
certTools.convert_pem_to_pkcs12()

logger.info(
    "😬 this is a little awkward, but I don't have a way to compare the to certs yet.."
)

logger.info("🤷‍♂️ Oh well, lets try uploading to Palo anyway!")
panosTools.upload_certificate()
