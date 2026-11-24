"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPProfile."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPProfile
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from tests.unit.models.fakes import make_fake_element


def test_profile_is_a_package() -> None:
    fake = make_fake_element("Profile", properties={"name": "SysML"})
    profile = IRPProfile(fake)

    assert isinstance(profile, IRPPackage)
    assert profile.name == "SysML"


def test_profile_is_registered_for_meta_class_profile() -> None:
    fake = make_fake_element("Profile", properties={"name": "SysML"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPProfile)
