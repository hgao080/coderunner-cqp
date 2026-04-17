# CQP Test Questions for CodeRunner

Each question below tests one Code Quality Principle using template parameters.
Only includes principles suitable for automated testing in CodeRunner.

**Note:** Some principles (like Minimal Duplication) may require careful configuration
or longer code examples to work reliably with Pylint's default settings.

---

## 1. Clear Presentation

**Question Prompt:**
```
Write a function `calculate_total(price, quantity)` that returns the total cost.
Your code will be checked for clear presentation.
```

**Template Parameters (JSON):**
```json
{"cqp_principles": "clear_presentation"}
```

**Test Cases:**
| Test | Expected Output |
|------|----------------|
| `print(calculate_total(10, 3))` | `30` |
| `print(calculate_total(5.5, 2))` | `11.0` |
| `print(calculate_total(0, 100))` | `0` |

**Bad Answer (should fail):**
```python
def calculate_total(price, quantity):return price * quantity   
```

**Good Answer (should pass):**
```python
def calculate_total(price, quantity):
    return price * quantity
```

**Violations Triggered:**
- C0321 (multiple-statements): Multiple statements on one line

**CodeRunner Suitability:** ✅ Excellent - Clear, objective rules

---

## 2. Explanatory Language

**Question Prompt:**
```
Write a function `calculate_area(width, height)` that calculates and returns
the area of a rectangle. Include a docstring.
Your code will be checked for explanatory language.
```

**Template Parameters (JSON):**
```json
{"cqp_principles": "explanatory_language"}
```

**Test Cases:**
| Test | Expected Output |
|------|----------------|
| `print(calculate_area(5, 10))` | `50` |
| `print(calculate_area(3.5, 2))` | `7.0` |
| `print(calculate_area(1, 1))` | `1` |

**Bad Answer (should fail):**
```python
def f(x, y):
    return x * y
```

**Good Answer (should pass):**
```python
def calculate_area(width, height):
    """Calculate the area of a rectangle."""
    return width * height
```

**Violations Triggered:**
- C0103 (invalid-name): Non-descriptive function name 'f'
- C0103 (invalid-name): Non-descriptive variable names 'x', 'y'
- C0116 (missing-function-docstring): Missing docstring

**CodeRunner Suitability:** ✅ Excellent - Highly relevant for teaching good naming

---

## 3. Consistent Code

**Question Prompt:**
```
Write a function `greet(name, age)` that returns a greeting message in the format:
"Hello, NAME! You are AGE years old."

Use modern Python string formatting (f-strings).
Your code will be checked for consistent code style.
```

**Template Parameters (JSON):**
```json
{"cqp_principles": "consistent_code"}
```

**Test Cases:**
| Test | Expected Output |
|------|----------------|
| `print(greet("Alice", 25))` | `Hello, Alice! You are 25 years old.` |
| `print(greet("Bob", 30))` | `Hello, Bob! You are 30 years old.` |

**Bad Answer (should fail):**
```python
def greet(name, age):
    return "Hello, " + name + "! You are " + str(age) + " years old."
```

**Good Answer (should pass):**
```python
def greet(name, age):
    return f"Hello, {name}! You are {age} years old."
```

**Violations Triggered:**
- C0209 (consider-using-f-string): Inconsistent string formatting

**CodeRunner Suitability:** ⚠️ Good - Limited scope but teaches modern Python style

**Note:** Pylint has limited coverage of consistency beyond string formatting.
Consider this more as a "use modern idioms" check.

---

## 4. Used Content

**Question Prompt:**
```
Write a function `double(number)` that returns double the input number.
Do not import any modules or create any unused variables.
Your code will be checked to ensure all content is used.
```

**Template Parameters (JSON):**
```json
{"cqp_principles": "used_content"}
```

**Test Cases:**
| Test | Expected Output |
|------|----------------|
| `print(double(5))` | `10` |
| `print(double(7))` | `14` |
| `print(double(0))` | `0` |
| `print(double(-3))` | `-6` |

**Bad Answer (should fail):**
```python
import math
import random

def double(number):
    temp = 5
    result = number * 2
    return result
```

**Good Answer (should pass):**
```python
def double(number):
    return number * 2
```

**Violations Triggered:**
- W0611 (unused-import): Unused imports 'math' and 'random'
- W0612 (unused-variable): Unused variable 'temp'

**CodeRunner Suitability:** ✅ Excellent - Very common student mistake, clear feedback

---

## 5. Simple Constructs

**Question Prompt:**
```
Write a function `classify_age(age)` that returns:
- "child" if age < 13
- "teen" if 13 <= age < 20
- "adult" if age >= 20

Keep your solution simple and avoid unnecessary complexity.
Your code will be checked for simplicity.
```

**Template Parameters (JSON):**
```json
{"cqp_principles": "simple_constructs"}
```

**Test Cases:**
| Test | Expected Output |
|------|----------------|
| `print(classify_age(10))` | `child` |
| `print(classify_age(15))` | `teen` |
| `print(classify_age(25))` | `adult` |
| `print(classify_age(13))` | `teen` |
| `print(classify_age(19))` | `teen` |
| `print(classify_age(20))` | `adult` |

**Bad Answer (should fail):**
```python
def classify_age(age):
    a = age
    b = 13
    c = 20
    d = a < b
    e = a >= b
    f = a < c
    g = e and f
    h = a >= c
    
    if d:
        if True:
            if True:
                result = "child"
    elif g:
        if True:
            if True:
                result = "teen"
    elif h:
        if True:
            if True:
                result = "adult"
    
    return result
```

**Good Answer (should pass):**
```python
def classify_age(age):
    if age < 13:
        return "child"
    elif age < 20:
        return "teen"
    else:
        return "adult"
```

**Violations Triggered:**
- R0914 (too-many-locals): Too many local variables
- R0912 (too-many-branches): Too many branches

**CodeRunner Suitability:** ⚠️ Fair - Works for teaching, but artificial "bad" examples

**Note:** Students rarely write code *this* complex accidentally. Better suited
for refactoring exercises on pre-written complex code.

---

## 6. Minimal Duplication

**Note:** This principle is challenging to test automatically in CodeRunner because
Pylint's duplicate-code detection (R0801) requires significant code similarity
(typically 4-5+ similar lines) and may not trigger on small examples. Consider
using this for larger programming assignments or skip in intro courses.

**Question Prompt:**
```
Write a program with these functions:
- `calculate_circle_area(radius)` - returns area of circle (use pi = 3.14159)
- `calculate_circle_perimeter(radius)` - returns perimeter of circle
- `calculate_sphere_volume(radius)` - returns volume of sphere (4/3 * pi * r³)
- `calculate_sphere_surface(radius)` - returns surface area of sphere (4 * pi * r²)

Avoid duplicating the value of pi.
```

**Template Parameters (JSON):**
```json
{"cqp_principles": "minimal_duplication"}
```

**Test Cases:**
| Test | Expected Output (approx) |
|------|----------------|
| `print(round(calculate_circle_area(5), 2))` | `78.54` |
| `print(round(calculate_circle_perimeter(5), 2))` | `31.42` |
| `print(round(calculate_sphere_volume(3), 2))` | `113.1` |
| `print(round(calculate_sphere_surface(3), 2))` | `113.1` |

**Bad Answer (duplicates PI):**
```python
def calculate_circle_area(radius):
    pi = 3.14159
    return pi * radius * radius

def calculate_circle_perimeter(radius):
    pi = 3.14159
    return 2 * pi * radius

def calculate_sphere_volume(radius):
    pi = 3.14159
    return (4/3) * pi * radius ** 3

def calculate_sphere_surface(radius):
    pi = 3.14159
    return 4 * pi * radius ** 2
```

**Good Answer (DRY - Don't Repeat Yourself):**
```python
PI = 3.14159

def calculate_circle_area(radius):
    return PI * radius * radius

def calculate_circle_perimeter(radius):
    return 2 * PI * radius

def calculate_sphere_volume(radius):
    return (4/3) * PI * radius ** 3

def calculate_sphere_surface(radius):
    return 4 * PI * radius ** 2
```

**Violations Triggered:**
- R0801 (duplicate-code): Similar code in multiple locations

**CodeRunner Suitability:** ❌ Poor - R0801 is unreliable for small examples

**Recommendation:** Skip this principle for introductory CodeRunner questions,
or use manual code review instead. Better for larger projects where duplication
is more obvious.

---

## 7. Modular Structure

**Question Prompt:**
```
Write a function `calculate_sum(numbers)` that takes a list of numbers
and returns their sum. Do not use global variables.
Your code will be checked for modular structure.
```

**Template Parameters (JSON):**
```json
{"cqp_principles": "modular_structure"}
```

**Test Cases:**
| Test | Expected Output |
|------|----------------|
| `print(calculate_sum([1, 2, 3, 4, 5]))` | `15` |
| `print(calculate_sum([10, 20, 30]))` | `60` |
| `print(calculate_sum([]))` | `0` |
| `print(calculate_sum([-5, 5]))` | `0` |

**Bad Answer (uses global):**
```python
total = 0

def calculate_sum(numbers):
    global total
    total = 0
    for num in numbers:
        total = total + num
    return total
```

**Good Answer (properly encapsulated):**
```python
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total
```

**Violations Triggered:**
- W0603 (global-statement): Use of global statement

**CodeRunner Suitability:** ✅ Good - Teaches important encapsulation concepts

**Alternative Example (too many arguments):**

**Prompt:**
```
Write a function `add_numbers(num1, num2, num3)` that adds three numbers.
Limit functions to 5 or fewer parameters.
```

**Bad Answer:**
```python
def add_numbers(a, b, c, d, e, f, g):  # Too many params!
    return a + b + c + d + e + f + g
```

**Violation:** R0913 (too-many-arguments)

---

## 8. Problem Alignment

**Question Prompt:**
```
Write two functions:

1. `square(x)` - takes a number and returns its square
2. `square_all(numbers)` - takes a list of numbers and returns a new list 
   with each number squared, using map() and your square function

Your code will be checked for problem alignment.
```

**Template Parameters (JSON):**
```json
{"cqp_principles": "problem_alignment"}
```

**Test Cases:**
| Test | Expected Output |
|------|----------------|
| `print(square(5))` | `25` |
| `print(square_all([1, 2, 3, 4]))` | `[1, 4, 9, 16]` |
| `print(square_all([0, -2, 5]))` | `[0, 4, 25]` |
| `print(square_all([]))` | `[]` |

**Bad Answer (unnecessary lambda):**
```python
def square(x):
    return x ** 2

def square_all(numbers):
    return list(map(lambda x: x ** 2, numbers))  # Duplicates square()!
```

**Good Answer (uses existing function):**
```python
def square(x):
    return x ** 2

def square_all(numbers):
    return list(map(square, numbers))
```

**Violations Triggered:**
- W0108 (unnecessary-lambda): Lambda wrapping a function that could be used directly

**CodeRunner Suitability:** ✅ Good - Teaches functional programming best practices

**Note:** The question prompt explicitly asks students to use the `square` function
with `map()`, making the unnecessary lambda more obvious.

---

## Setting Up Questions in CodeRunner

For each question:

1. **Question Type:** Python3
2. **Template:** Use grader_template.py (with template parameter support)
3. **Template Parameters:** Add JSON like `{"cqp_principles": "used_content"}`
4. **Support Files:** 
   - `cqp_checker.py`
   - `cqp_principles.py`
5. **Test Cases:** Copy from tables above (use "Expected" as answer)
6. **Sample Answer:** Provide the "good" answer from above
7. **All or Nothing:** Recommended (student must fix style AND pass tests)

## Recommended Principles for CodeRunner

✅ **Highly Recommended:**
- **Clear Presentation** - Objective, clear violations
- **Explanatory Language** - Essential skill, good feedback
- **Used Content** - Common mistake, easy to fix
- **Modular Structure** - Important concept, clear issues

⚠️ **Use with Care:**
- **Consistent Code** - Limited scope (mostly f-strings)
- **Problem Alignment** - Works but needs careful prompt design
- **Simple Constructs** - Better for refactoring exercises

❌ **Not Recommended:**
- **Minimal Duplication** - Unreliable with small code samples

## Multiple Principles

You can check multiple principles at once:
```json
{"cqp_principles": ["clear_presentation", "explanatory_language", "used_content"]}
```

This is good for comprehensive coding questions where students should
demonstrate multiple quality principles simultaneously.
