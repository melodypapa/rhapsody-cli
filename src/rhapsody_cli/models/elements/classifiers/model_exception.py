"""Exception model-element wrapper."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class RPException(IRPModelElement):
    """Wraps ``IRPException``."""


IRPModelElement.register_wrapper("Exception", RPException)
