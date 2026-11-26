# Rhapsody API Validation: IRPFlow

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPFlow` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_flow.py`)
- Members: Python `14`, Java `17`, pywin32 `14`
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
<summary>Correct items (14) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_conveyed() -> addConveyed | addConveyed (method) | addConveyed (method) | MATCH | — |
| conveyed (property) -> conveyed | getConveyed (method) | conveyed (property) | MATCH | — |
| direction (property) -> direction | getDirection (method); setDirection (method) | direction (property) | MATCH | — |
| end1 (property) -> end1 | getEnd1 (method); setEnd1 (method) | end1 (property) | MATCH | — |
| end1_port (property) -> end1Port | getEnd1Port (method) | end1Port (property) | MATCH | — |
| end1_sys_ml_port (property) -> end1SysMLPort | getEnd1SysMLPort (method) | end1SysMLPort (property) | MATCH | — |
| end2 (property) -> end2 | getEnd2 (method); setEnd2 (method) | end2 (property) | MATCH | — |
| end2_port (property) -> end2Port | getEnd2Port (method) | end2Port (property) | MATCH | — |
| end2_sys_ml_port (property) -> end2SysMLPort | getEnd2SysMLPort (method) | end2SysMLPort (property) | MATCH | — |
| remove_conveyed() -> removeConveyed | removeConveyed (method) | removeConveyed (method) | MATCH | — |
| set_end1_via_port() -> setEnd1ViaPort | setEnd1ViaPort (method) | setEnd1ViaPort (method) | MATCH | — |
| set_end1_via_sys_ml_port() -> setEnd1ViaSysMLPort | setEnd1ViaSysMLPort (method) | setEnd1ViaSysMLPort (method) | MATCH | — |
| set_end2_via_port() -> setEnd2ViaPort | setEnd2ViaPort (method) | setEnd2ViaPort (method) | MATCH | — |
| set_end2_via_sys_ml_port() -> setEnd2ViaSysMLPort | setEnd2ViaSysMLPort (method) | setEnd2ViaSysMLPort (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
