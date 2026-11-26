"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPDependency."""

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPDependency
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_dependency_is_a_model_element() -> None:
    fake = make_fake_element("Dependency")
    dep = IRPDependency(fake)

    assert isinstance(dep, IRPModelElement)


def test_dependency_is_registered_for_meta_class_dependency() -> None:
    fake = make_fake_element("Dependency")

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPDependency)


def test_dependent_property_wraps_the_dependent_element() -> None:
    dependent_fake = make_fake_element("Class", properties={"name": "Client"})
    fake = make_fake_element("Dependency", properties={"dependent": dependent_fake})
    dep = IRPDependency(fake)

    assert dep.dependent is not None
    assert dep.dependent.name == "Client"


def test_dependent_property_is_none_when_not_set() -> None:
    fake = make_fake_element("Dependency", properties={"dependent": None})
    dep = IRPDependency(fake)

    assert dep.dependent is None


def test_dependent_property_writes_the_com_object() -> None:
    dependent_fake = make_fake_element("Class", properties={"name": "Client"})
    fake = make_fake_element("Dependency", properties={"dependent": None})
    dep = IRPDependency(fake)

    dep.dependent = IRPModelElement(dependent_fake)

    assert fake.dependent is dependent_fake
    fake.setDependent.assert_not_called()


def test_depends_on_property_wraps_the_supplier_element() -> None:
    supplier_fake = make_fake_element("Class", properties={"name": "Service"})
    fake = make_fake_element("Dependency", properties={"dependsOn": supplier_fake})
    dep = IRPDependency(fake)

    assert dep.depends_on is not None
    assert dep.depends_on.name == "Service"


def test_depends_on_property_is_none_when_not_set() -> None:
    fake = make_fake_element("Dependency", properties={"dependsOn": None})
    dep = IRPDependency(fake)

    assert dep.depends_on is None


def test_depends_on_property_writes_the_com_object() -> None:
    supplier_fake = make_fake_element("Class", properties={"name": "Service"})
    fake = make_fake_element("Dependency", properties={"dependsOn": None})
    dep = IRPDependency(fake)

    dep.depends_on = IRPModelElement(supplier_fake)

    assert fake.dependsOn is supplier_fake
    fake.setDependsOn.assert_not_called()


def test_is_need_to_migrate_is_documented_unavailable() -> None:
    fake = make_fake_element("Dependency")
    dep = IRPDependency(fake)

    with pytest.raises(NotImplementedError):
        dep.is_need_to_migrate()

    fake.isNeedToMigrate.assert_not_called()


def test_set_link_type_is_documented_unavailable() -> None:
    fake = make_fake_element("Dependency")
    dep = IRPDependency(fake)

    with pytest.raises(NotImplementedError):
        dep.set_link_type("Usage")

    fake.setLinkType.assert_not_called()


def test_set_owner_without_changing_dependent_delegates_to_com() -> None:
    owner_fake = make_fake_element("Class", properties={"name": "Owner"})
    fake = make_fake_element("Dependency")
    dep = IRPDependency(fake)

    dep.set_owner_without_changing_dependent(IRPModelElement(owner_fake))

    fake.setOwnerWithoutChangingDependent.assert_called_once_with(owner_fake)


def test_legacy_accessor_methods_are_removed() -> None:
    dep = IRPDependency(make_fake_element("Dependency"))

    for legacy in ("get_dependent", "set_dependent", "get_depends_on", "set_depends_on"):
        assert not hasattr(dep, legacy), legacy
