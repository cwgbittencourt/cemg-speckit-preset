"""Validate recorded readiness. Does not prove semantic quality or human identity."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


def contained(root, name):
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('Evidence path leaves feature directory: ' + name)
    return path


def validate(feature, record, stage, revision):
    requirements = json.loads((Path(__file__).resolve().parents[1] / 'policies/gate-requirements.json').read_text(encoding='utf-8'))
    data = json.loads(record.read_text(encoding='utf-8'))
    errors = []
    if data.get('schema_version') != 1:
        errors.append('Unsupported record schema')
    if data.get('stage') != stage or data.get('revision') != revision:
        errors.append('Stage or revision differs from requested candidate')
    if data.get('state') != 'READY' or data.get('blockers') != []:
        errors.append('Record is not READY or has missing/open blockers')
    for key in requirements[stage]:
        if data.get('checks', {}).get(key) is not True:
            errors.append('Required check is not true: ' + key)
    evidence = data.get('evidence')
    if not isinstance(evidence, list) or not evidence:
        errors.append('Evidence list is empty')
        evidence = []
    indexed = {}
    for item in evidence:
        try:
            path = contained(feature, item['path'])
            content = path.read_bytes()
            if not content or hashlib.sha256(content).hexdigest() != item.get('sha256'):
                raise ValueError('Evidence absent/empty or hash differs')
            if item.get('kind') == 'test-run':
                run = json.loads(content)
                if run.get('revision') != revision or run.get('result') != 'PASSED' or run.get('exit_code') != 0:
                    raise ValueError('Test execution failed or belongs to another revision')
                if not run.get('command') or not run.get('timestamp'):
                    raise ValueError('Incomplete execution record')
                for field in ('stdout', 'stderr'):
                    log = run[field]
                    if hashlib.sha256(contained(feature, log['path']).read_bytes()).hexdigest() != log['sha256']:
                        raise ValueError('Execution log changed')
            if item.get('kind') == 'product-execution':
                observed = json.loads(content)
                if observed.get('revision') != revision or observed.get('state') != 'OBSERVED':
                    raise ValueError('Product execution is missing or belongs to another revision')
                if observed.get('executor') not in ('AI', 'DEV', 'END_USER') or observed.get('medium') not in ('UI', 'API', 'INTEGRATION', 'MESSAGE', 'JOB', 'CLI', 'LIBRARY'):
                    raise ValueError('Invalid executor or product execution medium')
                if not all(observed.get(k) for k in ('startup', 'input', 'expected', 'observed', 'effects_checked', 'scenarios', 'artifacts')):
                    raise ValueError('Product execution lacks reproducible input/output evidence')
                for artifact in observed['artifacts']:
                    if hashlib.sha256(contained(feature, artifact['path']).read_bytes()).hexdigest() != artifact.get('sha256'):
                        raise ValueError('Product execution artifact changed')
                item = dict(item, executor=observed['executor'])
            indexed[item['path']] = item
        except (ValueError, OSError, KeyError, TypeError) as exc:
            errors.append('Invalid evidence: ' + str(exc))
    if stage in ('pr', 'acceptance', 'production'):
        executors = {e.get('executor') for e in indexed.values() if e.get('kind') == 'product-execution'}
        needed = {'AI'} if stage == 'pr' else ({'AI', 'DEV'} if stage == 'acceptance' else {'END_USER'})
        if not needed.issubset(executors):
            errors.append('Missing observed product execution for: ' + ', '.join(sorted(needed - executors)))
        if stage in ('pr', 'acceptance') and not any(e.get('kind') == 'test-run' for e in indexed.values()):
            errors.append('Candidate requires a recorded passing test execution')
        required_kinds = {'pr': ['pr-approval'], 'acceptance': ['story-acceptance'], 'production': ['production-approval', 'po-signoff']}[stage]
        decisions = data.get('human_decisions', [])
        for required_kind in required_kinds:
            valid = [d for d in decisions if d.get('kind') == required_kind
                     and d.get('decision') == 'APPROVED' and d.get('revision') == revision
                     and all(d.get(k) for k in ('actor', 'timestamp', 'source'))
                     and d.get('source') in indexed]
            if not valid:
                errors.append(f'Missing attributed human decision ({required_kind}) with hashed source evidence')
    return errors


def validate_impossibility(feature, record, revision):
    data = json.loads(record.read_text(encoding='utf-8'))
    errors = []
    if data.get('schema_version') != 1 or data.get('stage') != 'dev-impossibility' or data.get('revision') != revision:
        errors.append('Invalid impossibility schema, stage or revision')
    if data.get('state') != 'CONFIRMED_BY_DEV':
        errors.append('Impossibility not confirmed by DEV')
    for key in ('story', 'scenarios', 'reason', 'attempts', 'unverified', 'risk', 'scope', 'next_action', 'next_owner'):
        if not data.get(key):
            errors.append('Missing impossibility field: ' + key)
    if data.get('decision') not in ('WAIT', 'REJECT', 'ACCEPT_WITH_RESERVATIONS'):
        errors.append('Explicit DEV decision missing')
    indexed = set()
    for item in data.get('evidence', []):
        try:
            raw = contained(feature, item['path']).read_bytes()
            if not raw or hashlib.sha256(raw).hexdigest() != item.get('sha256'):
                raise ValueError('Empty or changed impossibility evidence')
            indexed.add(item['path'])
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(str(exc))
    confirmation = data.get('human_confirmation', {})
    if not all(confirmation.get(k) for k in ('actor', 'timestamp', 'source')) or confirmation.get('source') not in indexed:
        errors.append('Attributed DEV confirmation with hashed source is required')
    return errors


def _preset_identity():
    manifest = (Path(__file__).resolve().parents[1] / 'preset.yml').read_text(encoding='utf-8')
    id_match = re.search(r'(?m)^\s+id:\s*[\'"]?([^\s\'"]+)[\'"]?\s*$', manifest)
    ver_match = re.search(r'(?m)^\s+version:\s*[\'"]?([^\s\'"]+)[\'"]?\s*$', manifest)
    if not id_match or not ver_match:
        raise ValueError('Cannot determine preset id/version from preset.yml')
    return id_match.group(1), ver_match.group(1)


def active(project):
    preset_id, preset_version = _preset_identity()
    expected_marker = f'toplayerfrom:{preset_id}v{preset_version}'
    names = ['spec-template', 'plan-template', 'tasks-template', 'speckit.specify',
             'speckit.plan', 'speckit.tasks', 'speckit.analyze', 'speckit.implement']
    errors = []
    for name in names:
        result = subprocess.run(['specify', 'preset', 'resolve', name], cwd=project,
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
        normalized = re.sub(r'\s+', '', result.stdout)
        if result.returncode or expected_marker not in normalized:
            errors.append('Unexpected active source: ' + name)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--feature', required=True, type=Path)
    parser.add_argument('--record', required=True, help='Path relative to feature directory')
    parser.add_argument('--stage', required=True, choices=['spec', 'plan', 'tasks', 'pr', 'acceptance', 'production', 'dev-impossibility'])
    parser.add_argument('--revision', required=True, help='Actual candidate identifier supplied by trusted caller')
    parser.add_argument('--project', type=Path, help='Also check effective template/command resolution')
    args = parser.parse_args()
    try:
        errors = active(args.project) if args.project else []
        path = contained(args.feature, args.record)
        errors += (validate_impossibility(args.feature, path, args.revision)
                   if args.stage == 'dev-impossibility' else validate(args.feature, path, args.stage, args.revision))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors = [str(exc)]
    success = 'DEV_IMPOSSIBILITY_RECORDED' if args.stage == 'dev-impossibility' else 'READY'
    print(json.dumps({'result': 'BLOCKED' if errors else success, 'errors': errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
