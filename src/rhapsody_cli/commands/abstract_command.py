"""Abstract base class for all CLI command groups."""

import argparse
import logging
from typing import Dict, List, Optional

from rhapsody_cli.actions.abstract_action import AbstractAction
from rhapsody_cli.exceptions import CliExecutionError

logger = logging.getLogger(__name__)


class AbstractCommand:
    """Base class for all CLI command groups.

    Subclasses provide their set of AbstractAction instances via get_actions().
    Each group registers a subparser into the root parser (register) and
    dispatches to the action selected by the parsed namespace (run).
    """

    def __init__(self, args: Optional[List[str]] = None) -> None:
        """Initialize the group.

        Args:
            args: Legacy two-tier usage passes raw args for immediate parsing;
                registry usage constructs without args and defers to register().
        """
        self._sub_commands: Dict[str, AbstractAction] = {}
        self._parsed_args: Optional[argparse.Namespace] = None
        self._subcommand: Optional[str] = None
        if args is not None:
            self._legacy_parse(args)

    def _legacy_parse(self, args: List[str]) -> None:
        """Two-tier constructor path (removed when main() moves to the registry)."""
        name = self._command_name()
        parser = argparse.ArgumentParser(prog=f"rhapsody-cli {name}")
        actions = self.get_actions()
        self._sub_commands = {action.command_id: action for action in actions}
        sub_parsers = parser.add_subparsers(dest="subcommand")
        for action in actions:
            action.init_arguments(sub_parsers)
        self._parsed_args = parser.parse_args(args)
        self._subcommand = self._parsed_args.subcommand
        if not self._subcommand:
            parser.print_help()
            raise CliExecutionError(f"Missing subcommand for '{name}'", exit_code=2)

    def get_actions(self) -> List[AbstractAction]:
        """Return the list of actions (subcommands) for this command group.

        Subclasses must override this to register their own actions.
        """
        raise NotImplementedError(f"{self.__class__.__name__}.get_actions() must be implemented")

    def register(self, subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register this group's subparser and its actions' sub-subparsers.

        Args:
            subparsers: The root parser's subparsers action.
        """
        name = self._command_name()
        parser = subparsers.add_parser(name, help=f"Manage {name}s")
        actions = self.get_actions()
        self._sub_commands = {action.command_id: action for action in actions}
        sub_parsers = parser.add_subparsers(dest="subcommand", required=True, metavar="<subcommand>")
        for action in actions:
            action.init_arguments(sub_parsers)

    def run(self, namespace: argparse.Namespace) -> None:
        """Dispatch execution to the action selected by the namespace.

        Args:
            namespace: The parsed argparse namespace (from the root parser).

        Raises:
            CliExecutionError: If the requested subcommand is unknown.
        """
        action = self._sub_commands.get(namespace.subcommand)
        if action is None:
            logger.error("Unknown subcommand '%s'", namespace.subcommand)
            raise CliExecutionError(f"Unknown subcommand '{namespace.subcommand}'", exit_code=2)
        action.execute(namespace)

    def execute(self, output_format: str = "table") -> None:
        """Legacy two-tier dispatch (removed with _legacy_parse).

        Args:
            output_format: The output format ("table", "json", "csv") to set
                on the dispatched action before executing it.
        """
        action = self._sub_commands.get(self._subcommand) if self._subcommand else None
        if action is None or self._parsed_args is None:
            raise CliExecutionError(f"Unknown subcommand '{self._subcommand}'", exit_code=2)
        if hasattr(action, "output_format"):
            action.output_format = output_format
        action.execute(self._parsed_args)

    def _command_name(self) -> str:
        """Get the command name (lowercase class name)."""
        return self.__class__.__name__.replace("Command", "").lower()
