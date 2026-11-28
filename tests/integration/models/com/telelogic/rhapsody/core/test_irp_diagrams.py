"""Integration tests for IRPDiagram with live Rhapsody COM API.

Scope: only methods that IRPDiagram owns. ``IRPStatechart`` does not inherit
``IRPDiagram`` (it derives from IRPClass), so the statechart graphics tests do
not cover this surface; IRPUnit/IRPModelElement parent members are setup only.

The diagram fixtures wrap the concrete object-model diagram dispatch in
``IRPDiagram`` explicitly so the base-class members are exercised directly,
mirroring the IRPRelation/IRPInstance fixture pattern.

Remaining live blockers: ``add_new_edge_by_type`` dispatches with the JavaDoc
signature, but Rhapsody returns COM error ``-2147221498`` for the tested
anchor fixture; ``open_diagram_view`` needs a diagram view, but
``create_diagram_view`` is a documented stub; ``get_picture``/
``get_picture_as``/``get_picture_ex`` need a rendered-picture surface and are
not asserted here.
"""

import struct
import uuid
from pathlib import Path

import pytest

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPDiagram
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphEdge, IRPGraphElement, IRPGraphNode
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPDiagramIntegration:
    """Integration tests for IRPDiagram with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _diagram(pkg: IRPPackage) -> IRPDiagram:
        diagram = pkg.add_object_model_diagram(f"Diagram_{uuid.uuid4().hex[:8]}")
        assert diagram is not None
        return IRPDiagram(diagram._com)

    @staticmethod
    def _integer_collection(rhapsody_app: RhapsodyApplication, values: tuple[int, ...]) -> IRPCollection:
        collection = rhapsody_app.create_new_collection()
        collection.set_size(len(values))
        for index, value in enumerate(values, start=1):
            collection.set_integer(index, value)
        return collection

    @staticmethod
    def _bmp(tmp_path: Path, name: str) -> str:
        """Write a minimal 1x1 24-bit BMP and return its path string."""
        image_path = tmp_path / name
        pixel_data = b"\x00\x00\xff\x00"
        bitmap_file_size = 54 + len(pixel_data)
        bitmap_header = struct.pack("<2sIHHI", b"BM", bitmap_file_size, 0, 0, 54)
        dib_header = struct.pack("<IiiHHIIiiII", 40, 1, 1, 1, 24, 0, len(pixel_data), 2835, 2835, 0, 0)
        image_path.write_bytes(bitmap_header + dib_header + pixel_data)
        return str(image_path)

    def test_create_object_model_diagram(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("DiagPkg"))
        try:
            diagram_name = self._unique("MyDiagram")
            diagram = pkg.add_object_model_diagram(diagram_name)
            assert diagram is not None
            assert isinstance(diagram, IRPDiagram)
            assert diagram.name == diagram_name
        finally:
            pkg.delete_from_project()

    def test_add_text_box(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TextBoxPkg"))
        try:
            diagram = self._diagram(pkg)
            initial_count = diagram.graphical_elements.count
            text_box = diagram.add_text_box("Integration note", 20, 20, 180, 60)
            assert isinstance(text_box, IRPGraphElement)
            assert diagram.graphical_elements.count == initial_count + 1
        finally:
            pkg.delete_from_project()

    def test_add_image(self, test_project: IRPProject, tmp_path: Path) -> None:
        pkg = test_project.add_package(self._unique("ImagePkg"))
        try:
            diagram = self._diagram(pkg)
            initial_count = diagram.graphical_elements.count
            image = diagram.add_image(self._bmp(tmp_path, "diagram-image.bmp"), 20, 20, 40, 40)
            assert isinstance(image, IRPGraphElement)
            assert diagram.graphical_elements.count == initial_count + 1
        finally:
            pkg.delete_from_project()

    def test_add_free_shape_by_type(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = test_project.add_package(self._unique("FreeShapePkg"))
        try:
            diagram = self._diagram(pkg)
            x_points = self._integer_collection(rhapsody_app, (20, 100, 100, 20))
            y_points = self._integer_collection(rhapsody_app, (20, 20, 100, 100))
            initial_count = diagram.graphical_elements.count
            shape = diagram.add_free_shape_by_type("Polygon", x_points, y_points)
            assert isinstance(shape, IRPGraphElement)
            assert diagram.graphical_elements.count == initial_count + 1
        finally:
            pkg.delete_from_project()

    def test_add_new_node_by_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("NodeByTypePkg"))
        try:
            diagram = self._diagram(pkg)
            initial_count = diagram.graphical_elements.count
            node = diagram.add_new_node_by_type("Note", 20, 20, 80, 50)
            assert isinstance(node, IRPGraphNode)
            assert diagram.graphical_elements.count == initial_count + 1
        finally:
            pkg.delete_from_project()

    def test_add_new_node_for_element_and_get_elements_in_diagram(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("NodeForElemPkg"))
        try:
            diagram = self._diagram(pkg)
            created_class = pkg.add_class(self._unique("GraphClass"))
            initial_count = diagram.graphical_elements.count
            node = diagram.add_new_node_for_element(created_class, 20, 20, 80, 50)
            assert isinstance(node, IRPGraphNode)
            assert diagram.graphical_elements.count == initial_count + 1
            assert created_class in list(diagram.get_elements_in_diagram())
        finally:
            pkg.delete_from_project()

    def test_add_new_edge_for_element(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("EdgeForElemPkg"))
        try:
            diagram = self._diagram(pkg)
            source = pkg.add_class(self._unique("EdgeSource"))
            target = pkg.add_class(self._unique("EdgeTarget"))
            relation = source.add_relation_to(target, "targets", "Association", "1", "sources", "Association", "1", "")
            source_node = diagram.add_new_node_for_element(source, 20, 20, 80, 50)
            target_node = diagram.add_new_node_for_element(target, 200, 20, 80, 50)
            initial_count = diagram.graphical_elements.count
            edge = diagram.add_new_edge_for_element(relation, source_node, 60, 45, target_node, 200, 45)
            assert isinstance(edge, IRPGraphEdge)
            assert diagram.graphical_elements.count == initial_count + 1
        finally:
            pkg.delete_from_project()

    def test_graphical_elements_is_a_collection(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("GraphElemsPkg"))
        try:
            diagram = self._diagram(pkg)
            elements = diagram.graphical_elements
            assert isinstance(elements, IRPCollection)
            assert len(list(elements)) == 0
            diagram.add_new_node_by_type("Note", 20, 20, 80, 50)
            assert len(list(diagram.graphical_elements)) == 1
        finally:
            pkg.delete_from_project()

    def test_get_corresponding_graphic_elements(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("CorrGraphPkg"))
        try:
            diagram = self._diagram(pkg)
            created_class = pkg.add_class(self._unique("CorrClass"))
            diagram.add_new_node_for_element(created_class, 20, 20, 80, 50)
            corresponding = diagram.get_corresponding_graphic_elements(created_class)
            assert isinstance(corresponding, IRPCollection)
            assert len(list(corresponding)) >= 1
        finally:
            pkg.delete_from_project()

    def test_remove_graph_elements(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("RemoveGraphPkg"))
        try:
            diagram = self._diagram(pkg)
            node = diagram.add_new_node_by_type("Note", 20, 20, 80, 50)
            assert isinstance(node, IRPGraphNode)
            assert diagram.graphical_elements.count == 1
            diagram.remove_graph_elements(diagram.graphical_elements)
            assert diagram.graphical_elements.count == 0
            assert len(list(diagram.get_elements_in_diagram())) == 0  # model elements are untouched by graph removal
        finally:
            pkg.delete_from_project()

    def test_open_close_and_is_open(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("OpenClosePkg"))
        try:
            diagram = self._diagram(pkg)
            assert diagram.is_open() == 0
            diagram.open_diagram()
            assert diagram.is_open() == 1
            diagram.close_diagram()
        finally:
            pkg.delete_from_project()

    def test_show_diagram_frame_roundtrip(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("FramePkg"))
        try:
            diagram = self._diagram(pkg)
            original = diagram.is_show_diagram_frame()
            assert original in (0, 1)
            diagram.set_show_diagram_frame(1 - original)
            assert diagram.is_show_diagram_frame() == 1 - original
            diagram.set_show_diagram_frame(original)
            assert diagram.is_show_diagram_frame() == original
        finally:
            pkg.delete_from_project()

    def test_complete_relations(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = test_project.add_package(self._unique("CompleteRelPkg"))
        try:
            diagram = self._diagram(pkg)
            source = pkg.add_class(self._unique("RelationSource"))
            target = pkg.add_class(self._unique("RelationTarget"))
            source.add_relation_to(target, "targets", "Association", "1", "sources", "Association", "1", "")
            source_node = diagram.add_new_node_for_element(source, 20, 20, 80, 50)
            target_node = diagram.add_new_node_for_element(target, 200, 20, 80, 50)
            graph_elements = rhapsody_app.create_new_collection()
            graph_elements.add_graphical_item(source_node)
            graph_elements.add_graphical_item(target_node)

            diagram.complete_relations(graph_elements, 0)

            assert diagram.graphical_elements.count >= 3
        finally:
            pkg.delete_from_project()

    def test_populate_diagram(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = test_project.add_package(self._unique("PopulatePkg"))
        try:
            diagram = self._diagram(pkg)
            created_class = pkg.add_class(self._unique("PopulateCls"))
            elements_to_populate = rhapsody_app.create_new_collection()
            elements_to_populate.add_item(created_class)
            relations_types = rhapsody_app.create_new_collection()
            relations_types.set_size(1)
            relations_types.set_string(1, "AllRelations")

            diagram.populate_diagram(elements_to_populate, relations_types, "among")

            assert created_class in list(diagram.get_elements_in_diagram())
        finally:
            pkg.delete_from_project()

    def test_get_last_visualization_modified_time(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("VisTimePkg"))
        try:
            diagram = self._diagram(pkg)
            modified = diagram.get_last_visualization_modified_time()
            assert isinstance(modified, str)
        finally:
            pkg.delete_from_project()

    def test_get_pictures_with_image_map_creates_file(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication, tmp_path: Path) -> None:
        pkg = test_project.add_package(self._unique("PicturesMapPkg"))
        try:
            diagram = self._diagram(pkg)
            output_file = tmp_path / "diagram-map.emf"
            image_map = rhapsody_app.create_new_collection()

            filenames = diagram.get_pictures_with_image_map(str(output_file), image_map)

            assert filenames.count > 0
            assert output_file.exists()
        finally:
            pkg.delete_from_project()

    def test_get_picture_as_divided_metafiles_creates_file(self, test_project: IRPProject, tmp_path: Path) -> None:
        pkg = test_project.add_package(self._unique("DividedPkg"))
        try:
            diagram = self._diagram(pkg)
            output_file = tmp_path / "diagram-divided.emf"

            filenames = diagram.get_picture_as_divided_metafiles(str(output_file))

            assert filenames.count > 0
            assert output_file.exists()
        finally:
            pkg.delete_from_project()

    def test_diagram_view_and_custom_view_members_are_documented_unavailable(self, test_project: IRPProject) -> None:
        """The registered pywin32 interface exposes no diagram-view/custom-view
        members for IRPDiagram (absent from docs/reports/pywin32_authority.json),
        so the stubs raise before dispatch."""
        pkg = test_project.add_package(self._unique("UnavailablePkg"))
        try:
            diagram = self._diagram(pkg)
            views = IRPCollection(pkg.get_all_nested_elements()._com)
            with pytest.raises(NotImplementedError, match="createDiagramView is not exposed"):
                diagram.create_diagram_view("View1")
            with pytest.raises(NotImplementedError, match="getDiagramViewOf is not exposed"):
                diagram.get_diagram_view_of("View1")
            with pytest.raises(NotImplementedError, match="getDiagramViews is not exposed"):
                diagram.get_diagram_views()
            with pytest.raises(NotImplementedError, match="isDiagramView is not exposed"):
                diagram.is_diagram_view()
            with pytest.raises(NotImplementedError, match="getCustomViews is not exposed"):
                diagram.get_custom_views()
            with pytest.raises(NotImplementedError, match="setCustomViews is not exposed"):
                diagram.set_custom_views(views)
            with pytest.raises(NotImplementedError, match="rearrangePorts is not exposed"):
                diagram.rearrange_ports()
            with pytest.raises(NotImplementedError, match="updateViewOnServer is not exposed"):
                diagram.update_view_on_server()
        finally:
            pkg.delete_from_project()
