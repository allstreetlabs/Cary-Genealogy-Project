# Governance and continuity

## Authority

Research HQ controls the internal evidence record and permanent IDs. This repository is a curated public edition. Contributors propose changes; research editors assess sources; maintainers publish accepted editions. Record which HQ release and public editorial decision each edition reflects. No workflow automatically promotes a submission into an authoritative claim.

## Roles

- Contributor: proposes evidence/corrections.
- Research editor: assesses genealogy, citations and conflicts.
- Publication reviewer: checks privacy, rights and redaction.
- Maintainer: integrates reviewed changes, maintains software and releases.
- Repository/organization owner: manages access and succession.

One person may fill several roles initially, but the history must state actual review rather than invent independent approvals. Current repository owner is `allstreetlabs`; no additional reviewer or successor has been appointed by these documents.

## Continuity plan

Move to a family/research organization when ready; appoint at least two trusted organization owners and multiple editors. Document domain renewal and hosting responsibility, recovery arrangements, release procedures and handover. Keep credentials outside the repository. Maintain downloadable releases and independent backups. Periodically test a clean build using only public files.

A public repo can be forked, but forks alone do not transfer control of its domain, renew hosting, or solve editorial succession. Access and renewal duties must be assigned to people.

## Review controls

Recommended, NOT configured by these files: protect main; require pull requests and passing `validate` checks; require a second review when a qualified co-editor is available; disable force pushes; record emergency exceptions. CODEOWNERS review is only enforced if repository rules are configured to require it. Until then the process is editorial convention, not a technical guarantee.

Public editions have their own PUB numbers; internal M numbers are not republished wholesale. Corrections preserve earlier snapshots and explain old/new wording, source and reason. The pending private heritage-pass handoff is not incorporated into PUB001 merely because it exists.
