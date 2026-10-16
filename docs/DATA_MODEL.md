# Public data model v1

Files are UTF-8 JSON. Every data record has `id`, `visibility: public`, `publication_basis` and an independent `status` where applicable. Only deceased people are supported. Stable HQ IDs are retained without renumbering; gaps are expected.

- `people.json`: P IDs, display name, `living: false`, summary and claim references. Claims, not unsourced person fields, hold precise dates.
- `relationships.json`: L IDs, type (`parent_child` or `marriage`), two P IDs, claim references and status. Parent-child endpoints are parent then child. Marriage has no direction.
- `claims.json`: C IDs, proposition text, subject P IDs, source S IDs, classification and limitations. Do not treat a person-wide badge as proof of every fact.
- `sources.json`: S IDs, type, access, title, URL or null, and limits. Private evidence may be represented only by minimal withheld metadata.
- `release.json`: public edition, internal baseline, schema version, release state and scope. Draft editions are not approved just because a branch exists.

The validator checks IDs, required keys, allowed fields/statuses, reference integrity, self-links, duplicate relationships, cycles in parent links, source access, deceased-only records and selected private-data markers. It is not a full privacy/security scanner or genealogical proof engine. Manual review remains mandatory.

Do not allocate new permanent IDs without HQ coordination. Conflicting propositions should reference one question and preserve alternatives, not overwrite each other. Future source assets and public profile data need separate explicitly designed models.
