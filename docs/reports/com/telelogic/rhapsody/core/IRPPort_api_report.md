# Rhapsody API Validation: IRPPort

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPPort` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_port.py`)
- Members: Python `14`, Java `14`, pywin32 `9`
- Deviation items: `1` (actionable `0`, expected binding differences `1`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_contract() (no static COM member); set_contract() (no static COM member) | getContract (method); setContract (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (9) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_provided_interface() -> addProvidedInterface | addProvidedInterface (method) | addProvidedInterface (method) | MATCH | — |
| add_required_interface() -> addRequiredInterface | addRequiredInterface (method) | addRequiredInterface (method) | MATCH | — |
| get_is_behavioral() -> isBehavioral; set_is_behavioral() -> isBehavioral | getIsBehavioral (method); setIsBehavioral (method) | isBehavioral (property) | MATCH | — |
| get_is_reversed() -> isReversed; set_is_reversed() -> isReversed | getIsReversed (method); setIsReversed (method) | isReversed (property) | MATCH | — |
| get_port_contract() -> portContract; set_port_contract() -> portContract | getPortContract (method); setPortContract (method) | portContract (property) | MATCH | — |
| get_provided_interfaces() -> providedInterfaces | getProvidedInterfaces (method) | providedInterfaces (property) | MATCH | — |
| get_required_interfaces() -> requiredInterfaces | getRequiredInterfaces (method) | requiredInterfaces (property) | MATCH | — |
| remove_provided_interface() -> removeProvidedInterface | removeProvidedInterface (method) | removeProvidedInterface (method) | MATCH | — |
| remove_required_interface() -> removeRequiredInterface | removeRequiredInterface (method) | removeRequiredInterface (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
