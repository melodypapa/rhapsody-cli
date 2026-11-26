# Rhapsody API Validation: IRPTemplateParameter

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPTemplateParameter` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_templates.py`)
- Members: Python `5`, Java `5`, pywin32 `3`
- Deviation items: `3` (actionable `3`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_parameter_kind() -> parameterKind; set_parameter_kind() -> parameterKind | getParameterKind (method); setParameterKind (method) | parameterKind (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_representative() -> representative; set_representative() -> representative | getRepresentative (method); setRepresentative (method) | representative (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| set_class_type() -> setClassType | — | setClassType (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 0 parameter(s) (0 required; params: —; types: —). Pass the documented parameters. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| set_class_type() -> setClassType | setClassType (method) | setClassType (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPTemplateParameter` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_templates.py`
- **Affected call(s):** get_parameter_kind() -> parameterKind; set_parameter_kind() -> parameterKind; get_representative() -> representative; set_representative() -> representative
- **Java signature(s):** `IRPTemplateParameter.getParameterKind()`, `IRPTemplateParameter.setRepresentative(com.telelogic.rhapsody.core.IRPModelElement)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_ARITY_MISMATCH (1 finding)
- **Target:** `IRPTemplateParameter` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_templates.py`
- **Affected call(s):** set_class_type() -> setClassType
- **Recommended change:** Wrapper passes [1] arg(s) but pywin32 declares 0 parameter(s) (0 required; params: —; types: —). Pass the documented parameters.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
