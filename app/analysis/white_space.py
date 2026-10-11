from __future__ import annotations

from typing import Iterable, List, Sequence

from app.models import Opportunity


def score_white_space(feature_space: Sequence[str], covered_features: Iterable[str], domain: str = "general") -> float:
    covered = set(covered_features)
    gaps = [f for f in feature_space if f not in covered]
    return round(len(gaps) / max(len(feature_space), 1), 4)


def find_opportunities(feature_sets: Sequence[Sequence[str]], domain: str = "general") -> List[Opportunity]:
    feature_space = sorted(set(item for group in feature_sets for item in group))
    covered = set(item for group in feature_sets for item in group)
    gap_ratio = score_white_space(feature_space, covered, domain)

    return [
        Opportunity(
            name=f"{domain}-white-space-opportunity",
            domain=domain,
            summary=f"Feature-space gap analysis indicates {gap_ratio:.0%} uncovered space in this domain.",
            supporting_patents=[],
            gap_score=gap_ratio,
            confidence=0.68,
            review_required=True,
        )
    ]
