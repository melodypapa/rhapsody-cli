"""Characterization tests for the CURRENT top-level CLI dispatch.

These pin today's behavior before the registry refactor. Tests marked with
INTENDED-CHANGE comments are expected to be updated in stage 2 (flag
consolidation + argparse-generated help), everything else must keep passing.
"""

import json as _json
from typing import Dict, List, Tuple
from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.cli.cli import main
from rhapsody_cli.exceptions import CliExecutionError

ROUTE_CASES: List[Tuple[List[str], str]] = [
    (["connect"], "ConnectAction"),
    (["disconnect"], "DisconnectAction"),
    (["status"], "StatusAction"),
    (["version"], "VersionAction"),
    (["class", "list"], "ClassCommand"),
    (["attribute", "list"], "AttributeCommand"),
    (["package", "list"], "PackageCommand"),
    (["operation", "list"], "OperationCommand"),
    (["port", "list"], "PortCommand"),
    (["project", "list"], "ProjectCommand"),
]

SINGLE_LEVEL = {"ConnectAction", "DisconnectAction", "StatusAction", "VersionAction"}


def _run_main(argv: List[str]) -> Dict[str, MagicMock]:
    """Run main() with argv patched, mock-patching every dispatch target.

    Returns the dict of mock objects keyed by target name so tests can assert
    on exactly one being used.
    """
    with patch("sys.argv", ["rhapsody-cli"] + argv):
        with patch("rhapsody_cli.cli.cli.ConnectAction") as connect, patch(
            "rhapsody_cli.cli.cli.DisconnectAction"
        ) as disconnect, patch("rhapsody_cli.cli.cli.StatusAction") as status, patch(
            "rhapsody_cli.cli.cli.VersionAction"
        ) as version, patch("rhapsody_cli.cli.cli.ClassCommand") as klass, patch(
            "rhapsody_cli.cli.cli.AttributeCommand"
        ) as attribute, patch("rhapsody_cli.cli.cli.PackageCommand") as package, patch(
            "rhapsody_cli.cli.cli.OperationCommand"
        ) as operation, patch("rhapsody_cli.cli.cli.PortCommand") as port, patch(
            "rhapsody_cli.cli.cli.ProjectCommand"
        ) as project:
            main()
    return {
        "ConnectAction": connect,
        "DisconnectAction": disconnect,
        "StatusAction": status,
        "VersionAction": version,
        "ClassCommand": klass,
        "AttributeCommand": attribute,
        "PackageCommand": package,
        "OperationCommand": operation,
        "PortCommand": port,
        "ProjectCommand": project,
    }


@pytest.mark.parametrize("argv,target", ROUTE_CASES)
def test_command_routes_to_expected_target(argv: List[str], target: str) -> None:
    mocks = _run_main(argv)
    mock = mocks[target]
    if target in SINGLE_LEVEL:
        mock.return_value.execute.assert_called_once()
    else:
        # Groups receive the output format and dispatch internally.
        mock.return_value.execute.assert_called_once_with(output_format="table")


def test_format_flag_inside_command_args_is_scanned() -> None:
    """main() scans argv[2:] for --format, so it works only AFTER the command word.

    INTENDED-CHANGE: after stage 2, --format is a root-parser flag — the
    leading position (`rhapsody-cli --format json package list`) will work and
    positions inside/after the group will be rejected.
    """
    mocks = _run_main(["package", "--format", "json", "list"])
    mocks["PackageCommand"].return_value.execute.assert_called_once_with(output_format="json")


def test_format_flag_before_group_is_unknown_command_today() -> None:
    # INTENDED-CHANGE: after stage 2 this becomes the supported position.
    with patch("sys.argv", ["rhapsody-cli", "--format", "json", "package", "list"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 2


def test_format_flag_after_group_also_works_today() -> None:
    # INTENDED-CHANGE: after stage 2 this errors with argparse exit 2.
    mocks = _run_main(["package", "list", "--format", "json"])
    mocks["PackageCommand"].return_value.execute.assert_called_once_with(output_format="json")


def test_no_arguments_prints_usage_and_exits_zero(capsys: pytest.CaptureFixture) -> None:
    # INTENDED-CHANGE: with a registry root parser (required=True) this exits 2.
    with patch("sys.argv", ["rhapsody-cli"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 0
    out = capsys.readouterr().out
    assert "Usage" in out


def test_unknown_command_prints_error_and_exits_2(capsys: pytest.CaptureFixture) -> None:
    # INTENDED-CHANGE: argparse wording ("invalid choice") replaces the raw message.
    with patch("sys.argv", ["rhapsody-cli", "bogus"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 2
    err = capsys.readouterr().err
    assert "Unknown command: bogus" in err


def test_cli_execution_error_exits_with_its_code() -> None:
    with patch("sys.argv", ["rhapsody-cli", "package", "list"]):
        with patch("rhapsody_cli.cli.cli.PackageCommand") as mock_cls:
            mock_cls.return_value.execute.side_effect = CliExecutionError("boom", exit_code=3)
            with pytest.raises(SystemExit) as exc_info:
                main()
    assert exc_info.value.code == 3


def test_generic_exception_exits_1() -> None:
    with patch("sys.argv", ["rhapsody-cli", "package", "list"]):
        with patch("rhapsody_cli.cli.cli.PackageCommand") as mock_cls:
            mock_cls.return_value.execute.side_effect = RuntimeError("kaboom")
            with pytest.raises(SystemExit) as exc_info:
                main()
    assert exc_info.value.code == 1


# ---------------------------------------------------------------------------
# Action-level characterization (session gate + multi-format output)
# ---------------------------------------------------------------------------

from rhapsody_cli.actions.package_action import PackageListAction  # noqa: E402


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
