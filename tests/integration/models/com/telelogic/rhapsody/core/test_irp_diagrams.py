"""Integration tests for IRPDiagram with live Rhapsody COM API.

Scope: only methods that IRPDiagram owns. ``IRPStatechart`` does not inherit
``IRPDiagram`` (it derives from IRPClass), so the statechart graphics tests do
not cover this surface; IRPUnit/IRPModelElement parent members are setup only.

The diagram fixtures wrap the concrete object-model diagram dispatch in
``IRPDiagram`` explicitly so the base-class members are exercised directly,
mirroring the IRPRelation/IRPInstance fixture pattern.

Remaining live rows (checklist, not blockers): ``open_diagram_view`` (needs a
diagram view, but ``create_diagram_view`` is a documented stub so no view can
be created), ``get_picture``/``get_picture_as``/``get_picture_ex`` (need a
rendered-picture surface; only the file-producing picture members are
asserted here).
"""

import struct
import uuid
from pathlib import Path

import pytest

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPDiagram
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphElement
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
            text_box = diagram.add_text_box("Integration note", 20, 20, 180, 60)
            assert isinstance(text_box, IRPGraphElement)
            assert text_box in list(diagram.graphical_elements)
        finally:
            pkg.delete_from_project()

    def test_add_image(self, test_project: IRPProject, tmp_path: Path) -> None:
        pkg = test_project.add_package(self._unique("ImagePkg"))
        try:
            diagram = self._diagram(pkg)
            image = diagram.add_image(self._bmp(tmp_path, "diagram-image.bmp"), 20, 20, 40, 40)
            assert isinstance(image, IRPGraphElement)
            assert image in list(diagram.graphical_elements)
        finally:
            pkg.delete_from_project()

    def test_add_free_shape_by_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("FreeShapePkg"))
        try:
            diagram = self._diagram(pkg)
            shape = diagram.add_free_shape_by_type("Polygon", 20, 20, 80, 80)
            assert isinstance(shape, IRPGraphElement)
            assert shape in list(diagram.graphical_elements)
        finally:
            pkg.delete_from_project()

    def test_add_new_node_by_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("NodeByTypePkg"))
        try:
            diagram = self._diagram(pkg)
            node = diagram.add_new_node_by_type("Note", 20, 20, 80, 50)
            assert isinstance(node, IRPGraphElement)
            assert node in list(diagram.graphical_elements)
        finally:
            pkg.delete_from_project()

    def test_add_new_node_for_element_and_get_elements_in_diagram(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("NodeForElemPkg"))
        try:
            diagram = self._diagram(pkg)
            created_class = pkg.add_class(self._unique("GraphClass"))
            node = diagram.add_new_node_for_element(created_class, 20, 20, 80, 50)
            assert isinstance(node, IRPGraphElement)
            assert node in list(diagram.graphical_elements)
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
            diagram.add_new_node_for_element(source, 20, 20, 80, 50)
            diagram.add_new_node_for_element(target, 200, 20, 80, 50)
            edge = diagram.add_new_edge_for_element(relation)
            assert isinstance(edge, IRPGraphElement)
            assert edge in list(diagram.graphical_elements)
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
            assert node in list(diagram.graphical_elements)
            diagram.remove_graph_elements(diagram.graphical_elements)
            assert node not in list(diagram.graphical_elements)
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

    def test_complete_relations(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("CompleteRelPkg"))
        try:
            diagram = self._diagram(pkg)
            assert diagram.complete_relations() is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_populate_diagram(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("PopulatePkg"))
        try:
            diagram = self._diagram(pkg)
            pkg.add_class(self._unique("PopulateCls"))
            assert diagram.populate_diagram() is None  # type: ignore[func-returns-value]
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
