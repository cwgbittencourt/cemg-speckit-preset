import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('gate', ROOT / 'tools/check_gate.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
REQ = json.loads((ROOT / 'policies/gate-requirements.json').read_text())


class GateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.feature = Path(self.temp.name)
        self.record = self.feature / 'status.json'
        self.doc = self.feature / 'spec.md'
        self.doc.write_text('Critério e cenário aprovados no fixture de teste.', encoding='utf-8')
        self.data = {'schema_version': 1, 'stage': 'spec', 'revision': 'fixture-A',
                     'state': 'READY', 'blockers': [],
                     'checks': {k: True for k in REQ['spec']},
                     'evidence': [self.evidence(self.doc)], 'human_decisions': []}

    def tearDown(self):
        self.temp.cleanup()

    def evidence(self, path, kind='document'):
        return {'path': path.relative_to(self.feature).as_posix(), 'kind': kind,
                'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}

    def check(self, stage='spec', revision='fixture-A'):
        self.record.write_text(json.dumps(self.data), encoding='utf-8')
        return gate.validate(self.feature, self.record, stage, revision)

    def test_ready_record(self):
        self.assertEqual(self.check(), [])

    def test_missing_required_check(self):
        del self.data['checks']['criteria_observable']
        self.assertTrue(self.check())

    def test_false_check(self):
        self.data['checks']['material_decisions_resolved'] = False
        self.assertTrue(self.check())

    def test_open_blocker(self):
        self.data['blockers'] = ['Permissão não definida']
        self.assertTrue(self.check())

    def test_wrong_revision(self):
        self.assertTrue(self.check(revision='fixture-B'))

    def test_tampered_evidence(self):
        self.doc.write_text('Alterado após registro', encoding='utf-8')
        self.assertTrue(self.check())

    def test_empty_evidence(self):
        self.data['evidence'] = []
        self.assertTrue(self.check())

    def test_path_escape(self):
        self.data['evidence'][0]['path'] = '../outside.md'
        self.assertTrue(self.check())

    def run_test_command(self, code):
        proc = subprocess.run([sys.executable, str(ROOT / 'tools/record_test.py'),
                               '--feature', str(self.feature), '--cwd', str(self.feature),
                               '--revision', 'fixture-A', '--', sys.executable, '-c', code],
                              capture_output=True, text=True)
        return proc, json.loads(proc.stdout)

    def pr_record(self):
        self.data.update(stage='pr', checks={k: True for k in REQ['pr']})
        self.product('AI')

    def product(self, executor):
        record = {'schema_version': 1, 'revision': 'fixture-A', 'executor': executor,
                  'medium': 'API', 'state': 'OBSERVED', 'startup': 'fixture startup',
                  'input': 'fixture input', 'expected': 'fixture expected', 'observed': 'fixture observed',
                  'effects_checked': 'fixture state', 'scenarios': ['S1'],
                  'artifacts': [self.evidence(self.doc)]}
        p = self.feature / (executor + '-product.json')
        p.write_text(json.dumps(record), encoding='utf-8')
        self.data['evidence'].append(self.evidence(p, 'product-execution'))

    def test_runner_preserves_failure(self):
        proc, entry = self.run_test_command('import sys; print("failure"); sys.exit(7)')
        self.assertEqual(proc.returncode, 7)
        self.assertEqual(entry['result'], 'FAILED')
        self.pr_record()
        self.data['evidence'].append(entry)
        self.assertTrue(self.check(stage='pr'))

    def test_pr_requires_human_source(self):
        proc, entry = self.run_test_command('print("fixture execution")')
        self.assertEqual(proc.returncode, 0)
        self.pr_record()
        self.data['evidence'].append(entry)
        self.assertTrue(self.check(stage='pr'))

    def test_pr_complete_record_and_tampered_log(self):
        _, entry = self.run_test_command('print("fixture execution")')
        self.pr_record()
        self.data['evidence'].append(entry)
        self.data['human_decisions'] = [{'kind': 'pr-approval', 'decision': 'APPROVED',
                                        'actor': 'TEST-FIXTURE', 'timestamp': 'test',
                                        'revision': 'fixture-A', 'source': 'spec.md'}]
        self.assertEqual(self.check(stage='pr'), [])
        run = json.loads((self.feature / entry['path']).read_text())
        (self.feature / run['stdout']['path']).write_text('changed')
        self.assertTrue(self.check(stage='pr'))

    def test_acceptance_requires_separate_decision(self):
        _, entry = self.run_test_command('print("fixture execution")')
        self.data.update(stage='acceptance', checks={k: True for k in REQ['acceptance']})
        self.product('AI')
        self.product('DEV')
        self.data['evidence'].append(entry)
        self.data['human_decisions'] = [{'kind': 'pr-approval', 'decision': 'APPROVED',
                                        'actor': 'TEST-FIXTURE', 'timestamp': 'test',
                                        'revision': 'fixture-A', 'source': 'spec.md'}]
        self.assertTrue(self.check(stage='acceptance'))

    def test_cli_rejects_missing_record(self):
        p = subprocess.run([sys.executable, str(ROOT / 'tools/check_gate.py'),
                            '--feature', str(self.feature), '--record', 'missing.json',
                            '--stage', 'spec', '--revision', 'fixture-A'], capture_output=True)
        self.assertEqual(p.returncode, 1)

    def test_unit_execution_does_not_replace_product_execution(self):
        _, entry = self.run_test_command('print("unit-only fixture")')
        self.data.update(stage='pr', checks={k: True for k in REQ['pr']})
        self.data['evidence'].append(entry)
        self.data['human_decisions'] = [{'kind': 'pr-approval', 'decision': 'APPROVED',
                                        'actor': 'TEST-FIXTURE', 'timestamp': 'test',
                                        'revision': 'fixture-A', 'source': 'spec.md'}]
        self.assertTrue(any('product execution' in e for e in self.check(stage='pr')))

    def test_breakpoint_without_output_is_not_demonstration(self):
        self.pr_record()
        p = self.feature / 'AI-product.json'
        data = json.loads(p.read_text())
        data['observed'] = ''
        p.write_text(json.dumps(data))
        self.data['evidence'][-1] = self.evidence(p, 'product-execution')
        self.assertTrue(self.check(stage='pr'))

    def impossible(self):
        return {'schema_version': 1, 'stage': 'dev-impossibility', 'revision': 'fixture-A',
                'state': 'CONFIRMED_BY_DEV', 'story': 'US1', 'scenarios': ['S1'],
                'reason': 'Fixture service unavailable', 'attempts': ['fixture attempt'],
                'unverified': ['S1'], 'risk': 'Unknown integration behavior', 'scope': 'fixture only',
                'next_action': 'Restore fixture', 'next_owner': 'TEST-FIXTURE', 'decision': 'WAIT',
                'human_confirmation': {'actor': 'TEST-FIXTURE', 'timestamp': 'test', 'source': 'spec.md'},
                'evidence': [self.evidence(self.doc)]}

    def test_impossibility_requires_human_confirmation(self):
        data = self.impossible(); data['state'] = 'DRAFT'
        self.record.write_text(json.dumps(data))
        self.assertTrue(gate.validate_impossibility(self.feature, self.record, 'fixture-A'))

    def test_impossibility_requires_explicit_decision(self):
        data = self.impossible(); data['decision'] = ''
        self.record.write_text(json.dumps(data))
        self.assertTrue(gate.validate_impossibility(self.feature, self.record, 'fixture-A'))

    def test_recorded_impossibility_does_not_return_ready(self):
        for decision in ('WAIT', 'REJECT', 'ACCEPT_WITH_RESERVATIONS'):
            data = self.impossible(); data['decision'] = decision
            self.record.write_text(json.dumps(data))
            p = subprocess.run([sys.executable, str(ROOT / 'tools/check_gate.py'),
                                '--feature', str(self.feature), '--record', 'status.json',
                                '--stage', 'dev-impossibility', '--revision', 'fixture-A'], capture_output=True, text=True)
            self.assertEqual(p.returncode, 0)
            self.assertEqual(json.loads(p.stdout)['result'], 'DEV_IMPOSSIBILITY_RECORDED')
            self.assertTrue(gate.validate(self.feature, self.record, 'acceptance', 'fixture-A'))

    def test_impossibility_revision_and_source_integrity(self):
        data = self.impossible()
        self.record.write_text(json.dumps(data))
        self.assertTrue(gate.validate_impossibility(self.feature, self.record, 'fixture-B'))
        self.doc.write_text('changed')
        self.assertTrue(gate.validate_impossibility(self.feature, self.record, 'fixture-A'))

    def test_production_requires_end_user_execution_and_approval(self):
        self.data.update(stage='production', checks={k: True for k in REQ['production']})
        self.product('DEV')
        self.data['human_decisions'] = [{'kind': 'story-acceptance', 'decision': 'APPROVED',
                                        'actor': 'DEV-USER', 'timestamp': 'test',
                                        'revision': 'fixture-A', 'source': 'spec.md'}]
        self.assertTrue(self.check(stage='production'))
        self.product('END_USER')
        self.data['human_decisions'].append({'kind': 'production-approval', 'decision': 'APPROVED',
                                             'actor': 'END-USER', 'timestamp': 'test',
                                             'revision': 'fixture-A', 'source': 'spec.md'})
        self.assertTrue(self.check(stage='production'))
        self.data['human_decisions'].append({'kind': 'po-signoff', 'decision': 'APPROVED',
                                             'actor': 'PO-USER', 'timestamp': 'test',
                                             'revision': 'fixture-A', 'source': 'spec.md'})
        self.assertEqual(self.check(stage='production'), [])


if __name__ == '__main__':
    unittest.main()
