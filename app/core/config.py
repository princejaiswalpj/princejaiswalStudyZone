from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "study zone"
    debug: bool = True
    api_v1_str: str = "/api/v1"
    database_url: str   # required, must come from .env or environment
    secret_key: str     # required, must come from .env or environment
    access_token_expire_minutes: int = 1440
    algorithm: str = "HS256"

    @field_validator("debug", mode="before")
    @classmethod
    def parse_debug(cls, value):
        if isinstance(value, bool):
            return value

        if isinstance(value, str):
            normalized = value.strip().lower()
            truthy = {"1", "true", "yes", "on", "debug", "development", "dev"}
            falsy = {"0", "false", "no", "off", "release", "production", "prod"}

            if normalized in truthy:
                return True

            if normalized in falsy:
                return False

        return value

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# instantiate once
settings = Settings()


