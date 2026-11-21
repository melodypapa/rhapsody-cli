"""Unit tests for IRPCollection in the canonical Java package."""

from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.core import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_get_count_reads_the_count_property() -> None:
    collection = IRPCollection(make_fake_collection([1, 2, 3]))

    assert collection.get_count() == 3
    assert len(collection) == 3


def test_get_item_wraps_model_elements() -> None:
    fake_element = make_fake_element("Class", properties={"name": "C1"})
    collection = IRPCollection(make_fake_collection([fake_element]))

    wrapped = collection.get_item(1)

    assert isinstance(wrapped, IRPModelElement)
    assert wrapped.get_name() == "C1"


def test_iteration_and_indexing_are_one_based() -> None:
    items = [make_fake_element("Class", properties={"name": name}) for name in ("A", "B", "C")]
    collection = IRPCollection(make_fake_collection(items))

    assert [cast(IRPModelElement, element).get_name() for element in collection] == ["A", "B", "C"]
    assert cast(IRPModelElement, collection[0]).get_name() == "A"
    assert [cast(IRPModelElement, element).get_name() for element in collection[1:]] == ["B", "C"]


def test_mutators_delegate_to_single_com_members() -> None:
    fake = make_fake_collection([])
    collection = IRPCollection(fake)
    element = IRPModelElement(make_fake_element("Class"))

    collection.add_item(element)
    collection.set_size(4)
    collection.remove(1)
    collection.set_string(2, "value")
    collection.set_integer(3, 42)
    collection.set_model_element(1, element)
    collection.empty()

    fake.addItem.assert_called_once_with(element._com)
    fake.setSize.assert_called_once_with(4)
    fake.remove.assert_called_once_with(1)
    fake.setString.assert_called_once_with(2, "value")
    fake.setInteger.assert_called_once_with(3, 42)
    fake.setModelElement.assert_called_once_with(1, element._com)
    fake.empty.assert_called_once_with()


def test_to_list_returns_materialized_elements() -> None:
    items = [make_fake_element("Class", properties={"name": "A"})]
    collection = IRPCollection(make_fake_collection(items))

    result = collection.to_list()

    assert isinstance(result, list)
    assert len(result) == 1
