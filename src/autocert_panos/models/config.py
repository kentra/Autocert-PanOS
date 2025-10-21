from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from pydantic import SecretStr


class Panos(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=("/Users/daniko/Code/Autocert-PanOS/.secrets/panos/.panos.env"),
        env_file_encoding="utf-8",
    )
    MGMT: str
    API_KEY: SecretStr
    TLS_PROFILE: str


class CertBot(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=("/Users/daniko/Code/Autocert-PanOS/.secrets/certbot/.domeneshop.env"),
        env_file_encoding="utf-8",
    )
    dns_domeneshop_client_token: str  # SecretStr
    dns_domeneshop_client_secret: str  #  SecretStr
    DNS_SLEEP_TIME: str
    CERT_NAME: str
    EMAIL: Optional[str] = None
    DOMAIN: str
    CONFIG_DIR: str
    WORK_DIR: str
    LOGS_DIR: str
