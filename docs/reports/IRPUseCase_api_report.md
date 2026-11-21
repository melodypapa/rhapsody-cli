# Rhapsody API Validation: IRPUseCase

## Summary
- Target wrapper: `RPUseCase` (`src/rhapsody_cli/models/elements/classifiers/model_usecase.py`)
- Members: Python `15`, Java `15`, pywin32 `12`
- Deviations: `2`
- Deviations by status:
  - `PYWIN32_MEMBER_MISSING`: 2

- Informational binding differences (expected): `0`
- Wrapper backlog (supported members without wrappers): `0`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_event_reception_with_event() -> addEventReceptionWithEvent | addEventReceptionWithEvent (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| update_contained_diagrams_on_server() -> updateContainedDiagramsOnServer | updateContainedDiagramsOnServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

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

## AI Fix Guidance

### Finding 1: PYWIN32_MEMBER_MISSING
- **Target:** `RPUseCase` in `src/rhapsody_cli/models/elements/classifiers/model_usecase.py`
- **Current Python wrapper/COM call:** add_event_reception_with_event() -> addEventReceptionWithEvent
- **Expected Python method(s):** `add_event_reception_with_event`
- **Java signature(s):** `IRPUseCase.addEventReceptionWithEvent(java.lang.String, com.telelogic.rhapsody.core.IRPEvent)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 2: PYWIN32_MEMBER_MISSING
- **Target:** `RPUseCase` in `src/rhapsody_cli/models/elements/classifiers/model_usecase.py`
- **Current Python wrapper/COM call:** update_contained_diagrams_on_server() -> updateContainedDiagramsOnServer
- **Expected Python method(s):** `update_contained_diagrams_on_server`
- **Java signature(s):** `IRPUseCase.updateContainedDiagramsOnServer(int)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
