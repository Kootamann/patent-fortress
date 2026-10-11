from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from app.models import PatentRecord


class SourceConnector(ABC):
    """Public-source ingestion interface."""

    @abstractmethod
    def fetch(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def normalize(self, raw_item: Dict[str, Any]) -> PatentRecord:
        raise NotImplementedError
