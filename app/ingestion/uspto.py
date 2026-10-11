from __future__ import annotations

import hashlib
from typing import Any, Dict, List

from app.ingestion.base import SourceConnector
from app.models import PatentRecord, SourceRecord


class USPTOConnector(SourceConnector):
    """Example connector for public patent data retrieval.

    This is intentionally lightweight and source-aware. It does not make legal
    assertions and is designed for public research, review, and strategy work.
    """

    def fetch(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        # This is a placeholder until a real API wrapper or fetch layer is added.
        # The business reality is that public sources must be fetched via
        # official APIs or screenscraping with clear provenance.
        return [
            {
                "patent_id": "US-EXAMPLE-00001",
                "jurisdiction": "US",
                "title": "Example public patent record",
                "abstract": "Example abstract for architecture review.",
                "claims": [
                    "A system comprising a processing module configured to analyze public patent records.",
                    "The system further comprises a feature extraction engine.",
                ],
                "source_url": "https://example.com/patent/US-EXAMPLE-00001",
                "publication_date": "2025-01-01",
                "legal_status": "published",
                "query": query,
            }
        ][:max_results]

    def normalize(self, raw_item: Dict[str, Any]) -> PatentRecord:
        source = SourceRecord(
            source_name="USPTO",
            source_url=str(raw_item.get("source_url", "")),
            jurisdiction=str(raw_item.get("jurisdiction", "US")),
            publication_date=str(raw_item.get("publication_date") or ""),
            content_hash=hashlib.sha256(
                (str(raw_item.get("title", "")) + str(raw_item.get("abstract", ""))).encode("utf-8")
            ).hexdigest(),
        )

        claims = list(raw_item.get("claims") or [])

        return PatentRecord(
            patent_id=str(raw_item.get("patent_id", "unknown")),
            jurisdiction=str(raw_item.get("jurisdiction", "US")),
            title=str(raw_item.get("title", "untitled")),
            abstract=str(raw_item.get("abstract", "")),
            claims=claims,
            source=source,
            legal_status=str(raw_item.get("legal_status", "unknown")),
            publication_date=str(raw_item.get("publication_date") or None),
            confidence=0.7,
            tags=["example", "public-source"],
        )
