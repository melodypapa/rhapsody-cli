# Rhapsody API Validation: IRPPlugInWindow

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPPlugInWindow` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`)
- Members: Python `8`, Java `9`, pywin32 `9`
- Deviation items: `7` (actionable `7`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| destroy_window() -> destroyWindow | destroyWindow (method) | DestroyWindow (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_docking() -> docking; get_docking() -> getDocking; set_docking() -> docking; set_docking() -> setDocking | getDocking (method); setDocking (method) | GetDocking (method); SetDocking (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |
| get_pos_string() -> getPosString; get_pos_string() -> posString; set_pos_string() -> posString; set_pos_string() -> setPosString | getPosString (method); setPosString (method) | GetPosString (method); SetPosString (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| show_window() -> showWindow | showWindow (method) | ShowWindow (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| set_title() -> setTitle; set_title() -> title | setTitle (method) | SetTitle (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_window_handle() -> getWindowHandle; get_window_handle() -> windowHandle | getWindowHandle (method) | GetWindowHandle (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH (6 findings)
- **Target:** `IRPPlugInWindow` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** destroy_window() -> destroyWindow; get_docking() -> docking; get_docking() -> getDocking; set_docking() -> docking; set_docking() -> setDocking; get_pos_string() -> getPosString; get_pos_string() -> posString; set_pos_string() -> posString; set_pos_string() -> setPosString; show_window() -> showWindow; set_title() -> setTitle; set_title() -> title; get_window_handle() -> getWindowHandle; get_window_handle() -> windowHandle
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPPlugInWindow` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPPlugInWindow.getInterfaceName()`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
