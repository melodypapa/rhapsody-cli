"""Abstract base class for CLI actions (subcommands)."""

import argparse
import logging
from typing import NoReturn

from rhapsody_cli.cli.context import RhapsodyContext
from rhapsody_cli.exceptions import CliExecutionError, RhapsodyConnectionError
from rhapsody_cli.models.elements.containment import RPProject


class AbstractAction:
    """Base class for a single subcommand action.

    Each action owns:
      - command_id: The subcommand identifier (e.g., "add", "open", "import")
      - logger: Instance-specific logger for this action
      - its own argument registration (init_arguments)
      - its own execution logic (execute)

    Instance Attributes:
      command_id (str): Subcommand identifier used for CLI dispatch (e.g., "add" for "element add")
      logger (logging.Logger): Instance-specific logger using the class name
    """

    def __init__(self, command_id: str = "") -> None:
        """Initialize the action with a command identifier.

        Args:
            command_id: The subcommand identifier (e.g., "add", "open", "import")
        """
        self.command_id = command_id
        self.logger = logging.getLogger(self.__class__.__name__)

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register this action's subparser and arguments.

        Args:
            sub_parser: The subparsers object returned by
                ArgumentParser.add_subparsers(), used to add this action's
                own subparser via sub_parser.add_parser(...).
        """
        raise NotImplementedError("Subclasses must implement the init_arguments method.")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute the action using the parsed arguments.

        Args:
            args: The parsed argparse.Namespace for the command group.
        """
        raise NotImplementedError("Subclasses must implement the execute method.")

    @staticmethod
    def add_verbose_argument(parser: argparse.ArgumentParser) -> None:
        """Add the shared --verbose/-v flag to a subcommand parser.

        Args:
            parser: The argument parser to add the verbose flag to.
        """
        parser.add_argument(
            "--verbose",
            "-v",
            action="store_true",
            help="Enable DEBUG-level logging",
        )


class RhapsodyContextAction(AbstractAction):
    """Base class for actions that require RhapsodyContext.

    Provides shared error handling and context management.
    """

    _NO_ACTIVE_INSTANCE_MESSAGE = "No running Rhapsody instance found. Please open Rhapsody and a project first."

    def _handle_connection_error(self, error: RhapsodyConnectionError, context_msg: str = "") -> NoReturn:
        """Log a connection error and raise CliExecutionError for the user.

        Args:
            error: The RhapsodyConnectionError to handle.
            context_msg: Optional context message to log.

        Raises:
            CliExecutionError: Always, with the user-facing "no active
                instance" message.
        """
        msg = f"Failed to attach to Rhapsody: {error}"
        if context_msg:
            msg = f"{context_msg}: {msg}"
        self.logger.error(msg)
        raise CliExecutionError(self._NO_ACTIVE_INSTANCE_MESSAGE) from error

    def _handle_execution_error(self, error: Exception, operation: str = "Operation") -> NoReturn:
        """Log an execution error and raise CliExecutionError for the user.

        Args:
            error: The exception to handle.
            operation: Description of what operation failed.

        Raises:
            CliExecutionError: Always, wrapping `error`'s message.
        """
        self.logger.error("%s failed: %s", operation, error)
        raise CliExecutionError(f"Error: {error}") from error


class ElementManagementAction(RhapsodyContextAction):
    """Base class for element management actions (add, delete, query, view).

    Provides shared element-specific utilities.
    """

    def _get_active_project(self) -> RPProject:
        """Get the active project, handling errors appropriately.

        Returns:
            The active project object.

        Raises:
            CliExecutionError: If no active project or connection error occurs.
        """
        ctx = RhapsodyContext()
        try:
            return ctx.get_active_project()
        except RhapsodyConnectionError as e:
            self._handle_connection_error(e)
