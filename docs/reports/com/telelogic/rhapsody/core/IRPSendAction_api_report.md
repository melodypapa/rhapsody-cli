# Rhapsody API Validation: IRPSendAction

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPSendAction` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_send_action.py`)
- Members: Python `5`, Java `8`, pywin32 `5`
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
| add_argument_value() -> addArgumentValue | addArgumentValue (method) | addArgumentValue (method) | MATCH | — |
| arg_vals (property) -> argVals | getArgVals (method) | argVals (property) | MATCH | — |
| event (property) -> event | getEvent (method); setEvent (method) | event (property) | MATCH | — |
| invoked_operation (property) -> invokedOperation | getInvokedOperation (method); setInvokedOperation (method) | invokedOperation (property) | MATCH | — |
| target (property) -> target | getTarget (method); setTarget (method) | target (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
