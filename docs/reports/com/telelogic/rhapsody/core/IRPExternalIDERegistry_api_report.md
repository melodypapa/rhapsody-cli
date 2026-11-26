# Rhapsody API Validation: IRPExternalIDERegistry

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPExternalIDERegistry` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`)
- Members: Python `3`, Java `4`, pywin32 `4`
- Deviation items: `5` (actionable `5`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |
| progress_task_asynch_callback() -> progressTaskAsynchCallback | progressTaskAsynchCallback (method) | ProgressTaskAsynchCallback (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| progress_task_asynch_eliminate() -> progressTaskAsynchEliminate | progressTaskAsynchEliminate (method) | ProgressTaskAsynchEliminate (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| send_ide_text_message() -> sendIDETextMessage | sendIDETextMessage (method) | SendIDETextMessage (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| send_ide_text_message() -> sendIDETextMessage | — | sendIDETextMessage (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['object']. Match the documented COM parameter types. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPExternalIDERegistry` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPExternalIDERegistry.getInterfaceName()`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH (3 findings)
- **Target:** `IRPExternalIDERegistry` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** progress_task_asynch_callback() -> progressTaskAsynchCallback; progress_task_asynch_eliminate() -> progressTaskAsynchEliminate; send_ide_text_message() -> sendIDETextMessage
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPExternalIDERegistry` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** send_ide_text_message() -> sendIDETextMessage
- **Recommended change:** Wrapper passes types ['str'] but pywin32 declares ['object']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
