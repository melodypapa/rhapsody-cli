"""Tests for rhapsody_cli.models.elements.variables.model_variables.IRPArgument."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_argument import IRPArgument
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.elements.variables.model_variables import RPVariable
from tests.unit.models.fakes import make_fake_element


def test_argument_is_a_variable() -> None:
    fake = make_fake_element("Argument", properties={"name": "id"})
    argument = IRPArgument(fake)

    assert isinstance(argument, RPVariable)
    assert argument.get_name() == "id"


def test_argument_get_argument_direction_delegates_to_com() -> None:
    fake = make_fake_element("Argument", properties={"argumentDirection": "in"})
    argument = IRPArgument(fake)

    assert argument.get_argument_direction() == "in"


def test_argument_set_argument_direction_delegates_to_com() -> None:
    fake = make_fake_element("Argument")
    argument = IRPArgument(fake)

    argument.set_argument_direction("out")

    assert fake.argumentDirection == "out"


def test_argument_is_registered_for_meta_class_argument() -> None:
    fake = make_fake_element("Argument", properties={"name": "id"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPArgument)
