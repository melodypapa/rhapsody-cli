"""Tests for AttributeCommand dispatcher (register/run contract)."""

import argparse

import pytest

from rhapsody_cli.commands.attribute_command import AttributeCommand


class TestAttributeCommand:
    """Test AttributeCommand dispatcher."""

    def test_command_name_is_attribute(self) -> None:
        """Test that command name is 'attribute'."""
        cmd = AttributeCommand()
        assert cmd._command_name() == "attribute"

    def test_missing_subcommand_is_rejected(self) -> None:
        """Group-level subparsers are required: bare group parse exits 2."""
        root = argparse.ArgumentParser()
        subparsers = root.add_subparsers(required=True)
        cmd = AttributeCommand()
        cmd.register(subparsers)
        with pytest.raises(SystemExit) as exc_info:
            root.parse_args(["attribute"])
        assert exc_info.value.code == 2

    def test_registers_all_5_subcommands(self) -> None:
        """All 5 subcommands are registered."""
        cmd = AttributeCommand()
        actions = cmd.get_actions()
        command_ids = [a.command_id for a in actions]

        for expected in ["create", "delete", "list", "view", "update"]:
            assert expected in command_ids
        assert len(actions) == 5
