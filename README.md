# Cary Genealogy Project

An evolving, evidence-linked history of the Cary family: people, relationships, documents, photographs, places and stories, with uncertainty preserved.

This repository is the **public research-data and editorial repository**. A separate future website can read its published JSON and Markdown. It is not a website application or a complete certified family tree.

## Start here

- [Family overview](research/family-overview.md)
- [People](data/people.json), [relationships](data/relationships.json), [claims](data/claims.json), [sources](data/sources.json)
- [Research questions](research/questions.md) and [historical avenues](research/historical-avenues.md)
- [Contribute](CONTRIBUTING.md), [evidence standards](docs/EVIDENCE.md), [privacy](docs/PRIVACY.md)
- [Governance and continuity](GOVERNANCE.md), [data model](docs/DATA_MODEL.md), [website integration](docs/SITE_INTEGRATION.md)

## Evidence matters

Family testimony is evidence, but it is distinguished from examined records, published scholarship and hypotheses. A source being examined does not make all its statements true. Conflicts remain visible until a reasoned analysis resolves them. No seed relationship is classified as verified.

The starter tree contains six deceased people and seven relationships. Living family records are excluded. The public edition preserves applicable HQ IDs; gaps are intentional, not missing ancestors to invent. It does not join a modern family to medieval or royal ancestors by surname.

## Current public edition

`PUB001` is a proposed public starter edition, curated from internal HQ release `M007`. See [release metadata](data/release.json) and [changelog](CHANGELOG.md). The private HQ archive remains the controlled evidence base; this repository holds a deliberately selected public edition. Public contributions are proposals until reviewed and reconciled. Do not automatically copy internal masters into this repository.

A public branch/pull request is already public, even before merging. Submit only material appropriate for public release. There is no private upload/contact service configured here yet.

## Check the data

Run `python3 scripts/validate.py` using Python 3.11 or newer. No external Python packages are required. The validation workflow checks changes; it does not determine genealogical truth or prove consent/copyright clearance.

## Reuse

No blanket open-content or software license has been selected yet. Public visibility is not permission to republish photographs, letters or other protected works. See [rights policy](docs/RIGHTS.md). A suitable licensing decision should be made before outside sites redistribute substantial content.
