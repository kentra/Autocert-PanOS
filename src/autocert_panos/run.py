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
# logger.info("🌍 Hang on! Searching for certificate..(tqdm?)")
# certbotResult = certbotWrapper.run_certbot(dry_run=True)

# if certbotResult == "Certificate not yet due for renewal":
#     logger.stop(f"⚠️ {certbotResult}")

# Fetch old cert from Palo
paloCert = panosTools.get_certificate(cert_name=certbot_cfg.CERT_NAME)
if type(paloCert) is Certficate:
    # paloResp = paloCert.response.result.entry.not_valid_after.text
    logger.info(
        f"❤️‍🔥 Palo's certificate expires {paloCert.response.result.entry.not_valid_after.text} (expiry epoch: {paloCert.response.result.entry.expiry_epoch.text})"
    )

# Check local cert to compare
checkLocalCert = certTools.get_cert_expiry_from_file()
logger.debug(checkLocalCert)

# logger.info("😎 Lets test the converting job PAM to PKCS12")
# certTools.convert_pem_to_pkcs12()
# panosTools.upload_certificate()
