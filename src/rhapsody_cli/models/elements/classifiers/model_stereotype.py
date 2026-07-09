"""Wraps ``com.telelogic.rhapsody.core.IRPStereotype``."""

from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.classifiers.model_classifier import RPClassifier


class RPStereotype(RPClassifier):
    """Wraps ``IRPStereotype``: a stereotype that extends ``IRPClassifier``."""

    pass


AbstractRPModelElement.register_wrapper("Stereotype", RPStereotype)
