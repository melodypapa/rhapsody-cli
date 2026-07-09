"""Wraps ``com.telelogic.rhapsody.core.IRPModule``."""

from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.relations.model_instance import RPInstance


class RPModule(RPInstance):
    """Wraps ``IRPModule``: a module that extends ``IRPInstance``."""

    pass


AbstractRPModelElement.register_wrapper("Module", RPModule)
