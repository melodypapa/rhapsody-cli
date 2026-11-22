"""Tests for rhapsody_cli.models.elements.containment.RPProfile."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.containment import RPProfile
from tests.unit.models.fakes import make_fake_element


def test_profile_is_a_package() -> None:
    fake = make_fake_element("Profile", properties={"name": "SysML"})
    profile = RPProfile(fake)

    assert isinstance(profile, IRPPackage)
    assert profile.get_name() == "SysML"


def test_profile_is_registered_for_meta_class_profile() -> None:
    fake = make_fake_element("Profile", properties={"name": "SysML"})

    wrapped = AbstractRPModelElement.wrap(fake)

    assert isinstance(wrapped, RPProfile)
