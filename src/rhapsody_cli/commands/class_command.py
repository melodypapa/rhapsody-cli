"""Class command group - dispatches to per-subcommand Action classes."""

from typing import List

from rhapsody_cli.actions.abstract_action import AbstractAction
from rhapsody_cli.actions.class_action import (
    ClassCreateAction,
    ClassDeleteAction,
    ClassLinkAction,
    ClassListAction,
    ClassUpdateAction,
    ClassViewAction,
)
from rhapsody_cli.commands.abstract_command import AbstractCommand


class ClassCommand(AbstractCommand):
    """Class command group - handles class subcommands (create, delete, view, list, link, update)."""

    def get_actions(self) -> List[AbstractAction]:
        """Return the class subcommand actions."""
        return [
            ClassCreateAction(),
            ClassDeleteAction(),
            ClassViewAction(),
            ClassListAction(),
            ClassLinkAction(),
            ClassUpdateAction(),
        ]
