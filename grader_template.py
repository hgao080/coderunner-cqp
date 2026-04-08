import sys
from cqp_checker import check_principles

# -----------------------------------------------------------------------
# Configure which CQP principles to check for this question.
# Add or remove keys to match the learning objectives of the question.
#
# Available keys:
#   'explanatory_language'
#   'clear_layout'
#   'simple_constructs'
#   'be_consistent'
#   'no_unused_content'
#   'congruent_implementation'
#   'avoid_duplication'
#   'modular_structure'
# -----------------------------------------------------------------------
ACTIVE_PRINCIPLES = [
    'no_unused_content',
]


def code_ok(source_code):
    results = check_principles(source_code, ACTIVE_PRINCIPLES)

    # Collect only principles that have violations.
    failed = [r for r in results if r['violations']]

    if not failed:
        return True

    # Print one feedback block per failed principle.
    for result in failed:
        print('=' * 60, file=sys.stderr)
        print(f"CQP Principle: {result['name']}", file=sys.stderr)
        print(f"Principle:     {result['principle']}", file=sys.stderr)
        print(f"Rationale:     {result['rationale']}", file=sys.stderr)
        print('=' * 60, file=sys.stderr)

        for v in result['violations']:
            print(f"\n  Line {v['line_no']}: {v['raw']}", file=sys.stderr)
            print(f"  Why this matters: {v['explanation']}", file=sys.stderr)

        print('', file=sys.stderr)

    print("Please fix the above style issues and resubmit.", file=sys.stderr)
    return False


__student_answer__ = """{{ STUDENT_ANSWER | e('py') }}"""
if code_ok(__student_answer__):
    __student_answer__ += '\n' + """{{ TEST.testcode | e('py') }}"""
    exec(__student_answer__)
