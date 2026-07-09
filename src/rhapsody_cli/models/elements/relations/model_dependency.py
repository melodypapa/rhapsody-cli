"""Wraps ``com.telelogic.rhapsody.core.IRPDependency``."""

from rhapsody_cli.models.core import AbstractRPModelElement, RPModelElement


class RPDependency(RPModelElement):
    """Wraps ``IRPDependency``: a dependency relationship."""

    pass


AbstractRPModelElement.register_wrapper("Dependency", RPDependency)
