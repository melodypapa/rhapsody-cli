"""Tests for ClassCommand dispatcher (register/run contract)."""

import argparse

import pytest

from rhapsody_cli.commands.class_command import ClassCommand


class TestClassCommand:
    """Test ClassCommand dispatcher."""

    def test_command_name_is_class(self) -> None:
        """Test that command name is 'class'."""
        cmd = ClassCommand()
        assert cmd._command_name() == "class"

    def test_missing_subcommand_is_rejected(self) -> None:
        """Group-level subparsers are required: bare group parse exits 2."""
        root = argparse.ArgumentParser()
        subparsers = root.add_subparsers(required=True)
        cmd = ClassCommand()
        cmd.register(subparsers)
        with pytest.raises(SystemExit) as exc_info:
            root.parse_args(["class"])
        assert exc_info.value.code == 2

    def test_registers_all_6_subcommands(self) -> None:
        """All 6 subcommands are registered."""
        cmd = ClassCommand()
        actions = cmd.get_actions()
        command_ids = [a.command_id for a in actions]

        for expected in ["create", "delete", "list", "view", "link", "update"]:
            assert expected in command_ids
        assert len(actions) == 6
