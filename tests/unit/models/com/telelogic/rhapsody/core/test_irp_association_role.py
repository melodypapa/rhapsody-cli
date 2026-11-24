"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPAssociationRole."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPAssociationRole, IRPInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_association_role_is_an_instance() -> None:
    fake = make_fake_element("AssociationRole")
    role = IRPAssociationRole(fake)

    assert isinstance(role, IRPInstance)


def test_association_role_is_registered_for_meta_class_association_role() -> None:
    fake = make_fake_element("AssociationRole")

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPAssociationRole)
