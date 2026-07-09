"""Wraps ``com.telelogic.rhapsody.core.IRPGeneralization``."""

from rhapsody_cli.models.core import AbstractRPModelElement, RPModelElement


class RPGeneralization(RPModelElement):
    """Wraps ``IRPGeneralization``: a generalization (inheritance) relationship."""

    pass


AbstractRPModelElement.register_wrapper("Generalization", RPGeneralization)
