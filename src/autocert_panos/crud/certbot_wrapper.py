"""


certbot certonly --dns-cloudflare --dns-cloudflare-credentials $CLOUDFLARE_CREDS -d *.$FQDN -n --agree-tos --no-eff-email --quiet
"""

import subprocess
from pydantic_settings import BaseSettings


class CertbotWrapper:
    def __init__(self, certbot_cfg: BaseSettings) -> None:
        self.certbot_args = [
            "certbot",
            "certonly",
            "--authenticator",
            "dns-domeneshop",
            "--dns-domeneshop-credentials",
            certbot_cfg,
            "--dns-domeneshop-propagation-seconds",
            certbot_cfg.DNS_SLEEP_TIME,
            "-d",
            certbot_cfg.DOMAIN,
            "--quiet",
            "--agree-tos",
            "--config-dir",
            certbot_cfg.CONFIG_DIR,
            "--work-dir",
            certbot_cfg.WORK_DIR,
            "--logs-dir",
            certbot_cfg.LOGS_DIR,
            "--dry-run",
        ]

    def run_certbot(self):
        self.certbot = subprocess.Popen(args=self.certbot_args)
