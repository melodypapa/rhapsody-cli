# Rhapsody API Validation: IRPObjectNode

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPObjectNode` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_object_node.py`)
- Members: Python `5`, Java `7`, pywin32 `5`
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
<summary>Correct items (5) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_in_state() -> addInState | addInState (method) | addInState (method) | MATCH | — |
| in_state (property) -> inState | getInState (method); setInState (method) | inState (property) | MATCH | — |
| in_state_list (property) -> inStateList | getInStateList (method) | inStateList (property) | MATCH | — |
| remove_in_state() -> removeInState | removeInState (method) | removeInState (method) | MATCH | — |
| represents (property) -> represents | getRepresents (method); setRepresents (method) | represents (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
