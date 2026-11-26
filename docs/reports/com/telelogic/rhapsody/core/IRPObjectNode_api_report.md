# Rhapsody API Validation: IRPObjectNode

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPObjectNode` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`)
- Members: Python `7`, Java `7`, pywin32 `5`
- Deviation items: `5` (actionable `5`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_in_state() -> inState; set_in_state() -> inState | getInState (method); setInState (method) | inState (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_in_state_list() -> getInStateList | getInStateList (method) | inStateList (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the inStateList property or a getter/setter fallback instead of calling getInStateList directly. |
| get_represents() -> getRepresents; set_represents() -> represents | getRepresents (method); setRepresents (method) | represents (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| add_in_state() -> addInState | — | addInState (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| remove_in_state() -> removeInState | — | removeInState (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (2) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_in_state() -> addInState | addInState (method) | addInState (method) | MATCH | — |
| remove_in_state() -> removeInState | removeInState (method) | removeInState (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPObjectNode` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** get_in_state() -> inState; set_in_state() -> inState; get_represents() -> getRepresents; set_represents() -> represents
- **Java signature(s):** `IRPObjectNode.getInState()`, `IRPObjectNode.setRepresents(com.telelogic.rhapsody.core.IRPModelElement)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPObjectNode` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** get_in_state_list() -> getInStateList
- **Java signature(s):** `IRPObjectNode.getInStateList()`
- **Recommended change:** Use the inStateList property or a getter/setter fallback instead of calling getInStateList directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (2 findings)
- **Target:** `IRPObjectNode` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** add_in_state() -> addInState; remove_in_state() -> removeInState
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
