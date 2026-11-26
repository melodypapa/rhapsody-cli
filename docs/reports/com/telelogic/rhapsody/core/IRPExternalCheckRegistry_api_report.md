# Rhapsody API Validation: IRPExternalCheckRegistry

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPExternalCheckRegistry` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`)
- Members: Python `2`, Java `3`, pywin32 `3`
- Deviation items: `1` (actionable `1`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |

<details>
<summary>Correct items (2) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| append_failed_elements_comments() -> appendFailedElementsComments | appendFailedElementsComments (method) | appendFailedElementsComments (method) | MATCH | — |
| set_failed_elements_comments() -> setFailedElementsComments | setFailedElementsComments (method) | setFailedElementsComments (method) | MATCH | — |

</details>

## AI Fix Guidance

### MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPExternalCheckRegistry` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPExternalCheckRegistry.getInterfaceName()`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
