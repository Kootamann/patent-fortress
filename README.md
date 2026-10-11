# patent-fortress

Public patent intelligence engine for discovering public white space, tracking feature coverage, and producing evidence-backed opportunity briefs.

This repository is a practical foundation for a real business in patent intelligence. It is designed to ingest public patent records, normalize claim metadata, map technical feature coverage, and rank near-term opportunities for deeper human review.

Important:
- This project is not legal advice.
- It does not file patents or guarantee patentability.
- It is a research and strategy tool grounded in public evidence, source provenance, and reviewable output.

## Mission

Use public patent data to answer:
- what exists in the public record?
- what feature combinations are already covered?
- what gaps remain?
- which gaps are worth validating with counsel and technical research?
- what emerging standards, fields, or combinations are underserved?

## Product thesis

The business is not “AI invents patents.”

The business is:
- source-aware patent intelligence for technical teams
- a research engine for lawyers, founders, and labs
- a white-space mapping workflow that helps prioritize filing or licensing strategy

## Core workflow

1. Ingest public patent records from official sources
2. Record source URL, jurisdiction, publication date, and content hash
3. Normalize lifecycle and legal status
4. Extract claim features and technical dimensions
5. Map feature coverage across domains
6. Rank white-space opportunities by novelty risk and strategic value
7. Produce a reviewable patent brief for human counsel

## Repository layout

- `app/` — application code
- `docs/` — business plan and operating model
- `scripts/` — operational scripts

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
python -m app.main
```

## What this repo contains

- public-source ingestion interface
- data models for patents and opportunities
- claim feature extraction heuristics
- white-space scoring and ranking
- startup-friendly architecture for service and analytics workflow

## Business model

The product can become a real company by selling:
- patent intelligence subscriptions to labs and startups
- white-space reports for specific technical domains
- AI-assisted counsel preparation for defined sectors
- licensing and M&A diligence modules
- custom data feeds for targeted industries

## Why this is real

This repo is structured around public evidence, not hype. Every opportunity is associated with:
- source provenance
- jurisdiction
- publication date
- confidence rating
- human review flag

That is how you build a defensible system without pretending a model can auto-claim ownership.

## Roadmap

- Phase 1: public ingestion and evidence model
- Phase 2: claim extraction and clustering
- Phase 3: white-space scoring and opportunity reports
- Phase 4: API and SaaS workflow
- Phase 5: custom domain research and strategic intelligence

## License

Apache 2.0
