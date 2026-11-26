# Rhapsody API Validation: IRPTemplateInstantiationParameter

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPTemplateInstantiationParameter` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_templates.py`)
- Members: Python `4`, Java `4`, pywin32 `2`
- Deviation items: `2` (actionable `2`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_arg_value() -> argValue; set_arg_value() -> argValue | getArgValue (method); setArgValue (method) | argValue (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_type() -> type; set_type() -> type | getType (method); setType (method) | type (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPTemplateInstantiationParameter` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_templates.py`
- **Affected call(s):** get_arg_value() -> argValue; set_arg_value() -> argValue; get_type() -> type; set_type() -> type
- **Java signature(s):** `IRPTemplateInstantiationParameter.getArgValue()`, `IRPTemplateInstantiationParameter.setType(com.telelogic.rhapsody.core.IRPClassifier)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
