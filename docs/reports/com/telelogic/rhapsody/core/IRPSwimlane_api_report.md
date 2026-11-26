# Rhapsody API Validation: IRPSwimlane

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPSwimlane` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_swimlane.py`)
- Members: Python `4`, Java `5`, pywin32 `4`
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
<summary>Correct items (4) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_swimlane() -> addSwimlane | addSwimlane (method) | addSwimlane (method) | MATCH | — |
| contents (property) -> contents | getContents (method) | contents (property) | MATCH | — |
| represents (property) -> represents | getRepresents (method); setRepresents (method) | represents (property) | MATCH | — |
| swimlanes (property) -> swimlanes | getSwimlanes (method) | swimlanes (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
