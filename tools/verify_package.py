"""Verify preset package integrity against preset.yml and checksums.json."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {'.git', '__pycache__', '.cemg-installer'}
IGNORED_FILES = {'checksums.json'}


def iter_package_files(root: Path):
    for path in sorted(root.rglob('*')):
        if any(part in IGNORED_DIRS for part in path.relative_to(root).parts):
            continue
        if path.is_file() and path.name not in IGNORED_FILES and path.suffix != '.pyc':
            yield path


def parse_manifest_files(root: Path):
    text = (root / 'preset.yml').read_text(encoding='utf-8')
    id_match = re.search(r'(?m)^\s+id:\s*[\'"]?([^\s\'"]+)[\'"]?\s*$', text)
    ver_match = re.search(r'(?m)^\s+version:\s*[\'"]?([^\s\'"]+)[\'"]?\s*$', text)
    files = re.findall(r'(?m)^\s+file:\s*[\'"]?([^\s\'"]+)[\'"]?\s*$', text)
    if not id_match or not ver_match:
        raise ValueError('Invalid preset.yml: missing id or version')
    return id_match.group(1), ver_match.group(1), files


def generate_checksums(root: Path):
    preset_id, preset_version, _ = parse_manifest_files(root)
    entries = []
    for path in iter_package_files(root):
        data = path.read_bytes()
        entries.append({
            'path': path.relative_to(root).as_posix(),
            'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
        })
    payload = {'preset': preset_id, 'version': preset_version, 'files': entries}
    (root / 'checksums.json').write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return len(entries)


def verify(root: Path):
    errors = []
    preset_id, preset_version, declared_files = parse_manifest_files(root)
    for rel in declared_files:
        if not (root / rel).is_file():
            errors.append(f'Missing file declared in preset.yml: {rel}')
    for stray in root.rglob('*.pyc'):
        errors.append(f'Stray bytecode file found: {stray.relative_to(root).as_posix()}')
    checksum_path = root / 'checksums.json'
    if not checksum_path.is_file():
        errors.append('Missing checksums.json')
        return errors
    manifest = json.loads(checksum_path.read_text(encoding='utf-8'))
    if manifest.get('preset') != preset_id or manifest.get('version') != preset_version:
        errors.append('checksums.json preset/version mismatch with preset.yml')
    expected = {item['path']: item for item in manifest.get('files', [])}
    actual_paths = {p.relative_to(root).as_posix() for p in iter_package_files(root)}
    for missing in sorted(set(expected) - actual_paths):
        errors.append(f'Missing file from checksums.json: {missing}')
    for extra in sorted(actual_paths - set(expected)):
        errors.append(f'Untracked file not in checksums.json: {extra}')
    for rel, item in sorted(expected.items()):
        p = root / rel
        if p.is_file():
            data = p.read_bytes()
            if hashlib.sha256(data).hexdigest() != item.get('sha256'):
                errors.append(f'SHA-256 mismatch: {rel}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generate', action='store_true', help='Regenerate checksums.json')
    args = parser.parse_args()
    if args.generate:
        count = generate_checksums(ROOT)
        print(json.dumps({'result': 'GENERATED', 'files': count}, ensure_ascii=False))
        return 0
    errors = verify(ROOT)
    print(json.dumps({'result': 'OK' if not errors else 'FAILED', 'errors': errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
