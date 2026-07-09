"""Wraps ``com.telelogic.rhapsody.core.IRPConfiguration``."""

from rhapsody_cli.models.core import AbstractRPModelElement, RPUnit


class RPConfiguration(RPUnit):
    """Wraps ``IRPConfiguration``: a configuration that extends ``IRPUnit``."""

    pass


AbstractRPModelElement.register_wrapper("Configuration", RPConfiguration)
