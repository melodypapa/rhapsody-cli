"""Wraps ``com.telelogic.rhapsody.core.IRPComponentInstance``."""

from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.relations.model_instance import RPInstance


class RPComponentInstance(RPInstance):
    """Wraps ``IRPComponentInstance``: a component instance that extends ``IRPInstance``."""

    pass


AbstractRPModelElement.register_wrapper("ComponentInstance", RPComponentInstance)
