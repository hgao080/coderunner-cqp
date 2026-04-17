import sys
import json
import io
import contextlib
from cqp_checker import check_principles

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

# Student answer and all test cases, injected by Twig
__student_answer__ = """{{ STUDENT_ANSWER | e("py") }}"""

__test_cases__ = [
{% for TEST in TESTCASES %}
    {
        "testcode": """{{ TEST.testcode | e("py") }}""",
        "expected": """{{ TEST.expected | e("py") }}""",
    },
{% endfor %}
]


def build_feedback_html(results):
    failed = [r for r in results if r.get("violations")]

    annotations = []
    feedback_lines = []

    for result in failed:
        name = result.get("name")
        principle = result.get("principle")
        rationale = result.get("rationale")

        feedback_lines.append("<hr>")
        feedback_lines.append(f"<b>CQP Principle: {name}</b><br>")
        feedback_lines.append(f"<i>{principle}</i><br>")
        feedback_lines.append(f"Rationale: {rationale}<br>")

        for v in result.get("violations", []):
            line_no = v.get("line_no")
            raw = v.get("raw")
            explanation = v.get("explanation")

            feedback_lines.append(
                f"<br>Line {line_no}: <code>{raw}</code><br>"
                f"&nbsp;&nbsp;Why this matters: {explanation}<br>"
            )
            annotations.append({
                "row": int(line_no) - 1,
                "column": 0,
                "text": f"[{name}] {explanation}",
                "type": "warning"
            })

    feedback_html = "\n".join(feedback_lines)
    feedback_html += "<br><b>Please fix the above style issues and resubmit.</b>"

    annotations_json = json.dumps(annotations)

    # Use epiloguehtml so this renders below the result table and answer box,
    # avoiding any DOM disruption to the Ace editor above.
    # We retrieve the existing Ace instance via ace.edit() which returns the
    # existing instance if the element has already been initialised.
    script = (
        "<script>"
        "(function() {"
        "function applyAnnotations() {"
        "var divs = document.querySelectorAll('.ace_editor');"
        "if (divs.length === 0) return;"
        "var editor = ace.edit(divs[0]);"
        "var annotations = " + annotations_json + ";"
        "editor.getSession().setAnnotations(annotations);"
        "}"
        "setTimeout(applyAnnotations, 500);"
        "})();"
        "</script>"
    )

    return feedback_html + script


def run_tests():
    test_results = [["Test", "Expected", "Got", "Pass?"]]
    total = len(__test_cases__)
    passed = 0

    exec_env = {}
    try:
        exec(__student_answer__, exec_env)
    except Exception as e:
        for tc in __test_cases__:
            test_results.append([tc["testcode"], tc["expected"], str(e), "✗"])
        return 0, test_results

    for tc in __test_cases__:
        testcode = tc["testcode"]
        expected = tc["expected"].strip()
        try:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                exec(testcode, dict(exec_env))
            got = buf.getvalue().strip()
            ok = got == expected
            passed += 1 if ok else 0
            test_results.append([testcode, expected, got, "✓" if ok else "✗"])
        except Exception as e:
            test_results.append([testcode, expected, str(e), "✗"])

    fraction = passed / total if total > 0 else 0
    return fraction, test_results


# --- Main grading logic ---
results = check_principles(__student_answer__, ACTIVE_PRINCIPLES)
failed = [r for r in results if r.get("violations")]

if failed:
    feedback_html = build_feedback_html(results)
    outcome = {
        "fraction": 0,
        "epiloguehtml": feedback_html,
        "testresults": []
    }
else:
    fraction, test_results = run_tests()
    outcome = {
        "fraction": fraction,
        "epiloguehtml": "",
        "testresults": test_results
    }

print(json.dumps(outcome))