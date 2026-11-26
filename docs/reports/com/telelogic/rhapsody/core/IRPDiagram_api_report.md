# Rhapsody API Validation: IRPDiagram

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPDiagram` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_diagrams.py`)
- Members: Python `33`, Java `33`, pywin32 `25`
- Deviation items: `19` (actionable `19`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_free_shape_by_type() -> addFreeShapeByType | addFreeShapeByType (method) | AddFreeShapeByType (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| add_image() -> addImage | addImage (method) | AddImage (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| add_new_edge_by_type() -> addNewEdgeByType | addNewEdgeByType (method) | AddNewEdgeByType (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| add_new_edge_for_element() -> addNewEdgeForElement | addNewEdgeForElement (method) | AddNewEdgeForElement (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| add_new_node_by_type() -> addNewNodeByType | addNewNodeByType (method) | AddNewNodeByType (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| add_new_node_for_element() -> addNewNodeForElement | addNewNodeForElement (method) | AddNewNodeForElement (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| add_text_box() -> addTextBox | addTextBox (method) | AddTextBox (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| create_diagram_view() -> createDiagramView | createDiagramView (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_custom_views() -> customViews; get_custom_views() -> getCustomViews; set_custom_views() -> setCustomViews | getCustomViews (method); setCustomViews (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_diagram_view_of() -> getDiagramViewOf | getDiagramViewOf (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_diagram_views() -> getDiagramViews | getDiagramViews (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_graphical_elements() -> getGraphicalElements | getGraphicalElements (method) | graphicalElements (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the graphicalElements property or a getter/setter fallback instead of calling getGraphicalElements directly. |
| is_diagram_view() -> isDiagramView | isDiagramView (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| open_diagram_view() -> openDiagramView | openDiagramView (method) | OpenDiagramView (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| rearrange_ports() -> rearrangePorts | rearrangePorts (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| update_view_on_server() -> updateViewOnServer | updateViewOnServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| add_free_shape_by_type() -> addFreeShapeByType | — | addFreeShapeByType (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [5] arg(s) but pywin32 declares 3 parameter(s) (0 required; params: metaType, xPoints, yPoints; types: str, com, com). Pass the documented parameters. |
| get_picture_ex() -> getPictureEx | — | getPictureEx (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [4] arg(s) but pywin32 declares 3 parameter(s) (0 required; params: filename, exportScale, smartZoom; types: str, str, int). Pass the documented parameters. |
| open_diagram_view() -> openDiagramView | — | openDiagramView (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 0 parameter(s) (0 required; params: —; types: —). Pass the documented parameters. |

<details>
<summary>Correct items (16) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| close_diagram() -> closeDiagram | closeDiagram (method) | closeDiagram (method) | MATCH | — |
| complete_relations() -> completeRelations | completeRelations (method) | completeRelations (method) | MATCH | — |
| get_corresponding_graphic_elements() -> getCorrespondingGraphicElements | getCorrespondingGraphicElements (method) | getCorrespondingGraphicElements (method) | MATCH | — |
| get_elements_in_diagram() -> getElementsInDiagram | getElementsInDiagram (method) | getElementsInDiagram (method) | MATCH | — |
| is_open() -> isOpen | isOpen (method) | isOpen (method) | MATCH | — |
| is_show_diagram_frame() -> isShowDiagramFrame | isShowDiagramFrame (method) | isShowDiagramFrame (method) | MATCH | — |
| get_last_visualization_modified_time() -> getLastVisualizationModifiedTime | getLastVisualizationModifiedTime (method) | getLastVisualizationModifiedTime (method) | MATCH | — |
| open_diagram() -> openDiagram | openDiagram (method) | openDiagram (method) | MATCH | — |
| get_picture() -> getPicture | getPicture (method) | getPicture (method) | MATCH | — |
| get_picture_as() -> getPictureAs | getPictureAs (method) | getPictureAs (method) | MATCH | — |
| get_picture_as_divided_metafiles() -> getPictureAsDividedMetafiles | getPictureAsDividedMetafiles (method) | getPictureAsDividedMetafiles (method) | MATCH | — |
| get_picture_ex() -> getPictureEx | getPictureEx (method) | getPictureEx (method) | MATCH | — |
| get_pictures_with_image_map() -> getPicturesWithImageMap | getPicturesWithImageMap (method) | getPicturesWithImageMap (method) | MATCH | — |
| populate_diagram() -> populateDiagram | populateDiagram (method) | populateDiagram (method) | MATCH | — |
| remove_graph_elements() -> removeGraphElements | removeGraphElements (method) | removeGraphElements (method) | MATCH | — |
| set_show_diagram_frame() -> setShowDiagramFrame | setShowDiagramFrame (method) | setShowDiagramFrame (method) | MATCH | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH (8 findings)
- **Target:** `IRPDiagram` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_diagrams.py`
- **Affected call(s):** add_free_shape_by_type() -> addFreeShapeByType; add_image() -> addImage; add_new_edge_by_type() -> addNewEdgeByType; add_new_edge_for_element() -> addNewEdgeForElement; add_new_node_by_type() -> addNewNodeByType; add_new_node_for_element() -> addNewNodeForElement; add_text_box() -> addTextBox; open_diagram_view() -> openDiagramView
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### PYWIN32_MEMBER_MISSING (7 findings)
- **Target:** `IRPDiagram` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_diagrams.py`
- **Affected call(s):** create_diagram_view() -> createDiagramView; get_custom_views() -> customViews; get_custom_views() -> getCustomViews; set_custom_views() -> setCustomViews; get_diagram_view_of() -> getDiagramViewOf; get_diagram_views() -> getDiagramViews; is_diagram_view() -> isDiagramView; rearrange_ports() -> rearrangePorts; update_view_on_server() -> updateViewOnServer
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPDiagram` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_diagrams.py`
- **Affected call(s):** get_graphical_elements() -> getGraphicalElements
- **Java signature(s):** `IRPDiagram.getGraphicalElements()`
- **Recommended change:** Use the graphicalElements property or a getter/setter fallback instead of calling getGraphicalElements directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_ARITY_MISMATCH (3 findings)
- **Target:** `IRPDiagram` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_diagrams.py`
- **Affected call(s):** add_free_shape_by_type() -> addFreeShapeByType; get_picture_ex() -> getPictureEx; open_diagram_view() -> openDiagramView
- **Recommended change:** Wrapper passes [5] arg(s) but pywin32 declares 3 parameter(s) (0 required; params: metaType, xPoints, yPoints; types: str, com, com). Pass the documented parameters.
- **Recommended change:** Wrapper passes [4] arg(s) but pywin32 declares 3 parameter(s) (0 required; params: filename, exportScale, smartZoom; types: str, str, int). Pass the documented parameters.
- **Recommended change:** Wrapper passes [1] arg(s) but pywin32 declares 0 parameter(s) (0 required; params: —; types: —). Pass the documented parameters.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
