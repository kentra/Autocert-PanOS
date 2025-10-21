from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional
from pydantic import SecretStr


class Panos(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".secrets/panos/.panos.env"),
        env_file_encoding="utf-8",
    )
    MGMT: str
    API_KEY: SecretStr
    TLS_PROFILE: str


class CertBot(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".secrets/certbot/.domeneshop.env"),
        env_file_encoding="utf-8",
    )
    DOMENESHOP_TOKEN: SecretStr
    DOMENESHOP_SECRET: SecretStr
    DNS_SLEEP_TIME: str
    CERT_NAME: str
    EMAIL: Optional[str] = None
    DOMAIN: str
    CONFIG_DIR: str
    WORK_DIR: str
    LOGS_DIR: str
