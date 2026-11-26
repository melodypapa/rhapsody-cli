# Rhapsody API Validation: IRPDependency

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPDependency` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_dependency.py`)
- Members: Python `5`, Java `7`, pywin32 `3`
- Deviation items: `2` (actionable `0`, expected binding differences `2`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| is_need_to_migrate() (no static COM member) | isNeedToMigrate (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| set_link_type() (no static COM member) | setLinkType (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (3) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| dependent (property) -> dependent | getDependent (method); setDependent (method) | dependent (property) | MATCH | — |
| depends_on (property) -> dependsOn | getDependsOn (method); setDependsOn (method) | dependsOn (property) | MATCH | — |
| set_owner_without_changing_dependent() -> setOwnerWithoutChangingDependent | setOwnerWithoutChangingDependent (method) | setOwnerWithoutChangingDependent (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
