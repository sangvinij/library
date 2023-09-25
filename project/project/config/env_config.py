import os
from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=True, env_file=os.path.join(BASE_DIR, ".env"), env_file_encoding="utf-8", extra="ignore"
    )
    DATABASE_URL: str
    SECRET_KEY: str
    SUPERUSER_USERNAME: str
    SUPERUSER_PASSWORD: str
    ALLOWED_HOSTS: str
    DEBUG: Optional[bool] = False


env = Settings()
