"""Integration tests for IRPCollection with live Rhapsody COM API."""

import pytest

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPCollection
from rhapsody_cli.models.elements.containment import RPProject


@pytest.mark.integration
class TestIRPCollectionIntegration:
    """Own-method coverage for the canonical IRPCollection wrapper."""

    def test_nested_elements_are_wrapped_collections(self, test_project: RPProject) -> None:
        elements = test_project.get_nested_elements()

        assert isinstance(elements, IRPCollection)
        assert len(list(elements)) >= 0

    def test_create_new_collection_is_empty(self, rhapsody_app: RhapsodyApplication) -> None:
        collection = rhapsody_app.create_new_collection()

        assert isinstance(collection, IRPCollection)
        assert collection.get_count() == 0
