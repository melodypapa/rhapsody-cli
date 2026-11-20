"""Tests for the top-level CLI dispatcher (rhapsody_cli.cli.cli)."""

from typing import List
from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.cli.cli import main


def _run_main(argv: List[str]) -> MagicMock:
    """Run main() with the given argv (excluding the program name), returning the mocked Command class."""
    with patch("sys.argv", ["rhapsody-cli"] + argv):
        with patch("rhapsody_cli.cli.cli.PackageCommand") as mock_command_cls:
            mock_instance = MagicMock()
            mock_command_cls.return_value = mock_instance
            main()
    return mock_instance


def test_format_flag_is_parsed_and_passed_to_execute() -> None:
    """--format json should result in cmd.execute(output_format='json')."""
    mock_instance = _run_main(["package", "query", "--format", "json"])

    mock_instance.execute.assert_called_once_with(output_format="json")


def test_missing_format_flag_defaults_to_table() -> None:
    """Without --format, cmd.execute(output_format='table') should be used."""
    mock_instance = _run_main(["package", "query"])

    mock_instance.execute.assert_called_once_with(output_format="table")


class TestSuspendedCommands:
    """Tests for the suspended-command mechanism (attribute/operation/port)."""

    @pytest.mark.parametrize("command", ["attribute", "operation", "port"])
    def test_suspended_command_prints_notice_and_exits_2(self, command: str, capsys: pytest.CaptureFixture[str]) -> None:
        """A suspended command prints a notice to stderr and exits with code 2."""
        with patch("sys.argv", ["rhapsody-cli", command, "list"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
        assert exc_info.value.code == 2
        captured = capsys.readouterr()
        assert f"command '{command}' is temporarily suspended" in captured.err

    def test_suspended_check_fires_before_dispatch(self) -> None:
        """The suspended check must reject the command before any command group is constructed."""
        with patch("sys.argv", ["rhapsody-cli", "attribute", "list"]):
            with patch("rhapsody_cli.cli.cli.AttributeCommand") as mock_command_cls:
                with pytest.raises(SystemExit):
                    main()
        mock_command_cls.assert_not_called()

    def test_unknown_command_still_rejected(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Unknown commands keep the existing 'Unknown command' usage-error path."""
        with patch("sys.argv", ["rhapsody-cli", "definitely_not_real"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
        assert exc_info.value.code == 2
        assert "Unknown command" in capsys.readouterr().err


class TestUsageText:
    """Tests for the top-level usage rendering."""

    def test_help_lists_active_and_suspended_sections(self, capsys: pytest.CaptureFixture[str]) -> None:
        """--help renders Single-Level, Two-Level, and Suspended sections."""
        with patch("sys.argv", ["rhapsody-cli", "--help"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
        assert exc_info.value.code == 0
        out = capsys.readouterr().out
        assert "Single-Level Commands:" in out
        assert "Two-Level Commands:" in out
        assert "Suspended Commands" in out
        for active in ("project", "package", "class"):
            assert f"  {active} " in out
        for suspended in ("attribute", "operation", "port"):
            assert f"  {suspended} " in out


class TestSingleLevelExchangeCommands:
    """Tests for the single-level export/import commands."""

    def test_export_dispatches_with_file_and_default_root_path(self) -> None:
        with patch("rhapsody_cli.cli.cli.PackageExportAction") as mock_action_cls:
            mock_instance = MagicMock()
            mock_action_cls.return_value = mock_instance
            with patch("sys.argv", ["rhapsody-cli", "export", "--file", "out.yaml"]):
                main()
        mock_instance.execute.assert_called_once()
        args = mock_instance.execute.call_args[0][0]
        assert args.file == "out.yaml"
        assert args.path is None

    def test_export_dispatches_with_explicit_path(self) -> None:
        with patch("rhapsody_cli.cli.cli.PackageExportAction") as mock_action_cls:
            mock_instance = MagicMock()
            mock_action_cls.return_value = mock_instance
            with patch("sys.argv", ["rhapsody-cli", "export", "--path", "Sensors", "--file", "sensors.yaml"]):
                main()
        args = mock_instance.execute.call_args[0][0]
        assert args.path == "Sensors"
        assert args.file == "sensors.yaml"

    def test_import_dispatches_with_file_and_explicit_path(self) -> None:
        with patch("rhapsody_cli.cli.cli.PackageImportAction") as mock_action_cls:
            mock_instance = MagicMock()
            mock_action_cls.return_value = mock_instance
            with patch("sys.argv", ["rhapsody-cli", "import", "--path", "Sensors", "--file", "in.yaml"]):
                main()
        mock_instance.execute.assert_called_once()
        args = mock_instance.execute.call_args[0][0]
        assert args.path == "Sensors"
        assert args.file == "in.yaml"

    def test_export_requires_file_argument(self, capsys: pytest.CaptureFixture[str]) -> None:
        with patch("sys.argv", ["rhapsody-cli", "export"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
        assert exc_info.value.code == 2
        assert "required" in capsys.readouterr().err.lower()
