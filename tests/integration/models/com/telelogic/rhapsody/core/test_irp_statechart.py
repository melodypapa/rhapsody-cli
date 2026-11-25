"""Live integration tests for the JavaDoc-owned IRPStatechart API."""

import struct
import uuid
from pathlib import Path
from typing import Tuple, cast

import pytest

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass, IRPStatechart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPStatechartIntegration:
    """Exercise statechart-owned behavior with objects from a live project."""

    @staticmethod
    def _unique(prefix: str) -> str:
        return f"{prefix}_{uuid.uuid4().hex}"

    def _create_statechart(self, project: IRPProject, prefix: str = "Statechart") -> Tuple[IRPPackage, IRPClass, IRPStatechart]:
        package = project.add_package(self._unique(f"{prefix}Pkg"))
        classifier = package.add_class(self._unique(f"{prefix}Class"))
        statechart = classifier.add_statechart()
        assert statechart is not None
        statechart.create_graphics()
        return package, classifier, statechart

    @staticmethod
    def _new_integer_collection(rhapsody_app: RhapsodyApplication, values: tuple[int, ...]) -> IRPCollection:
        collection = rhapsody_app.create_new_collection()
        collection.set_size(len(values))
        for index, value in enumerate(values, start=1):
            collection.set_integer(index, value)
        return collection

    def test_add_free_shape_by_type(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        package, _, statechart = self._create_statechart(test_project, "FreeShape")
        try:
            x_points = self._new_integer_collection(rhapsody_app, (20, 80, 80, 20))
            y_points = self._new_integer_collection(rhapsody_app, (20, 20, 80, 80))

            shape = statechart.add_free_shape_by_type("Polygon", x_points, y_points)

            assert shape._com in list(statechart.graphical_elements)
        finally:
            package.delete_from_project()

    def test_add_image(self, test_project: IRPProject, tmp_path: Path) -> None:
        package, _, statechart = self._create_statechart(test_project, "Image")
        try:
            image_path = tmp_path / "statechart-image.bmp"
            pixel_data = b"\x00\x00\xff\x00"
            bitmap_file_size = 54 + len(pixel_data)
            bitmap_header = struct.pack("<2sIHHI", b"BM", bitmap_file_size, 0, 0, 54)
            dib_header = struct.pack("<IiiHHIIiiII", 40, 1, 1, 1, 24, 0, len(pixel_data), 2835, 2835, 0, 0)
            image_path.write_bytes(bitmap_header + dib_header + pixel_data)

            image = statechart.add_image(str(image_path), 20, 20, 40, 40)

            assert image._com in list(statechart.graphical_elements)
        finally:
            package.delete_from_project()

    def test_add_new_edge_for_element(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "ModelEdge")
        try:
            root_state = statechart.root_state
            assert root_state is not None
            source_state = root_state.add_state(self._unique("SourceState"))
            target_state = root_state.add_state(self._unique("TargetState"))
            transition = source_state.add_transition(target_state)
            source_node = statechart.add_new_node_for_element(source_state, 20, 20, 80, 50)
            target_node = statechart.add_new_node_for_element(target_state, 200, 20, 80, 50)

            edge = statechart.add_new_edge_for_element(transition, source_node, 60, 40, target_node, 240, 40)

            assert edge._com in list(statechart.graphical_elements)
        finally:
            package.delete_from_project()

    def test_add_new_node_by_type_and_get_elements_in_diagram(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "GraphNode")
        try:
            node = statechart.add_new_node_by_type("Note", 20, 20, 80, 50)

            assert node._com in list(statechart.graphical_elements)
            assert statechart.get_elements_in_diagram().count > 0
        finally:
            package.delete_from_project()

    def test_add_new_node_for_element(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "ModelNode")
        try:
            root_state = statechart.root_state
            assert root_state is not None
            created_state = root_state.add_state(self._unique("ChildState"))

            node = statechart.add_new_node_for_element(created_state, 20, 20, 80, 50)

            assert node._com in list(statechart.graphical_elements)
            assert created_state in list(statechart.get_elements_in_diagram())
        finally:
            package.delete_from_project()

    def test_add_text_box(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "TextBox")
        try:
            text_box = statechart.add_text_box("Statechart integration note", 20, 20, 180, 60)

            assert text_box._com in list(statechart.graphical_elements)
        finally:
            package.delete_from_project()

    def test_add_new_accept_event_action_is_documented_unavailable(self, test_project: IRPProject) -> None:
        """JavaDoc declares addNewAcceptEventAction(name, parent), but the registered IRPStatechart typelib and authority catalog expose no such member; the wrapper raises before COM dispatch."""
        package, _, statechart = self._create_statechart(test_project, "UnavailableAcceptEvent")
        try:
            root_state = statechart.root_state
            assert root_state is not None

            with pytest.raises(NotImplementedError):
                statechart.add_new_accept_event_action(self._unique("AcceptEvent"), root_state)
        finally:
            package.delete_from_project()

    def test_add_new_accept_time_event_is_documented_unavailable(self, test_project: IRPProject) -> None:
        """JavaDoc declares addNewAcceptTimeEvent(name, parent), but the registered IRPStatechart typelib and authority catalog expose no such member; the wrapper raises before COM dispatch."""
        package, _, statechart = self._create_statechart(test_project, "UnavailableAcceptTime")
        try:
            root_state = statechart.root_state
            assert root_state is not None

            with pytest.raises(NotImplementedError):
                statechart.add_new_accept_time_event(self._unique("AcceptTime"), root_state)
        finally:
            package.delete_from_project()

    def test_close_diagram(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "CloseDiagram")
        try:
            statechart.close_diagram()
            assert statechart.get_statechart_diagram() is not None
        finally:
            package.delete_from_project()

    def test_create_graphics(self, test_project: IRPProject) -> None:
        package = test_project.add_package(self._unique("CreateGraphicsPkg"))
        classifier = package.add_class(self._unique("CreateGraphicsClass"))
        statechart = classifier.add_statechart()
        assert statechart is not None
        try:
            statechart.create_graphics()
            assert statechart.get_statechart_diagram() is not None
        finally:
            package.delete_from_project()

    def test_delete_state(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "DeleteState")
        try:
            root_state = statechart.root_state
            assert root_state is not None
            state = root_state.add_state(self._unique("DeletedState"))
            assert state in list(root_state.get_sub_states())

            statechart.delete_state(state)

            assert state not in list(root_state.get_sub_states())
        finally:
            package.delete_from_project()

    def test_find_trigger_with_attached_event_reception(self, test_project: IRPProject) -> None:
        package, classifier, statechart = self._create_statechart(test_project, "FindTrigger")
        try:
            event_reception = classifier.add_event_reception(self._unique("TriggerReception"))
            event = cast(IRPEvent, package.add_event(self._unique("TriggerEvent")))
            event_reception.set_event(event)
            root_state = statechart.root_state
            assert root_state is not None
            root_state.add_internal_transition(event_reception)

            assert statechart.find_trigger(cast(IRPInterfaceItem, event)) == 1
        finally:
            package.delete_from_project()

    def test_all_triggers_contains_transition_trigger(self, test_project: IRPProject) -> None:
        package, classifier, statechart = self._create_statechart(test_project, "AllTriggers")
        try:
            event_reception = classifier.add_event_reception(self._unique("TriggerReception"))
            event = cast(IRPEvent, package.add_event(self._unique("TriggerEvent")))
            event_reception.set_event(event)
            root_state = statechart.root_state
            assert root_state is not None
            root_state.add_internal_transition(event_reception)

            assert event in list(statechart.get_all_triggers())
        finally:
            package.delete_from_project()

    def test_elements_in_diagram_contains_created_state(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "DiagramElements")
        try:
            root_state = statechart.root_state
            assert root_state is not None
            created_state = root_state.add_state(self._unique("DiagramState"))
            statechart.add_new_node_for_element(created_state, 20, 20, 80, 50)

            assert created_state in list(statechart.get_elements_in_diagram())
        finally:
            package.delete_from_project()

    def test_graphical_elements(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "GraphicalElements")
        try:
            node = statechart.add_new_node_by_type("Note", 20, 20, 80, 50)

            assert node._com in list(statechart.graphical_elements)
        finally:
            package.delete_from_project()

    def test_is_main_behavior(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "MainBehavior")
        try:
            statechart.set_as_main_behavior()

            assert statechart.is_main_behavior == 1
        finally:
            package.delete_from_project()

    def test_is_overridden(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "IsOverridden")
        try:
            assert statechart.is_overridden == 1
        finally:
            package.delete_from_project()

    def test_its_class(self, test_project: IRPProject) -> None:
        package, classifier, statechart = self._create_statechart(test_project, "ItsClass")
        try:
            assert statechart.its_class == classifier
        finally:
            package.delete_from_project()

    def test_get_picture_saves_statechart_file(self, test_project: IRPProject, tmp_path: Path) -> None:
        package, _, statechart = self._create_statechart(test_project, "Picture")
        try:
            output_file = tmp_path / "statechart.emf"
            statechart.get_picture(str(output_file))

            assert output_file.exists()
        finally:
            package.delete_from_project()

    def test_get_picture_as_saves_requested_format(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication, tmp_path: Path) -> None:
        package, _, statechart = self._create_statechart(test_project, "PictureAs")
        try:
            output_file = tmp_path / "statechart-as.emf"
            image_map = rhapsody_app.create_new_collection()

            filenames = statechart.get_picture_as(str(output_file), "EMF", 0, image_map)

            assert filenames.count > 0
            assert output_file.exists()
        finally:
            package.delete_from_project()

    def test_get_picture_as_divided_metafiles_creates_file(self, test_project: IRPProject, tmp_path: Path) -> None:
        package, _, statechart = self._create_statechart(test_project, "DividedMetafiles")
        try:
            output_file = tmp_path / "statechart-divided.emf"

            filenames = statechart.get_picture_as_divided_metafiles(str(output_file))

            assert filenames.count > 0
            assert output_file.exists()
        finally:
            package.delete_from_project()

    def test_get_pictures_with_image_map_creates_file(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication, tmp_path: Path) -> None:
        package, _, statechart = self._create_statechart(test_project, "PicturesWithMap")
        try:
            output_file = tmp_path / "statechart-map.emf"
            image_map = rhapsody_app.create_new_collection()

            filenames = statechart.get_pictures_with_image_map(str(output_file), image_map)

            assert filenames.count > 0
            assert output_file.exists()
        finally:
            package.delete_from_project()

    def test_root_state(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "RootState")
        try:
            root_state = statechart.root_state
            assert root_state is not None
            created_state = root_state.add_state(self._unique("RootChild"))

            assert created_state in list(root_state.get_sub_states())
        finally:
            package.delete_from_project()

    def test_statechart_diagram_returns_diagram_for_statechart(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "StatechartDiagram")
        try:
            diagram = statechart.get_statechart_diagram()

            assert diagram.get_statechart() == statechart
        finally:
            package.delete_from_project()

    def test_populate_diagram_adds_selected_model_element(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        package, _, statechart = self._create_statechart(test_project, "PopulateDiagram")
        try:
            root_state = statechart.root_state
            assert root_state is not None
            target_state = root_state.add_state(self._unique("DiagramTarget"))
            elements = rhapsody_app.create_new_collection()
            elements.set_size(1)
            elements.set_model_element(1, target_state)
            relation_types = rhapsody_app.create_new_collection()
            relation_types.set_size(1)
            relation_types.set_string(1, "AllRelations")

            statechart.populate_diagram(elements, relation_types, "among")

            assert target_state in list(statechart.get_elements_in_diagram())
        finally:
            package.delete_from_project()

    def test_set_as_main_behavior_and_show_diagram_frame(self, test_project: IRPProject) -> None:
        package, _, statechart = self._create_statechart(test_project, "MainAndFrame")
        try:
            statechart.set_as_main_behavior()
            assert statechart.is_main_behavior == 1
            statechart.set_show_diagram_frame(1)
            statechart.set_show_diagram_frame(0)
        finally:
            package.delete_from_project()
