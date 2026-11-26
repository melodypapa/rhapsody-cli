# Rhapsody API Validation: IRPFlowchart

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPFlowchart` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_flowchart.py`)
- Members: Python `12`, Java `14`, pywin32 `12`
- Deviation items: `0` (actionable `0`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (12) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_accept_event_action() -> addAcceptEventAction | addAcceptEventAction (method) | addAcceptEventAction (method) | MATCH | — |
| add_accept_time_event() -> addAcceptTimeEvent | addAcceptTimeEvent (method) | addAcceptTimeEvent (method) | MATCH | — |
| add_activity_parameter() -> addActivityParameter | addActivityParameter (method) | addActivityParameter (method) | MATCH | — |
| add_call_behavior() -> addCallBehavior | addCallBehavior (method) | addCallBehavior (method) | MATCH | — |
| add_call_operation() -> addCallOperation | addCallOperation (method) | addCallOperation (method) | MATCH | — |
| add_object_node() -> addObjectNode | addObjectNode (method) | addObjectNode (method) | MATCH | — |
| add_reference_activity() -> addReferenceActivity | addReferenceActivity (method) | addReferenceActivity (method) | MATCH | — |
| add_swimlane() -> addSwimlane | addSwimlane (method) | addSwimlane (method) | MATCH | — |
| get_flowchart_diagram() -> getFlowchartDiagram | getFlowchartDiagram (method) | getFlowchartDiagram (method) | MATCH | — |
| is_analysis_only (property) -> isAnalysisOnly | getIsAnalysisOnly (method); setIsAnalysisOnly (method) | isAnalysisOnly (property) | MATCH | — |
| its_owner (property) -> itsOwner | getItsOwner (method); setItsOwner (method) | itsOwner (property) | MATCH | — |
| swimlanes (property) -> swimlanes | getSwimlanes (method) | swimlanes (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
