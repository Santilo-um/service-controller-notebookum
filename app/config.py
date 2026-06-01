import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

class Settings:
    FASTAPI_HOST: str = os.getenv("FASTAPI_HOST", "0.0.0.0")
    FASTAPI_PORT: int = int(os.getenv("FASTAPI_PORT", 8000))
    NOTEBOOKUM_SERVICE_URL: str = os.getenv("NOTEBOOKUM_SERVICE_URL", "")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")
    PYTHONUNBUFFERED: str = os.getenv("PYTHONUNBUFFERED", "1")


settings = Settings()
