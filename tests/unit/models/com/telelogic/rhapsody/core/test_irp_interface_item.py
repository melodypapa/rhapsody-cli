"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPInterfaceItem."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_interface_item_is_a_classifier() -> None:
    fake = make_fake_element("InterfaceItem", properties={"name": "doIt"})
    item = IRPInterfaceItem(fake)

    assert isinstance(item, IRPClassifier)
    assert item.name == "doIt"


def test_interface_item_add_argument_wraps_result() -> None:
    fake = make_fake_element("InterfaceItem")
    argument = make_fake_element("Argument", properties={"name": "x"})
    fake.addArgument.return_value = argument
    item = IRPInterfaceItem(fake)

    result = item.add_argument("x")

    fake.addArgument.assert_called_once_with("x")
    assert result.name == "x"


def test_interface_item_add_argument_before_position_wraps_result() -> None:
    fake = make_fake_element("InterfaceItem")
    argument = make_fake_element("Argument", properties={"name": "y"})
    fake.addArgumentBeforePosition.return_value = argument
    item = IRPInterfaceItem(fake)

    result = item.add_argument_before_position("y", 1)

    fake.addArgumentBeforePosition.assert_called_once_with("y", 1)
    assert result.name == "y"


def test_interface_item_arguments_returns_collection() -> None:
    inner = make_fake_element("Argument", properties={"name": "x"})
    fake = make_fake_element("InterfaceItem")
    fake.arguments = make_fake_collection([inner])
    item = IRPInterfaceItem(fake)

    result = item.arguments

    assert isinstance(result, IRPCollection)
    assert len(result) == 1


def test_interface_item_signature_delegates_to_com() -> None:
    fake = make_fake_element("InterfaceItem", properties={"signature": "void doIt(int x)"})
    item = IRPInterfaceItem(fake)

    assert item.signature == "void doIt(int x)"


def test_interface_item_get_signature_no_arg_names_delegates_to_com() -> None:
    fake = make_fake_element("InterfaceItem", getSignatureNoArgNames="void doIt(int)")
    item = IRPInterfaceItem(fake)

    assert item.get_signature_no_arg_names() == "void doIt(int)"


def test_interface_item_get_signature_no_arg_types_delegates_to_com() -> None:
    fake = make_fake_element("InterfaceItem", getSignatureNoArgTypes="void doIt(x)")
    item = IRPInterfaceItem(fake)

    assert item.get_signature_no_arg_types() == "void doIt(x)"


def test_interface_item_match_on_signature_delegates_to_com() -> None:
    fake = make_fake_element("InterfaceItem", matchOnSignature=1)
    other = make_fake_element("InterfaceItem")
    item = IRPInterfaceItem(fake)

    result = item.match_on_signature(IRPInterfaceItem(other))

    fake.matchOnSignature.assert_called_once_with(other)
    assert result is True
