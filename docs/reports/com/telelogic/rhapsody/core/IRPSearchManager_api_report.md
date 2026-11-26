# Rhapsody API Validation: IRPSearchManager

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPSearchManager` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`)
- Members: Python `4`, Java `5`, pywin32 `5`
- Deviation items: `8` (actionable `8`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| create_search_query() -> createSearchQuery | createSearchQuery (method) | CreateSearchQuery (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |
| search() -> search | search (method) | Search (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| search_and_show_results() -> searchAndShowResults | searchAndShowResults (method) | SearchAndShowResults (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| search_async() -> searchAsync | searchAsync (method) | SearchAsync (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| search() -> search | — | search (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| search_and_show_results() -> searchAndShowResults | — | searchAndShowResults (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| search_async() -> searchAsync | — | searchAsync (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH (4 findings)
- **Target:** `IRPSearchManager` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`
- **Affected call(s):** create_search_query() -> createSearchQuery; search() -> search; search_and_show_results() -> searchAndShowResults; search_async() -> searchAsync
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPSearchManager` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPSearchManager.getInterfaceName()`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (3 findings)
- **Target:** `IRPSearchManager` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`
- **Affected call(s):** search() -> search; search_and_show_results() -> searchAndShowResults; search_async() -> searchAsync
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
