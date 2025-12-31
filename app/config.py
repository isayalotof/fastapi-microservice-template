from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "FastAPI Microservice"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS - изменено на str, будем парсить вручную
    ALLOWED_ORIGINS: str = "http://localhost:3000,http://localhost:8000"
    
    # Database
    DATABASE_URL: str
    
    # Redis
    REDIS_URL: str
    
    class Config:
        env_file = ".env"
        case_sensitive = True
    
    def get_allowed_origins(self) -> List[str]:
        """Parse ALLOWED_ORIGINS string into list"""
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]


settings = Settings()