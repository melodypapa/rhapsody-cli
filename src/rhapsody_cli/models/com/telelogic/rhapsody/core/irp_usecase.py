"""Extension-point wrapper (``IRPUseCase`` itself lives in the canonical package)."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPExtensionPoint(IRPModelElement):
    """Wraps extension point concept (returned as IRPModelElement from COM)."""

    pass


IRPModelElement.register_wrapper("ExtensionPoint", IRPExtensionPoint)
