# Rhapsody API Validation: IRPAnnotation

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPAnnotation` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_requirements.py`)
- Members: Python `10`, Java `10`, pywin32 `7`
- Deviation items: `4` (actionable `4`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_anchored_by_me() -> anchoredByMe | getAnchoredByMe (method) | anchoredByMe (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_body() -> body; set_body() -> body | getBody (method); setBody (method) | body (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_specification() -> specification; set_specification() -> specification | getSpecification (method); setSpecification (method) | specification (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_specification_rtf() -> specificationRTF; is_specification_rtf() -> specificationRTF; set_specification_rtf() -> specificationRTF | getSpecificationRTF (method); setSpecificationRTF (method) | specificationRTF (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (3) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_anchor() -> addAnchor | addAnchor (method) | addAnchor (method) | MATCH | — |
| is_specification_rtf() -> isSpecificationRTF | isSpecificationRTF (method) | isSpecificationRTF (method) | MATCH | — |
| remove_anchor() -> removeAnchor | removeAnchor (method) | removeAnchor (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (4 findings)
- **Target:** `IRPAnnotation` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_requirements.py`
- **Affected call(s):** get_anchored_by_me() -> anchoredByMe; get_body() -> body; set_body() -> body; get_specification() -> specification; set_specification() -> specification; get_specification_rtf() -> specificationRTF; is_specification_rtf() -> specificationRTF; set_specification_rtf() -> specificationRTF
- **Java signature(s):** `IRPAnnotation.setSpecificationRTF(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
