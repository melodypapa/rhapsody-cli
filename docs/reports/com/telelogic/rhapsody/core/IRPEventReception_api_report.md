# Rhapsody API Validation: IRPEventReception

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPEventReception` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interactions.py`)
- Members: Python `2`, Java `2`, pywin32 `2`
- Deviation items: `0` (actionable `0`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | PASS | No change needed. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_event() -> getEvent; set_event() -> setEvent | getEvent (method); setEvent (method) | getEvent (method); setEvent (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
