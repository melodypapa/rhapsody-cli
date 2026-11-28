"""Tests for the IRPSysMLPort wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPLink
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_relation import IRPRelation
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_sysml_port import IRPSysMLPort
from tests.unit.models.fakes import make_fake_element


def test_is_registered_for_meta_class_sys_ml_port() -> None:
    fake = make_fake_element("SysMLPort", properties={"name": "P1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPSysMLPort)
    assert wrapped.name == "P1"


def test_is_reversed_returns_int() -> None:
    fake = make_fake_element("SysMLPort", properties={"isReversed": 1})
    assert IRPSysMLPort(fake).is_reversed == 1


def test_is_reversed_setter() -> None:
    fake = make_fake_element("SysMLPort")
    IRPSysMLPort(fake).is_reversed = 1
    assert fake.isReversed == 1


def test_port_direction_returns_string() -> None:
    fake = make_fake_element("SysMLPort", properties={"portDirection": "InOut"})
    assert IRPSysMLPort(fake).port_direction == "InOut"


def test_port_direction_setter() -> None:
    fake = make_fake_element("SysMLPort")
    IRPSysMLPort(fake).port_direction = "Out"
    assert fake.portDirection == "Out"


def test_type_wraps_result() -> None:
    type_ = make_fake_element("Class", properties={"name": "T1"})
    fake = make_fake_element("SysMLPort", properties={"type": type_})
    result = IRPSysMLPort(fake).type
    assert result is not None
    assert result.name == "T1"


def test_type_setter() -> None:
    fake = make_fake_element("SysMLPort")
    type_ = make_fake_element("Class", properties={"name": "T1"})
    IRPSysMLPort(fake).type = cast(IRPClassifier, IRPModelElement.wrap(type_))
    assert fake.type is type_


def test_add_link_delegates_and_wraps() -> None:
    fake = make_fake_element("SysMLPort")
    from_part = make_fake_element("Instance", properties={"name": "From"})
    to_part = make_fake_element("Instance", properties={"name": "To"})
    assoc = make_fake_element("Relation", properties={"name": "R"})
    to_port = make_fake_element("SysMLPort", properties={"name": "ToPort"})
    new_owner = make_fake_element("Package", properties={"name": "Pkg"})
    link = make_fake_element("Link", properties={"name": "L1"})
    fake.addLink.return_value = link
    wrapped = IRPSysMLPort(fake).add_link(
        IRPInstance(from_part),
        IRPInstance(to_part),
        IRPRelation(assoc),
        IRPSysMLPort(to_port),
        IRPPackage(new_owner),
    )
    assert isinstance(wrapped, IRPLink)
    assert wrapped.name == "L1"
    fake.addLink.assert_called_once_with(from_part, to_part, assoc, to_port, new_owner)


def test_add_link_passes_null_association_for_flowports() -> None:
    fake = make_fake_element("SysMLPort")
    from_part = make_fake_element("Object", properties={"name": "From"})
    to_part = make_fake_element("Object", properties={"name": "To"})
    to_port = make_fake_element("SysMLPort", properties={"name": "ToPort"})
    new_owner = make_fake_element("Package", properties={"name": "Pkg"})
    link = make_fake_element("Link", properties={"name": "L2"})
    fake.addLink.return_value = link

    wrapped = IRPSysMLPort(fake).add_link(IRPInstance(from_part), IRPInstance(to_part), None, IRPSysMLPort(to_port), IRPPackage(new_owner))

    assert isinstance(wrapped, IRPLink)
    assert wrapped.name == "L2"
    fake.addLink.assert_called_once_with(from_part, to_part, None, to_port, new_owner)
