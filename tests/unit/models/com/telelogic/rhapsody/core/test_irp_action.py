"""Tests for the IRPAction wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_action import IRPAction
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_is_registered_for_meta_class_action() -> None:
    fake = make_fake_element("Action", properties={"name": "Act1", "body": "doSomething()"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPAction)
    assert wrapped.name == "Act1"


def test_body_returns_string() -> None:
    fake = make_fake_element("Action", properties={"body": "doSomething()"})
    assert IRPAction(fake).body == "doSomething()"


def test_body_setter() -> None:
    fake = make_fake_element("Action")
    IRPAction(fake).body = "doOther()"
    assert fake.body == "doOther()"
