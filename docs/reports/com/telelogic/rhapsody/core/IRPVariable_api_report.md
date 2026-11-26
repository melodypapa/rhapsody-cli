# Rhapsody API Validation: IRPVariable

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPVariable` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_variables.py`)
- Members: Python `10`, Java `10`, pywin32 `7`
- Deviation items: `4` (actionable `4`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_declaration() -> declaration; set_declaration() -> declaration | getDeclaration (method); setDeclaration (method) | declaration (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_default_value() -> defaultValue; set_default_value() -> defaultValue | getDefaultValue (method); setDefaultValue (method) | defaultValue (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_type() -> type; set_type() -> type | getType (method); setType (method) | type (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_value_specifications() -> valueSpecifications | getValueSpecifications (method) | valueSpecifications (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (3) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_element_default_value() -> addElementDefaultValue | addElementDefaultValue (method) | addElementDefaultValue (method) | MATCH | — |
| add_string_default_value() -> addStringDefaultValue | addStringDefaultValue (method) | addStringDefaultValue (method) | MATCH | — |
| set_type_declaration() -> setTypeDeclaration | setTypeDeclaration (method) | setTypeDeclaration (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (4 findings)
- **Target:** `IRPVariable` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_variables.py`
- **Affected call(s):** get_declaration() -> declaration; set_declaration() -> declaration; get_default_value() -> defaultValue; set_default_value() -> defaultValue; get_type() -> type; set_type() -> type; get_value_specifications() -> valueSpecifications
- **Java signature(s):** `IRPVariable.getDeclaration()`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
