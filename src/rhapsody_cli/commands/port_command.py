"""Port command group - dispatches to per-subcommand Action classes."""

from typing import List

from rhapsody_cli.actions.abstract_action import AbstractAction
from rhapsody_cli.actions.port_action import (
    PortCreateAction,
    PortDeleteAction,
    PortListAction,
    PortUpdateAction,
    PortViewAction,
)
from rhapsody_cli.commands.abstract_command import AbstractCommand


class PortCommand(AbstractCommand):
    """Port command group - handles port subcommands (create, delete, view, list, update)."""

    def __init__(self, args: List[str]) -> None:
        """Initialize PortCommand and parse port subcommands.

        Args:
            args: Arguments after 'port' command
                (e.g., ['create', '--path', 'Sensors/Cls', '{"name":"clientPort"}'])
        """
        super().__init__("port", args)

    def get_actions(self) -> List[AbstractAction]:
        """Return the port subcommand actions."""
        return [
            PortCreateAction(),
            PortDeleteAction(),
            PortViewAction(),
            PortListAction(),
            PortUpdateAction(),
        ]
