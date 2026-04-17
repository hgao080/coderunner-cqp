import sys
from cqp_checker import check_principles

# -----------------------------------------------------------------------
# Configure which CQP principles to check for this question.
#
# Set via Template Parameters (JSON) in the question authoring form:
#   {"cqp_principles": ["clear_presentation", "explanatory_language"]}
#
# Or use a single principle:
#   {"cqp_principles": "used_content"}
#
# Available principle keys:
#   'clear_presentation'    - Layout, formatting, indentation
#   'explanatory_language'  - Naming, docstrings, comments
#   'consistent_code'       - Consistent style choices
#   'used_content'          - No unused imports/variables
#   'simple_constructs'     - Minimize complexity
#   'minimal_duplication'   - Avoid code repetition
#   'modular_structure'     - Good function/class design
#   'problem_alignment'     - Implementation matches problem
#
# If no parameters are provided, defaults to all principles.
# -----------------------------------------------------------------------

# Read from template parameters, with fallback to all principles
{% if cqp_principles is defined %}
{% if cqp_principles is iterable %}
ACTIVE_PRINCIPLES = [{% for p in cqp_principles %}'{{ p }}'{% if not loop.last %}, {% endif %}{% endfor %}]
{% else %}
ACTIVE_PRINCIPLES = ['{{ cqp_principles }}']
{% endif %}
{% else %}
ACTIVE_PRINCIPLES = [
    'clear_presentation',
    'explanatory_language',
    'consistent_code',
    'used_content',
    'simple_constructs',
    'minimal_duplication',
    'modular_structure',
    'problem_alignment',
]
{% endif %}


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
