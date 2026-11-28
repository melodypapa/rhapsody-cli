"""Tests for PortCommand dispatcher (register/run contract)."""

import argparse

import pytest

from rhapsody_cli.commands.port_command import PortCommand


class TestPortCommand:
    """Test PortCommand dispatcher."""

    def test_command_name_is_port(self) -> None:
        """Test that command name is 'port'."""
        cmd = PortCommand()
        assert cmd._command_name() == "port"

    def test_missing_subcommand_is_rejected(self) -> None:
        """Group-level subparsers are required: bare group parse exits 2."""
        root = argparse.ArgumentParser()
        subparsers = root.add_subparsers(required=True)
        cmd = PortCommand()
        cmd.register(subparsers)
        with pytest.raises(SystemExit) as exc_info:
            root.parse_args(["port"])
        assert exc_info.value.code == 2

    def test_registers_all_5_subcommands(self) -> None:
        """All 5 subcommands are registered."""
        cmd = PortCommand()
        actions = cmd.get_actions()
        command_ids = [a.command_id for a in actions]

        for expected in ["create", "delete", "list", "view", "update"]:
            assert expected in command_ids
        assert len(actions) == 5
