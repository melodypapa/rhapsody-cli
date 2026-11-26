# Rhapsody API Validation: IRPMessagePoint

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPMessagePoint` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`)
- Members: Python `5`, Java `5`, pywin32 `5`
- Deviation items: `4` (actionable `4`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_interaction_occurrence() -> getInteractionOccurrence | getInteractionOccurrence (method) | interactionOccurrence (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the interactionOccurrence property or a getter/setter fallback instead of calling getInteractionOccurrence directly. |
| get_interaction_operator() -> getInteractionOperator | getInteractionOperator (method) | interactionOperator (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the interactionOperator property or a getter/setter fallback instead of calling getInteractionOperator directly. |
| get_message() -> getMessage | getMessage (method) | message (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the message property or a getter/setter fallback instead of calling getMessage directly. |
| get_type() -> type | getType (method) | type (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_classifier_role() -> getClassifierRole | getClassifierRole (method) | getClassifierRole (method) | MATCH | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (3 findings)
- **Target:** `IRPMessagePoint` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_interaction_occurrence() -> getInteractionOccurrence; get_interaction_operator() -> getInteractionOperator; get_message() -> getMessage
- **Recommended change:** Use the interactionOccurrence property or a getter/setter fallback instead of calling getInteractionOccurrence directly.
- **Recommended change:** Use the interactionOperator property or a getter/setter fallback instead of calling getInteractionOperator directly.
- **Recommended change:** Use the message property or a getter/setter fallback instead of calling getMessage directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPMessagePoint` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_type() -> type
- **Java signature(s):** `IRPMessagePoint.getType()`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
