# Rhapsody API Validation: IRPUseCase

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPUseCase` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_use_case.py`)
- Members: Python `15`, Java `15`, pywin32 `12`
- Deviation items: `2` (actionable `0`, expected binding differences `2`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | PASS | No change needed. |

<details>
<summary>Correct items (12) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_describing_diagram() -> addDescribingDiagram | addDescribingDiagram (method) | addDescribingDiagram (method) | MATCH | — |
| add_extension_point() -> addExtensionPoint | addExtensionPoint (method) | addExtensionPoint (method) | MATCH | — |
| delete_describing_diagram() -> deleteDescribingDiagram | deleteDescribingDiagram (method) | deleteDescribingDiagram (method) | MATCH | — |
| delete_entry_point() -> deleteEntryPoint | deleteEntryPoint (method) | deleteEntryPoint (method) | MATCH | — |
| delete_extension_point() -> deleteExtensionPoint | deleteExtensionPoint (method) | deleteExtensionPoint (method) | MATCH | — |
| get_describing_diagram() -> getDescribingDiagram | getDescribingDiagram (method) | getDescribingDiagram (method) | MATCH | — |
| describing_diagrams (property) -> describingDiagrams | getDescribingDiagrams (method) | describingDiagrams (property) | MATCH | — |
| entry_points (property) -> entryPoints | getEntryPoints (method) | entryPoints (property) | MATCH | — |
| extension_points (property) -> extensionPoints | getExtensionPoints (method) | extensionPoints (property) | MATCH | — |
| find_entry_point() -> findEntryPoint | findEntryPoint (method) | findEntryPoint (method) | MATCH | — |
| find_extension_point() -> findExtensionPoint | findExtensionPoint (method) | findExtensionPoint (method) | MATCH | — |
| is_behavior_overriden (property) -> isBehaviorOverriden; set_is_behavior_overriden() (no static COM member) | getIsBehaviorOverriden (method); setIsBehaviorOverriden (method) | isBehaviorOverriden (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
