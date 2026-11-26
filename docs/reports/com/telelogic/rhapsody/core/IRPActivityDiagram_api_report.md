# Rhapsody API Validation: IRPActivityDiagram

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPActivityDiagram` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_diagram_types.py`)
- Members: Python `2`, Java `2`, pywin32 `1`
- Deviation items: `1` (actionable `1`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| decompose_swimlane() -> decomposeSwimlane | decomposeSwimlane (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_flowchart() -> getFlowchart | getFlowchart (method) | getFlowchart (method) | MATCH | — |

</details>

## AI Fix Guidance

### PYWIN32_MEMBER_MISSING (1 finding)
- **Target:** `IRPActivityDiagram` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_diagram_types.py`
- **Affected call(s):** decompose_swimlane() -> decomposeSwimlane
- **Java signature(s):** `IRPActivityDiagram.decomposeSwimlane(com.telelogic.rhapsody.core.IRPGraphElement)`
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
