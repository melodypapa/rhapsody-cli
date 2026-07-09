"""Wraps ``com.telelogic.rhapsody.core.IRPAssociationClass``."""

from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.classifiers.model_class import RPClass


class RPAssociationClass(RPClass):
    """Wraps ``IRPAssociationClass``: an association class that extends ``IRPClass``."""

    pass


AbstractRPModelElement.register_wrapper("AssociationClass", RPAssociationClass)
