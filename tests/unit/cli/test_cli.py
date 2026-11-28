"""Tests for the registry-driven root CLI dispatcher (rhapsody_cli.cli.cli)."""

import argparse
from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.cli.cli import build_registry, build_root_parser, main
from rhapsody_cli.exceptions import CliExecutionError


def test_registry_covers_all_commands() -> None:
    commands = build_registry()
    assert set(commands) == {
        "connect",
        "disconnect",
        "status",
        "version",
        "export",
        "import",
        "class",
        "attribute",
        "operation",
        "package",
        "port",
        "project",
    }


def test_root_parser_registers_every_command() -> None:
    parser = build_root_parser(build_registry())
    subparsers = next(a for a in parser._actions if isinstance(a, argparse._SubParsersAction))
    assert set(subparsers.choices) == set(build_registry())


def test_global_format_default_is_table() -> None:
    parser = build_root_parser(build_registry())
    namespace = parser.parse_args(["package", "list", "--path", "X"])
    assert namespace.format == "table"
    assert namespace.subcommand == "list"


def test_unknown_command_exits_2(capsys: pytest.CaptureFixture) -> None:
    with patch("sys.argv", ["rhapsody-cli", "bogus"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 2
    assert "invalid choice" in capsys.readouterr().err


def test_missing_command_exits_2(capsys: pytest.CaptureFixture) -> None:
    with patch("sys.argv", ["rhapsody-cli"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 2
    assert "the following arguments are required: <command>" in capsys.readouterr().err


def test_main_runs_selected_entry() -> None:
    entry = MagicMock()
    namespace = MagicMock(subcommand="list", verbose=False, entry=entry)
    with patch("sys.argv", ["rhapsody-cli", "package", "list"]):
        with patch("rhapsody_cli.cli.cli.build_registry") as mock_registry:
            with patch("rhapsody_cli.cli.cli.build_root_parser") as mock_build:
                mock_parser = MagicMock()
                mock_parser.parse_args.return_value = namespace
                mock_build.return_value = mock_parser
                mock_registry.return_value = {"package": entry}
                with patch("rhapsody_cli.cli.cli.CliLoggingConfigurator") as mock_log:
                    main()
    entry.run.assert_called_once_with(namespace)
    mock_log.return_value.configure.assert_called_once()


def test_main_cli_execution_error_uses_exit_code() -> None:
    entry = MagicMock()
    entry.run.side_effect = CliExecutionError("boom", exit_code=3)
    with patch("sys.argv", ["rhapsody-cli", "package", "list"]):
        with patch("rhapsody_cli.cli.cli.build_registry", return_value={"package": entry}):
            with patch("rhapsody_cli.cli.cli.build_root_parser") as mock_build:
                mock_parser = MagicMock()
                mock_parser.parse_args.return_value = MagicMock(verbose=False, entry=entry)
                mock_build.return_value = mock_parser
                with pytest.raises(SystemExit) as exc_info:
                    main()
    assert exc_info.value.code == 3


def test_main_keyboard_interrupt_exits_130() -> None:
    entry = MagicMock()
    entry.run.side_effect = KeyboardInterrupt
    with patch("sys.argv", ["rhapsody-cli", "package", "list"]):
        with patch("rhapsody_cli.cli.cli.build_registry", return_value={"package": entry}):
            with patch("rhapsody_cli.cli.cli.build_root_parser") as mock_build:
                mock_parser = MagicMock()
                mock_parser.parse_args.return_value = MagicMock(verbose=False, entry=entry)
                mock_build.return_value = mock_parser
                with pytest.raises(SystemExit) as exc_info:
                    main()
    assert exc_info.value.code == 130


def test_main_generic_exception_exits_1() -> None:
    entry = MagicMock()
    entry.run.side_effect = RuntimeError("kaboom")
    with patch("sys.argv", ["rhapsody-cli", "package", "list"]):
        with patch("rhapsody_cli.cli.cli.build_registry", return_value={"package": entry}):
            with patch("rhapsody_cli.cli.cli.build_root_parser") as mock_build:
                mock_parser = MagicMock()
                mock_parser.parse_args.return_value = MagicMock(verbose=False, entry=entry)
                mock_build.return_value = mock_parser
                with pytest.raises(SystemExit) as exc_info:
                    main()
    assert exc_info.value.code == 1


def test_global_format_before_group_is_accepted() -> None:
    """--format as a root flag works in the leading position (consolidated)."""
    parser = build_root_parser(build_registry())
    namespace = parser.parse_args(["--format", "json", "package", "list", "--path", "X"])
    assert namespace.format == "json"


def test_format_after_group_is_rejected() -> None:
    """--format inside/after the group is rejected once consolidation completes."""
    parser = build_root_parser(build_registry())
    with pytest.raises(SystemExit) as exc_info:
        parser.parse_args(["package", "list", "--path", "X", "--format", "json"])
    assert exc_info.value.code == 2


def test_global_verbose_flag_propagates() -> None:
    """-v before the group lands on the namespace (strictly global)."""
    parser = build_root_parser(build_registry())
    namespace = parser.parse_args(["-v", "project", "list"])
    assert namespace.verbose is True
