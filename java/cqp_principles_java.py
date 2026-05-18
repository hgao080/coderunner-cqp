"""
CQP (Code Quality Principles) — PMD rule mappings for Java.

Each principle is a dict keyed by PMD rule name, with a tuple of:
    (symbolic_name, explanation)

Rule sources:
    Standard PMD rules:  built-in PMD rulesets (category/java/...)
    Custom rules:        implemented in cqp_custom_checkers_java.py

Custom rules (no standard PMD rule exists for these):
    LineLength       — line exceeds length limit (default 100 chars)
    FieldVisibility  — non-private/protected field at class level
    CastUse          — cast expression outside equals(Object)
    InstanceOfUse    — instanceof expression outside equals(Object)
"""

# ---------------------------------------------------------------------------
# Tool routing — cqp_checker_java.py uses this to decide which runner to call.
# Any rule name not listed here is assumed to be a standard PMD rule.
# ---------------------------------------------------------------------------
CUSTOM_RULES = frozenset({
    'LineLength',
    'FieldVisibility',
    'CastUse',
    'InstanceOfUse',
})

# Maps each standard PMD rule to its category XML path (PMD 7 format).
PMD_RULE_CATEGORIES = {
    # codestyle
    'ControlStatementBraces':               'category/java/codestyle.xml',
    'FieldDeclarationsShouldBeAtStartOfClass': 'category/java/codestyle.xml',
    'ShortClassName':                        'category/java/codestyle.xml',
    'ShortMethodName':                       'category/java/codestyle.xml',
    'ShortVariable':                         'category/java/codestyle.xml',
    'PackageCase':                           'category/java/codestyle.xml',
    'ClassNamingConventions':                'category/java/codestyle.xml',
    'MethodNamingConventions':               'category/java/codestyle.xml',
    'FormalParameterNamingConventions':      'category/java/codestyle.xml',
    'LocalVariableNamingConventions':        'category/java/codestyle.xml',
    'FieldNamingConventions':               'category/java/codestyle.xml',
    'UnnecessaryReturn':                     'category/java/codestyle.xml',
    'UnnecessaryImport':                     'category/java/codestyle.xml',
    'UnnecessaryCast':                       'category/java/codestyle.xml',
    # bestpractices
    'DefaultLabelNotLastInSwitch':          'category/java/bestpractices.xml',
    'UnusedAssignment':                      'category/java/bestpractices.xml',
    'UnusedLocalVariable':                   'category/java/bestpractices.xml',
    'UnusedPrivateField':                    'category/java/bestpractices.xml',
    'UnusedPrivateMethod':                   'category/java/bestpractices.xml',
    'AvoidReassigningLoopVariables':         'category/java/bestpractices.xml',
    'AvoidReassigningParameters':            'category/java/bestpractices.xml',
    'LooseCoupling':                         'category/java/bestpractices.xml',
    'ConstantsInInterface':                  'category/java/bestpractices.xml',
    'MethodReturnsInternalArray':            'category/java/bestpractices.xml',
    'ReplaceHashtableWithMap':               'category/java/bestpractices.xml',
    'ReplaceVectorWithList':                 'category/java/bestpractices.xml',
    # design
    'SimplifyBooleanExpressions':           'category/java/design.xml',
    'SimplifyBooleanReturns':               'category/java/design.xml',
    'AvoidCatchingGenericException':        'category/java/design.xml',
    'AbstractClassWithoutAnyMethod':        'category/java/design.xml',
    'CyclomaticComplexity':                 'category/java/design.xml',
    'AvoidDeeplyNestedIfStmts':             'category/java/design.xml',
    'CouplingBetweenObjects':               'category/java/design.xml',
    'DataClass':                             'category/java/design.xml',
    'GodClass':                              'category/java/design.xml',
    'NcssCount':                             'category/java/design.xml',
    'TooManyFields':                         'category/java/design.xml',
    'TooManyMethods':                        'category/java/design.xml',
    'ExcessiveParameterList':               'category/java/design.xml',
    # errorprone
    'EmptyCatchBlock':                       'category/java/errorprone.xml',
}


# ---------------------------------------------------------------------------
# 1. Clear Presentation
# ---------------------------------------------------------------------------
CLEAR_PRESENTATION = {
    'ControlStatementBraces': (
        'control-statement-braces',
        "This control statement (if/for/while/etc.) is missing curly braces. "
        "Always add braces even for a single-statement body — they make the "
        "structure of the code visually explicit and prevent subtle bugs when "
        "a second statement is added later."
    ),
    'FieldDeclarationsShouldBeAtStartOfClass': (
        'field-declarations-start',
        "Fields are declared in the middle of the class rather than at the "
        "top. Place all field declarations at the beginning of the class so "
        "readers can immediately see what state the class holds."
    ),
    'LineLength': (
        'line-too-long',
        "This line exceeds the recommended length of 100 characters. Long "
        "lines force the reader to scroll horizontally and make it harder to "
        "see the structure of the code at a glance. Break the line, extract "
        "a variable, or split the expression."
    ),
}

# ---------------------------------------------------------------------------
# 2. Explanatory Language
# ---------------------------------------------------------------------------
EXPLANATORY_LANGUAGE = {
    'ShortClassName': (
        'short-class-name',
        "This class name is too short to be descriptive. Use a name that "
        "clearly communicates what the class represents or what it does."
    ),
    'ShortMethodName': (
        'short-method-name',
        "This method name is too short to be meaningful. Use a name that "
        "communicates what action the method performs."
    ),
    'ShortVariable': (
        'short-variable',
        "This variable or parameter name is too short to be meaningful. "
        "Choose a name that describes what the variable stores or represents "
        "so a reader does not need to trace through the code to understand it."
    ),
}

# ---------------------------------------------------------------------------
# 3. Consistent Code
# ---------------------------------------------------------------------------
CONSISTENT_CODE = {
    'PackageCase': (
        'package-case',
        "Package names must be all lowercase. Mixed-case package names "
        "break Java conventions and are harder to distinguish from class names."
    ),
    'ClassNamingConventions': (
        'class-naming-conventions',
        "Type names (classes, interfaces, enums, annotations) must use "
        "UpperCamelCase. This is the Java convention for types — consistent "
        "capitalisation makes them immediately recognisable as types."
    ),
    'MethodNamingConventions': (
        'method-naming-conventions',
        "Method names must use lowerCamelCase. This is the Java convention "
        "for methods — consistent naming makes them easy to distinguish from "
        "class names and constants."
    ),
    'FormalParameterNamingConventions': (
        'formal-parameter-naming-conventions',
        "Parameter names must use lowerCamelCase. Consistent naming helps "
        "readers immediately identify parameters versus class names or constants."
    ),
    'LocalVariableNamingConventions': (
        'local-variable-naming-conventions',
        "Local variable names must use lowerCamelCase. Consistent naming "
        "reduces the mental effort needed to read and understand the code."
    ),
    'FieldNamingConventions': (
        'field-naming-conventions',
        "Field names must use lowerCamelCase (non-public fields may start "
        "with an underscore). Consistent naming makes it easy to distinguish "
        "fields from local variables and parameters."
    ),
    'DefaultLabelNotLastInSwitch': (
        'default-label-not-last-in-switch',
        "The 'default' label must be the last case in a switch statement. "
        "Placing it elsewhere is non-standard and surprises readers who "
        "expect it at the end."
    ),
}

# ---------------------------------------------------------------------------
# 4. Used Content
# ---------------------------------------------------------------------------
USED_CONTENT = {
    'UnusedAssignment': (
        'unused-assignment',
        "This assigned value is never read. Either the assignment is "
        "unnecessary or the variable was meant to be used elsewhere. "
        "Remove unused assignments to avoid misleading readers."
    ),
    'UnusedLocalVariable': (
        'unused-local-variable',
        "This local variable is declared but never used. Remove it — unused "
        "variables suggest incomplete code and require readers to mentally "
        "track something that serves no purpose."
    ),
    'UnusedPrivateField': (
        'unused-private-field',
        "This private field is declared but never read. Remove it or use it "
        "— a field that is never accessed suggests the class does not actually "
        "need it."
    ),
    'UnusedPrivateMethod': (
        'unused-private-method',
        "This private method is declared but never called. Remove it — dead "
        "code requires unnecessary reading and maintenance effort."
    ),
    'UnnecessaryReturn': (
        'unnecessary-return',
        "This return statement at the end of a void method is redundant. "
        "Remove it — the method already returns at this point and the extra "
        "statement adds no information."
    ),
    'UnnecessaryImport': (
        'unnecessary-import',
        "This import is not used anywhere in the file. Remove it — unused "
        "imports add noise and can confuse readers about what the class "
        "actually depends on."
    ),
    'UnnecessaryCast': (
        'unnecessary-cast',
        "This cast is not needed. Unnecessary casts add complexity without "
        "benefit and suggest the author was uncertain about the type at this "
        "point in the code."
    ),
}

# ---------------------------------------------------------------------------
# 5. Simple Constructs
# ---------------------------------------------------------------------------
SIMPLE_CONSTRUCTS = {
    'SimplifyBooleanExpressions': (
        'simplify-boolean-expressions',
        "This boolean expression contains an unnecessary comparison. For "
        "example, 'if (x == true)' should be written as 'if (x)', and "
        "'if (x == false)' as 'if (!x)'. The simpler form is easier to read "
        "and is the standard Java idiom."
    ),
    'SimplifyBooleanReturns': (
        'simplify-boolean-returns',
        "This return can be simplified. Instead of "
        "'if (cond) { return true; } else { return false; }' write "
        "'return cond;'. The simplified form removes unnecessary complexity."
    ),
    'AvoidReassigningLoopVariables': (
        'avoid-reassigning-loop-variables',
        "Reassigning the loop variable inside the loop body obscures the "
        "control flow. Use a separate local variable instead so the loop's "
        "progression remains clear and predictable."
    ),
    'AvoidReassigningParameters': (
        'avoid-reassigning-parameters',
        "Reassigning a parameter inside a method obscures what value was "
        "originally passed in. Use a separate local variable to hold the "
        "modified value so the parameter's original value remains accessible."
    ),
    'EmptyCatchBlock': (
        'empty-catch-block',
        "This catch block is empty. Silently ignoring exceptions hides "
        "failures and makes debugging extremely difficult. At minimum, log "
        "or rethrow the exception so failures are visible."
    ),
    'AvoidCatchingGenericException': (
        'avoid-catching-generic-exception',
        "Catching 'Exception' (or 'Throwable', 'RuntimeException') is too "
        "broad — it silently swallows programmer errors like "
        "NullPointerException that should propagate. Catch the specific "
        "exception type(s) you expect and can meaningfully handle."
    ),
    'AbstractClassWithoutAnyMethod': (
        'abstract-class-without-any-method',
        "This abstract class has no methods. An abstract class with no "
        "methods provides nothing that an interface does not also provide. "
        "Replace it with an interface, or add the shared implementation "
        "that justifies the abstract class."
    ),
    'CyclomaticComplexity': (
        'cyclomatic-complexity',
        "This method's cyclomatic complexity is too high — it has too many "
        "branches and decision points. Break it into smaller, focused methods "
        "so each part is easier to read, understand, and test independently."
    ),
    'AvoidDeeplyNestedIfStmts': (
        'avoid-deeply-nested-if-stmts',
        "This code has deeply nested if statements. Deep nesting makes code "
        "much harder to follow. Consider using early returns, extracting "
        "logic into helper methods, or restructuring to reduce nesting."
    ),
}

# ---------------------------------------------------------------------------
# 6. Minimal Duplication
# ---------------------------------------------------------------------------
MINIMAL_DUPLICATION = {
    # PMD has no built-in rule for duplicate code in this configuration.
    # Use PMD CPD (Copy-Paste Detector) separately for duplication checks.
}

# ---------------------------------------------------------------------------
# 7. Modular Structure
# ---------------------------------------------------------------------------
MODULAR_STRUCTURE = {
    'FieldVisibility': (
        'field-visibility',
        "This field is public (or package-private). Public fields create "
        "global-variable-like dependencies that tightly couple other classes "
        "to this class's internal representation. Make the field private and "
        "provide a method if external access is needed."
    ),
    'CouplingBetweenObjects': (
        'coupling-between-objects',
        "This class is coupled to too many other types. High coupling makes "
        "the class harder to understand in isolation and harder to change "
        "without ripple effects across the codebase."
    ),
    'DataClass': (
        'data-class',
        "This class is a 'data class' — it only holds data with getters and "
        "setters and has no meaningful behaviour. Consider moving related "
        "operations into the class to reduce external dependencies and improve "
        "cohesion."
    ),
    'GodClass': (
        'god-class',
        "This class has too many responsibilities (weak cohesion, strong "
        "coupling). Break it into smaller, focused classes where each has "
        "a single clear responsibility."
    ),
    'LooseCoupling': (
        'loose-coupling',
        "This code depends on a concrete type (e.g. ArrayList) instead of "
        "an interface (e.g. List). Depending on the interface reduces coupling "
        "and makes the code easier to change without affecting callers."
    ),
    'ConstantsInInterface': (
        'constants-in-interface',
        "Defining constants in an interface forces every implementing class "
        "to inherit them, creating strong dependencies across the design. "
        "Move constants to a class or enum instead."
    ),
    'NcssCount': (
        'ncss-count',
        "This class or method is too large (Non-Commenting Source Statements "
        "count exceeds the threshold). Large units attract many dependencies. "
        "Break it into smaller, more focused pieces with clear responsibilities."
    ),
    'TooManyFields': (
        'too-many-fields',
        "This class has too many fields. Many fields often means the class "
        "is doing too much and has low cohesion. Consider splitting related "
        "groups of fields into separate, focused classes."
    ),
    'TooManyMethods': (
        'too-many-methods',
        "This class has too many methods. Many methods often means the class "
        "is trying to do too much. Consider splitting related groups of methods "
        "into separate classes with clear responsibilities."
    ),
    'ExcessiveParameterList': (
        'excessive-parameter-list',
        "This method has too many parameters. Many parameters create many "
        "external dependencies and make the method harder to call correctly. "
        "Consider grouping related parameters into an object."
    ),
}

# ---------------------------------------------------------------------------
# 8. Problem Alignment
# ---------------------------------------------------------------------------
PROBLEM_ALIGNMENT = {
    'MethodReturnsInternalArray': (
        'method-returns-internal-array',
        "This method returns a direct reference to an internal array, allowing "
        "callers to modify the class's private state. This breaks encapsulation. "
        "Return a copy of the array or a domain abstraction instead."
    ),
    'ReplaceHashtableWithMap': (
        'replace-hashtable-with-map',
        "Use the Map interface (e.g. HashMap) instead of the legacy Hashtable "
        "class. Map is the modern, flexible abstraction and reduces unnecessary "
        "coupling to a specific implementation detail."
    ),
    'ReplaceVectorWithList': (
        'replace-vector-with-list',
        "Use List (e.g. ArrayList) instead of the legacy Vector class. "
        "List is the modern, flexible abstraction for ordered collections "
        "and better reflects the intent of the code."
    ),
    'CastUse': (
        'cast-use',
        "A cast (outside of an equals() method) typically indicates that "
        "inheritance is being used incorrectly. If you need to cast to access "
        "a subtype's operations, consider redesigning using polymorphism or "
        "a more specific declared type."
    ),
    'InstanceOfUse': (
        'instanceof-use',
        "Using 'instanceof' (outside of an equals() method) typically indicates "
        "incorrect use of inheritance. If you need to test the runtime type, "
        "consider redesigning with polymorphism so each type handles its own "
        "behaviour without the caller needing to know the concrete type."
    ),
}

# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
PRINCIPLES = {
    'clear_presentation': {
        'name': 'Clear Presentation',
        'principle': (
            'Different elements are easy to recognise and distinguish and '
            'the relationships between them are apparent.'
        ),
        'rationale': (
            'Clear layout improves our shared understanding by making the '
            'individual elements easy to identify and signalling the elements '
            'the author considers to be related.'
        ),
        'codes': CLEAR_PRESENTATION,
    },
    'explanatory_language': {
        'name': 'Explanatory Language',
        'principle': 'The rationale, intent and meaning of code is explicit.',
        'rationale': (
            'Being explicit in describing the purpose of the code elements '
            "helps us understand the author's intention, thus improving "
            'understandability.'
        ),
        'codes': EXPLANATORY_LANGUAGE,
    },
    'consistent_code': {
        'name': 'Consistent Code',
        'principle': (
            'Elements that are similar in nature are presented and used in '
            'a similar way.'
        ),
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
        'principle': (
            'Coding constructs are selected to minimise complexity for the '
            'intended reader.'
        ),
        'rationale': (
            'Code that is perceived by the reader as simple is easier to '
            'understand.'
        ),
        'codes': SIMPLE_CONSTRUCTS,
    },
    'minimal_duplication': {
        'name': 'Minimal Duplication',
        'principle': 'Code repetition is avoided.',
        'rationale': (
            'Repeated code can be difficult to change because changes need '
            'to be made multiple times, there is a risk that not all items '
            'are changed and/or it is difficult to understand because you '
            'have to read more of it.'
        ),
        'codes': MINIMAL_DUPLICATION,
    },
    'modular_structure': {
        'name': 'Modular Structure',
        'principle': (
            'Related code is grouped together and dependencies between groups '
            'minimised.'
        ),
        'rationale': (
            'Placing related elements together makes code easier to understand. '
            'Reducing inter-connectedness means that isolated pieces can be '
            'more easily understood and can be modified independently.'
        ),
        'codes': MODULAR_STRUCTURE,
    },
    'problem_alignment': {
        'name': 'Problem Alignment',
        'principle': (
            'Implementation choices are consistent with the problem to be '
            'solved.'
        ),
        'rationale': (
            'An implementation that reflects the problem is easier to '
            'understand and change.'
        ),
        'codes': PROBLEM_ALIGNMENT,
    },
}
