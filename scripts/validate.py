#!/usr/bin/env python3
"""Check the public data contract; not a proof or consent certification."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {
    'people': {'id', 'name', 'living', 'claim_ids', 'visibility', 'publication_basis'},
    'claims': {'id', 'subject_ids', 'text', 'status', 'source_ids', 'limitations', 'visibility', 'publication_basis'},
    'relationships': {'id', 'type', 'person_ids', 'claim_ids', 'status', 'limitations', 'visibility', 'publication_basis'},
    'sources': {'id', 'title', 'type', 'access', 'url', 'limitations', 'visibility', 'publication_basis'},
}
PREFIX = {'people': 'P', 'claims': 'C', 'relationships': 'L', 'sources': 'S'}
STATUSES = {'testimony', 'described_record', 'published_support', 'documentary_statement', 'conditional', 'unresolved'}
ACCESS = {'examined_publication', 'examined_derivative', 'described_unexamined', 'reference_only', 'withheld'}

def validate(root=ROOT):
    data = {}
    def require(ok, message):
        if not ok:
            raise ValueError(message)
    for kind, fields in FIELDS.items():
        records = json.loads((root / 'data' / (kind + '.json')).read_text())
        require(isinstance(records, list), kind + ': expected list')
        data[kind] = {}
        for row in records:
            require(isinstance(row, dict) and set(row) == fields, kind + ': wrong fields')
            rid = row['id']
            require(isinstance(rid, str) and re.fullmatch(PREFIX[kind] + r'\d{3,}', rid), kind + ': invalid ID')
            require(rid not in data[kind], rid + ': duplicate ID')
            data[kind][rid] = row
            require(row['visibility'] == 'public' and isinstance(row['publication_basis'], str) and row['publication_basis'].strip(), rid + ': publication metadata missing')
            if kind == 'people':
                require(row['living'] is False and isinstance(row['name'], str) and row['name'].strip(), rid + ': only named deceased people supported')
            if kind in {'claims', 'relationships'}:
                require(row['status'] in STATUSES, rid + ': unsupported status; verified requires future proof model')
            for field in {'text', 'title', 'limitations', 'type'} & fields:
                require(isinstance(row[field], str) and row[field].strip(), rid + ': missing ' + field)
            if kind == 'sources':
                require(row['access'] in ACCESS, rid + ': invalid access')
                require(row['url'] is None or (isinstance(row['url'], str) and row['url'].startswith('https://')), rid + ': invalid URL')
                require(row['access'] != 'withheld' or row['url'] is None, rid + ': withheld URL exposed')
    def refs(row, field, target):
        ids = row[field]
        require(isinstance(ids, list) and ids and all(isinstance(x, str) for x in ids), row['id'] + ': invalid references')
        require(len(ids) == len(set(ids)) and all(x in data[target] for x in ids), row['id'] + ': duplicate or missing reference')
        return ids
    for row in data['people'].values():
        refs(row, 'claim_ids', 'claims')
    for row in data['claims'].values():
        refs(row, 'subject_ids', 'people')
        refs(row, 'source_ids', 'sources')
    graph, seen = {}, set()
    for row in data['relationships'].values():
        ids = refs(row, 'person_ids', 'people')
        claims = refs(row, 'claim_ids', 'claims')
        require(len(ids) == 2 and ids[0] != ids[1], row['id'] + ': invalid endpoints')
        require(row['type'] in {'parent_child', 'marriage'}, row['id'] + ': invalid relationship type')
        key = (row['type'], *(sorted(ids) if row['type'] == 'marriage' else ids))
        require(key not in seen, row['id'] + ': duplicate relationship')
        seen.add(key)
        for cid in claims:
            require(set(ids) <= set(data['claims'][cid]['subject_ids']), row['id'] + ': claim does not cover endpoints')
        if row['type'] == 'parent_child':
            graph.setdefault(ids[0], []).append(ids[1])
    def visit(node, ancestors):
        require(node not in ancestors, 'ancestry cycle: ' + node)
        for child in graph.get(node, []):
            visit(child, ancestors | {node})
    for node in graph:
        visit(node, set())
    release = json.loads((root / 'data/release.json').read_text())
    require(set(release) == {'schema_version', 'public_edition', 'state', 'internal_baseline', 'prepared_at', 'scope', 'visibility', 'publication_basis'}, 'release: wrong fields')
    require(release['schema_version'] == '1' and release['state'] in {'draft', 'approved'}, 'release: invalid version/state')
    require(re.fullmatch(r'PUB\d{3,}', release['public_edition']), 'release: invalid edition')
    require(release['visibility'] == 'public' and release['publication_basis'], 'release: publication metadata missing')
    for path in (root / 'data').glob('*.json'):
        for marker in ['libfile_', 'file_0000', 'sandbox:', '/workspace/', '248 cM', 'P001', 'P002', 'P009']:
            require(marker not in path.read_text(), path.name + ': private/seed-excluded marker ' + marker)

if __name__ == '__main__':
    try:
        validate()
    except (ValueError, KeyError, TypeError, OSError) as exc:
        raise SystemExit('Validation failed: ' + str(exc))
    print('Public archive validated: IDs, references, statuses, deceased-only records and ancestry cycles.')
