from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class SourceRecord:
    source_name: str
    source_url: str
    jurisdiction: str
    publication_date: Optional[str] = None
    content_hash: Optional[str] = None


@dataclass
class PatentRecord:
    patent_id: str
    jurisdiction: str
    title: str
    abstract: str = ""
    claims: List[str] = field(default_factory=list)
    source: Optional[SourceRecord] = None
    legal_status: str = "unknown"
    publication_date: Optional[str] = None
    confidence: float = 0.0
    tags: List[str] = field(default_factory=list)


@dataclass
class FeatureSignal:
    name: str
    category: str
    evidence: str


@dataclass
class Opportunity:
    name: str
    domain: str
    summary: str
    supporting_patents: List[str] = field(default_factory=list)
    gap_score: float = 0.0
    confidence: float = 0.0
    review_required: bool = True
