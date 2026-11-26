# Rhapsody API Validation: IRPowPaneMgr

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPowPaneMgr` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`)
- Members: Python `4`, Java `5`, pywin32 `5`
- Deviation items: `3` (actionable `3`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_tab_notify() -> addTabNotify | addTabNotify (method) | AddTabNotify (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| close_tab_notify() -> closeTabNotify | closeTabNotify (method) | CloseTabNotify (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |

<details>
<summary>Correct items (2) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_ow_list_listener() -> getOWListListener | getOWListListener (method) | getOWListListener (method) | MATCH | — |
| get_ow_text_listener() -> getOWTextListener | getOWTextListener (method) | getOWTextListener (method) | MATCH | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH (2 findings)
- **Target:** `IRPowPaneMgr` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** add_tab_notify() -> addTabNotify; close_tab_notify() -> closeTabNotify
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPowPaneMgr` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPowPaneMgr.getInterfaceName()`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
