# Rhapsody API Validation: IRPActor

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPActor` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_actor.py`)
- Members: Python `3`, Java `4`, pywin32 `1`
- Deviation items: `2` (actionable `0`, expected binding differences `2`, wrapper backlog `0`)
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
| is_behavior_overriden (property) -> isBehaviorOverriden | getIsBehaviorOverriden (method); setIsBehaviorOverriden (method) | isBehaviorOverriden (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
