"""Tests for PackageCommand dispatcher (register/run contract)."""

import argparse

import pytest

from rhapsody_cli.commands.package_command import PackageCommand


class TestPackageCommand:
    """Test PackageCommand dispatcher."""

    def test_command_name_is_package(self) -> None:
        """Test that command name is 'package'."""
        cmd = PackageCommand()
        assert cmd._command_name() == "package"

    def test_missing_subcommand_is_rejected(self) -> None:
        """Group-level subparsers are required: bare group parse exits 2."""
        root = argparse.ArgumentParser()
        subparsers = root.add_subparsers(required=True)
        cmd = PackageCommand()
        cmd.register(subparsers)
        with pytest.raises(SystemExit) as exc_info:
            root.parse_args(["package"])
        assert exc_info.value.code == 2

    def test_registers_all_7_subcommands(self) -> None:
        """All 7 subcommands are registered."""
        cmd = PackageCommand()
        actions = cmd.get_actions()
        command_ids = [a.command_id for a in actions]

        for expected in ["create", "delete", "view", "list", "update", "export", "import"]:
            assert expected in command_ids
        assert len(actions) == 7
