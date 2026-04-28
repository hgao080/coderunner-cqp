# CQP CodeRunner Study Questions

Two sets of questions for COMPSCI 101 (Principles of Programming), University of Auckland. Each question uses the custom `grader_template.py` which runs Pylint / pycodestyle / custom checks before executing functional test cases. Style violations must be resolved before the test score is awarded.

All questions use **type `python3_cqp`**. The grader blocks `input()` at module level, so all submissions must be function-based. Early-semester questions provide a function stub for students to complete, which is standard scaffolding in CS1 regardless of whether functions have been formally taught.

Guidelines are referenced by ID from Tables 5 and 6 of: Kirk, Luxton-Reilly & Tempero, *Distilling PEP 8 for Teaching Introductory Programming*, ACE 2025.

---

## SET A — Questions organised by teaching topic

---

### A1 — Variables & Expressions: BMI Calculator

**Question type**: `python3`

**Justification**: The grader's module-level `input()` block means script-style submissions error before the style check runs. A single-function stub is the cleanest vehicle for naming and alignment violations at variables/expressions level and matches the format of existing test questions in this repo.

---

**Task description (shown to student)**:

Complete the function below. It receives a person's height in metres and weight in kilograms, and should **return** their BMI rounded to one decimal place.

BMI = weight ÷ (height × height)

Include a brief description of your file at the very top (a triple-quoted string). Do **not** add any `input()` calls — only the function body is needed.

```python
def calculate_bmi(height, weight):
    pass
```

---

**Target guidelines and CQP/CSM mapping**:

| Primer ID | Guideline | CSM Principle | CQP key |
|-----------|-----------|--------------|---------|
| 1–3 | Recognise and use a consistent naming style; use descriptive names | Explanatory Language | `explanatory_language` |
| 4 | Never use `l`, `O`, or `I` as single-character variable names | Explanatory Language | `explanatory_language` |
| 5 | Limit lines to 79 characters | Clear Layout | `clear_presentation` |
| 7 | Use 4 spaces per indentation level | Clear Layout | `clear_presentation` |
| 31 | Always surround binary operators with a single space on either side | Clear Layout | `clear_presentation` |

**Template parameters**: `{"cqp_principles": ["explanatory_language", "clear_presentation"]}`

---

**Bad answer** (realistic beginner — abbreviates all names, omits operator spacing):

```python
def calculate_bmi(h, w):
    I=w/(h*h)
    return round(I,1)
```

**Violations triggered**:
- `C0103` × 3 — `h`, `w` (single-char, non-descriptive), `I` (single-char) → **explanatory_language** (IDs 3–4)
- `C0104` × 1 — `I` is a visually ambiguous single character (looks like `1`) → **explanatory_language** (ID 4)
- `C0114` — missing module docstring → **explanatory_language** (ID 13)
- `C0116` — missing function docstring → **explanatory_language** (ID 13)
- `E225` × 2 — `I=w/(h*h)` missing spaces around `=` and `/` → **clear_presentation** (ID 31)
- `E231` × 1 — `round(I,1)` missing space after `,` → **clear_presentation** (ID 36)

---

**Good answer**:

```python
"""BMI calculator functions."""


def calculate_bmi(height, weight):
    """Return BMI rounded to one decimal place."""
    bmi = weight / (height * height)
    return round(bmi, 1)
```

---

**Test case table**:

| Test # | Standard Input | Test code | Expected output | Visibility |
|--------|---------------|-----------|----------------|------------|
| 1 | — | `print(calculate_bmi(1.75, 70))` | `22.9` | visible |
| 2 | — | `print(calculate_bmi(1.60, 50))` | `19.5` | visible |
| 3 | — | `print(calculate_bmi(2.00, 100))` | `25.0` | hidden |
| 4 | — | `print(calculate_bmi(1.50, 45))` | `20.0` | hidden |
| 5 | — | `print(calculate_bmi(1.80, 90))` | `27.8` | hidden |

---

**Set A vs Set B note**: A topic-organised question like A1 tells a researcher how style awareness develops in step with programming concept complexity. A student encountering this question early in the semester receives style feedback in the context of the very first concepts they are learning — variables and arithmetic — so the violations (poor naming, missing spacing) arise naturally from the cognitive habits of a novice who is focused on getting the arithmetic right. Data from A1, A2, and A3 together can track whether style literacy improves as topics grow more complex, which is the central question for a longitudinal, topic-sequenced curriculum study. By contrast, the principle-organised counterpart (Set B, B1) holds the programming task constant and varies only the principle targeted, generating data about whether the Explanatory Language principle is adopted independent of when in the semester it is assessed.

---

### A2 — Conditionals: Grade Classifier

**Question type**: `python3`

**Justification**: A single function returning a letter grade requires exactly the kind of multi-branch conditional logic that naturally produces layout and spacing violations. The comparison operators (`>=`) are what students are focused on getting logically right, making spacing omissions realistic. Mixed-quote violations arise naturally when students transcribe return values from different sources.

---

**Task description (shown to student)**:

Complete the function below. It receives an integer exam score (0–100) and should **return** the corresponding letter grade: `"A"` for 85–100, `"B"` for 70–84, `"C"` for 55–69, `"D"` for 40–54, and `"F"` for below 40.

Include a brief description of your file at the very top. Do **not** add any `input()` calls.

```python
def get_grade(score):
    pass
```

---

**Target guidelines and CQP/CSM mapping**:

| Primer ID | Guideline | CSM Principle | CQP key |
|-----------|-----------|--------------|---------|
| 7 | Use 4 spaces per indentation level | Clear Layout | `clear_presentation` |
| 31 | Surround binary operators with a single space on either side | Clear Layout | `clear_presentation` |
| 36 | Avoid extraneous whitespace immediately inside parentheses or before a colon | Clear Layout | `clear_presentation` |
| 29 | Pick a quote style (single or double) and stick to it | Consistent Design | `consistent_code` |
| 33 | Use `is not` rather than `not … is` | Simple Constructs | `simple_constructs` |
| 34 | When comparing boolean values, don't include `== value` | Simple Constructs | `simple_constructs` |

**Template parameters**: `{"cqp_principles": ["clear_presentation", "consistent_code", "simple_constructs"]}`

---

**Bad answer** (realistic beginner — inconsistent formatting, mixed quote styles, inconsistent indentation):

```python
def get_grade( score ):
    if score>=85:
        return 'A'
    elif score>=70:
        return "B"
    elif score>=55:
        return 'C'
    elif score>=40:
        return "D"
    else:
      return "F"
```

**Violations triggered**:
- `E201`, `E202` — `get_grade( score )` has spaces inside parentheses → **clear_presentation** (ID 36)
- `E225` × 4 — `score>=85`, `score>=70`, `score>=55`, `score>=40` missing spaces around `>=` → **clear_presentation** (ID 31)
- `W9003` — single quotes for `'A'`, `'C'` mixed with double quotes for `"B"`, `"D"`, `"F"` → **consistent_code** (ID 29)
- `W0311` / `E111` — `return "F"` uses 2-space indent in the `else` block → **clear_presentation** (ID 7)

Note: `simple_constructs` is included in the template params so the grader flags it if a student uses `== True` or `not score >= 85`. The bad answer above does not trigger it, which is intentional: a realistic beginner making layout mistakes is not necessarily making construct mistakes simultaneously.

---

**Good answer**:

```python
"""Grade classification functions."""


def get_grade(score):
    """Return the letter grade for the given exam score."""
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 55:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"
```

---

**Test case table**:

| Test # | Standard Input | Test code | Expected output | Visibility |
|--------|---------------|-----------|----------------|------------|
| 1 | — | `print(get_grade(90))` | `A` | visible |
| 2 | — | `print(get_grade(75))` | `B` | visible |
| 3 | — | `print(get_grade(60))` | `C` | hidden |
| 4 | — | `print(get_grade(45))` | `D` | hidden |
| 5 | — | `print(get_grade(30))` | `F` | hidden |
| 6 | — | `print(get_grade(85))` | `A` | hidden (lower boundary of A) |
| 7 | — | `print(get_grade(40))` | `D` | hidden (lower boundary of D) |

---

**Set A vs Set B note**: Placing this question at the Conditionals stage means students encounter it when they have just mastered `if`/`elif`/`else` syntax and are focused on getting the branching logic right. The layout violations — missing operator spaces, inconsistent indentation in the else clause, extraneous whitespace in the function signature — emerge naturally when cognitive load is high and formatting is an afterthought. A topic-organised study tracks whether students who receive style feedback at this stage retain it when they later write loops and functions. The principle-organised counterpart (Set B, B2) targets overlapping layout violations in a different task at a potentially different point in the semester, generating data about the persistence of the Clear Layout principle across tasks rather than its acquisition at a specific topic stage.

---

### A3 — Functions: Temperature Utilities

**Question type**: `python3`

**Justification**: A two-function question is the minimum needed to naturally elicit function-level style guidelines — blank lines between definitions, consistent return statements, function naming conventions. Splitting conversion and classification across two functions also makes an unused import realistic: a student who begins with `import math` for potential `sqrt` use before realising it is not needed.

---

**Task description (shown to student)**:

Write the two functions described below. Do **not** include any `input()` calls — only the function definitions are needed. Include a brief description of your file at the top.

**Function 1** — `celsius_to_fahrenheit(celsius)`: converts a Celsius temperature to Fahrenheit and **returns** the result as a float. Formula: F = C × 9 / 5 + 32

**Function 2** — `classify_temperature(celsius)`: **returns** `"cold"` if the temperature is below 10°C, `"warm"` if it is 10–25°C (inclusive), and `"hot"` if it is above 25°C.

---

**Target guidelines and CQP/CSM mapping**:

| Primer ID | Guideline | CSM Principle | CQP key |
|-----------|-----------|--------------|---------|
| 1–4 | Descriptive names; no single-char or ambiguous names | Explanatory Language | `explanatory_language` |
| 37 | Function names should be lowercase with underscores | Explanatory Language | `explanatory_language` |
| 38 | Surround top-level function definitions with two blank lines | Clear Layout | `clear_presentation` |
| 39 | Use blank lines in functions sparingly to indicate logical sections | Clear Layout | `clear_presentation` |
| 40 | Be consistent in return statements (all return an expression or none do) | Consistent Design | `consistent_code` |
| 41 | Parameter names should be descriptive and not clash with reserved words | Explanatory Language | `explanatory_language` |
| 31 | Surround binary operators with a single space on either side | Clear Layout | `clear_presentation` |

**Template parameters**: `{"cqp_principles": ["explanatory_language", "clear_presentation", "consistent_code", "used_content"]}`

---

**Bad answer** (realistic beginner — abbreviated names, no blank lines between functions, unused import, bare `return`):

```python
import math
def CtoF(c):
    return c*9/5+32
def ClassifyTemp(c):
    if c<10:
        return "cold"
    elif c<=25:
        return "warm"
    return
```

**Violations triggered**:
- `W0611` — `math` imported but unused → **used_content** (Non-redundant Content)
- `C0103` × 4 — `CtoF` (not lowercase_underscores), `ClassifyTemp` (not lowercase_underscores), `c` × 2 (single-char parameter) → **explanatory_language** (IDs 3–4, 37, 41)
- `C0114` — missing module docstring → **explanatory_language** (ID 13)
- `C0116` × 2 — missing function docstrings → **explanatory_language** (ID 13)
- `E302` × 2 — `def CtoF` and `def ClassifyTemp` each missing 2 blank lines before them → **clear_presentation** (ID 38)
- `E225` × 3 — `c*9/5+32`, `c<10`, `c<=25` missing spaces → **clear_presentation** (ID 31)
- `R1710` — `ClassifyTemp` has `return "cold"` and `return "warm"` (expressions) but a bare `return` (returns `None`) at the end → **consistent_code** (ID 40)

Note: the bare `return` also makes `ClassifyTemp` logically incorrect for temperatures above 25°C (returns `None` instead of `"hot"`). This is intentional — R1710 catches a real bug masquerading as a style issue, which is a strong teaching moment about why consistent return statements matter.

---

**Good answer**:

```python
"""Temperature conversion and classification utilities."""


def celsius_to_fahrenheit(celsius):
    """Return the Fahrenheit equivalent of the given Celsius temperature."""
    return celsius * 9 / 5 + 32


def classify_temperature(celsius):
    """Return 'cold', 'warm', or 'hot' based on the Celsius temperature."""
    if celsius < 10:
        return "cold"
    elif celsius <= 25:
        return "warm"
    else:
        return "hot"
```

---

**Test case table**:

| Test # | Standard Input | Test code | Expected output | Visibility |
|--------|---------------|-----------|----------------|------------|
| 1 | — | `print(celsius_to_fahrenheit(0))` | `32.0` | visible |
| 2 | — | `print(classify_temperature(5))` | `cold` | visible |
| 3 | — | `print(celsius_to_fahrenheit(100))` | `212.0` | hidden |
| 4 | — | `print(celsius_to_fahrenheit(-40))` | `-40.0` | hidden |
| 5 | — | `print(classify_temperature(10))` | `warm` | hidden (lower boundary of warm) |
| 6 | — | `print(classify_temperature(25))` | `warm` | hidden (upper boundary of warm) |
| 7 | — | `print(classify_temperature(26))` | `hot` | hidden |

---

**Set A vs Set B note**: This question sits at a natural inflection point in CS1 where style complexity peaks: students must simultaneously manage naming at the function and parameter level, blank-line layout between definitions, docstring placement, return-statement consistency, and unused import removal. The data it generates — which principles are most frequently violated when students write multi-function code for the first time — complements A1 and A2 by revealing whether style challenges compound as topic complexity grows. The principle-organised equivalents in Set B isolate Explanatory Language (B1) or Clear Layout (B2), making it easier to track a single principle's acquisition curve but harder to observe how all principles interact within a realistic multi-function programming task.

---

## SET B — Questions organised by CQP principle

---

### B1 — Explanatory Language: Discount Calculator

**Question type**: `python3`

**Justification**: A discount calculation requires several distinctly named elements (function name, two parameters, one intermediate variable) while keeping the arithmetic simple enough that a student can attempt it without prior knowledge of functions. The naming dimension is the only challenge; the logic is a single expression. This makes any naming violations clearly attributable to poor naming discipline rather than confusion about the programming task.

---

**Task description (shown to student)**:

Complete the function below. It receives an item's original price and a discount percentage, and should **return** the final price after applying the discount, rounded to 2 decimal places.

Example: an item costing $100.00 with a 20% discount should return `80.0`.

Include a brief description of your file at the very top. Do **not** add any `input()` calls.

```python
def calculate_discounted_price(original_price, discount_percent):
    pass
```

---

**Target guidelines and CQP/CSM mapping**:

| Primer ID | Guideline | CSM Principle | CQP key |
|-----------|-----------|--------------|---------|
| 1–3 | Recognise and use a consistent naming style; names should be descriptive | Explanatory Language | `explanatory_language` |
| 4 | Never use `l`, `O`, or `I` as single-character names | Explanatory Language | `explanatory_language` |
| 24–25 | Variable names should be lowercase with underscores | Explanatory Language | `explanatory_language` |
| 37 | Function names should be lowercase with underscores | Explanatory Language | `explanatory_language` |
| 41 | Parameter names should be descriptive | Explanatory Language | `explanatory_language` |

**Template parameters**: `{"cqp_principles": ["explanatory_language"]}`

---

**Bad answer** (realistic beginner — rewrites the stub with abbreviated names; beginners frequently retype provided signatures in a shorter form):

```python
def calc(p, d):
    x = p * (1 - d / 100)
    return round(x, 2)
```

**Violations triggered**:
- `C0103` × 4 — `calc` (vague abbreviation, not descriptive), `p` and `d` (single-char parameters), `x` (meaningless intermediate variable) → **explanatory_language** (IDs 1–4, 37, 41)
- `C0114` — missing module docstring → **explanatory_language** (ID 13)
- `C0116` — missing function docstring → **explanatory_language** (ID 13)

---

**Good answer**:

```python
"""Shopping discount calculation functions."""


def calculate_discounted_price(original_price, discount_percent):
    """Return the price after applying the given discount percentage."""
    discounted_price = original_price * (1 - discount_percent / 100)
    return round(discounted_price, 2)
```

---

**Test case table**:

| Test # | Standard Input | Test code | Expected output | Visibility |
|--------|---------------|-----------|----------------|------------|
| 1 | — | `print(calculate_discounted_price(100, 20))` | `80.0` | visible |
| 2 | — | `print(calculate_discounted_price(50, 10))` | `45.0` | visible |
| 3 | — | `print(calculate_discounted_price(200, 25))` | `150.0` | hidden |
| 4 | — | `print(calculate_discounted_price(75, 0))` | `75.0` | hidden (zero discount) |
| 5 | — | `print(calculate_discounted_price(30, 100))` | `0.0` | hidden (full discount) |

---

**Set A vs Set B note**: A principle-organised question signals to students that naming is explicitly the focus, independent of the programming task. Assessed at the start of the semester using an arithmetic-only task, B1 generates data on whether students can apply good naming habits before the cognitive load of new programming concepts is introduced. This is a fundamentally different signal from A1, where naming violations appear alongside layout violations in the context of learning variables and arithmetic. Combining B1 and A1 data in a study could test whether isolating the naming principle — rather than pairing it with layout — changes the rate or quality of student improvement, offering direct insight into whether principle-focused or topic-focused framing is more effective for style instruction.

---

### B2 — Clear Layout: Vowel Counter

**Question type**: `python3`

**Justification**: Counting vowels in a string requires a loop with a conditional nested inside, producing multiple indentation levels and a natural location for a block comment. This structure reliably elicits the layout violations that define the Clear Layout principle: indentation (students use 2 spaces), operator spacing (assignments missing spaces), extraneous whitespace (space before a colon), and comment format (missing space after `#`). All violations map exclusively to `clear_presentation`, making this a principle-pure question.

---

**Task description (shown to student)**:

Complete the function below. It receives a string and should **return** the number of vowels it contains. Count both upper- and lowercase vowels (a, e, i, o, u and their uppercase forms).

Include a brief description of your file at the very top. Do **not** add any `input()` calls.

```python
def count_vowels(text):
    pass
```

---

**Target guidelines and CQP/CSM mapping**:

| Primer ID | Guideline | CSM Principle | CQP key |
|-----------|-----------|--------------|---------|
| 7 | Use 4 spaces per indentation level | Clear Layout | `clear_presentation` |
| 18–19 | Block comments are indented to the same level as code; each line starts with `#` and a single space | Clear Layout | `clear_presentation` |
| 31 | Surround binary operators with a single space on either side | Clear Layout | `clear_presentation` |
| 36 | Avoid extraneous whitespace immediately inside brackets or immediately before a colon | Clear Layout | `clear_presentation` |

**Template parameters**: `{"cqp_principles": ["clear_presentation"]}`

---

**Bad answer** (realistic beginner — 2-space indent, omits operator spacing, space before colon, missing space after `#`):

```python
def count_vowels(text):
  count=0
  #count vowels in text
  for c in text:
    if c in "aeiouAEIOU" :
        count=count+1
  return count
```

**Violations triggered**:
- `E111` / `W0311` × 2 — `count=0`, `for c in text:`, `if c in`, `return count` all use 2-space indent → **clear_presentation** (ID 7)
- `E265` — `#count vowels in text` has no space after `#` → **clear_presentation** (ID 19)
- `E225` × 2 — `count=0`, `count=count+1` missing spaces around `=` and `+` → **clear_presentation** (ID 31)
- `E203` — `"aeiouAEIOU" :` has a space before the `:` → **clear_presentation** (ID 36)

---

**Good answer**:

```python
"""Text analysis functions."""


def count_vowels(text):
    """Return the number of vowels in the given string."""
    count = 0
    # Count each vowel character in the text.
    for character in text:
        if character in "aeiouAEIOU":
            count = count + 1
    return count
```

---

**Test case table**:

| Test # | Standard Input | Test code | Expected output | Visibility |
|--------|---------------|-----------|----------------|------------|
| 1 | — | `print(count_vowels("hello"))` | `2` | visible |
| 2 | — | `print(count_vowels("python"))` | `1` | visible |
| 3 | — | `print(count_vowels("aeiou"))` | `5` | hidden |
| 4 | — | `print(count_vowels("rhythm"))` | `0` | hidden (no vowels) |
| 5 | — | `print(count_vowels("HELLO"))` | `2` | hidden (uppercase vowels) |
| 6 | — | `print(count_vowels(""))` | `0` | hidden (empty string) |

---

**Set A vs Set B note**: Organising by the Clear Layout principle rather than by programming construct means students encounter B2 as an explicit test of layout awareness, not a test of loop logic. The task involves the same loop-with-conditional structure that appears in A2, but the pedagogical frame differs: students are told layout is the focus rather than conditional correctness. Data from B2 compared with A2 could reveal whether framing changes the types of violations students make — specifically, whether knowing layout is under scrutiny leads students to fix spacing while inadvertently introducing other issues. For study design, B2 data is most valuable in a cross-sectional analysis (is layout consistently the weakest principle across the cohort at a given point in time?), whereas A2 data is most valuable in a longitudinal design (does layout improve as students progress from conditionals to functions?).

---

### B3 — Consistent Code: Season Finder

**Question type**: `python3`

**Justification**: A multi-branch classifier returning season names is the cleanest CS1 vehicle for the Consistent Code principle. Mixed quote style arises naturally when students type return strings from different sources. A bare `return` in the else branch arises when students forget that all branches must return a value, making the inconsistency a real logic bug. The task uses `in` with a list — a construct different from the comparison chains in A2 — so there is no structural overlap with existing questions.

---

**Task description (shown to student)**:

Complete the function below. It receives a month number (1–12) and should **return** the name of the corresponding meteorological season: `"winter"` for December–February (months 12, 1, 2), `"spring"` for March–May, `"summer"` for June–August, and `"autumn"` for September–November.

Include a brief description of your file at the very top. Do **not** add any `input()` calls.

```python
def get_season(month):
    pass
```

---

**Target guidelines and CQP/CSM mapping**:

| Primer ID | Guideline | CSM Principle | CQP key |
|-----------|-----------|--------------|---------|
| 29 | Pick a quote style (single or double) and stick to it | Consistent Code | `consistent_code` |
| 40 | Be consistent in return statements (all return an expression or none do) | Consistent Code | `consistent_code` |
| 32 | When breaking a long expression across lines, always place the operator at the same position | Consistent Code | `consistent_code` |

**Template parameters**: `{"cqp_principles": ["consistent_code"]}`

---

**Bad answer** (realistic beginner — mixes quote styles when transcribing string literals, forgets to return a value in the final else branch):

```python
def get_season(month):
    """Return the season for the given month number."""
    if month in [12, 1, 2]:
        return 'winter'
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return 'summer'
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return
```

**Violations triggered**:
- `W9003` — `'winter'` and `'summer'` use single quotes while `"spring"` and `"autumn"` use double quotes → **consistent_code** (ID 29)
- `R1710` — four branches return a string but the `else` branch has a bare `return` (returns `None`) → **consistent_code** (ID 40)

Note: `W9004` (operator line break consistency) is part of the `consistent_code` principle but is not triggered by this answer because all expressions fit on a single line. It would appear in a student submission with very long multi-line expressions that use inconsistent break placement — before operators in some places and after operators in others.

Note: the bare `return` also makes `get_season` logically incorrect for any month outside 1–11 (returns `None` instead of a season name). This is intentional — R1710 catches a real bug masquerading as a style issue, which is a strong teaching moment about why consistent return statements matter.

---

**Good answer**:

```python
"""Season classification functions."""


def get_season(month):
    """Return the season name for the given month number (1–12)."""
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    else:
        return "autumn"
```

---

**Test case table**:

| Test # | Standard Input | Test code | Expected output | Visibility |
|--------|---------------|-----------|----------------|------------|
| 1 | — | `print(get_season(1))` | `winter` | visible |
| 2 | — | `print(get_season(4))` | `spring` | visible |
| 3 | — | `print(get_season(7))` | `summer` | hidden |
| 4 | — | `print(get_season(10))` | `autumn` | hidden |
| 5 | — | `print(get_season(12))` | `winter` | hidden (December in winter) |
| 6 | — | `print(get_season(2))` | `winter` | hidden (February boundary) |
| 7 | — | `print(get_season(9))` | `autumn` | hidden (start of autumn) |

---

**Set A vs Set B note**: A principle-organised question signals that consistency is the explicit focus, independent of the programming construct. B3 uses a multi-branch classifier — a structure already familiar from A2 (Conditionals) — so students are not challenged by new control-flow complexity. Any consistency violations are therefore attributable to style habits rather than task confusion. Comparing B3 data with A2 data can test whether framing a question around Consistent Code (vs. treating it as one of several simultaneously-flagged principles) changes the rate at which students adopt uniform quote style and complete return statements. A longitudinal study could also use B3 as a delayed assessment — administered after A2 — to measure whether the style feedback from A2 transfers to a new task assessed on consistency alone.

---

### B4 — Used Content: Digit Counter

**Question type**: `python3`

**Justification**: A loop over a string counting characters is the minimum task for which three distinct used-content violations arise naturally: an unused import (student imports `string` or `math` while exploring potential helpers), an unused variable (student computes a total intending to use it in a ratio but then just returns the count), and unreachable code (student leaves a debug `print` after the return statement). The task structure is deliberately familiar — identical in shape to B2 (Vowel Counter) — so cognitive load from the programming challenge is low and any redundancy violations are clearly attributable to code-hygiene habits.

---

**Task description (shown to student)**:

Complete the function below. It receives a string and should **return** the number of digit characters (0–9) it contains.

Include a brief description of your file at the very top. Do **not** add any `input()` calls.

```python
def count_digits(text):
    pass
```

---

**Target guidelines and CQP/CSM mapping**:

| Primer ID | Guideline | CSM Principle | CQP key |
|-----------|-----------|--------------|---------|
| Non-redundant Content | Remove imports that are not used anywhere in the file | Used Content | `used_content` |
| Non-redundant Content | Remove variables that are assigned but whose value is never read | Used Content | `used_content` |
| Non-redundant Content | Remove code that can never be executed | Used Content | `used_content` |

**Template parameters**: `{"cqp_principles": ["used_content"]}`

---

**Bad answer** (realistic beginner — imports modules "just in case", computes a total that never gets used, leaves a debug print after the return):

```python
import string
import math

def count_digits(text):
    """Return the number of digit characters in the text."""
    digit_count = 0
    total_chars = len(text)
    for char in text:
        if char.isdigit():
            digit_count = digit_count + 1
    return digit_count
    print("Done")
```

**Violations triggered**:
- `W0611` × 2 — `string` and `math` are imported but used nowhere in the file → **used_content**
- `W0612` — `total_chars` is assigned but its value is never read → **used_content**
- `W0101` — `print("Done")` appears after `return digit_count` and can never execute → **used_content**

The pattern is realistic: a beginner imports `string` and `math` while exploring potential helpers, calculates `total_chars` intending to compute a ratio (e.g., percentage of digits) but then just returns the raw count, and leaves a debugging print after the return without noticing it is unreachable.

---

**Good answer**:

```python
"""Text analysis utility functions."""


def count_digits(text):
    """Return the number of digit characters in the text."""
    digit_count = 0
    for char in text:
        if char.isdigit():
            digit_count = digit_count + 1
    return digit_count
```

---

**Test case table**:

| Test # | Standard Input | Test code | Expected output | Visibility |
|--------|---------------|-----------|----------------|------------|
| 1 | — | `print(count_digits("hello123"))` | `3` | visible |
| 2 | — | `print(count_digits("abc"))` | `0` | visible |
| 3 | — | `print(count_digits("1234567890"))` | `10` | hidden |
| 4 | — | `print(count_digits(""))` | `0` | hidden (empty string) |
| 5 | — | `print(count_digits("abc123def456"))` | `6` | hidden |
| 6 | — | `print(count_digits("Python3"))` | `1` | hidden (mixed case) |

---

**Set A vs Set B note**: Organising by the Used Content principle makes redundancy the explicit focus rather than an incidental check embedded alongside naming and layout. The task — a character-counting loop — is structurally identical to B2 (Vowel Counter), so any redundancy violations arise from code-hygiene habits rather than unfamiliar constructs. Data from B4 compared with A3 can reveal whether explicitly framing the question around Used Content changes the rate at which students remove unused imports and dead code — in A3, `used_content` is one of four simultaneously-checked principles, making it easy for a student to overlook. B4 data is most valuable in a cross-sectional analysis (what fraction of the cohort leaves unused elements at a given point in the semester?) while A3 data is most valuable longitudinally (does the rate of used-content violations decline as topic complexity grows and students are repeatedly reminded via style feedback?).

---

## Deployment notes

**CodeRunner question editor settings for all five questions**:

| Field | Value |
|-------|-------|
| Question type | `python3_cqp` |
| Support files | `cqp_principles.py`, `cqp_checker.py`, `grader_template.py` |
| Grader template | contents of `grader_template.py` |
| Template params | see each question above |
| Precheck | Enable and set `IS_PRECHECK` — CQP check runs on precheck, functional tests run on final submit |

**Module docstrings**: Questions including `explanatory_language` in their template params will flag `C0114` (missing module docstring) and `C0116` (missing function docstring). The task descriptions above prompt students to include a file-level description. If docstrings have not yet been covered at the point a question is deployed, the instructor should either postpone the question or edit `cqp_principles.py` to remove `C0114`/`C0116` from `explanatory_language` for that deployment.

**Guideline → code reference**:

| Primer ID | Pylint / pycodestyle code | CQP principle key |
|-----------|--------------------------|-------------------|
| 1–4 | `C0103`, `C0104` | `explanatory_language` |
| 5 | `C0301` / `E501` | `clear_presentation` |
| 7 | `W0311` / `E111` | `clear_presentation` |
| 13 (docstrings) | `C0114`, `C0116` | `explanatory_language` |
| 19 (comment `# `) | `E265` | `clear_presentation` |
| 29 (quote style) | `W9003` | `consistent_code` |
| 31 (operator spacing) | `E225` | `clear_presentation` |
| 32 (operator line break) | `W9004` | `consistent_code` |
| 33 (`is not`) | `C0113` | `simple_constructs` |
| 34 (bool comparison) | `C0121` | `simple_constructs` |
| 36 (extraneous whitespace) | `E201`, `E202`, `E203`, `E231` | `clear_presentation` |
| 37–38 (function names, blank lines) | `C0103`, `E302` | `explanatory_language`, `clear_presentation` |
| 40 (consistent returns) | `R1710` | `consistent_code` |
| 41 (parameter names) | `C0103` | `explanatory_language` |
| Non-redundant Content | `W0101` (unreachable), `W0104` (pointless-statement), `W0107` (unnecessary-pass), `W0401` (wildcard-import), `W0404` (reimported), `W0611` (unused-import), `W0612` (unused-variable), `W0613` (unused-argument), `W0614` (unused-wildcard-import) | `used_content` |
