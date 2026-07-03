import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Financial Coach"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # LLM settings
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY")
    
    # Vector DB
    CHROMA_HOST: str = os.getenv("CHROMA_HOST", "localhost")
    CHROMA_PORT: int = int(os.getenv("CHROMA_PORT", "8000"))

    class Config:
        case_sensitive = True

settings = Settings()
