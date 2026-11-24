"""Tests for rhapsody_cli.models.elements.relations.IRPPort."""

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port import IRPPort
from rhapsody_cli.models.elements.relations import RPInstance
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_port_is_an_instance() -> None:
    fake = make_fake_element("Port", properties={"name": "clientPort"})
    port = IRPPort(fake)

    assert isinstance(port, RPInstance)
    assert port.name == "clientPort"


def test_port_is_registered_for_meta_class_port() -> None:
    fake = make_fake_element("Port")

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPPort)


def test_port_get_is_behavioral_delegates_to_com() -> None:
    fake = make_fake_element("Port", properties={"isBehavioral": 1})
    port = IRPPort(fake)

    assert port.get_is_behavioral() == 1


def test_port_set_is_behavioral_delegates_to_com() -> None:
    fake = make_fake_element("Port")
    port = IRPPort(fake)

    port.set_is_behavioral(1)

    assert fake.isBehavioral == 1


def test_port_get_is_reversed_delegates_to_com() -> None:
    fake = make_fake_element("Port", properties={"isReversed": 0})
    port = IRPPort(fake)

    assert port.get_is_reversed() == 0


def test_port_set_is_reversed_delegates_to_com() -> None:
    fake = make_fake_element("Port")
    port = IRPPort(fake)

    port.set_is_reversed(1)

    assert fake.isReversed == 1


def test_port_get_port_contract_wraps_result() -> None:
    contract_fake = make_fake_element("Class", properties={"name": "IEngine"})
    fake = make_fake_element("Port")
    fake.portContract = contract_fake
    port = IRPPort(fake)

    result = port.get_port_contract()

    assert isinstance(result, IRPClass)
    assert result.name == "IEngine"


def test_port_set_port_contract_delegates_to_com() -> None:
    contract_fake = make_fake_element("Class", properties={"name": "IEngine"})
    contract = IRPClass(contract_fake)
    fake = make_fake_element("Port")
    port = IRPPort(fake)

    port.set_port_contract(contract)

    assert fake.portContract == contract_fake


def test_port_get_provided_interfaces_returns_collection() -> None:
    fake = make_fake_element("Port")
    interface = make_fake_element("Class", properties={"name": "IProvided"})
    fake.providedInterfaces = make_fake_collection([interface])
    port = IRPPort(fake)

    result = port.get_provided_interfaces()

    assert isinstance(result, IRPCollection)
    assert len(result) == 1
    assert result[0].name == "IProvided"


def test_port_add_provided_interface_delegates_to_com() -> None:
    interface_fake = make_fake_element("Class", properties={"name": "IProvided"})
    interface = IRPClass(interface_fake)
    fake = make_fake_element("Port")
    port = IRPPort(fake)

    port.add_provided_interface(interface)

    fake.addProvidedInterface.assert_called_once_with(interface_fake)


def test_port_remove_provided_interface_delegates_to_com() -> None:
    interface_fake = make_fake_element("Class", properties={"name": "IProvided"})
    interface = IRPClass(interface_fake)
    fake = make_fake_element("Port")
    port = IRPPort(fake)

    port.remove_provided_interface(interface)

    fake.removeProvidedInterface.assert_called_once_with(interface_fake)


def test_port_get_required_interfaces_returns_collection() -> None:
    fake = make_fake_element("Port")
    interface = make_fake_element("Class", properties={"name": "IRequired"})
    fake.requiredInterfaces = make_fake_collection([interface])
    port = IRPPort(fake)

    result = port.get_required_interfaces()

    assert isinstance(result, IRPCollection)
    assert len(result) == 1
    assert result[0].name == "IRequired"


def test_port_add_required_interface_delegates_to_com() -> None:
    interface_fake = make_fake_element("Class", properties={"name": "IRequired"})
    interface = IRPClass(interface_fake)
    fake = make_fake_element("Port")
    port = IRPPort(fake)

    port.add_required_interface(interface)

    fake.addRequiredInterface.assert_called_once_with(interface_fake)


def test_port_remove_required_interface_delegates_to_com() -> None:
    interface_fake = make_fake_element("Class", properties={"name": "IRequired"})
    interface = IRPClass(interface_fake)
    fake = make_fake_element("Port")
    port = IRPPort(fake)

    port.remove_required_interface(interface)

    fake.removeRequiredInterface.assert_called_once_with(interface_fake)


def test_port_get_contract_raises_not_implemented_without_com_dispatch() -> None:
    fake = make_fake_element("Port")
    port = IRPPort(fake)

    with pytest.raises(NotImplementedError):
        port.get_contract()

    fake.getContract.assert_not_called()


def test_port_set_contract_raises_not_implemented_without_com_dispatch() -> None:
    contract = IRPClass(make_fake_element("Class", properties={"name": "IEngine"}))
    fake = make_fake_element("Port")
    port = IRPPort(fake)

    with pytest.raises(NotImplementedError):
        port.set_contract(contract)

    fake.setContract.assert_not_called()


def test_classifier_get_ports_returns_actual_rpport_instances() -> None:
    fake = make_fake_element("Class")
    fake.ports = make_fake_collection([make_fake_element("Port", properties={"name": "clientPort"})])
    classifier = IRPClassifier(fake)

    result = classifier.get_ports()

    assert len(result) == 1
    assert isinstance(result[0], IRPPort)
    assert result[0].name == "clientPort"
