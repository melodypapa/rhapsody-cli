"""Integration tests for IRPCollection with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPCollectionIntegration:
    """Own-method coverage for the canonical IRPCollection wrapper."""

    def test_nested_elements_are_wrapped_collections(self, test_project: IRPProject) -> None:
        created = test_project.add_package(f"NestedPkg_{uuid.uuid4().hex[:8]}")
        try:
            elements = test_project.get_nested_elements()

            assert isinstance(elements, IRPCollection)
            assert created in list(elements)
        finally:
            created.delete_from_project()

    def test_create_new_collection_is_empty(self, rhapsody_app: RhapsodyApplication) -> None:
        collection = rhapsody_app.create_new_collection()

        assert isinstance(collection, IRPCollection)
        assert collection.count == 0

    def test_collection_mutators_and_accessors(self, rhapsody_app: RhapsodyApplication, test_project: IRPProject) -> None:
        collection = rhapsody_app.create_new_collection()
        assert collection.count == 0
        collection.set_size(3)
        assert len(collection) == 3
        collection.set_string(1, "value")
        collection.set_integer(2, 7)
        collection.set_model_element(3, test_project)
        assert collection[0] == "value"
        assert collection[1] == 7
        assert collection[2] == test_project
        collection.remove(1)
        collection.add_item(test_project)
        collection.empty()
        assert collection.count == 0

    def test_add_graphical_item_adds_real_graph_element(self, rhapsody_app: RhapsodyApplication, test_project: IRPProject) -> None:
        """Live proof for the documented alias addGraphicalItem -> addGraphicalElementItem.

        The fixture creates the real IRPGraphElement through the wrapper's
        ``IRPDiagram.add_text_box`` (pywin32-exposed ``AddTextBox``).
        Passing a non-graph model element instead faults with COM Type mismatch.
        """
        pkg = test_project.add_package(f"GraphPkg_{uuid.uuid4().hex[:8]}")
        try:
            diagram = pkg.add_object_model_diagram("GraphDiagram")
            graph = diagram.add_text_box("probe", 10, 10, 120, 40)
            collection = rhapsody_app.create_new_collection()

            collection.add_graphical_item(graph)

            assert collection.count == 1
        finally:
            pkg.delete_from_project()

    def test_to_list_raises_not_implemented(self, rhapsody_app: RhapsodyApplication) -> None:
        """JavaDoc IRPCollection.toList exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        collection = rhapsody_app.create_new_collection()

        with pytest.raises(NotImplementedError):
            collection.to_list()
