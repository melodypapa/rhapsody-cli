"""Wraps ``com.telelogic.rhapsody.core.IRPNode``."""

from rhapsody_cli.models.core import AbstractRPModelElement, RPUnit


class RPNode(RPUnit):
    """Wraps ``IRPNode``: a node that extends ``IRPUnit``."""

    pass


AbstractRPModelElement.register_wrapper("Node", RPNode)
