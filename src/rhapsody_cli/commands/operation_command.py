"""Operation command group - dispatches to per-subcommand Action classes."""

from typing import List

from rhapsody_cli.actions.abstract_action import AbstractAction
from rhapsody_cli.actions.operation import (
    OperationCreateAction,
    OperationDeleteAction,
    OperationListAction,
    OperationUpdateAction,
    OperationViewAction,
)
from rhapsody_cli.commands.abstract_command import AbstractCommand


class OperationCommand(AbstractCommand):
    """Operation command group - handles operation subcommands (create, delete, view, list, update)."""

    def get_actions(self) -> List[AbstractAction]:
        """Return the operation subcommand actions."""
        return [
            OperationCreateAction(),
            OperationDeleteAction(),
            OperationViewAction(),
            OperationListAction(),
            OperationUpdateAction(),
        ]
