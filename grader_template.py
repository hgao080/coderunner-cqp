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
        "stdin": """{{ TEST.stdin | e("py") }}""",
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
        "<style>.ace_tooltip { white-space: pre-wrap !important; max-width: 400px !important; word-break: break-word !important; }</style>"
        "<script>"
        "(function() {"
        "var attempts = 0;"
        "var interval = setInterval(function() {"
        "attempts++;"
        "var divs = document.querySelectorAll('.ace_editor');"
        "if (divs.length > 0) {"
        "ace.edit(divs[0]).getSession().setAnnotations(" + annotations_json + ");"
        "clearInterval(interval);"
        "} else if (attempts >= 20) {"
        "clearInterval(interval);"
        "}"
        "}, 100);"
        "})();"
        "</script>"
    )

    return feedback_html + script


def run_tests():
    test_results = [["Test", "Expected", "Got", "iscorrect"]]
    total = len(__test_cases__)
    passed = 0

    exec_env = {}

    def _no_stdin_input(prompt=''):
        raise EOFError("input() called at module level — move input() calls inside a function")

    exec_env['input'] = _no_stdin_input
    try:
        exec(__student_answer__, exec_env)
    except Exception as e:
        for tc in __test_cases__:
            test_results.append([tc["testcode"], tc["expected"], str(e), 0])
        return 0, test_results

    for tc in __test_cases__:
        testcode = tc["testcode"]
        expected = tc["expected"].strip()
        stdin_text = tc.get("stdin", "") or ""
        stdin_lines = stdin_text.splitlines()
        try:
            buf = io.StringIO()
            test_env = dict(exec_env)
            test_env['input'] = make_fake_input(stdin_lines, buf)
            with contextlib.redirect_stdout(buf):
                exec(testcode, test_env)
            got = buf.getvalue().strip()
            ok = got == expected
            passed += 1 if ok else 0
            test_results.append([testcode, expected, got, 1 if ok else 0])
        except Exception as e:
            test_results.append([testcode, expected, str(e), 0])

    fraction = passed / total if total > 0 else 0
    return fraction, test_results


def make_fake_input(stdin_lines, stdout_buf):
    iterator = iter(stdin_lines)

    def fake_input(prompt=''):
        stdout_buf.write(str(prompt))
        try:
            value = next(iterator)
        except StopIteration:
            raise EOFError("No more input lines available for this test case")
        stdout_buf.write(value + '\n')
        return value

    return fake_input


# --- Main grading logic ---
{% if IS_PRECHECK %}
results = check_principles(__student_answer__, ACTIVE_PRINCIPLES)
failed = [r for r in results if r.get("violations")]

if failed:
    feedback_html = build_feedback_html(results)
    placeholder_rows = [["Test", "Expected", "Got", "iscorrect"]] + [
        [tc["testcode"], tc["expected"], "— style check failed —", 0]
        for tc in __test_cases__
    ]
    outcome = {
        "fraction": 0,
        "epiloguehtml": feedback_html,
        "testresults": placeholder_rows
    }
else:
    outcome = {
        "fraction": 1,
        "epiloguehtml": "<p><b>Style check passed.</b> Submit your answer when ready.</p>",
        "testresults": [["Style Check", "Pass", "Pass", 1]]
    }
{% else %}
fraction, test_results = run_tests()
outcome = {
    "fraction": fraction,
    "epiloguehtml": "",
    "testresults": test_results
}
{% endif %}

print(json.dumps(outcome))