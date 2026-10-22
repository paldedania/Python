"""Run assignment examples without prompts, with a timeout for each program."""

import ast
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RUNNER = """
import builtins, contextlib, io, json, runpy, sys
from unittest.mock import patch
request = json.load(sys.stdin)
values = iter(request['input'])
def read(prompt=''):
    try:
        return next(values)
    except StopIteration:
        raise EOFError('Verification fixture ran out of input') from None
with patch.object(builtins, 'input', read):
    runpy.run_path(request['path'], run_name='__main__')
"""


def check(case):
    request = dict(case, path=str(ROOT / case['file']))
    try:
        result = subprocess.run(
            [sys.executable, '-I', '-c', RUNNER],
            input=json.dumps(request), text=True, capture_output=True,
            timeout=8, cwd=ROOT,
        )
    except subprocess.TimeoutExpired:
        return dict(file=case['file'], passed=False, reason='Timed out')
    failures = []
    if result.returncode:
        failures.append(result.stderr.strip())
    output = result.stdout
    if 'expected' in case:
        expected = case['expected']
        matches = (
            output.split() == expected.split()
            if case.get('mode') == 'tokens' else output == expected
        )
        if not matches:
            failures.append(f'Expected {expected!r}; got {output!r}')
    for fragment in case.get('contains', []):
        if fragment not in output:
            failures.append(f'Missing {fragment!r} in {output!r}')
    return dict(file=case['file'], passed=not failures, reasons=failures)


def main():
    syntax_errors = []
    files = list(ROOT.rglob('*.py'))
    for file in files:
        try:
            ast.parse(file.read_text(), filename=str(file))
        except SyntaxError as error:
            syntax_errors.append(str(error))
    cases = json.loads((HERE / 'cases.json').read_text())
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, cases))
    failed = [result for result in results if not result['passed']]
    summary = {
        'checkedAt': datetime.now(timezone.utc).isoformat(),
        'python': sys.version.split()[0],
        'syntaxFiles': len(files),
        'syntaxErrors': syntax_errors,
        'executionCases': len(cases),
        'executionFiles': len({case['file'] for case in cases}),
        'assertedCases': sum('expected' in case or 'contains' in case for case in cases),
        'passed': len(results) - len(failed),
        'failures': failed,
    }
    (HERE / 'results.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))
    return 1 if syntax_errors or failed else 0


if __name__ == '__main__':
    sys.exit(main())
