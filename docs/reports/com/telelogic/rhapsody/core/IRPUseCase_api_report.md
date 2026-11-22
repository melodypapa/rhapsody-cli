# Rhapsody API Validation: IRPUseCase

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPUseCase` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_use_case.py`)
- Members: Python `15`, Java `15`, pywin32 `12`
- Deviation items: `4` (actionable `2`, expected binding differences `2`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| find_entry_point() -> findEntryPoint | — | findEntryPoint (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| find_extension_point() -> findExtensionPoint | — | findExtensionPoint (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_event_reception_with_event() (no static COM member) | addEventReceptionWithEvent (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| update_contained_diagrams_on_server() (no static COM member) | updateContainedDiagramsOnServer (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

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
| find_entry_point() -> findEntryPoint | findEntryPoint (method) | findEntryPoint (method) | MATCH | — |
| find_extension_point() -> findExtensionPoint | findExtensionPoint (method) | findExtensionPoint (method) | MATCH | — |
| get_describing_diagram() -> getDescribingDiagram | getDescribingDiagram (method) | getDescribingDiagram (method) | MATCH | — |
| get_describing_diagrams() -> describingDiagrams | getDescribingDiagrams (method) | describingDiagrams (property) | MATCH | — |
| get_entry_points() -> entryPoints | getEntryPoints (method) | entryPoints (property) | MATCH | — |
| get_extension_points() -> extensionPoints | getExtensionPoints (method) | extensionPoints (property) | MATCH | — |
| get_is_behavior_overriden() -> isBehaviorOverriden; set_is_behavior_overriden() (no static COM member) | getIsBehaviorOverriden (method); setIsBehaviorOverriden (method) | isBehaviorOverriden (property) | MATCH | — |

</details>

## AI Fix Guidance

### SIGNATURE_TYPE_MISMATCH (2 findings)
- **Target:** `IRPUseCase` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_use_case.py`
- **Affected call(s):** find_entry_point() -> findEntryPoint; find_extension_point() -> findExtensionPoint
- **Recommended change:** Wrapper passes types ['str'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
