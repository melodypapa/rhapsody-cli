# Rhapsody API Validation: IRPUseCase

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPUseCase` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_use_case.py`)
- Members: Python `15`, Java `15`, pywin32 `12`
- Deviation items: `2` (actionable `0`, expected binding differences `2`, wrapper backlog `0`)

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_event_reception_with_event() (no static COM member) | addEventReceptionWithEvent (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| update_contained_diagrams_on_server() (no static COM member) | updateContainedDiagramsOnServer (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_describing_diagram() -> addDescribingDiagram | addDescribingDiagram (method) | addDescribingDiagram (method) | MATCH | — |
| add_extension_point() -> addExtensionPoint | addExtensionPoint (method) | addExtensionPoint (method) | MATCH | — |
| delete_describing_diagram() -> deleteDescribingDiagram | deleteDescribingDiagram (method) | deleteDescribingDiagram (method) | MATCH | — |
| delete_entry_point() -> deleteEntryPoint | deleteEntryPoint (method) | deleteEntryPoint (method) | MATCH | — |
| delete_extension_point() -> deleteExtensionPoint | deleteExtensionPoint (method) | deleteExtensionPoint (method) | MATCH | — |
| find_entry_point() -> findEntryPoint | findEntryPoint (method) | findEntryPoint (method) | MATCH | — |
| find_extension_point() -> findExtensionPoint | findExtensionPoint (method) | findExtensionPoint (method) | MATCH | — |
| get_describing_diagram() -> getDescribingDiagram | getDescribingDiagram (method) | getDescribingDiagram (method) | MATCH | — |
| get_describing_diagrams() -> describingDiagrams | getDescribingDiagrams (method) | describingDiagrams (property) | MATCH | — |
| get_entry_points() -> entryPoints | getEntryPoints (method) | entryPoints (property) | MATCH | — |
| get_extension_points() -> extensionPoints | getExtensionPoints (method) | extensionPoints (property) | MATCH | — |
| get_is_behavior_overriden() -> isBehaviorOverriden; set_is_behavior_overriden() (no static COM member) | getIsBehaviorOverriden (method); setIsBehaviorOverriden (method) | isBehaviorOverriden (property) | MATCH | — |

## Signature Validation

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| find_entry_point() -> findEntryPoint | — | findEntryPoint (method; types: com) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| find_extension_point() -> findExtensionPoint | — | findExtensionPoint (method; types: com) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types. |

## AI Fix Guidance
No deviations require changes.
