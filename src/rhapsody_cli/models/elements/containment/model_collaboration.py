"""Wraps ``com.telelogic.rhapsody.core.IRPCollaboration``."""

from rhapsody_cli.models.core import AbstractRPModelElement, RPUnit


class RPCollaboration(RPUnit):
    """Wraps ``IRPCollaboration``: a collaboration that extends ``IRPUnit``."""

    pass


AbstractRPModelElement.register_wrapper("Collaboration", RPCollaboration)
