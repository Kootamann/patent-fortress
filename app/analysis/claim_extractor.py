from __future__ import annotations

import re
from typing import List


def extract_claim_features(claim_text: str) -> List[str]:
    """Very small heuristics layer for feature extraction.

    This is intentionally transparent and easy to replace with a stronger NLP
    stack later. The goal is to convert claims into structured, reviewable
    technical dimensions.
    """
    text = claim_text.lower()
    tokens = re.findall(r"[a-z0-9_\-]+", text)
    features = []

    if "quantum" in text:
        features.append("quantum")
    if "routing" in text:
        features.append("routing")
    if "entanglement" in text:
        features.append("entanglement")
    if "memory" in text:
        features.append("memory")
    if "latency" in text:
        features.append("latency")
    if "compliance" in text:
        features.append("compliance")
    if "ai" in text:
        features.append("ai")
    if "security" in text:
        features.append("security")
    if "pqc" in text:
        features.append("pqc")
    if "cryptography" in text:
        features.append("cryptography")

    features.extend(tokens[:5])
    deduped = []
    for item in features:
        if item not in deduped:
            deduped.append(item)
    return deduped


def extract_claim_bundle(claims: List[str]) -> List[str]:
    all_features = []
    for claim in claims:
        all_features.extend(extract_claim_features(claim))
    return sorted(set(all_features))
