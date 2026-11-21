"""Exception model-element wrapper."""

from rhapsody_cli.models.core import AbstractRPModelElement, IRPModelElement


class RPException(IRPModelElement):
    """Wraps ``IRPException``."""


AbstractRPModelElement.register_wrapper("Exception", RPException)
