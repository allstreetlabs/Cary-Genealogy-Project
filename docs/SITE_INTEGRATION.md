# Future site integration

## Repository contract

The data repo owns reviewed public content; the future site repo owns presentation, search and rendering. Keep the site replaceable. Site edits must never silently mutate genealogical facts.

A site build should:

1. Read a configured repository and explicit content ref (commit/tag preferred for reproducibility).
2. Retrieve only `data/` and approved `research/` content; never depend on private HQ paths.
3. Run the same validation and refuse broken references, cycles or non-public records.
4. Render source access/limitations and relationship-level uncertainty visibly.
5. Record and display the source commit and public edition used.
6. Publish only after the configured editorial/build gates pass; retain the last successful version if new data fails.

## Updating across two repos

A commit here does NOT automatically start an unrelated site's workflow. Choose one explicit integration later:

- Simple first choice: the site polls for approved data refs on a schedule plus a manual refresh. GitHub schedules may be delayed and inactive public repos can have scheduled workflows disabled; monitor it.
- Event-driven: after approved publication, a GitHub App with narrowly scoped access sends a repository-dispatch event to the site. The ordinary GITHUB_TOKEN is scoped to its own repo; do not assume cross-repository write permission.

Avoid fetching a floating main ref at arbitrary runtime if you want auditable releases. A site can track newest approved public content, resolve it to a commit, validate, then publish that exact version. Main-branch source changes and approved public release changes are separate concepts.

No second repository, hosting, credentials, synchronization schedule or deployment is created here. Do not enable automatic publication of a draft public edition as if it had passed editorial review.

## Portability

Keep owner/repo/ref configurable for a later organization transfer. Use relative links inside this repository. Keep a transfer checklist for remote URLs, dispatch permissions, hosted media, secrets and domain configuration; redirects alone should not be the continuity plan.

## Documentation

- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
- https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches
