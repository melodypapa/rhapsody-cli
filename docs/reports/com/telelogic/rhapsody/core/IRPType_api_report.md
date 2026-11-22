# Rhapsody API Validation: IRPType

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPType` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_type.py`)
- Members: Python `35`, Java `35`, pywin32 `28`
- Deviations: `0`
- Deviations by status:
  - None

- Informational binding differences (expected): `0`
- Wrapper backlog (supported members without wrappers): `0`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_enumeration_literal() -> addEnumerationLiteral | addEnumerationLiteral (method) | addEnumerationLiteral (method) | MATCH | — |
| delete_enumeration_literal() -> deleteEnumerationLiteral | deleteEnumerationLiteral (method) | deleteEnumerationLiteral (method) | MATCH | — |
| get_declaration() -> declaration; set_declaration() -> declaration | getDeclaration (method); setDeclaration (method) | declaration (property) | MATCH | — |
| get_enumeration_literals() -> enumerationLiterals | getEnumerationLiterals (method) | enumerationLiterals (property) | MATCH | — |
| get_is_predefined() -> isPredefined | getIsPredefined (method) | isPredefined (property) | MATCH | — |
| get_is_typedef() -> isTypedef | getIsTypedef (method) | isTypedef (property) | MATCH | — |
| get_is_typedef_constant() -> isTypedefConstant; set_is_typedef_constant() -> isTypedefConstant | getIsTypedefConstant (method); setIsTypedefConstant (method) | isTypedefConstant (property) | MATCH | — |
| get_is_typedef_ordered() -> isTypedefOrdered; set_is_typedef_ordered() -> isTypedefOrdered | getIsTypedefOrdered (method); setIsTypedefOrdered (method) | isTypedefOrdered (property) | MATCH | — |
| get_is_typedef_reference() -> isTypedefReference; set_is_typedef_reference() -> isTypedefReference | getIsTypedefReference (method); setIsTypedefReference (method) | isTypedefReference (property) | MATCH | — |
| get_kind() -> kind; set_kind() -> kind | getKind (method); setKind (method) | kind (property) | MATCH | — |
| get_typedef_base_type() -> typedefBaseType; set_typedef_base_type() -> typedefBaseType | getTypedefBaseType (method); setTypedefBaseType (method) | typedefBaseType (property) | MATCH | — |
| get_typedef_multiplicity() -> typedefMultiplicity; set_typedef_multiplicity() -> typedefMultiplicity | getTypedefMultiplicity (method); setTypedefMultiplicity (method) | typedefMultiplicity (property) | MATCH | — |
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
| is_reference() -> isReference | isReference (method) | isReference (method) | MATCH | — |
| is_reference_to_pointer() -> isReferenceToPointer | isReferenceToPointer (method) | isReferenceToPointer (method) | MATCH | — |
| is_struct() -> isStruct | isStruct (method) | isStruct (method) | MATCH | — |
| is_template() -> isTemplate | isTemplate (method) | isTemplate (method) | MATCH | — |
| is_union() -> isUnion | isUnion (method) | isUnion (method) | MATCH | — |

## AI Fix Guidance
No deviations require changes.
