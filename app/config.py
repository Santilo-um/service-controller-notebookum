from pathlib import Path

from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    NOTEBOOKUM_SERVICE_URL: AnyHttpUrl = Field(..., env="NOTEBOOKUM_SERVICE_URL")
    FASTAPI_HOST: str = Field("0.0.0.0", env="FASTAPI_HOST")
    FASTAPI_PORT: int = Field(8000, env="FASTAPI_PORT")
    LOG_LEVEL: str = Field("info", env="LOG_LEVEL")
    PYTHONUNBUFFERED: str = Field("1", env="PYTHONUNBUFFERED")

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
    )


settings = Settings()
