"""
cqp_checker.py — Core logic for CQP-based Pylint feedback.

Intended to be uploaded as a CodeRunner support file so it is available
in the working directory when the grader template runs.

Public interface:
    check_principles(source_code, principle_keys) -> list[PrincipleResult]

Each PrincipleResult is a dict:
    {
        'name':      str,               # e.g. "No Unused Content"
        'principle': str,               # one-line principle statement
        'rationale': str,               # why this principle matters
        'violations': list[Violation],  # may be empty
    }

Each Violation is a dict:
    {
        'code':        str,  # e.g. "W0611"
        'line_no':     str,  # line number as string
        'raw':         str,  # the raw pylint output line
        'explanation': str,  # pedagogical explanation for the student
    }
"""

import re
import subprocess
import os

from cqp_principles import PRINCIPLES


def _run_pylint(source_code, codes):
    """
    Write source_code to source.py and run pylint restricted to the
    given set of message codes. Returns the raw stdout+stderr string.

    Raises FileNotFoundError if pylint is not installed.
    """
    with open('source.py', 'w') as f:
        f.write(source_code)

    env = os.environ.copy()
    env['HOME'] = os.getcwd()

    enabled = ','.join(codes)
    cmd = ['pylint', '--disable=all', f'--enable={enabled}', 'source.py']

    try:
        output = subprocess.check_output(
            cmd, universal_newlines=True, stderr=subprocess.STDOUT, env=env
        )
    except subprocess.CalledProcessError as e:
        # Pylint exits non-zero when violations are found — this is expected.
        output = e.output

    return output


def _parse_violations(output, codes_map):
    """
    Parse raw pylint output and return a list of Violation dicts for
    codes that appear in codes_map.

    Pylint output format:
        source.py:LINE:COL: CODE (symbolic-name) message text
    """
    violations = []
    pattern = re.compile(r':(\d+):\d+: ([A-Z]\d+)')

    for line in output.splitlines():
        match = pattern.search(line)
        if match:
            line_no = match.group(1)
            code = match.group(2)
            if code in codes_map:
                _, explanation = codes_map[code]
                violations.append({
                    'code': code,
                    'line_no': line_no,
                    'raw': line.strip(),
                    'explanation': explanation,
                })

    return violations


def check_principles(source_code, principle_keys):
    """
    Run pylint once against source_code for all active principles combined
    and return a list of PrincipleResult dicts (one per principle,
    regardless of whether violations were found).

    principle_keys: list of strings matching keys in PRINCIPLES, e.g.
        ['no_unused_content', 'clear_layout']

    Unknown keys are silently skipped.
    """
    valid = {k: PRINCIPLES[k] for k in principle_keys if k in PRINCIPLES}

    # Build combined codes map and reverse lookup: code -> principle_key
    all_codes = {}
    code_to_principle = {}
    for key, principle in valid.items():
        for code, (_, explanation) in principle['codes'].items():
            all_codes[code] = ('', explanation)
            code_to_principle[code] = key

    # Single pylint invocation across all active codes
    by_principle = {key: [] for key in valid}
    if all_codes:
        output = _run_pylint(source_code, list(all_codes.keys()))
        for v in _parse_violations(output, all_codes):
            by_principle[code_to_principle[v['code']]].append(v)

    results = []
    for key in principle_keys:
        if key not in valid:
            continue
        principle = valid[key]
        results.append({
            'name': principle['name'],
            'principle': principle['principle'],
            'rationale': principle['rationale'],
            'violations': by_principle[key],
        })

    return results
