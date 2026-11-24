"""Tests for rhapsody_cli.elements.statechart.IRPStatechart."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass, IRPStatechart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_statechart_is_a_class() -> None:
    fake = make_fake_element("Statechart", properties={"name": "Behavior"})
    statechart = IRPStatechart(fake)

    assert isinstance(statechart, IRPClass)
    assert statechart.name == "Behavior"


def test_statechart_add_new_node_by_type_wraps_result() -> None:
    fake = make_fake_element("Statechart")
    node = make_fake_element("State", properties={"name": "Idle"})
    fake.addNewNodeByType.return_value = node
    statechart = IRPStatechart(fake)

    result = statechart.add_new_node_by_type("State", 10, 20, 100, 50)

    fake.addNewNodeByType.assert_called_once_with("State", 10, 20, 100, 50)
    assert result.name == "Idle"


def test_statechart_create_graphics_delegates_to_com() -> None:
    fake = make_fake_element("Statechart")
    statechart = IRPStatechart(fake)

    statechart.create_graphics()

    fake.createGraphics.assert_called_once_with()


def test_statechart_close_diagram_delegates_to_com() -> None:
    fake = make_fake_element("Statechart")
    statechart = IRPStatechart(fake)

    statechart.close_diagram()

    fake.closeDiagram.assert_called_once_with()


def test_statechart_delete_state_delegates_to_com() -> None:
    fake = make_fake_element("Statechart")
    state = make_fake_element("State", properties={"name": "Idle"})
    statechart = IRPStatechart(fake)

    statechart.delete_state(IRPModelElement(state))

    fake.deleteState.assert_called_once_with(state)


def test_statechart_is_registered_for_meta_class_statechart() -> None:
    fake = make_fake_element("Statechart", properties={"name": "Behavior"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPStatechart)


def test_statechart_get_pictures_with_image_map_delegates_to_com_with_two_args() -> None:
    fake = make_fake_element("Statechart")
    file_names = make_fake_collection([])
    fake.getPicturesWithImageMap.return_value = file_names
    statechart = IRPStatechart(fake)
    diagram_map = IRPCollection(make_fake_collection([]))

    result = statechart.get_pictures_with_image_map("output.emf", diagram_map)

    fake.getPicturesWithImageMap.assert_called_once_with("output.emf", diagram_map._com)
    assert isinstance(result, IRPCollection)
