"""Tests for rhapsody_cli.models.elements.classifiers.model_exception.RPException."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.elements.classifiers import RPException
from tests.unit.models.fakes import make_fake_element


def test_exception_is_model_element() -> None:
    fake = make_fake_element("Exception", properties={"name": "Exc1"})
    exc = RPException(fake)
    assert isinstance(exc, IRPModelElement)
    assert exc.name == "Exc1"


def test_exception_is_registered() -> None:
    fake = make_fake_element("Exception", properties={"name": "Exc1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, RPException)
