# Rhapsody API Validation: IRPRhapsodyServer

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPRhapsodyServer` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`)
- Members: Python `4`, Java `5`, pywin32 `5`
- Deviation items: `2` (actionable `2`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |
| initialize_application() -> initializeApplication | — | initializeApplication (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (4) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_application() -> getApplication | getApplication (method) | getApplication (method) | MATCH | — |
| get_hidden_application() -> getHiddenApplication | getHiddenApplication (method) | getHiddenApplication (method) | MATCH | — |
| initialize_application() -> initializeApplication | initializeApplication (method) | initializeApplication (method) | MATCH | — |
| get_uninitialized_application() -> getUninitializedApplication | getUninitializedApplication (method) | getUninitializedApplication (method) | MATCH | — |

</details>

## AI Fix Guidance

### MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPRhapsodyServer` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPRhapsodyServer.getInterfaceName()`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPRhapsodyServer` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`
- **Affected call(s):** initialize_application() -> initializeApplication
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
