# Rhapsody API Validation: IRPType

## Summary
- Target wrapper: `RPType` (`src/rhapsody_cli/models/elements/common/model_other_model.py`)
- Members: Python `35`, Java `35`, pywin32 `28`
- Deviations: `4`
- Deviations by status:
  - `COM_MEMBER_NOT_EXPOSED`: 4

- Informational binding differences (expected): `3`
- Wrapper backlog (supported members without wrappers): `0`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_enumeration_literals() -> getEnumerationLiterals | getEnumerationLiterals (method) | enumerationLiterals (property) | COM_MEMBER_NOT_EXPOSED | Use the enumerationLiterals property or a getter/setter fallback instead of calling getEnumerationLiterals directly. |
| get_is_predefined() -> getIsPredefined | getIsPredefined (method) | isPredefined (property) | COM_MEMBER_NOT_EXPOSED | Use the isPredefined property or a getter/setter fallback instead of calling getIsPredefined directly. |
| get_is_typedef() -> getIsTypedef | getIsTypedef (method) | isTypedef (property) | COM_MEMBER_NOT_EXPOSED | Use the isTypedef property or a getter/setter fallback instead of calling getIsTypedef directly. |
| get_typedef_base_type() -> getTypedefBaseType; set_typedef_base_type() -> setTypedefBaseType | getTypedefBaseType (method); setTypedefBaseType (method) | typedefBaseType (property) | COM_MEMBER_NOT_EXPOSED | Use the typedefBaseType property or a getter/setter fallback instead of calling getTypedefBaseType and setTypedefBaseType directly. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_is_typedef_constant() -> getIsTypedefConstant; set_is_typedef_constant() -> isTypedefConstant | getIsTypedefConstant (method); setIsTypedefConstant (method) | isTypedefConstant (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_typedef_ordered() -> getIsTypedefOrdered; set_is_typedef_ordered() -> isTypedefOrdered | getIsTypedefOrdered (method); setIsTypedefOrdered (method) | isTypedefOrdered (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_typedef_reference() -> getIsTypedefReference; set_is_typedef_reference() -> isTypedefReference | getIsTypedefReference (method); setIsTypedefReference (method) | isTypedefReference (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |

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
| get_kind() -> kind; set_kind() -> kind | getKind (method); setKind (method) | kind (property) | MATCH | — |
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

### Finding 1: COM_MEMBER_NOT_EXPOSED
- **Target:** `RPType` in `src/rhapsody_cli/models/elements/common/model_other_model.py`
- **Current Python wrapper/COM call:** get_enumeration_literals() -> getEnumerationLiterals
- **Expected Python method(s):** `get_enumeration_literals`
- **Java signature(s):** `IRPType.getEnumerationLiterals()`
- **pywin32 member(s):** enumerationLiterals (property)
- **Recommended change:** Use the enumerationLiterals property or a getter/setter fallback instead of calling getEnumerationLiterals directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 2: COM_MEMBER_NOT_EXPOSED
- **Target:** `RPType` in `src/rhapsody_cli/models/elements/common/model_other_model.py`
- **Current Python wrapper/COM call:** get_is_predefined() -> getIsPredefined
- **Expected Python method(s):** `get_is_predefined`
- **Java signature(s):** `IRPType.getIsPredefined()`
- **pywin32 member(s):** isPredefined (property)
- **Recommended change:** Use the isPredefined property or a getter/setter fallback instead of calling getIsPredefined directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 3: COM_MEMBER_NOT_EXPOSED
- **Target:** `RPType` in `src/rhapsody_cli/models/elements/common/model_other_model.py`
- **Current Python wrapper/COM call:** get_is_typedef() -> getIsTypedef
- **Expected Python method(s):** `get_is_typedef`
- **Java signature(s):** `IRPType.getIsTypedef()`
- **pywin32 member(s):** isTypedef (property)
- **Recommended change:** Use the isTypedef property or a getter/setter fallback instead of calling getIsTypedef directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 4: COM_MEMBER_NOT_EXPOSED
- **Target:** `RPType` in `src/rhapsody_cli/models/elements/common/model_other_model.py`
- **Current Python wrapper/COM call:** get_typedef_base_type() -> getTypedefBaseType; set_typedef_base_type() -> setTypedefBaseType
- **Expected Python method(s):** `get_typedef_base_type`, `set_typedef_base_type`
- **Java signature(s):** `IRPType.getTypedefBaseType()`, `IRPType.setTypedefBaseType(com.telelogic.rhapsody.core.IRPClassifier)`
- **pywin32 member(s):** typedefBaseType (property)
- **Recommended change:** Use the typedefBaseType property or a getter/setter fallback instead of calling getTypedefBaseType and setTypedefBaseType directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
