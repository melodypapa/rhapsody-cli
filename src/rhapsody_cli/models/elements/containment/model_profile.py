"""Wraps ``com.telelogic.rhapsody.core.IRPProfile``."""

from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.containment.model_package import RPPackage


class RPProfile(RPPackage):
    """Wraps ``IRPProfile``: a profile that extends ``IRPPackage``."""

    pass


AbstractRPModelElement.register_wrapper("Profile", RPProfile)
