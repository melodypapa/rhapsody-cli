# Rhapsody API Validation: IRPowTextListener

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPowTextListener` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`)
- Members: Python `2`, Java `3`, pywin32 `3`
- Deviation items: `3` (actionable `3`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| dbl_click_notify() -> dblClickNotify | dblClickNotify (method) | DblClickNotify (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |
| set_obj_id() -> objID; set_obj_id() -> setObjID | setObjID (method) | SetObjID (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH (2 findings)
- **Target:** `IRPowTextListener` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** dbl_click_notify() -> dblClickNotify; set_obj_id() -> objID; set_obj_id() -> setObjID
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPowTextListener` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPowTextListener.getInterfaceName()`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
