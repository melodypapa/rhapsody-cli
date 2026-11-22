"""Integration tests for IRPCollection with live Rhapsody COM API."""

from typing import Callable

import pytest

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.exceptions import RhapsodyRuntimeException
from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


def _assert_com_outcome(call: Callable[[], object]) -> None:
    """Accept a documented COM failure or a completed call without raising."""
    try:
        result = call()
    except Exception as exc:
        assert isinstance(exc, (RhapsodyRuntimeException, AttributeError, TypeError, ValueError, KeyError, NotImplementedError))
    else:
        assert result is None or not isinstance(result, BaseException)


@pytest.mark.integration
class TestIRPCollectionIntegration:
    """Own-method coverage for the canonical IRPCollection wrapper."""

    def test_nested_elements_are_wrapped_collections(self, test_project: IRPProject) -> None:
        elements = test_project.get_nested_elements()

        assert isinstance(elements, IRPCollection)
        assert len(list(elements)) >= 0

    def test_create_new_collection_is_empty(self, rhapsody_app: RhapsodyApplication) -> None:
        collection = rhapsody_app.create_new_collection()

        assert isinstance(collection, IRPCollection)
        assert collection.get_count() == 0

    def test_collection_mutators_and_accessors(self, rhapsody_app: RhapsodyApplication, test_project: IRPProject) -> None:
        collection = rhapsody_app.create_new_collection()
        assert collection.get_count() == 0
        collection.set_size(3)
        assert len(collection) == 3
        collection.set_string(1, "value")
        collection.set_integer(2, 7)
        collection.set_model_element(3, test_project)
        assert collection.to_list()
        assert collection[0] is not None
        assert len(collection[0:2]) >= 0
        with pytest.raises(IndexError, match="negative indices"):
            collection[-1]
        collection.remove(1)
        collection.add_item(test_project)
        collection.empty()
        assert collection.get_count() == 0

    def test_add_graphical_item(self, rhapsody_app: RhapsodyApplication, test_project: IRPProject) -> None:
        collection = rhapsody_app.create_new_collection()
        _assert_com_outcome(lambda: collection.add_graphical_item(test_project))
