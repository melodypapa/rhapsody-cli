"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.irp_other_model.IRPSysMLPort."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPSysMLPort
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


class TestRPSysMLPort:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("SysMLPort", properties={"name": "P1"})
        port = IRPSysMLPort(fake)
        assert isinstance(port, IRPModelElement)
        assert port.name == "P1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("SysMLPort", properties={"name": "P1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPSysMLPort)

    def test_get_is_reversed_returns_int(self) -> None:
        # Pattern G — boolean check returning int
        fake = make_fake_element("SysMLPort", getIsReversed=True)
        port = IRPSysMLPort(fake)
        assert port.get_is_reversed() == 1

    def test_get_port_direction_returns_string(self) -> None:
        # Pattern A
        fake = make_fake_element("SysMLPort", getPortDirection="InOut")
        port = IRPSysMLPort(fake)
        assert port.get_port_direction() == "InOut"

    def test_get_type_wraps_result(self) -> None:
        # Pattern B
        fake = make_fake_element("SysMLPort")
        t = make_fake_element("Class", properties={"name": "T1"})
        fake.getType.return_value = t
        port = IRPSysMLPort(fake)
        wrapped = port.get_type()
        assert wrapped.name == "T1"

    def test_set_is_reversed_delegates(self) -> None:
        # Pattern D — single-arg setter (int arg)
        fake = make_fake_element("SysMLPort")
        port = IRPSysMLPort(fake)
        port.set_is_reversed(1)
        fake.setIsReversed.assert_called_once_with(1)

    def test_set_port_direction_delegates(self) -> None:
        # Pattern D — single-arg setter (str arg)
        fake = make_fake_element("SysMLPort")
        port = IRPSysMLPort(fake)
        port.set_port_direction("Out")
        fake.setPortDirection.assert_called_once_with("Out")

    def test_set_type_delegates(self) -> None:
        # Pattern F — multi-arg void method (single IRPClassifier arg)
        fake = make_fake_element("SysMLPort")
        t = make_fake_element("Class", properties={"name": "T1"})
        fake.setType.return_value = None
        port = IRPSysMLPort(fake)
        port.set_type(IRPClassifier(t))
        fake.setType.assert_called_once_with(t)

    def test_add_link_delegates_and_wraps(self) -> None:
        # Pattern E — multi-arg method returning wrapped element
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPInstance, IRPRelation
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage

        fake = make_fake_element("SysMLPort")
        from_part = make_fake_element("Instance", properties={"name": "From"})
        to_part = make_fake_element("Instance", properties={"name": "To"})
        assoc = make_fake_element("Relation", properties={"name": "R"})
        to_port = make_fake_element("SysMLPort", properties={"name": "ToPort"})
        new_owner = make_fake_element("Package", properties={"name": "Pkg"})
        link = make_fake_element("Link", properties={"name": "L1"})
        fake.addLink.return_value = link
        port = IRPSysMLPort(fake)
        wrapped = port.add_link(
            IRPInstance(from_part),
            IRPInstance(to_part),
            IRPRelation(assoc),
            IRPSysMLPort(to_port),
            IRPPackage(new_owner),
        )
        assert wrapped.name == "L1"
        fake.addLink.assert_called_once_with(from_part, to_part, assoc, to_port, new_owner)
