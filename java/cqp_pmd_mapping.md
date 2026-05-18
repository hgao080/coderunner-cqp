# CQP to PMD Rules Mapping

| CQP Principle | PMD Rule | Rule Category | Custom Rule? | Notes |
|---|---|---|---|---|
| Clear Presentation | ControlStatementBraces | codestyle | No | Braces required on control statements |
| Clear Presentation | FieldDeclarationsShouldBeAtStartOfClass | codestyle | No | Fields must appear at top of class |
| Clear Presentation | LineLength | codestyle | **Yes** | Long lines wrap and reduce readability |
| Explanatory Language | ShortClassName | codestyle | No | Class names must be sufficiently long |
| Explanatory Language | ShortMethodName | codestyle | No | Method names must be sufficiently long |
| Explanatory Language | ShortVariable | codestyle | No | Variable/parameter names must be sufficiently long (some 2-char exceptions) |
| Consistent Code | PackageCase | codestyle | No | Package names must be all lowercase |
| Consistent Code | ClassNamingConventions | codestyle | No | Types must be UpperCamelCase |
| Consistent Code | MethodNamingConventions | codestyle | No | Methods must be lowerCamelCase |
| Consistent Code | FormalParameterNamingConventions | codestyle | No | Parameters must be lowerCamelCase |
| Consistent Code | LocalVariableNamingConventions | codestyle | No | Local variables must be lowerCamelCase |
| Consistent Code | FieldNamingConventions | codestyle | No | Fields must be lowerCamelCase; non-public may start with `_` |
| Consistent Code | DefaultLabelNotLastInSwitch | bestpractices | No | `default` label must be last in switch |
| Used Content | UnusedAssignment | bestpractices | No | Assigned values must actually be used |
| Used Content | UnusedLocalVariable | bestpractices | No | Local variables must be used |
| Used Content | UnusedPrivateField | bestpractices | No | Private fields must be used |
| Used Content | UnusedPrivateMethod | bestpractices | No | Private methods must be used |
| Used Content | UnnecessaryReturn | codestyle | No | Redundant return statements must be removed |
| Used Content | UnnecessaryImport | codestyle | No | Unused imports must be removed (can cause compile failure) |
| Used Content | UnnecessaryCast | codestyle | No | Casts that are not needed indicate design confusion |
| Simple Constructs | SimplifyBooleanExpressions | design | No | Unnecessary boolean comparisons add complexity |
| Simple Constructs | SimplifyBooleanReturns | design | No | Unnecessary boolean comparisons in returns add complexity |
| Simple Constructs | AvoidReassigningLoopVariables | bestpractices | No | Reassigning loop variables obscures control flow |
| Simple Constructs | AvoidReassigningParameters | bestpractices | No | Reassigning parameters obscures their value |
| Simple Constructs | EmptyCatchBlock | errorprone | No | Empty catch blocks hide faults and indicate poor design |
| Simple Constructs | AvoidCatchingGenericException | design | No | Catching generic exceptions hides programmer errors |
| Simple Constructs | AbstractClassWithoutAnyMethod | design | No | Abstract classes with no methods should be replaced with better mechanisms |
| Simple Constructs | CyclomaticComplexity | design | No | High cyclomatic complexity indicates code can be simplified |
| Simple Constructs | AvoidDeeplyNestedIfStmts | design | No | Deep nesting is avoidable with good design |
| Minimal Duplication | *(none)* | — | — | PMD has no rule for duplicate code; use `pmd cpd` separately |
| Modular Structure | FieldVisibility | — | **Yes** | Fields must be `private` (or at most `protected`); public fields create global-variable-like dependencies |
| Modular Structure | CouplingBetweenObjects | design | No | Too many coupled types reduces modularity (threshold tailored to assignment) |
| Modular Structure | DataClass | design | No | Data classes force external dependencies that could be internalised |
| Modular Structure | GodClass | design | No | God classes have weak internal cohesion and strong external coupling |
| Modular Structure | LooseCoupling | bestpractices | No | Depend on interfaces/abstractions rather than concrete types |
| Modular Structure | ConstantsInInterface | bestpractices | No | Constant interfaces create strong dependencies across the design |
| Modular Structure | NcssCount | design | No | Larger classes attract more dependencies; threshold tailored to assignment |
| Modular Structure | TooManyFields | design | No | Many fields imply many external dependencies and low cohesion |
| Modular Structure | TooManyMethods | design | No | Many methods imply many external dependencies and low cohesion |
| Modular Structure | ExcessiveParameterList | design | No | Many parameters imply many external dependencies |
| Problem Alignment | MethodReturnsInternalArray | bestpractices | No | Returning internal arrays breaks encapsulation; replace with domain abstraction |
| Problem Alignment | ReplaceHashtableWithMap | bestpractices | No | `Hashtable` → `Map` interface reduces coupling strength |
| Problem Alignment | ReplaceVectorWithList | bestpractices | No | `Vector` → `ArrayList`/`List` for modern idiom |
| Problem Alignment | CastUse | — | **Yes** | Casts (outside `equals(Object)`) indicate incorrect use of inheritance |
| Problem Alignment | InstanceOfUse | — | **Yes** | `instanceof` (outside `equals(Object)`) indicates incorrect use of inheritance |
