"""Attribute command group - dispatches to per-subcommand Action classes."""

from typing import List

from rhapsody_cli.actions.abstract_action import AbstractAction
from rhapsody_cli.actions.attribute import (
    AttributeCreateAction,
    AttributeDeleteAction,
    AttributeListAction,
    AttributeUpdateAction,
    AttributeViewAction,
)
from rhapsody_cli.commands.abstract_command import AbstractCommand


class AttributeCommand(AbstractCommand):
    """Attribute command group - handles attribute subcommands (create, delete, view, list, update)."""

    def get_actions(self) -> List[AbstractAction]:
        """Return the attribute subcommand actions."""
        return [
            AttributeCreateAction(),
            AttributeDeleteAction(),
            AttributeViewAction(),
            AttributeListAction(),
            AttributeUpdateAction(),
        ]
