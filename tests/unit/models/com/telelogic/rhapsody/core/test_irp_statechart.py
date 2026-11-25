"""Fake-COM tests for the JavaDoc-owned IRPStatechart API."""

from unittest.mock import MagicMock

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass, IRPStatechart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphElement, IRPGraphNode
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart import IRPStatechart as IRPStatechartModuleClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_statechart_is_a_class_and_registered() -> None:
    fake = make_fake_element("Statechart", properties={"name": "Behavior"})
    statechart = IRPStatechart(fake)

    assert isinstance(statechart, IRPClass)
    assert statechart.name == "Behavior"
    assert isinstance(IRPModelElement.wrap(fake), IRPStatechart)


def test_add_free_shape_by_type_uses_authoritative_member_and_collections() -> None:
    fake = make_fake_element("Statechart")
    shape = MagicMock(spec=[])
    fake.AddFreeShapeByType.return_value = shape
    statechart = IRPStatechart(fake)
    x_points = IRPCollection(make_fake_collection([]))
    y_points = IRPCollection(make_fake_collection([]))

    result = statechart.add_free_shape_by_type("Ellipse", x_points, y_points)

    fake.AddFreeShapeByType.assert_called_once_with("Ellipse", x_points._com, y_points._com)
    assert result._com is shape


def test_add_image_passes_file_and_geometry() -> None:
    fake = make_fake_element("Statechart")
    image = MagicMock(spec=[])
    fake.AddImage.return_value = image
    statechart = IRPStatechart(fake)

    result = statechart.add_image("image.emf", 10, 20, 100, 80)

    fake.AddImage.assert_called_once_with("image.emf", 10, 20, 100, 80)
    assert result._com is image


def test_add_new_edge_by_type_unwraps_graph_elements() -> None:
    fake = make_fake_element("Statechart")
    edge = MagicMock(spec=[])
    fake.AddNewEdgeByType.return_value = edge
    statechart = IRPStatechart(fake)
    source_com = make_fake_element("GraphNode")
    target_com = make_fake_element("GraphNode")

    result = statechart.add_new_edge_by_type("anchor", IRPGraphElement(source_com), 1, 2, IRPGraphElement(target_com), 3, 4)

    fake.AddNewEdgeByType.assert_called_once_with("anchor", source_com, 1, 2, target_com, 3, 4)
    assert result._com is edge


def test_add_new_edge_for_element_unwraps_model_and_graph_elements() -> None:
    fake = make_fake_element("Statechart")
    edge = MagicMock(spec=[])
    fake.AddNewEdgeForElement.return_value = edge
    statechart = IRPStatechart(fake)
    model_com = make_fake_element("Transition")
    source_com = make_fake_element("GraphNode")
    target_com = make_fake_element("GraphNode")

    result = statechart.add_new_edge_for_element(IRPModelElement(model_com), IRPGraphNode(source_com), 1, 2, IRPGraphNode(target_com), 3, 4)

    fake.AddNewEdgeForElement.assert_called_once_with(model_com, source_com, 1, 2, target_com, 3, 4)
    assert result._com is edge


def test_add_new_node_by_type_wraps_result() -> None:
    fake = make_fake_element("Statechart")
    node = MagicMock(spec=[])
    fake.AddNewNodeByType.return_value = node
    statechart = IRPStatechart(fake)

    result = statechart.add_new_node_by_type("State", 10, 20, 100, 50)

    fake.AddNewNodeByType.assert_called_once_with("State", 10, 20, 100, 50)
    assert result._com is node


def test_add_new_node_for_element_unwraps_element_and_wraps_node() -> None:
    fake = make_fake_element("Statechart")
    node = MagicMock(spec=[])
    fake.AddNewNodeForElement.return_value = node
    statechart = IRPStatechart(fake)
    model_com = make_fake_element("Class")

    result = statechart.add_new_node_for_element(IRPModelElement(model_com), 10, 20, 100, 50)

    fake.AddNewNodeForElement.assert_called_once_with(model_com, 10, 20, 100, 50)
    assert result._com is node


def test_add_text_box_passes_text_and_geometry() -> None:
    fake = make_fake_element("Statechart")
    text_box = MagicMock(spec=[])
    fake.AddTextBox.return_value = text_box
    statechart = IRPStatechart(fake)

    result = statechart.add_text_box("note", 10, 20, 100, 50)

    fake.AddTextBox.assert_called_once_with("note", 10, 20, 100, 50)
    assert result._com is text_box


def test_open_diagram_view_wraps_ax_view_controller() -> None:
    fake = make_fake_element("Statechart")
    view_controller = make_fake_element("AXViewCtrl")
    fake.OpenDiagramView.return_value = view_controller
    statechart = IRPStatechart(fake)

    result = statechart.open_diagram_view()

    fake.OpenDiagramView.assert_called_once_with()
    assert result._com is view_controller


@pytest.mark.parametrize("method_name", ["addNewAcceptEventAction", "addNewAcceptTimeEvent"])
def test_accept_event_creation_stubs_without_com_dispatch(method_name: str) -> None:
    fake = make_fake_element("Statechart")
    statechart = IRPStatechart(fake)
    parent = IRPState(make_fake_element("State"))

    with pytest.raises(NotImplementedError):
        if method_name == "addNewAcceptEventAction":
            statechart.add_new_accept_event_action("Accept", parent)
        else:
            statechart.add_new_accept_time_event("Accept", parent)

    getattr(fake, method_name).assert_not_called()


def test_close_diagram_calls_com() -> None:
    fake = make_fake_element("Statechart")
    IRPStatechart(fake).close_diagram()
    fake.closeDiagram.assert_called_once_with()


def test_create_graphics_calls_com() -> None:
    fake = make_fake_element("Statechart")
    IRPStatechart(fake).create_graphics()
    fake.createGraphics.assert_called_once_with()


def test_delete_state_unwraps_state() -> None:
    fake = make_fake_element("Statechart")
    state_com = make_fake_element("State")
    IRPStatechart(fake).delete_state(IRPState(state_com))
    fake.deleteState.assert_called_once_with(state_com)


def test_find_trigger_uses_interface_item_and_returns_integer() -> None:
    fake = make_fake_element("Statechart", findTrigger=1)
    item_com = make_fake_element("EventReception")

    result = IRPStatechart(fake).find_trigger(IRPInterfaceItem(item_com))

    fake.findTrigger.assert_called_once_with(item_com)
    assert result == 1


def test_get_all_triggers_wraps_collection() -> None:
    fake = make_fake_element("Statechart")
    triggers = make_fake_collection([])
    fake.getAllTriggers.return_value = triggers

    result = IRPStatechart(fake).get_all_triggers()

    fake.getAllTriggers.assert_called_once_with()
    assert isinstance(result, IRPCollection)
    assert result._com is triggers


def test_get_elements_in_diagram_wraps_collection() -> None:
    fake = make_fake_element("Statechart")
    elements = make_fake_collection([])
    fake.getElementsInDiagram.return_value = elements

    result = IRPStatechart(fake).get_elements_in_diagram()

    fake.getElementsInDiagram.assert_called_once_with()
    assert isinstance(result, IRPCollection)
    assert result._com is elements


def test_graphical_elements_property_wraps_collection() -> None:
    fake = make_fake_element("Statechart", properties={"graphicalElements": make_fake_collection([])})

    result = IRPStatechart(fake).graphical_elements

    assert isinstance(result, IRPCollection)
    assert result._com is fake.graphicalElements


def test_get_inherits_from_wraps_statechart() -> None:
    fake = make_fake_element("Statechart")
    inherited = make_fake_element("Statechart")
    fake.getInheritsFrom.return_value = inherited

    result = IRPStatechart(fake).get_inherits_from()

    fake.getInheritsFrom.assert_called_once_with()
    assert result is not None
    assert result._com is inherited


def test_is_main_behavior_property_returns_integer() -> None:
    fake = make_fake_element("Statechart", properties={"isMainBehavior": 1})

    assert IRPStatechart(fake).is_main_behavior == 1


def test_is_overridden_property_returns_integer() -> None:
    fake = make_fake_element("Statechart", properties={"isOverridden": 0})

    assert IRPStatechart(fake).is_overridden == 0


def test_its_class_property_wraps_owner() -> None:
    fake = make_fake_element("Statechart")
    owner = make_fake_element("Class")
    fake.itsClass = owner

    result = IRPStatechart(fake).its_class

    assert result._com is owner


def test_get_picture_passes_filename() -> None:
    fake = make_fake_element("Statechart")
    IRPStatechart(fake).get_picture("statechart.emf")
    fake.getPicture.assert_called_once_with("statechart.emf")


def test_get_picture_as_passes_all_export_arguments_and_wraps_collection() -> None:
    fake = make_fake_element("Statechart")
    files = make_fake_collection([])
    returned_map = make_fake_collection([])
    fake.getPictureAs.return_value = (files, returned_map)
    diagram_map = IRPCollection(make_fake_collection([]))
    input_map = diagram_map._com

    result = IRPStatechart(fake).get_picture_as("statechart.emf", "EMF", 0, diagram_map)

    fake.getPictureAs.assert_called_once_with("statechart.emf", "EMF", 0, input_map)
    assert result._com is files
    assert diagram_map._com is returned_map


def test_get_picture_as_divided_metafiles_passes_filename() -> None:
    fake = make_fake_element("Statechart")
    files = make_fake_collection([])
    fake.getPictureAsDividedMetafiles.return_value = files

    result = IRPStatechart(fake).get_picture_as_divided_metafiles("statechart.emf")

    fake.getPictureAsDividedMetafiles.assert_called_once_with("statechart.emf")
    assert result._com is files


def test_get_pictures_with_image_map_unwraps_map_collection() -> None:
    fake = make_fake_element("Statechart")
    files = make_fake_collection([])
    returned_map = make_fake_collection([])
    fake.getPicturesWithImageMap.return_value = (files, returned_map)
    diagram_map = IRPCollection(make_fake_collection([]))
    input_map = diagram_map._com

    result = IRPStatechart(fake).get_pictures_with_image_map("statechart.emf", diagram_map)

    fake.getPicturesWithImageMap.assert_called_once_with("statechart.emf", input_map)
    assert result._com is files
    assert diagram_map._com is returned_map


def test_root_state_property_wraps_root_state() -> None:
    fake = make_fake_element("Statechart")
    root_state = make_fake_element("State")
    fake.rootState = root_state

    result = IRPStatechart(fake).root_state

    assert result is not None
    assert result._com is root_state


def test_get_statechart_diagram_wraps_diagram() -> None:
    fake = make_fake_element("Statechart")
    diagram = make_fake_element("StatechartDiagram")
    fake.getStatechartDiagram.return_value = diagram

    result = IRPStatechart(fake).get_statechart_diagram()

    fake.getStatechartDiagram.assert_called_once_with()
    assert result._com is diagram


def test_override_inheritance_calls_com() -> None:
    fake = make_fake_element("Statechart")
    IRPStatechart(fake).override_inheritance()
    fake.overrideInheritance.assert_called_once_with()


def test_populate_diagram_unwraps_collections() -> None:
    fake = make_fake_element("Statechart")
    elements = IRPCollection(make_fake_collection([]))
    relation_types = IRPCollection(make_fake_collection([]))

    IRPStatechart(fake).populate_diagram(elements, relation_types, "among")

    fake.populateDiagram.assert_called_once_with(elements._com, relation_types._com, "among")


def test_set_as_main_behavior_has_no_arguments() -> None:
    fake = make_fake_element("Statechart")
    IRPStatechart(fake).set_as_main_behavior()
    fake.setAsMainBehavior.assert_called_once_with()


def test_set_show_diagram_frame_calls_com() -> None:
    fake = make_fake_element("Statechart")
    IRPStatechart(fake).set_show_diagram_frame(1)
    fake.setShowDiagramFrame.assert_called_once_with(1)


def test_unoverride_inheritance_calls_com() -> None:
    fake = make_fake_element("Statechart")
    IRPStatechart(fake).unoverride_inheritance()
    fake.unoverrideInheritance.assert_called_once_with()


# Keep the module binding explicit so imports exercise the canonical module path.
assert IRPStatechartModuleClass is IRPStatechart
