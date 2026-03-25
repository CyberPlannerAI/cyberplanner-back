import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = "CyberPlanner API"
    APP_VERSION: str = "1.0.0"
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    GOOGLE_API_KEY: str | None = os.getenv("GOOGLE_API_KEY")

    # CORS
    ALLOW_ORIGINS: list[str] = ["*"]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: list[str] = ["*"]
    ALLOW_HEADERS: list[str] = ["*"]


settings = Settings()
