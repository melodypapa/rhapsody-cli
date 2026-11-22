"""Variables package — wrappers for IRPVariable and its subtypes.

``IRPAttribute`` and ``IRPArgument`` are re-exported from their canonical
modules so the wrapper registry stays populated on plain package import.
"""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_argument import IRPArgument  # noqa: F401
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute  # noqa: F401
from rhapsody_cli.models.elements.variables.model_variables import (  # noqa: F401
    RPTag,
    RPVariable,
)

__all__ = [
    "IRPArgument",
    "IRPAttribute",
    "RPTag",
    "RPVariable",
]
