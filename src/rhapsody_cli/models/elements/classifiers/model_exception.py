"""Exception model-element wrapper."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.core import AbstractRPModelElement


class RPException(IRPModelElement):
    """Wraps ``IRPException``."""


AbstractRPModelElement.register_wrapper("Exception", RPException)
