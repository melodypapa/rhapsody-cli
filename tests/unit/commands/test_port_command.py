"""Tests for PortCommand dispatcher.

UTS_PORT_00022: PortCommand registers all subcommands
"""

import pytest

from rhapsody_cli.exceptions import CliExecutionError


class TestPortCommand:
    """Test PortCommand dispatcher."""

    def test_command_id_is_port(self) -> None:
        """Test that command name is 'port'."""
        from rhapsody_cli.commands.port_command import PortCommand

        cmd = PortCommand(["create", "--path", "Sensors/Cls", '{"name":"Test"}'])
        assert cmd._subcommand == "create"

    def test_missing_subcommand_raises_error(self) -> None:
        """Test that missing subcommand raises error."""
        from rhapsody_cli.commands.port_command import PortCommand

        with pytest.raises(CliExecutionError):
            PortCommand([])

    def test_registers_all_five_subcommands(self) -> None:
        """UTS_PORT_00022: Test that all 5 subcommands are registered."""
        from rhapsody_cli.commands.port_command import PortCommand

        cmd = PortCommand(["create", "--path", "Sensors/Cls", '{"name":"Test"}'])
        actions = cmd.get_actions()
        command_ids = [a.command_id for a in actions]

        assert "create" in command_ids
        assert "delete" in command_ids
        assert "view" in command_ids
        assert "list" in command_ids
        assert "update" in command_ids
        assert len(actions) == 5
