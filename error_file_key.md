# Error File — Instructor Answer Key

**For instructor use only.** Documents all intended violations in `error_file.py` for the CQP study.

The error file is a realistic beginner Python submission for a coin collection tracker. Students examine it across three study phases: initial written response, post-lab revision, and tool-based self-evaluation.

All violations are statically detectable (Pylint, pycodestyle, or custom W90xx checkers). No human-judgment violations are included.

---

## Violation Summary

21 violations across 6 CQP principles. Expected student find-rate in ~30 min: 10–13.

| # | Code | Principle | Line | Difficulty |
|---|------|-----------|------|------------|
| 1 | C0114 | Explanatory Language | — | Obvious |
| 2 | C0410 | Clear Presentation | 1 | Obvious |
| 3 | W0611 | Used Content | 1 | Obvious |
| 4 | W0611 | Used Content | 1 | Obvious |
| 5 | C0116 | Explanatory Language | 4 | Obvious |
| 6 | E302 | Clear Presentation | 4 | Subtle |
| 7 | W9005 | Modular Structure | 5 | Subtle |
| 8 | C0116 | Explanatory Language | 11 | Obvious |
| 9 | E302 | Clear Presentation | 11 | Subtle |
| 10 | C0103 | Explanatory Language | 14 | Subtle |
| 11 | C0121 | Simple Constructs | 18 | Obvious |
| 12 | C0116 | Explanatory Language | 22 | Obvious |
| 13 | E302 | Clear Presentation | 22 | Subtle |
| 14 | W9003 | Consistent Code | 26 | Subtle |
| 15 | W0107 | Used Content | 28 | Subtle |
| 16 | R1710 | Consistent Code | 22–30 | Obvious |
| 17 | E302 | Clear Presentation | 32 | Subtle |
| 18 | C0116 | Explanatory Language | 32 | Obvious |
| 19 | W0613 | Used Content | 32 | Subtle |
| 20 | W0612 | Used Content | 35 | Subtle |
| 21 | C0301 | Clear Presentation | 36 | Obvious |

---

## Violations by Principle

### Clear Presentation

- `C0410` — Line 1: `import os, random` places two modules on one import line. Each module should be on its own line so the file's dependencies are immediately clear.
- `E302` — Line 4: `def get_total` is preceded by 0 blank lines. Two blank lines are required before every top-level function definition.
- `E302` — Line 11: `def find_rarest` is preceded by 1 blank line. Two required.
- `E302` — Line 22: `def format_collection` is preceded by 1 blank line. Two required.
- `E302` — Line 32: `def show_details` is preceded by 1 blank line. Two required.
- `C0301` — Line 36: the `print` statement is approximately 105 characters including indentation, exceeding the 79-character limit.

---

### Explanatory Language

- `C0114` — (file level): the file has no module docstring. A brief description at the top orients the reader before they read any code.
- `C0116` — Line 4: `get_total` has no docstring.
- `C0116` — Line 11: `find_rarest` has no docstring.
- `C0116` — Line 22: `format_collection` has no docstring.
- `C0116` — Line 32: `show_details` has no docstring.
- `C0103` — Line 14: the loop variable `x` is a single-character, non-descriptive name. A name like `coin` or `denomination` would communicate what is being iterated.

---

### Consistent Code

- `W9003` — Line 26: `' cents'` uses single quotes while all other string literals in the file use double quotes. One quote style should be used consistently throughout.
- `R1710` — Lines 22–30: `format_collection` returns a list value (`return result`) when `coins` is non-empty but falls through (implicitly returns `None`) when `coins` is empty. All return paths should return a value of the same type.

---

### Used Content

- `W0611` — Line 1: `os` is imported but never used anywhere in the file.
- `W0611` — Line 1: `random` is imported but never used anywhere in the file.
- `W0107` — Line 28: `pass` inside the `for` loop body serves no purpose. The loop body already has three statements; `pass` adds no meaning and misleads the reader.
- `W0613` — Line 32: the `owner` parameter of `show_details` is never used inside the function body.
- `W0612` — Line 35: `formatted` is assigned the return value of `format_collection(coins)` but is never read.

---

### Simple Constructs

- `C0121` — Line 18: `if rarest == None:` compares against `None` using `==`. The simpler, idiomatic form is `if rarest is None:`.

---

### Modular Structure

- `W9005` — Line 5: `MULTIPLIER = 100` uses an ALL_CAPS name, signalling a constant, but is defined inside a function body. Constants should be defined at module level so they are easy to find and can be shared across functions.

---

## Student Response Format

Each violation should be reported using:

```
Violation: [line number / description]
CQP Principle: [principle name]
Why it matters: [explanation]
```

---

## Verification

Run the checker against `error_file.py` with all six covered principles:

```python
from cqp_checker import check_principles

with open("error_file.py") as f:
    src = f.read()

results = check_principles(src, [
    "clear_presentation",
    "explanatory_language",
    "consistent_code",
    "used_content",
    "simple_constructs",
    "modular_structure",
])

for r in results:
    if r["violations"]:
        print(f"\n=== {r['name']} ===")
        for v in r["violations"]:
            print(f"  Line {v['line_no']}: [{v['code']}] {v['raw']}")
```

Expected: 21 violations across 6 principles. If `W9003` or `W9005` are absent, confirm `cqp_custom_checkers.py` is on the Python path.
