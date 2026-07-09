"""Wraps ``com.telelogic.rhapsody.core.IRPComponent``."""

from rhapsody_cli.models.core import AbstractRPModelElement, RPUnit


class RPComponent(RPUnit):
    """Wraps ``IRPComponent``: a component that extends ``IRPUnit``."""

    pass


AbstractRPModelElement.register_wrapper("Component", RPComponent)
