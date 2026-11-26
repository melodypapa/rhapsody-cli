# Rhapsody API Validation: IRPFlowItem

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPFlowItem` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`)
- Members: Python `3`, Java `3`, pywin32 `3`
- Deviation items: `3` (actionable `3`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_represented() -> getRepresented | getRepresented (method) | represented (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the represented property or a getter/setter fallback instead of calling getRepresented directly. |
| add_represented() -> addRepresented | — | addRepresented (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| remove_represented() -> removeRepresented | — | removeRepresented (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (2) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_represented() -> addRepresented | addRepresented (method) | addRepresented (method) | MATCH | — |
| remove_represented() -> removeRepresented | removeRepresented (method) | removeRepresented (method) | MATCH | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPFlowItem` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** get_represented() -> getRepresented
- **Java signature(s):** `IRPFlowItem.getRepresented()`
- **Recommended change:** Use the represented property or a getter/setter fallback instead of calling getRepresented directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (2 findings)
- **Target:** `IRPFlowItem` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** add_represented() -> addRepresented; remove_represented() -> removeRepresented
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
