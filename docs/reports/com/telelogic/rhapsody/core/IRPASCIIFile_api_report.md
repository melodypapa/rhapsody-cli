# Rhapsody API Validation: IRPASCIIFile

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPASCIIFile` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_files.py`)
- Members: Python `3`, Java `4`, pywin32 `4`
- Deviation items: `1` (actionable `1`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |

<details>
<summary>Correct items (3) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| close() -> close | close (method) | close (method) | MATCH | — |
| open() -> open | open (method) | open (method) | MATCH | — |
| write() -> write | write (method) | write (method) | MATCH | — |

</details>

## AI Fix Guidance

### MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPASCIIFile` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_files.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPASCIIFile.getInterfaceName()`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
