# Rhapsody API Validation: IRPInteractionOperator

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPInteractionOperator` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interactions.py`)
- Members: Python `3`, Java `3`, pywin32 `2`
- Deviation items: `2` (actionable `2`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_interaction_operands() -> interactionOperands | getInteractionOperands (method) | interactionOperands (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_interaction_type() -> interactionType; set_interaction_type() -> interactionType | getInteractionType (method); setInteractionType (method) | interactionType (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPInteractionOperator` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interactions.py`
- **Affected call(s):** get_interaction_operands() -> interactionOperands; get_interaction_type() -> interactionType; set_interaction_type() -> interactionType
- **Java signature(s):** `IRPInteractionOperator.setInteractionType(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
