import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validate', ROOT / 'scripts/validate.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class PublicContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT / 'data', self.root / 'data')
        self.addCleanup(self.tmp.cleanup)

    def change(self, name, mutate):
        file = self.root / 'data' / (name + '.json')
        value = json.loads(file.read_text())
        mutate(value)
        file.write_text(json.dumps(value))

    def test_seed_valid(self):
        module.validate(self.root)

    def test_living_person_rejected(self):
        self.change('people', lambda rows: rows[0].update(living=True))
        with self.assertRaisesRegex(ValueError, 'deceased'):
            module.validate(self.root)

    def test_broken_reference_rejected(self):
        self.change('claims', lambda rows: rows[0].update(source_ids=['S999']))
        with self.assertRaisesRegex(ValueError, 'missing reference'):
            module.validate(self.root)

    def test_withheld_link_rejected(self):
        self.change('sources', lambda rows: rows[0].update(url='https://example.com/private'))
        with self.assertRaisesRegex(ValueError, 'withheld URL'):
            module.validate(self.root)

    def test_unknown_personal_field_rejected(self):
        self.change('people', lambda rows: rows[0].update(email='example@example.com'))
        with self.assertRaisesRegex(ValueError, 'wrong fields'):
            module.validate(self.root)

    def test_cycle_rejected(self):
        def mutate(rows):
            copy = dict(rows[0])
            copy.update(id='L999', person_ids=list(reversed(copy['person_ids'])))
            rows.append(copy)
        self.change('relationships', mutate)
        with self.assertRaisesRegex(ValueError, 'ancestry cycle'):
            module.validate(self.root)

    def test_unsupported_verified_claim_rejected(self):
        self.change('claims', lambda rows: rows[0].update(status='verified'))
        with self.assertRaisesRegex(ValueError, 'unsupported status'):
            module.validate(self.root)

if __name__ == '__main__':
    unittest.main()
