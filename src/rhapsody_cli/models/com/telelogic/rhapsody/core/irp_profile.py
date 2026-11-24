"""Wraps ``com.telelogic.rhapsody.core.IRPProfile``."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage


class IRPProfile(IRPPackage):
    """Wraps ``IRPProfile``: a profile that extends ``IRPPackage``."""

    # IRPProfile method parity checklist:
    # [inherited] irp_package / irp_unit / irp_model_element methods (covered by rp_package / rp_unit / rp_model_element checklists)
    # No deprecated IRPProfile methods.

    pass


IRPModelElement.register_wrapper("Profile", IRPProfile)
