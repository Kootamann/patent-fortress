from __future__ import annotations

from pydantic import BaseModel, Field


class SourceConfig(BaseModel):
    jurisdiction: str = "US"
    base_url: str = "https://patents.google.com"
    user_agent: str = "patent-fortress/0.1"


class AppSettings(BaseModel):
    source_config: SourceConfig = Field(default_factory=SourceConfig)
    max_pages_per_run: int = 10
    confidence_threshold: float = 0.65
    strict_mode: bool = True


def get_settings() -> AppSettings:
    return AppSettings()
