import json
import os
import re
import subprocess
from cqp_checker_java import check_principles

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


def _strip_public_class(source):
    """Remove 'public' from top-level class/interface/enum so student code and
    __tester__ can coexist in a single compilation unit."""
    return re.sub(
        r'\bpublic(\s+(?:(?:abstract|final|strictfp)\s+)*(?:class|interface|enum)\b)',
        r'\1',
        source,
    )


def build_feedback_html(results):
    failed = [r for r in results if r.get('violations')]

    annotations = []
    blocks = []

    for result in failed:
        name = result.get('name')
        principle = result.get('principle')
        rationale = result.get('rationale')

        violation_items = []
        for v in result.get('violations', []):
            line_no = v.get('line_no')
            raw = v.get('raw')
            explanation = v.get('explanation')

            violation_items.append(
                f'<li>Line {line_no}: <code>{raw}</code><br>'
                f'Why this matters: {explanation}</li>'
            )
            annotations.append({
                'row': int(line_no) - 1,
                'column': 0,
                'text': f'[{name}] {explanation}',
                'type': 'warning',
            })

        violations_html = '<ul>' + ''.join(violation_items) + '</ul>'
        blocks.append(
            f'<div style="margin-bottom:1em;">'
            f'<div><b>CQP Principle: {name}</b></div>'
            f'<div><i>{principle}</i></div>'
            f'<div>Rationale: {rationale}</div>'
            f'{violations_html}'
            f'</div>'
        )

    feedback_html = '<hr>'.join(blocks)
    feedback_html += '<b>Please fix the above style issues and resubmit.</b>'

    annotations_json = json.dumps(annotations)

    script = (
        '<style>.ace_tooltip { white-space: pre-wrap !important; max-width: 400px !important; word-break: break-word !important; }</style>'
        '<script>'
        '(function() {'
        'var attempts = 0;'
        'var interval = setInterval(function() {'
        'attempts++;'
        'var divs = document.querySelectorAll(\'.ace_editor\');'
        'if (divs.length > 0) {'
        'ace.edit(divs[0]).getSession().setAnnotations(' + annotations_json + ');'
        'clearInterval(interval);'
        '} else if (attempts >= 20) {'
        'clearInterval(interval);'
        '}'
        '}, 100);'
        '})();'
        '</script>'
    )

    return feedback_html + script


_JVM_FLAGS = [
    '-Xmx96m',                       # heap
    '-Xms4m',                         # initial heap
    '-Xss256k',                       # thread stack (default 512k-1m)
    '-XX:+UseSerialGC',               # serial GC — lowest overhead
    '-XX:CompressedClassSpaceSize=16m',
    '-XX:MaxMetaspaceSize=48m',
    '-XX:ReservedCodeCacheSize=32m',  # JIT code cache (default 240m!)
    '-XX:-TieredCompilation',         # disable tiered JIT — saves memory
]
_JAVAC_FLAGS = [f'-J{f}' for f in _JVM_FLAGS]


def run_tests():
    student_code = _strip_public_class(__student_answer__)

    env = os.environ.copy()
    for var in ('JAVA_TOOL_OPTIONS', '_JAVA_OPTIONS', 'JDK_JAVA_OPTIONS'):
        env.pop(var, None)

    test_results = [['Test', 'Expected', 'Got', 'iscorrect']]
    total = len(__test_cases__)
    passed = 0

    for tc in __test_cases__:
        testcode = tc['testcode'].strip()
        expected = tc['expected'].strip()
        stdin_text = tc.get('stdin', '') or ''

        indented = '\n'.join('        ' + line for line in testcode.splitlines())
        combined = (
            student_code + '\n\n'
            'public class __tester__ {\n'
            '    public static void main(String[] args) throws Exception {\n'
            + indented + '\n'
            '    }\n'
            '}\n'
        )

        with open('__tester__.java', 'w', encoding='utf-8') as f:
            f.write(combined)

        compile_result = subprocess.run(
            ['javac'] + _JAVAC_FLAGS + ['__tester__.java'],
            capture_output=True, text=True,
            env=env,
        )

        if compile_result.returncode != 0:
            error_msg = compile_result.stderr or compile_result.stdout or 'Compilation error'
            test_results.append([testcode, expected, f'Compilation failed:\n{error_msg.strip()}', 0])
            continue

        try:
            result = subprocess.run(
                ['java'] + _JVM_FLAGS + ['__tester__'],
                input=stdin_text,
                capture_output=True, text=True,
                timeout=10,
                env=env,
            )
            got = result.stdout.strip()
            ok = got == expected
            passed += 1 if ok else 0
            test_results.append([testcode, expected, got, 1 if ok else 0])
        except subprocess.TimeoutExpired:
            test_results.append([testcode, expected, 'Time limit exceeded', 0])
        except Exception as e:
            test_results.append([testcode, expected, str(e), 0])

    fraction = passed / total if total > 0 else 0
    return fraction, test_results


# --- Main grading logic ---
{% if IS_PRECHECK %}
results = check_principles(__student_answer__, ACTIVE_PRINCIPLES)
failed = [r for r in results if r.get('violations')]

if failed:
    feedback_html = build_feedback_html(results)
    placeholder_rows = [['Test', 'Expected', 'Got', 'iscorrect']] + [
        [tc['testcode'], tc['expected'], '— style check failed —', 0]
        for tc in __test_cases__
    ]
    outcome = {
        'fraction': 0,
        'epiloguehtml': feedback_html,
        'testresults': placeholder_rows,
    }
else:
    outcome = {
        'fraction': 1,
        'epiloguehtml': '<p><b>Style check passed.</b> Submit your answer when ready.</p>',
        'testresults': [['Style Check', 'Pass', 'Pass', 1]],
    }
{% else %}
fraction, test_results = run_tests()
outcome = {
    'fraction': fraction,
    'epiloguehtml': '',
    'testresults': test_results,
}
{% endif %}

print(json.dumps(outcome))
