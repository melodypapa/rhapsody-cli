"""Tests for the IRPContextSpecification wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_context_specification import IRPContextSpecification
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_values import IRPValueSpecification
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_is_registered_for_meta_class_context_specification() -> None:
    fake = make_fake_element("ContextSpecification", properties={"name": "CS1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPContextSpecification)
    assert isinstance(wrapped, IRPValueSpecification)
    assert wrapped.name == "CS1"


def test_multiplicities_returns_collection() -> None:
    fake = make_fake_element("ContextSpecification", properties={"multiplicities": make_fake_collection(["1", "2"])})
    result = IRPContextSpecification(fake).multiplicities
    assert isinstance(result, IRPCollection)
    assert len(result) == 2


def test_multiplicities_setter() -> None:
    fake = make_fake_element("ContextSpecification")
    values = make_fake_collection(["1", "2"])
    IRPContextSpecification(fake).multiplicities = IRPCollection(values)
    assert fake.multiplicities is values


def test_value_returns_collection() -> None:
    fake = make_fake_element("ContextSpecification", properties={"value": make_fake_collection(["pkg", "cls"])})
    result = IRPContextSpecification(fake).value
    assert isinstance(result, IRPCollection)
    assert len(result) == 2


def test_value_setter() -> None:
    fake = make_fake_element("ContextSpecification")
    values = make_fake_collection(["pkg", "cls"])
    IRPContextSpecification(fake).value = IRPCollection(values)
    assert fake.value is values
