"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagrams.IRPDiagram."""

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagrams import IRPDiagram
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphEdge, IRPGraphElement, IRPGraphNode
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_diagram_is_a_unit() -> None:
    fake = make_fake_element("ActivityDiagram", properties={"name": "MainFlow"})
    diagram = IRPDiagram(fake)

    assert isinstance(diagram, IRPUnit)
    assert diagram.name == "MainFlow"


def test_diagram_close_diagram_delegates_to_com() -> None:
    fake = make_fake_element("ActivityDiagram")
    diagram = IRPDiagram(fake)

    diagram.close_diagram()

    fake.closeDiagram.assert_called_once_with()


def test_diagram_get_picture_as_divided_metafiles_passes_first_filename() -> None:
    fake = make_fake_element("ActivityDiagram")
    returned_files = make_fake_collection([])
    fake.getPictureAsDividedMetafiles.return_value = returned_files
    diagram = IRPDiagram(fake)

    result = diagram.get_picture_as_divided_metafiles("first-page.emf")

    fake.getPictureAsDividedMetafiles.assert_called_once_with("first-page.emf")
    assert isinstance(result, IRPCollection)


def test_diagram_add_text_box_delegates_to_authoritative_add_text_box_member() -> None:
    fake = make_fake_element("ActivityDiagram")
    text_box = make_fake_element("GraphElement", properties={"name": "Note1"})
    fake.AddTextBox.return_value = text_box
    diagram = IRPDiagram(fake)

    result = diagram.add_text_box("hello", 0, 0, 50, 20)

    fake.AddTextBox.assert_called_once_with("hello", 0, 0, 50, 20)
    assert isinstance(result, IRPGraphElement)
    assert result._com is text_box


def test_diagram_add_image_delegates_to_com_and_wraps_result() -> None:
    fake = make_fake_element("ActivityDiagram")
    image = make_fake_element("GraphElement", properties={"name": "Logo"})
    fake.AddImage.return_value = image
    diagram = IRPDiagram(fake)

    result = diagram.add_image("logo.bmp", 10, 10, 40, 40)

    fake.AddImage.assert_called_once_with("logo.bmp", 10, 10, 40, 40)
    assert isinstance(result, IRPGraphElement)
    assert result._com is image


def test_diagram_add_free_shape_by_type_passes_coordinate_collections() -> None:
    fake = make_fake_element("ActivityDiagram")
    shape = make_fake_element("GraphElement")
    fake.AddFreeShapeByType.return_value = shape
    diagram = IRPDiagram(fake)
    x_points = IRPCollection(make_fake_collection([]))
    y_points = IRPCollection(make_fake_collection([]))

    result = diagram.add_free_shape_by_type("Polygon", x_points, y_points)

    fake.AddFreeShapeByType.assert_called_once_with("Polygon", x_points._com, y_points._com)
    assert isinstance(result, IRPGraphElement)
    assert result._com is shape


def test_diagram_add_new_node_by_type_wraps_graph_node_directly() -> None:
    fake = make_fake_element("ActivityDiagram")
    graph_node = make_fake_element("GraphNode")
    fake.AddNewNodeByType.return_value = graph_node
    diagram = IRPDiagram(fake)

    result = diagram.add_new_node_by_type("Note", 10, 20, 40, 30)

    fake.AddNewNodeByType.assert_called_once_with("Note", 10, 20, 40, 30)
    assert isinstance(result, IRPGraphNode)
    assert result._com is graph_node


def test_diagram_add_new_node_for_element_wraps_graph_node_directly() -> None:
    fake = make_fake_element("ActivityDiagram")
    graph_node = make_fake_element("GraphNode")
    fake.AddNewNodeForElement.return_value = graph_node
    diagram = IRPDiagram(fake)
    model_element = make_fake_element("Class")

    result = diagram.add_new_node_for_element(IRPModelElement(model_element), 10, 20, 40, 30)

    fake.AddNewNodeForElement.assert_called_once_with(model_element, 10, 20, 40, 30)
    assert isinstance(result, IRPGraphNode)
    assert result._com is graph_node


def test_diagram_add_new_edge_by_type_passes_both_nodes_and_positions() -> None:
    fake = make_fake_element("ActivityDiagram")
    graph_edge = make_fake_element("GraphEdge")
    fake.AddNewEdgeByType.return_value = graph_edge
    diagram = IRPDiagram(fake)
    source_com = make_fake_element("GraphElement")
    target_com = make_fake_element("GraphElement")
    source = IRPGraphElement(source_com)
    target = IRPGraphElement(target_com)

    result = diagram.add_new_edge_by_type("anchor", source, 10, 20, target, 30, 40)

    fake.AddNewEdgeByType.assert_called_once_with("anchor", source_com, 10, 20, target_com, 30, 40)
    assert isinstance(result, IRPGraphEdge)
    assert result._com is graph_edge


def test_diagram_add_new_edge_for_element_passes_both_nodes_and_positions() -> None:
    fake = make_fake_element("ActivityDiagram")
    graph_edge = make_fake_element("GraphEdge")
    fake.AddNewEdgeForElement.return_value = graph_edge
    diagram = IRPDiagram(fake)
    element_com = make_fake_element("Dependency")
    source_com = make_fake_element("GraphNode")
    target_com = make_fake_element("GraphNode")

    result = diagram.add_new_edge_for_element(IRPModelElement(element_com), IRPGraphNode(source_com), 10, 20, IRPGraphNode(target_com), 30, 40)

    fake.AddNewEdgeForElement.assert_called_once_with(element_com, source_com, 10, 20, target_com, 30, 40)
    assert isinstance(result, IRPGraphEdge)
    assert result._com is graph_edge


def test_diagram_get_custom_views_is_documented_unavailable() -> None:
    """The catalog exposes neither getCustomViews nor customViews for IRPDiagram."""
    fake = make_fake_element("ActivityDiagram")
    diagram = IRPDiagram(fake)

    with pytest.raises(NotImplementedError, match="getCustomViews is not exposed"):
        diagram.get_custom_views()


def test_diagram_graphical_elements_reads_catalog_property() -> None:
    fake = make_fake_element("ActivityDiagram")
    graphic = make_fake_element("GraphElement", properties={"name": "Shape1"})
    fake.graphicalElements = make_fake_collection([graphic])
    diagram = IRPDiagram(fake)

    elements = diagram.graphical_elements

    assert len(elements) == 1
    assert elements[0].name == "Shape1"


def test_diagram_get_corresponding_graphic_elements_returns_collection() -> None:
    fake = make_fake_element("ActivityDiagram")
    graphic = make_fake_element("GraphElement", properties={"name": "Shape1"})
    fake.getCorrespondingGraphicElements.return_value = make_fake_collection([graphic])
    diagram = IRPDiagram(fake)
    model_element = make_fake_element("Class", properties={"name": "Widget"})

    elements = diagram.get_corresponding_graphic_elements(IRPModelElement(model_element))

    fake.getCorrespondingGraphicElements.assert_called_once_with(model_element)
    assert len(elements) == 1
    assert elements[0].name == "Shape1"


def test_diagram_get_last_visualization_modified_time_delegates_to_com() -> None:
    fake = make_fake_element("ActivityDiagram")
    fake.getLastVisualizationModifiedTime.return_value = "2026-11-27 10:00:00"
    diagram = IRPDiagram(fake)

    modified = diagram.get_last_visualization_modified_time()

    fake.getLastVisualizationModifiedTime.assert_called_once_with()
    assert modified == "2026-11-27 10:00:00"


def test_diagram_create_diagram_view_is_documented_unavailable() -> None:
    """createDiagramView is absent from the registered pywin32 interface."""
    fake = make_fake_element("ActivityDiagram")
    diagram = IRPDiagram(fake)

    with pytest.raises(NotImplementedError, match="createDiagramView is not exposed"):
        diagram.create_diagram_view("View1")


def test_diagram_get_diagram_view_of_is_documented_unavailable() -> None:
    """getDiagramViewOf is absent from the registered pywin32 interface."""
    fake = make_fake_element("ActivityDiagram")
    diagram = IRPDiagram(fake)

    with pytest.raises(NotImplementedError, match="getDiagramViewOf is not exposed"):
        diagram.get_diagram_view_of("View1")


def test_diagram_get_diagram_views_is_documented_unavailable() -> None:
    """getDiagramViews is absent from the registered pywin32 interface."""
    fake = make_fake_element("ActivityDiagram")
    diagram = IRPDiagram(fake)

    with pytest.raises(NotImplementedError, match="getDiagramViews is not exposed"):
        diagram.get_diagram_views()


def test_diagram_is_diagram_view_is_documented_unavailable() -> None:
    """isDiagramView is absent from the registered pywin32 interface."""
    fake = make_fake_element("ActivityDiagram")
    diagram = IRPDiagram(fake)

    with pytest.raises(NotImplementedError, match="isDiagramView is not exposed"):
        diagram.is_diagram_view()


def test_diagram_rearrange_ports_is_documented_unavailable() -> None:
    """rearrangePorts is absent from the registered pywin32 interface."""
    fake = make_fake_element("ActivityDiagram")
    diagram = IRPDiagram(fake)

    with pytest.raises(NotImplementedError, match="rearrangePorts is not exposed"):
        diagram.rearrange_ports()


def test_diagram_set_custom_views_is_documented_unavailable() -> None:
    """setCustomViews is absent from the registered pywin32 interface."""
    fake = make_fake_element("ActivityDiagram")
    diagram = IRPDiagram(fake)
    views = IRPCollection(make_fake_collection([]))

    with pytest.raises(NotImplementedError, match="setCustomViews is not exposed"):
        diagram.set_custom_views(views)


def test_diagram_update_view_on_server_is_documented_unavailable() -> None:
    """updateViewOnServer is absent from the registered pywin32 interface."""
    fake = make_fake_element("ActivityDiagram")
    diagram = IRPDiagram(fake)

    with pytest.raises(NotImplementedError, match="updateViewOnServer is not exposed"):
        diagram.update_view_on_server()


def test_diagram_is_registered_for_meta_class_activity_diagram() -> None:
    fake = make_fake_element("ActivityDiagram", properties={"name": "MainFlow"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPDiagram)


def test_diagram_complete_relations_passes_graph_collection_and_scope() -> None:
    fake = make_fake_element("ActivityDiagram")
    diagram = IRPDiagram(fake)
    graph_elements = IRPCollection(make_fake_collection([]))

    diagram.complete_relations(graph_elements, 1)

    fake.completeRelations.assert_called_once_with(graph_elements._com, 1)


def test_diagram_populate_diagram_passes_elements_relation_types_and_content_mode() -> None:
    fake = make_fake_element("ActivityDiagram")
    diagram = IRPDiagram(fake)
    elements = IRPCollection(make_fake_collection([]))
    relation_types = IRPCollection(make_fake_collection([]))

    diagram.populate_diagram(elements, relation_types, "among")

    fake.populateDiagram.assert_called_once_with(elements._com, relation_types._com, "among")


def test_diagram_get_pictures_with_image_map_wraps_pywin_return_and_passes_two_args() -> None:
    fake = make_fake_element("ObjectModelDiagram")
    file_names = make_fake_collection([])
    diagram_map_com = make_fake_collection([])
    fake.getPicturesWithImageMap.return_value = (file_names, diagram_map_com)
    diagram = IRPDiagram(fake)
    diagram_map = IRPCollection(diagram_map_com)

    result = diagram.get_pictures_with_image_map("output.emf", diagram_map)

    fake.getPicturesWithImageMap.assert_called_once_with("output.emf", diagram_map._com)
    assert isinstance(result, IRPCollection)
    assert result._com is file_names
