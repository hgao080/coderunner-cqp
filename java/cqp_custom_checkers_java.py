"""
cqp_custom_checkers_java.py — Custom CQP checks for Java that PMD does not
cover with a standard built-in rule.

Public interface:
    run_custom_checks(source_code, rules) -> str

Returns raw violation lines in the format:
    source.java:LINE:COL: RuleName symbolic-name

This format is identical to what _parse_violations in cqp_checker_java.py
expects, so all three runners (PMD, custom) share the same parser.

Custom rules:
    LineLength       — line exceeds 100 characters (Clear Presentation)
    FieldVisibility  — non-private/protected field at class level (Modular Structure)
    CastUse          — cast expression outside equals(Object) (Problem Alignment)
    InstanceOfUse    — instanceof expression outside equals(Object) (Problem Alignment)
"""

import re

LINE_LENGTH_LIMIT = 100


def run_custom_checks(source_code, rules):
    """
    Run custom checks for the given set of rule name strings.
    Returns a raw violation string (one line per violation).
    """
    rules = set(rules)
    lines = []

    if 'LineLength' in rules:
        for lineno, col, rule in _check_line_length(source_code):
            lines.append(f'source.java:{lineno}:{col}: {rule} line-too-long')

    if 'FieldVisibility' in rules:
        for lineno, col, rule in _check_field_visibility(source_code):
            lines.append(f'source.java:{lineno}:{col}: {rule} field-visibility')

    if 'CastUse' in rules or 'InstanceOfUse' in rules:
        cast_viols, instanceof_viols = _check_cast_and_instanceof(source_code)
        if 'CastUse' in rules:
            for lineno, col, rule in cast_viols:
                lines.append(f'source.java:{lineno}:{col}: {rule} cast-use')
        if 'InstanceOfUse' in rules:
            for lineno, col, rule in instanceof_viols:
                lines.append(f'source.java:{lineno}:{col}: {rule} instanceof-use')

    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# LineLength
# ---------------------------------------------------------------------------

def _check_line_length(source_code):
    violations = []
    for i, line in enumerate(source_code.splitlines(), 1):
        if len(line) > LINE_LENGTH_LIMIT:
            violations.append((i, LINE_LENGTH_LIMIT + 1, 'LineLength'))
    return violations


# ---------------------------------------------------------------------------
# FieldVisibility
# ---------------------------------------------------------------------------

def _check_field_visibility(source_code):
    """
    Flag public field declarations at class level that are not constants
    (public static final). Uses brace counting to identify class scope.

    Limitations: brace counting does not account for braces inside string
    literals or comments — may produce false results in pathological cases,
    but is reliable for typical CS1/CS2 Java code.
    """
    violations = []
    lines = source_code.splitlines()

    depth = 0
    class_depth = None

    for i, line in enumerate(lines, 1):
        stripped = _strip_line_comment(line).strip()

        open_count = stripped.count('{')
        close_count = stripped.count('}')
        depth += open_count - close_count

        if class_depth is None and re.search(r'\bclass\b', stripped) and open_count > 0:
            class_depth = depth

        if class_depth is None or depth != class_depth:
            continue

        # At class level: look for public non-constant, non-method declarations.
        # Exclude: public static final (constants), class/interface/enum headers,
        # method declarations (contain a '(' before ';' or '{').
        if not stripped.startswith('public'):
            continue
        if 'static' in stripped and 'final' in stripped:
            continue
        if re.search(r'\b(class|interface|enum|@interface)\b', stripped):
            continue
        # If there is a '(' before a ';' or end-of-content it is a method signature.
        before_semi = stripped.split(';')[0]
        if '(' in before_semi:
            continue

        violations.append((i, 0, 'FieldVisibility'))

    return violations


def _strip_line_comment(line):
    """Remove a trailing // comment from a line (naively — ignores strings)."""
    idx = line.find('//')
    return line[:idx] if idx >= 0 else line


# ---------------------------------------------------------------------------
# CastUse / InstanceOfUse — shared equals() body detection
# ---------------------------------------------------------------------------

def _check_cast_and_instanceof(source_code):
    """
    Return (cast_violations, instanceof_violations).

    Both checks exclude the body of any equals(Object ...) method because
    casts and instanceof are acceptable idioms there.

    Brace counting is used to track method scope; same limitations as above.
    """
    cast_violations = []
    instanceof_violations = []

    lines = source_code.splitlines()
    depth = 0
    in_equals = False
    equals_depth = None

    # Matches reference-type casts: (TypeName) or (TypeName<...>)
    # Requires the cast to be followed by a word character or '(' so we
    # don't match ordinary parenthesised expressions.
    cast_re = re.compile(r'\(\s*[A-Z]\w*(?:\s*<[^>]*>)?\s*\)\s*[\w("]')

    for i, line in enumerate(lines, 1):
        stripped = _strip_line_comment(line).strip()

        open_count = stripped.count('{')
        close_count = stripped.count('}')
        depth += open_count - close_count

        # Detect entry into an equals(Object ...) method.
        if re.search(r'\bpublic\s+boolean\s+equals\s*\(\s*Object\b', stripped):
            in_equals = True
            equals_depth = depth - open_count  # depth before this line's braces

        # Detect exit from equals() when we return to the pre-method depth.
        if in_equals and equals_depth is not None and depth <= equals_depth:
            in_equals = False
            equals_depth = None

        if in_equals:
            continue

        # Skip comment lines.
        if stripped.startswith('//') or stripped.startswith('*'):
            continue

        if cast_re.search(stripped):
            cast_violations.append((i, 0, 'CastUse'))

        if re.search(r'\binstanceof\b', stripped):
            instanceof_violations.append((i, 0, 'InstanceOfUse'))

    return cast_violations, instanceof_violations
