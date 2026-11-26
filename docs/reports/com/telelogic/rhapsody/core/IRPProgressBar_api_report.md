# Rhapsody API Validation: IRPProgressBar

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPProgressBar` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`)
- Members: Python `2`, Java `24`, pywin32 `3`
- Deviation items: `13` (actionable `2`, expected binding differences `11`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |
| tick() -> tick | getTick (method); tick (method) | tick (method) | PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| reset() -> reset | reset (method) | reset (method) | MATCH | — |

</details>

## AI Fix Guidance

### MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPProgressBar` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPProgressBar.getInterfaceName()`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPProgressBar` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** tick() -> tick
- **Java signature(s):** `IRPProgressBar.getTick()`, `IRPProgressBar.tick(int)`
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
