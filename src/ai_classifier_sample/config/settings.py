from functools import lru_cache
from typing import Optional

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings for AI classification service."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    # Cloud Provider Configuration
    cloud_region: str = Field(
        default="us-east-1",
        description="Cloud provider region for AI service"
    )
    
    cloud_profile: Optional[str] = Field(
        default=None,
        description="Cloud provider profile to use for authentication"
    )
    
    # AI Model Configuration
    model_arn: str = Field(
        default="arn:aws:bedrock:us-east-1:123456789:inference-profile/us.anthropic.claude-sonnet-4-20250514-v1:0",
        description="AI model ARN or identifier"
    )
    
    max_tokens: int = Field(
        default=5000,
        description="Maximum tokens for AI model responses"
    )
    
    provider: str = Field(
        default="aws",
        description="AI service provider type"
    )


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    load_dotenv()
    return Settings()