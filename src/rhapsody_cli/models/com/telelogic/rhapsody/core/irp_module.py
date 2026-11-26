"""Wraps ``com.telelogic.rhapsody.core.IRPModule``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPModule(IRPInstance):
    """Wraps ``IRPModule``: a module that extends ``IRPInstance``."""

    # IRPModule method parity checklist:
    # [inherited] irp_instance / irp_relation / irp_unit / irp_model_element methods (covered by their own checklists)
    # No deprecated IRPModule methods.

    pass


IRPModelElement.register_wrapper("Module", IRPModule)
