# Rhapsody API Validation: IRPStatechart

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPStatechart` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statechart.py`)
- Members: Python `32`, Java `32`, pywin32 `30`
- Deviation items: `10` (actionable `0`, expected binding differences `10`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | PASS | No change needed. |

<details>
<summary>Correct items (22) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_all_triggers() -> getAllTriggers | getAllTriggers (method) | getAllTriggers (method) | MATCH | — |
| set_as_main_behavior() -> setAsMainBehavior | setAsMainBehavior (method) | setAsMainBehavior (method) | MATCH | — |
| close_diagram() -> closeDiagram | closeDiagram (method) | closeDiagram (method) | MATCH | — |
| create_graphics() -> createGraphics | createGraphics (method) | createGraphics (method) | MATCH | — |
| delete_state() -> deleteState | deleteState (method) | deleteState (method) | MATCH | — |
| get_elements_in_diagram() -> getElementsInDiagram | getElementsInDiagram (method) | getElementsInDiagram (method) | MATCH | — |
| find_trigger() -> findTrigger | findTrigger (method) | findTrigger (method) | MATCH | — |
| graphical_elements (property) -> graphicalElements | getGraphicalElements (method) | graphicalElements (property) | MATCH | — |
| get_inherits_from() -> getInheritsFrom | getInheritsFrom (method) | getInheritsFrom (method) | MATCH | — |
| is_main_behavior (property) -> isMainBehavior | getIsMainBehavior (method) | isMainBehavior (property) | MATCH | — |
| is_overridden (property) -> isOverridden | getIsOverridden (method) | isOverridden (property) | MATCH | — |
| its_class (property) -> itsClass | getItsClass (method) | itsClass (property) | MATCH | — |
| override_inheritance() -> overrideInheritance | overrideInheritance (method) | overrideInheritance (method) | MATCH | — |
| get_picture() -> getPicture | getPicture (method) | getPicture (method) | MATCH | — |
| get_picture_as() -> getPictureAs | getPictureAs (method) | getPictureAs (method) | MATCH | — |
| get_picture_as_divided_metafiles() -> getPictureAsDividedMetafiles | getPictureAsDividedMetafiles (method) | getPictureAsDividedMetafiles (method) | MATCH | — |
| get_pictures_with_image_map() -> getPicturesWithImageMap | getPicturesWithImageMap (method) | getPicturesWithImageMap (method) | MATCH | — |
| populate_diagram() -> populateDiagram | populateDiagram (method) | populateDiagram (method) | MATCH | — |
| root_state (property) -> rootState | getRootState (method) | rootState (property) | MATCH | — |
| set_show_diagram_frame() -> setShowDiagramFrame | setShowDiagramFrame (method) | setShowDiagramFrame (method) | MATCH | — |
| get_statechart_diagram() -> getStatechartDiagram | getStatechartDiagram (method) | getStatechartDiagram (method) | MATCH | — |
| unoverride_inheritance() -> unoverrideInheritance | unoverrideInheritance (method) | unoverrideInheritance (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
