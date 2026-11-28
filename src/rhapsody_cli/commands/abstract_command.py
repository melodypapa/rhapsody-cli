"""Abstract base class for all CLI command groups."""

import argparse
import logging
from typing import Dict, List

from rhapsody_cli.actions.abstract_action import AbstractAction
from rhapsody_cli.exceptions import CliExecutionError

logger = logging.getLogger(__name__)


class AbstractCommand:
    """Base class for all CLI command groups.

    Subclasses provide their set of AbstractAction instances via get_actions().
    Each group registers a subparser into the root parser (register) and
    dispatches to the action selected by the parsed namespace (run).
    """

    def __init__(self) -> None:
        """Initialize the group with an empty subcommand map (filled by register)."""
        self._sub_commands: Dict[str, AbstractAction] = {}

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
        help_text = f"Manage {name}es" if name.endswith("s") else f"Manage {name}s"
        parser = subparsers.add_parser(name, help=help_text)
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

    def _command_name(self) -> str:
        """Get the command name (lowercase class name)."""
        return self.__class__.__name__.replace("Command", "").lower()
