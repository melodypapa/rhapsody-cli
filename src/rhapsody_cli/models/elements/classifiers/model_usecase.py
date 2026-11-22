"""Extension-point wrapper (``IRPUseCase`` itself lives in the canonical package)."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.core import AbstractRPModelElement


class RPExtensionPoint(IRPModelElement):
    """Wraps extension point concept (returned as IRPModelElement from COM)."""

    pass


AbstractRPModelElement.register_wrapper("ExtensionPoint", RPExtensionPoint)
