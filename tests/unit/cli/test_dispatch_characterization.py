"""Characterization tests for the CLI surface after the registry refactor.

Stage-1 characterization pinned the pre-registry behavior; the flag/usage/
routing contract tests now live in test_cli.py (they were the documented
INTENDED-CHANGE flips). This file keeps the action-level behavior pins that
must survive every later refactor: the session gate, output formats, and one
end-to-end proof that a session-gated command reaches its action through the
registry and exits with the CLI error funnel.
"""

import json as _json
from typing import Dict, List, Tuple
from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.cli.cli import CliEntry, build_registry, build_root_parser, main
from rhapsody_cli.exceptions import CliExecutionError

PARSE_ROUTE_CASES: List[Tuple[List[str], str]] = [
    (["connect"], "connect"),
    (["disconnect"], "disconnect"),
    (["status"], "status"),
    (["version"], "version"),
    (["class", "list", "--path", "X"], "class"),
    (["attribute", "list", "--path", "X"], "attribute"),
    (["package", "list", "--path", "X"], "package"),
    (["operation", "list", "--path", "X"], "operation"),
    (["port", "list", "--path", "X"], "port"),
    (["project", "list"], "project"),
]


@pytest.mark.parametrize("argv,command", PARSE_ROUTE_CASES)
def test_command_parses_and_selects_its_registry_entry(argv: List[str], command: str) -> None:
    commands: Dict[str, CliEntry] = build_registry()
    parser = build_root_parser(commands)
    namespace = parser.parse_args(argv)
    assert namespace.command == command
    assert namespace.entry is commands[command]


def test_session_gated_command_reaches_the_action_end_to_end() -> None:
    """`package list` flows root parser -> group -> action -> session gate -> exit 1."""
    with patch("sys.argv", ["rhapsody-cli", "package", "list", "--path", "X"]):
        with patch("rhapsody_cli.actions.abstract_action.SessionManager") as mock_sm:
            mock_sm.return_value.load.return_value = None
            with pytest.raises(SystemExit) as exc_info:
                main()
    assert exc_info.value.code == 1


def test_cli_execution_error_exits_with_its_code() -> None:
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


def test_generic_exception_exits_1() -> None:
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


# ---------------------------------------------------------------------------
# Action-level characterization (session gate + multi-format output)
# ---------------------------------------------------------------------------

from rhapsody_cli.actions.package import PackageListAction  # noqa: E402


def test_session_gate_blocks_when_not_connected() -> None:
    action = PackageListAction()
    args = MagicMock()
    with patch("rhapsody_cli.actions.abstract_action.SessionManager") as mock_sm:
        mock_sm.return_value.load.return_value = None
        with pytest.raises(CliExecutionError) as exc_info:
            action.execute(args)
    assert "Not connected. Run 'rhapsody-cli connect' first." in str(exc_info.value)


def test_package_list_format_output_json() -> None:
    action = PackageListAction()
    output = action._format_output(["Alpha", "Beta"], "json")
    assert _json.loads(output) == ["Alpha", "Beta"]


def test_package_list_format_output_csv() -> None:
    # csv.writer's default terminator is \r\n; a single-column table has no comma.
    action = PackageListAction()
    output = action._format_output(["Alpha", "Beta"], "csv")
    assert output == "Name\r\nAlpha\r\nBeta\r\n"


def test_package_list_format_output_table() -> None:
    action = PackageListAction()
    output = action._format_output(["Alpha", "Beta"], "table")
    assert "Alpha" in output and "Beta" in output
