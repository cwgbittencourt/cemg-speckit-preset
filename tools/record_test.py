"""Execute an authorized test command and preserve exit code and output hashes."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import uuid


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--feature', required=True, type=Path)
    parser.add_argument('--cwd', required=True, type=Path)
    parser.add_argument('--revision', required=True, help='Actual tested revision, not a guessed value')
    parser.add_argument('--timeout', type=int, default=600, help='Maximum execution time in seconds (default: 600)')
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ['--'] else args.command
    if not command:
        parser.error('Provide an authorized test command after --')
    folder = args.feature.resolve() / 'verification' / ('run-' + uuid.uuid4().hex)
    folder.mkdir(parents=True)
    try:
        proc = subprocess.run(command, cwd=args.cwd, capture_output=True, shell=False, timeout=args.timeout)
        code, stdout, stderr = proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as exc:
        code = 124
        stdout = exc.stdout or b''
        stderr = (exc.stderr or b'') + f'\nCommand timed out after {args.timeout}s\n'.encode('utf-8')
    except OSError as exc:
        code, stdout, stderr = 127, b'', str(exc).encode('utf-8')
    record = {'schema_version': 1, 'revision': args.revision,
              'timestamp': datetime.now(timezone.utc).isoformat(),
              'cwd': str(args.cwd.resolve()), 'command': command,
              'exit_code': code, 'result': 'PASSED' if code == 0 else 'FAILED'}
    for name, data in [('stdout', stdout), ('stderr', stderr)]:
        path = folder / (name + '.log')
        path.write_bytes(data)
        record[name] = {'path': path.relative_to(args.feature.resolve()).as_posix(),
                        'sha256': hashlib.sha256(data).hexdigest()}
    path = folder / 'execution.json'
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'path': path.relative_to(args.feature.resolve()).as_posix(),
                      'kind': 'test-run', 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                      'result': record['result']}, ensure_ascii=False))
    return code if 0 <= code <= 255 else 1


if __name__ == '__main__':
    sys.exit(main())
