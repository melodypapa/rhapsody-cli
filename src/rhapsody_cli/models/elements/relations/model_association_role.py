"""Wraps ``com.telelogic.rhapsody.core.IRPAssociationRole``."""

from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.relations.model_instance import RPInstance


class RPAssociationRole(RPInstance):
    """Wraps ``IRPAssociationRole``: an association role that extends ``IRPInstance``."""

    pass


AbstractRPModelElement.register_wrapper("AssociationRole", RPAssociationRole)
