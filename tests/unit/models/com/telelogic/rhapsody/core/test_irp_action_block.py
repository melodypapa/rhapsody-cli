"""Fake-COM unit tests for the IRPActionBlock wrapper."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_action_block import IRPActionBlock
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPMessage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_action_block_inherits_message_and_model_element_members() -> None:
    fake = make_fake_element("ActionBlock", properties={"name": "AB1"})

    action_block = IRPActionBlock(fake)

    assert isinstance(action_block, IRPMessage)
    assert isinstance(action_block, IRPModelElement)
    assert action_block.name == "AB1"


def test_action_block_is_registered_by_meta_class() -> None:
    fake = make_fake_element("ActionBlock", properties={"name": "AB1"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPActionBlock)
