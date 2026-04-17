"""
CQP (Code Quality Principles) — Pylint code mappings for each principle.

Each principle is a dict keyed by Pylint message code, with a tuple of:
    (symbolic_name, explanation)

The explanation is the pedagogical "why this matters" shown to students.

Principles not yet mapped are stubbed with empty dicts and a TODO comment.
"""

# ---------------------------------------------------------------------------
# 1. Clear Presentation
#    Principle: Different elements are easy to recognise and distinguish and
#               the relationships between them are apparent.
#    Rationale: Clear layout improves our shared understanding by making the
#               individual elements easy to identify and signalling the
#               elements the author considers to be related.
# ---------------------------------------------------------------------------
CLEAR_PRESENTATION = {
    'C0301': (
        'line-too-long',
        "This line exceeds the recommended length. Long lines force the reader to "
        "scroll horizontally and make it harder to see the structure of the code at a glance."
    ),
    'C0303': (
        'trailing-whitespace',
        "There is trailing whitespace on this line. While invisible, it adds noise "
        "to diffs and version history, making changes harder to follow."
    ),
    'C0304': (
        'missing-final-newline',
        "The file does not end with a newline. This is a widely expected convention "
        "that some tools rely on and which keeps file boundaries clear."
    ),
    'C0321': (
        'multiple-statements',
        "Multiple statements appear on one line. Placing each statement on its own line "
        "makes the structure of the code easier to follow."
    ),
    'W0311': (
        'bad-indentation',
        "The indentation on this line is inconsistent. Consistent indentation is how "
        "Python signals code structure — inconsistent indentation misleads the reader."
    ),
}

# ---------------------------------------------------------------------------
# 2. Explanatory Language
#    Principle: The rationale, intent and meaning of code is explicit.
#    Rationale: Being explicit in describing the purpose of the code elements
#               helps us understand the author's intention, thus improving
#               understandability.
# ---------------------------------------------------------------------------
EXPLANATORY_LANGUAGE = {
    'C0103': (
        'invalid-name',
        "This name doesn't follow a descriptive naming convention. "
        "Names should communicate the purpose of a variable, function, or class "
        "so a reader doesn't have to trace through the code to understand it."
    ),
    'C0104': (
        'disallowed-name',
        "This name (e.g. 'foo', 'bar', 'x') is a placeholder that carries no meaning. "
        "Choose a name that describes what the element represents."
    ),
    'C0116': (
        'missing-function-docstring',
        "This function has no docstring. A docstring explains what the function does "
        "and how to use it, so a reader doesn't need to read the body to understand its purpose."
    ),
    'C0115': (
        'missing-class-docstring',
        "This class has no docstring. Documenting a class helps readers understand "
        "what it represents and how it should be used."
    ),
    'C0114': (
        'missing-module-docstring',
        "This module has no docstring. A brief description at the top of a file "
        "orients the reader before they read any code."
    ),
}



# ---------------------------------------------------------------------------
# 3. Consistent Code
#    Principle: Elements that are similar in nature are presented and
#               used in a similar way.
#    Rationale: Consistency leverages familiarity to reduce the mental
#               effort required to understand the code.
# ---------------------------------------------------------------------------
CONSISTENT_CODE = {
    'C0209': (
        'consider-using-f-string',
        "String formatting is done inconsistently with the rest of modern Python style. "
        "Using f-strings consistently makes string construction easier to read and predict."
    ),
    # TODO: Pylint has limited coverage of consistency concerns at the style level.
    # This principle may be better served by a custom checker in future.
}

# ---------------------------------------------------------------------------
# 4. Used Content
#    Principle: All elements that are introduced are meaningfully used.
#    Rationale: Non-contributing code elements require unnecessary mental
#               effort.
# ---------------------------------------------------------------------------
USED_CONTENT = {
    'W0611': (
        'unused-import',
        "You've imported something that isn't used anywhere in your code. "
        "Unused imports force a reader to wonder whether the import matters — "
        "remove it to keep your code clear."
    ),
    'W0612': (
        'unused-variable',
        "You've declared a variable that is never read. "
        "A reader will spend time trying to understand its purpose. "
        "Either use it, or remove it."
    ),
    'W0613': (
        'unused-argument',
        "A function parameter is never used inside the function body. "
        "This suggests the function signature doesn't match its implementation. "
        "Consider removing the parameter or using it."
    ),
    'W0614': (
        'unused-wildcard-import',
        "A wildcard import (import *) has brought in names that are never used. "
        "This makes it unclear where names come from and clutters the namespace."
    ),
    'W0107': (
        'unnecessary-pass',
        "This 'pass' statement does nothing and adds no meaning. "
        "Remove it unless it's the sole statement in a block that requires one."
    ),
    'W0101': (
        'unreachable',
        "This code can never be executed — it appears after a return or raise. "
        "Unreachable code misleads the reader into thinking it has an effect."
    ),
}

# ---------------------------------------------------------------------------
# 5. Simple Constructs
#    Principle: Coding constructs are selected to minimise complexity
#               for the intended reader.
#    Rationale: Code that is perceived by the reader as simple is easier
#               to understand.
# ---------------------------------------------------------------------------
SIMPLE_CONSTRUCTS = {
    'R0912': (
        'too-many-branches',
        "This function has too many branches (if/elif/else/try). "
        "High branching makes it hard to follow all possible paths through the code. "
        "Consider breaking it into smaller functions."
    ),
    'R0914': (
        'too-many-locals',
        "This function defines too many local variables. "
        "A large number of variables increases the mental effort needed to track state. "
        "Consider simplifying or splitting the function."
    ),
    'R0915': (
        'too-many-statements',
        "This function contains too many statements. "
        "Long functions are harder to understand in one reading. "
        "Breaking it into smaller, focused functions improves clarity."
    ),
    'C0123': (
        'unidiomatic-typecheck',
        "Using type() for a type check is more complex than necessary. "
        "Using isinstance() is the simpler, more readable Python idiom."
    ),
}

# ---------------------------------------------------------------------------
# 6. Minimal Duplication
#    Principle: Code repetition is avoided.
#    Rationale: Repeated code can be difficult to change because changes
#               need to be made multiple times, there is a risk that not all
#               items are changed and/or difficult to understand because you
#               have to read more of it.
# ---------------------------------------------------------------------------
MINIMAL_DUPLICATION = {
    'R0801': (
        'duplicate-code',
        "Similar code appears in more than one place. "
        "Duplicated logic means that a future change must be made in multiple places, "
        "risking inconsistency. Consider extracting the shared logic into a function."
    ),
    # TODO: Pylint's duplicate-code detection is coarse. A custom checker may
    # be needed to catch smaller-scale duplication (e.g. repeated expressions).
}

# ---------------------------------------------------------------------------
# 7. Modular Structure
#    Principle: Related code is grouped together and dependencies between
#               groups minimised.
#    Rationale: Placing related elements together makes code easier to
#               understand. Reducing inter-connectedness means that isolated
#               pieces can be more easily understood and can be modified
#               independently.
# ---------------------------------------------------------------------------
MODULAR_STRUCTURE = {
    'R0902': (
        'too-many-instance-attributes',
        "This class has too many instance attributes. "
        "This may indicate the class is doing too much. "
        "Consider splitting responsibilities across multiple classes."
    ),
    'R0903': (
        'too-few-public-methods',
        "This class has very few public methods, which may mean it isn't "
        "pulling its weight as a class. A plain data structure or function "
        "might be a simpler, more appropriate choice."
    ),
    'R0911': (
        'too-many-return-statements',
        "This function has many return statements, which can make it hard "
        "to follow all exit paths. Consider restructuring to reduce complexity."
    ),
    'R0913': (
        'too-many-arguments',
        "This function takes too many arguments. "
        "A large parameter list often signals that a function is doing too much, "
        "or that related arguments should be grouped into a data structure."
    ),
    'W0603': (
        'global-statement',
        "Using 'global' creates a hidden dependency between a function and "
        "the module's global state. This makes the function harder to understand "
        "and test in isolation."
    ),
}

# ---------------------------------------------------------------------------
# 8. Problem Alignment
#    Principle: Implementation choices are consistent with the problem
#               to be solved.
#    Rationale: An implementation that reflects the problem is easier to
#               understand and change.
# ---------------------------------------------------------------------------
PROBLEM_ALIGNMENT = {
    'W0108': (
        'unnecessary-lambda',
        "This lambda wraps a function call that could be used directly. "
        "The simpler, more direct implementation better reflects the intent."
    ),
    'R1733': (
        'unnecessary-dict-index-lookup',
        "You are looking up a dictionary value by key when you already have "
        "the value available. The direct approach better matches the problem."
    ),
    # TODO: expand as more specific Pylint codes are identified for this principle.
}

# ---------------------------------------------------------------------------
# Registry — maps string keys (used in the template) to principle dicts.
# This is what cqp_checker.py imports.
# ---------------------------------------------------------------------------
PRINCIPLES = {
    'clear_presentation': {
        'name': 'Clear Presentation',
        'principle': 'Different elements are easy to recognise and distinguish and the relationships between them are apparent.',
        'rationale': (
            'Clear layout improves our shared understanding by making the individual elements '
            'easy to identify and signalling the elements the author considers to be related.'
        ),
        'codes': CLEAR_PRESENTATION,
    },
    'explanatory_language': {
        'name': 'Explanatory Language',
        'principle': 'The rationale, intent and meaning of code is explicit.',
        'rationale': (
            'Being explicit in describing the purpose of the code elements helps us '
            'understand the author\'s intention, thus improving understandability.'
        ),
        'codes': EXPLANATORY_LANGUAGE,
    },
    'consistent_code': {
        'name': 'Consistent Code',
        'principle': 'Elements that are similar in nature are presented and used in a similar way.',
        'rationale': (
            'Consistency leverages familiarity to reduce the mental effort '
            'required to understand the code.'
        ),
        'codes': CONSISTENT_CODE,
    },
    'used_content': {
        'name': 'Used Content',
        'principle': 'All elements that are introduced are meaningfully used.',
        'rationale': (
            'Non-contributing code elements require unnecessary mental effort.'
        ),
        'codes': USED_CONTENT,
    },
    'simple_constructs': {
        'name': 'Simple Constructs',
        'principle': 'Coding constructs are selected to minimise complexity for the intended reader.',
        'rationale': (
            'Code that is perceived by the reader as simple is easier to understand.'
        ),
        'codes': SIMPLE_CONSTRUCTS,
    },
    'minimal_duplication': {
        'name': 'Minimal Duplication',
        'principle': 'Code repetition is avoided.',
        'rationale': (
            'Repeated code can be difficult to change because changes need to be made multiple times, '
            'there is a risk that not all items are changed and/or difficult to understand because you '
            'have to read more of it.'
        ),
        'codes': MINIMAL_DUPLICATION,
    },
    'modular_structure': {
        'name': 'Modular Structure',
        'principle': 'Related code is grouped together and dependencies between groups minimised.',
        'rationale': (
            'Placing related elements together makes code easier to understand. '
            'Reducing inter-connectedness means that isolated pieces can be more easily understood '
            'and can be modified independently.'
        ),
        'codes': MODULAR_STRUCTURE,
    },
    'problem_alignment': {
        'name': 'Problem Alignment',
        'principle': 'Implementation choices are consistent with the problem to be solved.',
        'rationale': (
            'An implementation that reflects the problem is easier to understand and change.'
        ),
        'codes': PROBLEM_ALIGNMENT,
    },
}
