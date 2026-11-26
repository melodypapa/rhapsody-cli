# Rhapsody API Validation: IRPStateVertex

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPStateVertex` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statemachine.py`)
- Members: Python `7`, Java `7`, pywin32 `6`
- Deviation items: `4` (actionable `4`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_parent() -> parent; set_parent() -> setParent | getParent (method); setParent (method) | parent (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| add_flow() -> addFlow | — | addFlow (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str', 'object'] but pywin32 declares ['str', 'com']. Match the documented COM parameter types. |
| add_transition() -> addTransition | — | addTransition (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| delete_transition() -> deleteTransition | — | deleteTransition (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (5) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_flow() -> addFlow | addFlow (method) | addFlow (method) | MATCH | — |
| add_transition() -> addTransition | addTransition (method) | addTransition (method) | MATCH | — |
| delete_transition() -> deleteTransition | deleteTransition (method) | deleteTransition (method) | MATCH | — |
| get_in_transitions() -> getInTransitions | getInTransitions (method) | getInTransitions (method) | MATCH | — |
| get_out_transitions() -> getOutTransitions | getOutTransitions (method) | getOutTransitions (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPStateVertex` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statemachine.py`
- **Affected call(s):** get_parent() -> parent; set_parent() -> setParent
- **Java signature(s):** `IRPStateVertex.getParent()`, `IRPStateVertex.setParent(com.telelogic.rhapsody.core.IRPState)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (3 findings)
- **Target:** `IRPStateVertex` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statemachine.py`
- **Affected call(s):** add_flow() -> addFlow; add_transition() -> addTransition; delete_transition() -> deleteTransition
- **Recommended change:** Wrapper passes types ['str', 'object'] but pywin32 declares ['str', 'com']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
