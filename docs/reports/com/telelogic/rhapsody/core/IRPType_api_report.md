# Rhapsody API Validation: IRPType

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPType` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_type.py`)
- Members: Python `28`, Java `35`, pywin32 `28`
- Deviation items: `0` (actionable `0`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | PASS | No change needed. |

<details>
<summary>Correct items (28) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_enumeration_literal() -> addEnumerationLiteral | addEnumerationLiteral (method) | addEnumerationLiteral (method) | MATCH | — |
| declaration (property) -> declaration | getDeclaration (method); setDeclaration (method) | declaration (property) | MATCH | — |
| delete_enumeration_literal() -> deleteEnumerationLiteral | deleteEnumerationLiteral (method) | deleteEnumerationLiteral (method) | MATCH | — |
| enumeration_literals (property) -> enumerationLiterals | getEnumerationLiterals (method) | enumerationLiterals (property) | MATCH | — |
| is_array() -> isArray | isArray (method) | isArray (method) | MATCH | — |
| is_enum() -> isEnum | isEnum (method) | isEnum (method) | MATCH | — |
| is_equal_to() -> isEqualTo | isEqualTo (method) | isEqualTo (method) | MATCH | — |
| is_implicit() -> isImplicit | isImplicit (method) | isImplicit (method) | MATCH | — |
| is_kind_enumeration() -> isKindEnumeration | isKindEnumeration (method) | isKindEnumeration (method) | MATCH | — |
| is_kind_language() -> isKindLanguage | isKindLanguage (method) | isKindLanguage (method) | MATCH | — |
| is_kind_struct() -> isKindStruct | isKindStruct (method) | isKindStruct (method) | MATCH | — |
| is_kind_typedef() -> isKindTypedef | isKindTypedef (method) | isKindTypedef (method) | MATCH | — |
| is_kind_union() -> isKindUnion | isKindUnion (method) | isKindUnion (method) | MATCH | — |
| is_pointer() -> isPointer | isPointer (method) | isPointer (method) | MATCH | — |
| is_pointer_to_pointer() -> isPointerToPointer | isPointerToPointer (method) | isPointerToPointer (method) | MATCH | — |
| is_predefined (property) -> isPredefined | getIsPredefined (method) | isPredefined (property) | MATCH | — |
| is_reference() -> isReference | isReference (method) | isReference (method) | MATCH | — |
| is_reference_to_pointer() -> isReferenceToPointer | isReferenceToPointer (method) | isReferenceToPointer (method) | MATCH | — |
| is_struct() -> isStruct | isStruct (method) | isStruct (method) | MATCH | — |
| is_template() -> isTemplate | isTemplate (method) | isTemplate (method) | MATCH | — |
| is_typedef (property) -> isTypedef | getIsTypedef (method) | isTypedef (property) | MATCH | — |
| is_typedef_constant (property) -> isTypedefConstant | getIsTypedefConstant (method); setIsTypedefConstant (method) | isTypedefConstant (property) | MATCH | — |
| is_typedef_ordered (property) -> isTypedefOrdered | getIsTypedefOrdered (method); setIsTypedefOrdered (method) | isTypedefOrdered (property) | MATCH | — |
| is_typedef_reference (property) -> isTypedefReference | getIsTypedefReference (method); setIsTypedefReference (method) | isTypedefReference (property) | MATCH | — |
| is_union() -> isUnion | isUnion (method) | isUnion (method) | MATCH | — |
| kind (property) -> kind | getKind (method); setKind (method) | kind (property) | MATCH | — |
| typedef_base_type (property) -> typedefBaseType | getTypedefBaseType (method); setTypedefBaseType (method) | typedefBaseType (property) | MATCH | — |
| typedef_multiplicity (property) -> typedefMultiplicity | getTypedefMultiplicity (method); setTypedefMultiplicity (method) | typedefMultiplicity (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
