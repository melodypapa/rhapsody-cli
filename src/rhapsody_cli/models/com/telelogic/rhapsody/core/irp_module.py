"""Wraps ``com.telelogic.rhapsody.core.IRPModule``."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPModule(IRPInstance):
    """Wraps ``IRPModule``: a module that extends ``IRPInstance``."""

    # IRPModule method parity checklist:
    # [inherited] irp_instance / irp_relation / irp_unit / irp_model_element methods (covered by rp_instance / rp_relation / rp_unit / rp_model_element checklists)
    # No deprecated IRPModule methods.

    pass


IRPModelElement.register_wrapper("Module", IRPModule)
