# Rhapsody API Validation: IRPStatechart

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPStatechart` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statechart.py`)
- Members: Python `32`, Java `32`, pywin32 `30`
- Deviation items: `2` (actionable `0`, expected binding differences `2`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_new_accept_event_action() (no static COM member) | addNewAcceptEventAction (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| add_new_accept_time_event() (no static COM member) | addNewAcceptTimeEvent (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (30) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_free_shape_by_type() -> AddFreeShapeByType | addFreeShapeByType (method) | AddFreeShapeByType (method) | MATCH | — |
| add_image() -> AddImage | addImage (method) | AddImage (method) | MATCH | — |
| add_new_edge_by_type() -> AddNewEdgeByType | addNewEdgeByType (method) | AddNewEdgeByType (method) | MATCH | — |
| add_new_edge_for_element() -> AddNewEdgeForElement | addNewEdgeForElement (method) | AddNewEdgeForElement (method) | MATCH | — |
| add_new_node_by_type() -> AddNewNodeByType | addNewNodeByType (method) | AddNewNodeByType (method) | MATCH | — |
| add_new_node_for_element() -> AddNewNodeForElement | addNewNodeForElement (method) | AddNewNodeForElement (method) | MATCH | — |
| add_text_box() -> AddTextBox | addTextBox (method) | AddTextBox (method) | MATCH | — |
| close_diagram() -> closeDiagram | closeDiagram (method) | closeDiagram (method) | MATCH | — |
| create_graphics() -> createGraphics | createGraphics (method) | createGraphics (method) | MATCH | — |
| delete_state() -> deleteState | deleteState (method) | deleteState (method) | MATCH | — |
| find_trigger() -> findTrigger | findTrigger (method) | findTrigger (method) | MATCH | — |
| get_all_triggers() -> getAllTriggers | getAllTriggers (method) | getAllTriggers (method) | MATCH | — |
| get_elements_in_diagram() -> getElementsInDiagram | getElementsInDiagram (method) | getElementsInDiagram (method) | MATCH | — |
| get_inherits_from() -> getInheritsFrom | getInheritsFrom (method) | getInheritsFrom (method) | MATCH | — |
| get_picture() -> getPicture | getPicture (method) | getPicture (method) | MATCH | — |
| get_picture_as() -> getPictureAs | getPictureAs (method) | getPictureAs (method) | MATCH | — |
| get_picture_as_divided_metafiles() -> getPictureAsDividedMetafiles | getPictureAsDividedMetafiles (method) | getPictureAsDividedMetafiles (method) | MATCH | — |
| get_pictures_with_image_map() -> getPicturesWithImageMap | getPicturesWithImageMap (method) | getPicturesWithImageMap (method) | MATCH | — |
| get_statechart_diagram() -> getStatechartDiagram | getStatechartDiagram (method) | getStatechartDiagram (method) | MATCH | — |
| graphical_elements (property) -> graphicalElements | getGraphicalElements (method) | graphicalElements (property) | MATCH | — |
| is_main_behavior (property) -> isMainBehavior | getIsMainBehavior (method) | isMainBehavior (property) | MATCH | — |
| is_overridden (property) -> isOverridden | getIsOverridden (method) | isOverridden (property) | MATCH | — |
| its_class (property) -> itsClass | getItsClass (method) | itsClass (property) | MATCH | — |
| open_diagram_view() -> OpenDiagramView | openDiagramView (method) | OpenDiagramView (method) | MATCH | — |
| override_inheritance() -> overrideInheritance | overrideInheritance (method) | overrideInheritance (method) | MATCH | — |
| populate_diagram() -> populateDiagram | populateDiagram (method) | populateDiagram (method) | MATCH | — |
| root_state (property) -> rootState | getRootState (method) | rootState (property) | MATCH | — |
| set_as_main_behavior() -> setAsMainBehavior | setAsMainBehavior (method) | setAsMainBehavior (method) | MATCH | — |
| set_show_diagram_frame() -> setShowDiagramFrame | setShowDiagramFrame (method) | setShowDiagramFrame (method) | MATCH | — |
| unoverride_inheritance() -> unoverrideInheritance | unoverrideInheritance (method) | unoverrideInheritance (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
