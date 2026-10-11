from __future__ import annotations

from app.analysis.claim_extractor import extract_claim_bundle
from app.analysis.white_space import find_opportunities
from app.ingestion.uspto import USPTOConnector


def run_demo() -> None:
    connector = USPTOConnector()
    raw_patents = connector.fetch("quantum routing security", max_results=3)
    patents = [connector.normalize(item) for item in raw_patents]

    feature_sets = [extract_claim_bundle(p.claims) for p in patents]
    opportunities = find_opportunities(feature_sets, domain="quantum-security")

    for patent in patents:
        print(f"Patent: {patent.patent_id} | {patent.title}")
        print(f"  features: {sorted(set(extract_claim_bundle(patent.claims)))}")

    print("\nOpportunity:")
    for op in opportunities:
        print(f"- {op.name} | gap_score={op.gap_score} | review_required={op.review_required}")


if __name__ == "__main__":
    run_demo()
