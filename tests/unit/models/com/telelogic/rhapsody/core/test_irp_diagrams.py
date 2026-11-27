"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagrams.IRPDiagram."""

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagrams import IRPDiagram
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
    assert result.name == "Note1"


def test_diagram_add_image_delegates_to_com_and_wraps_result() -> None:
    fake = make_fake_element("ActivityDiagram")
    image = make_fake_element("GraphElement", properties={"name": "Logo"})
    fake.AddImage.return_value = image
    diagram = IRPDiagram(fake)

    result = diagram.add_image("logo.bmp", 10, 10, 40, 40)

    fake.AddImage.assert_called_once_with("logo.bmp", 10, 10, 40, 40)
    assert result.name == "Logo"


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


def test_diagram_get_pictures_with_image_map_delegates_to_com_with_two_args() -> None:
    fake = make_fake_element("ObjectModelDiagram")
    file_names = make_fake_collection([])
    fake.getPicturesWithImageMap.return_value = file_names
    diagram = IRPDiagram(fake)
    diagram_map = IRPCollection(make_fake_collection([]))

    result = diagram.get_pictures_with_image_map("output.emf", diagram_map)

    fake.getPicturesWithImageMap.assert_called_once_with("output.emf", diagram_map._com)
    assert isinstance(result, IRPCollection)
