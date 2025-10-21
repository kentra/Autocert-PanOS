import subprocess
import shlex
import logging
from typing import List
from pydantic_settings import BaseSettings
from log_handler import logger


logger = logging.getLogger(__name__)


class CertbotWrapper:
    def __init__(self, certbot_cfg: BaseSettings) -> None:
        # Config from Pydantic model
        self.cfg = certbot_cfg

    def build_certbot_args(self, dry_run: bool = False) -> List[str]:
        domains = [self.cfg.DOMAIN]

        args = [
            "certbot",
            "certonly",
            "--authenticator",
            "dns-domeneshop",
            "--dns-domeneshop-credentials",
            "/Users/daniko/Code/Autocert-PanOS/.secrets/certbot/.certbot.env",  # or direct field if you have it
            "--dns-domeneshop-propagation-seconds",
            self.cfg.DNS_SLEEP_TIME,
            "--agree-tos",
            "--non-interactive",
            "--config-dir",
            self.cfg.CONFIG_DIR,
            "--work-dir",
            self.cfg.WORK_DIR,
            "--logs-dir",
            self.cfg.LOGS_DIR,
            "--quiet",
        ]

        for domain in domains:
            args += ["-d", domain]

        if self.cfg.EMAIL:
            args += ["--email", self.cfg.EMAIL]
        else:
            args += ["--register-unsafely-without-email"]

        if dry_run:
            args.append("--dry-run")

        return args

    def run_certbot(self, dry_run: bool = False):
        args = self.build_certbot_args(dry_run)
        logger.info(
            f"Running certbot command: {' '.join(shlex.quote(a) for a in args)}"
        )

        result = subprocess.run(args, capture_output=True, text=True)
        if result.returncode != 0:
            logger.error(f"🤦 Certbot failed: {result.stderr}")
            raise RuntimeError(f"Certbot error: {result.stderr}")

        logger.info(f"Certbot succeeded: {result.stdout}")
        return result.stdout
