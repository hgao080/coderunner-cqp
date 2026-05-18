"""
cqp_checker_java.py — Core logic for CQP-based PMD feedback on Java code.

Intended to be uploaded as a CodeRunner support file so it is available
in the working directory when the grader template runs.

Public interface:
    check_principles(source_code, principle_keys) -> list[PrincipleResult]

Each PrincipleResult is a dict:
    {
        'name':      str,               # e.g. "Clear Presentation"
        'principle': str,               # one-line principle statement
        'rationale': str,               # why this principle matters
        'violations': list[Violation],  # may be empty
    }

Each Violation is a dict:
    {
        'code':        str,  # PMD rule name, e.g. "ControlStatementBraces"
        'line_no':     str,  # line number as string
        'raw':         str,  # formatted display line shown to the student
        'explanation': str,  # pedagogical explanation
    }

Tool routing:
    Rules in CUSTOM_RULES  → cqp_custom_checkers_java.run_custom_checks()
    All other rules         → PMD subprocess (via generated ruleset XML)

PMD version compatibility:
    PMD 7.x command: pmd check -d source.java -R ruleset.xml -f xml
    PMD 6.x command: pmd -d source.java -R ruleset.xml -f xml
    Version is detected automatically at first call.
"""

import os
import re
import subprocess
import tempfile

from cqp_principles_java import CUSTOM_RULES, PMD_RULE_CATEGORIES, PRINCIPLES


# ---------------------------------------------------------------------------
# PMD version detection (cached after first call)
# ---------------------------------------------------------------------------

_pmd_base_cmd = None


def _get_pmd_base_cmd():
    """Return the PMD base command list, detecting PMD 7 vs PMD 6."""
    global _pmd_base_cmd
    if _pmd_base_cmd is not None:
        return _pmd_base_cmd
    try:
        r = subprocess.run(
            ['pmd', '--version'],
            capture_output=True, text=True, timeout=5,
        )
        version_str = r.stdout + r.stderr
        if re.search(r'\b7\.', version_str):
            _pmd_base_cmd = ['pmd', 'check']
        else:
            _pmd_base_cmd = ['pmd']
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        _pmd_base_cmd = ['pmd', 'check']
    return _pmd_base_cmd


# ---------------------------------------------------------------------------
# Ruleset XML generation
# ---------------------------------------------------------------------------

def _build_ruleset_xml(rule_names):
    """Generate a PMD ruleset XML string for the given PMD rule names."""
    refs = []
    for rule in sorted(rule_names):
        category = PMD_RULE_CATEGORIES.get(rule)
        if category:
            refs.append(f'    <rule ref="{category}/{rule}"/>')

    return (
        '<?xml version="1.0"?>\n'
        '<ruleset name="CQP Rules"\n'
        '    xmlns="http://pmd.sourceforge.net/ruleset/2.0.0"\n'
        '    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'
        '    xsi:schemaLocation="http://pmd.sourceforge.net/ruleset/2.0.0 '
        'https://pmd.github.io/ruleset_2_0_0.xsd">\n'
        '    <description>CQP Java Rules</description>\n'
        + '\n'.join(refs) + '\n'
        '</ruleset>\n'
    )


# ---------------------------------------------------------------------------
# PMD runner
# ---------------------------------------------------------------------------

def _run_pmd(pmd_rules, source_code):
    """
    Write source_code to source.java, generate a ruleset XML, run PMD,
    and return the raw XML output string.

    Returns empty string if PMD is not installed or produces no output.
    """
    if not pmd_rules:
        return ''

    source_path = os.path.abspath('source.java')
    ruleset_path = os.path.abspath('cqp_ruleset.xml')

    try:
        with open(source_path, 'w', encoding='utf-8') as f:
            f.write(source_code)

        ruleset_xml = _build_ruleset_xml(pmd_rules)
        with open(ruleset_path, 'w', encoding='utf-8') as f:
            f.write(ruleset_xml)

        cmd = _get_pmd_base_cmd() + [
            '-d', source_path,
            '-R', ruleset_path,
            '-f', 'xml',
            '--no-cache',
        ]
        result = subprocess.run(
            cmd,
            capture_output=True, text=True, timeout=30,
        )
        return result.stdout or result.stderr

    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        return ''
    finally:
        for path in (source_path, ruleset_path):
            try:
                os.remove(path)
            except OSError:
                pass


# ---------------------------------------------------------------------------
# PMD XML output parser
# ---------------------------------------------------------------------------

def _parse_pmd_xml(xml_output, codes_map):
    """
    Parse PMD XML output and return Violation dicts for rules in codes_map.

    Extracts beginline and rule attributes from each <violation> element.
    Attribute order in the XML is not guaranteed, so each attribute is
    matched independently.
    """
    violations = []
    attr_re = re.compile(r'\b(\w+)="([^"]*)"')
    viol_re = re.compile(r'<violation\b([^>]*)(?:/>|>)', re.DOTALL)

    for viol_match in viol_re.finditer(xml_output):
        attrs = dict(attr_re.findall(viol_match.group(1)))
        line_no = attrs.get('beginline', '0')
        rule = attrs.get('rule', '')
        if rule in codes_map:
            _, explanation = codes_map[rule]
            raw = f'source.java:{line_no}: [{rule}]'
            violations.append({
                'code': rule,
                'line_no': line_no,
                'raw': raw,
                'explanation': explanation,
            })

    return violations


# ---------------------------------------------------------------------------
# Custom checker runner
# ---------------------------------------------------------------------------

def _run_custom(source_code, rules):
    """
    Run custom checks and return violation lines in the standard format.
    Imports lazily so the tool still works if this file is not deployed.
    """
    try:
        from cqp_custom_checkers_java import run_custom_checks
        return run_custom_checks(source_code, rules)
    except ImportError:
        return ''


def _parse_custom_output(output, codes_map):
    """
    Parse custom checker output (source.java:LINE:COL: RuleName symbolic-name)
    into Violation dicts.
    """
    violations = []
    pattern = re.compile(r':(\d+):\d+: (\w+)')

    for line in output.splitlines():
        m = pattern.search(line)
        if m:
            line_no = m.group(1)
            rule = m.group(2)
            if rule in codes_map:
                _, explanation = codes_map[rule]
                violations.append({
                    'code': rule,
                    'line_no': line_no,
                    'raw': line.strip(),
                    'explanation': explanation,
                })

    return violations


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

def check_principles(source_code, principle_keys):
    """
    Run PMD and custom checks against source_code for all active principles.

    Returns a list of PrincipleResult dicts (one per principle, regardless
    of whether violations were found), in the same order as principle_keys.

    Unknown keys are silently skipped.
    """
    valid = {k: PRINCIPLES[k] for k in principle_keys if k in PRINCIPLES}

    all_codes = {}
    code_to_principle = {}
    for key, principle in valid.items():
        for rule, (_, explanation) in principle['codes'].items():
            all_codes[rule] = ('', explanation)
            code_to_principle[rule] = key

    pmd_rules = [r for r in all_codes if r not in CUSTOM_RULES]
    custom_rules = [r for r in all_codes if r in CUSTOM_RULES]

    by_principle = {key: [] for key in valid}

    if pmd_rules:
        xml_output = _run_pmd(pmd_rules, source_code)
        for v in _parse_pmd_xml(xml_output, all_codes):
            by_principle[code_to_principle[v['code']]].append(v)

    if custom_rules:
        custom_output = _run_custom(source_code, custom_rules)
        for v in _parse_custom_output(custom_output, all_codes):
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
