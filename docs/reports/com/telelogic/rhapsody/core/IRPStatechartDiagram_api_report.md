# Rhapsody API Validation: IRPStatechartDiagram

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPStatechartDiagram` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_diagram_types.py`)
- Members: Python `3`, Java `3`, pywin32 `3`
- Deviation items: `1` (actionable `1`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_and_line() -> addAndLine | — | addAndLine (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object', 'int', 'int', 'int', 'int'] but pywin32 declares ['com', 'int', 'int', 'int', 'int']. Match the documented COM parameter types. |

<details>
<summary>Correct items (3) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_and_line() -> addAndLine | addAndLine (method) | addAndLine (method) | MATCH | — |
| create_graphics() -> createGraphics | createGraphics (method) | createGraphics (method) | MATCH | — |
| get_statechart() -> getStatechart | getStatechart (method) | getStatechart (method) | MATCH | — |

</details>

## AI Fix Guidance

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPStatechartDiagram` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_diagram_types.py`
- **Affected call(s):** add_and_line() -> addAndLine
- **Recommended change:** Wrapper passes types ['object', 'int', 'int', 'int', 'int'] but pywin32 declares ['com', 'int', 'int', 'int', 'int']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
