"""Tests for the IRPFlow wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flow import IRPFlow
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_other_model import IRPSysMLPort
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port import IRPPort
from tests.unit.models.fakes import make_fake_collection, make_fake_element

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance


def test_is_registered_for_meta_class_flow() -> None:
    fake = make_fake_element("Flow", properties={"name": "MyFlow"})
    flow = IRPModelElement.wrap(fake)
    assert isinstance(flow, IRPFlow)
    assert flow.name == "MyFlow"


def test_add_conveyed_delegates() -> None:
    fake = make_fake_element("Flow")
    element = make_fake_element("Class", properties={"name": "ConveyedClass"})
    IRPFlow(fake).add_conveyed(cast(IRPModelElement, IRPModelElement.wrap(element)))
    fake.addConveyed.assert_called_once_with(element)


def test_conveyed_returns_collection() -> None:
    item1 = make_fake_element("Class", properties={"name": "Item1"})
    item2 = make_fake_element("Class", properties={"name": "Item2"})
    fake = make_fake_element("Flow", properties={"conveyed": make_fake_collection([item1, item2])})
    result = IRPFlow(fake).conveyed
    assert isinstance(result, IRPCollection)
    assert len(result) == 2


def test_direction_returns_string() -> None:
    fake = make_fake_element("Flow", properties={"direction": "toEnd2"})
    assert IRPFlow(fake).direction == "toEnd2"


def test_direction_setter() -> None:
    fake = make_fake_element("Flow")
    IRPFlow(fake).direction = "bidirectional"
    assert fake.direction == "bidirectional"


def test_end1_wraps_result() -> None:
    end1 = make_fake_element("State", properties={"name": "End1State"})
    fake = make_fake_element("Flow", properties={"end1": end1})
    result = IRPFlow(fake).end1
    assert result is not None
    assert result.name == "End1State"


def test_end1_setter() -> None:
    fake = make_fake_element("Flow")
    end1 = make_fake_element("State", properties={"name": "End1State"})
    IRPFlow(fake).end1 = cast(IRPModelElement, IRPModelElement.wrap(end1))
    assert fake.end1 is end1


def test_end1_port_wraps_result() -> None:
    port = make_fake_element("Port", properties={"name": "Port1"})
    fake = make_fake_element("Flow", properties={"end1Port": port})
    result = IRPFlow(fake).end1_port
    assert isinstance(result, IRPPort)
    assert result.name == "Port1"


def test_end1_sys_ml_port_wraps_result() -> None:
    sysml_port = make_fake_element("SysMLPort", properties={"name": "SysMLPort1"})
    fake = make_fake_element("Flow", properties={"end1SysMLPort": sysml_port})
    result = IRPFlow(fake).end1_sys_ml_port
    assert isinstance(result, IRPSysMLPort)
    assert result.name == "SysMLPort1"


def test_end2_wraps_result() -> None:
    end2 = make_fake_element("State", properties={"name": "End2State"})
    fake = make_fake_element("Flow", properties={"end2": end2})
    result = IRPFlow(fake).end2
    assert result is not None
    assert result.name == "End2State"


def test_end2_setter() -> None:
    fake = make_fake_element("Flow")
    end2 = make_fake_element("State", properties={"name": "End2State"})
    IRPFlow(fake).end2 = cast(IRPModelElement, IRPModelElement.wrap(end2))
    assert fake.end2 is end2


def test_end2_port_wraps_result() -> None:
    port = make_fake_element("Port", properties={"name": "Port2"})
    fake = make_fake_element("Flow", properties={"end2Port": port})
    result = IRPFlow(fake).end2_port
    assert isinstance(result, IRPPort)
    assert result.name == "Port2"


def test_end2_sys_ml_port_wraps_result() -> None:
    sysml_port = make_fake_element("SysMLPort", properties={"name": "SysMLPort2"})
    fake = make_fake_element("Flow", properties={"end2SysMLPort": sysml_port})
    result = IRPFlow(fake).end2_sys_ml_port
    assert isinstance(result, IRPSysMLPort)
    assert result.name == "SysMLPort2"


def test_remove_conveyed_delegates() -> None:
    fake = make_fake_element("Flow")
    element = make_fake_element("Class", properties={"name": "ConveyedClass"})
    IRPFlow(fake).remove_conveyed(cast(IRPModelElement, IRPModelElement.wrap(element)))
    fake.removeConveyed.assert_called_once_with(element)


def test_set_end1_via_port_delegates() -> None:
    fake = make_fake_element("Flow")
    instance = make_fake_element("Instance", properties={"name": "MyInstance"})
    port = make_fake_element("Port", properties={"name": "MyPort"})
    IRPFlow(fake).set_end1_via_port(
        cast("IRPInstance", IRPModelElement.wrap(instance)),
        cast(IRPPort, IRPModelElement.wrap(port)),
    )
    fake.setEnd1ViaPort.assert_called_once_with(instance, port)


def test_set_end1_via_sys_ml_port_delegates() -> None:
    fake = make_fake_element("Flow")
    instance = make_fake_element("Instance", properties={"name": "MyInstance"})
    sysml_port = make_fake_element("SysMLPort", properties={"name": "MySysMLPort"})
    IRPFlow(fake).set_end1_via_sys_ml_port(
        cast("IRPInstance", IRPModelElement.wrap(instance)),
        cast(IRPSysMLPort, IRPModelElement.wrap(sysml_port)),
    )
    fake.setEnd1ViaSysMLPort.assert_called_once_with(instance, sysml_port)


def test_set_end2_via_port_delegates() -> None:
    fake = make_fake_element("Flow")
    instance = make_fake_element("Instance", properties={"name": "MyInstance"})
    port = make_fake_element("Port", properties={"name": "MyPort"})
    IRPFlow(fake).set_end2_via_port(
        cast("IRPInstance", IRPModelElement.wrap(instance)),
        cast(IRPPort, IRPModelElement.wrap(port)),
    )
    fake.setEnd2ViaPort.assert_called_once_with(instance, port)


def test_set_end2_via_sys_ml_port_delegates() -> None:
    fake = make_fake_element("Flow")
    instance = make_fake_element("Instance", properties={"name": "MyInstance"})
    sysml_port = make_fake_element("SysMLPort", properties={"name": "MySysMLPort"})
    IRPFlow(fake).set_end2_via_sys_ml_port(
        cast("IRPInstance", IRPModelElement.wrap(instance)),
        cast(IRPSysMLPort, IRPModelElement.wrap(sysml_port)),
    )
    fake.setEnd2ViaSysMLPort.assert_called_once_with(instance, sysml_port)
