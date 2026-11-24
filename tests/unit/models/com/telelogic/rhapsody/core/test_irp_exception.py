"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.irp_exception.IRPException."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPException
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_exception_is_model_element() -> None:
    fake = make_fake_element("Exception", properties={"name": "Exc1"})
    exc = IRPException(fake)
    assert isinstance(exc, IRPModelElement)
    assert exc.name == "Exc1"


def test_exception_is_registered() -> None:
    fake = make_fake_element("Exception", properties={"name": "Exc1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPException)
