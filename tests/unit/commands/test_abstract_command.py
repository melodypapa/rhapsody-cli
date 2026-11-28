"""Tests for AbstractCommand base class (register/run contract)."""

import argparse
from typing import List, Optional

import pytest

from rhapsody_cli.actions.abstract_action import AbstractAction
from rhapsody_cli.commands.abstract_command import AbstractCommand
from rhapsody_cli.exceptions import CliExecutionError


class FakeAction(AbstractAction):
    """Fake action for testing dispatch."""

    def __init__(self) -> None:
        super().__init__(command_id="run")
        self.executed_with: Optional[argparse.Namespace] = None

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'run' subcommand and its arguments."""
        run_parser = sub_parser.add_parser("run", help="Run the fake action")
        run_parser.add_argument("--name", default="test")

    def execute(self, args: argparse.Namespace) -> None:
        """Record the parsed args it was called with."""
        self.executed_with = args


class ConcreteCommand(AbstractCommand):
    """Concrete implementation of AbstractCommand for testing."""

    def __init__(self, action: AbstractAction) -> None:
        super().__init__()
        self._action = action

    def get_actions(self) -> List[AbstractAction]:
        """Return the single fake action."""
        return [self._action]


def _registered_group(action: AbstractAction) -> argparse.ArgumentParser:
    """Build a root parser with a ConcreteCommand registered under 'concrete'."""
    root = argparse.ArgumentParser(prog="rhapsody-cli")
    subparsers = root.add_subparsers(dest="command", required=True)
    ConcreteCommand(action).register(subparsers)
    return root


class TestAbstractCommand:
    """Test AbstractCommand base class."""

    def test_get_actions_not_implemented(self) -> None:
        """Test that get_actions() raises NotImplementedError on base class."""
        cmd = AbstractCommand()
        with pytest.raises(NotImplementedError):
            cmd.get_actions()

    def test_missing_subcommand_rejected_by_argparse(self) -> None:
        """Group sub-subparsers are required: bare group parse exits 2."""
        root = _registered_group(FakeAction())
        with pytest.raises(SystemExit) as exc_info:
            root.parse_args(["concrete"])
        assert exc_info.value.code == 2

    def test_run_dispatches_to_action(self) -> None:
        """Test that run() dispatches to the matching action with the namespace."""
        action = FakeAction()
        group = ConcreteCommand(action)
        root = argparse.ArgumentParser(prog="rhapsody-cli")
        subparsers = root.add_subparsers(dest="command", required=True)
        group.register(subparsers)
        namespace = root.parse_args(["concrete", "run", "--name", "hello"])
        group.run(namespace)
        assert action.executed_with is not None
        assert action.executed_with.name == "hello"

    def test_run_unknown_subcommand_raises_cli_error(self) -> None:
        """run() with a namespace subcommand no action owns raises CliExecutionError."""
        group = ConcreteCommand(FakeAction())
        with pytest.raises(CliExecutionError) as exc_info:
            group.run(argparse.Namespace(subcommand="bogus"))
        assert "Unknown subcommand 'bogus'" in str(exc_info.value)

    def test_command_name(self) -> None:
        """Test command name derivation from class name."""
        cmd = ConcreteCommand(FakeAction())
        assert cmd._command_name() == "concrete"


class TestNamespaceFormatPropagation:
    """The namespace carries the global --format into the dispatched action."""

    def test_format_reaches_action_via_namespace(self) -> None:
        action = FakeAction()
        group = ConcreteCommand(action)
        root = argparse.ArgumentParser(prog="rhapsody-cli")
        root.add_argument("--format", choices=["table", "json", "csv"], default="table")
        subparsers = root.add_subparsers(dest="command", required=True)
        group.register(subparsers)
        namespace = root.parse_args(["--format", "json", "concrete", "run"])
        group.run(namespace)
        assert action.executed_with is not None
        assert action.executed_with.format == "json"

    def test_format_defaults_to_table(self) -> None:
        action = FakeAction()
        group = ConcreteCommand(action)
        root = argparse.ArgumentParser(prog="rhapsody-cli")
        root.add_argument("--format", choices=["table", "json", "csv"], default="table")
        subparsers = root.add_subparsers(dest="command", required=True)
        group.register(subparsers)
        namespace = root.parse_args(["concrete", "run"])
        group.run(namespace)
        assert action.executed_with is not None
        assert action.executed_with.format == "table"
