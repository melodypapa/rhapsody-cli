"""Containment package — wrappers for IRPPackage and IRPProject."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage  # noqa: F401
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject  # noqa: F401
from rhapsody_cli.models.elements.containment.model_collaboration import (  # noqa: F401
    RPCollaboration,
)
from rhapsody_cli.models.elements.containment.model_component import RPComponent  # noqa: F401
from rhapsody_cli.models.elements.containment.model_component_instance import (  # noqa: F401
    RPComponentInstance,
)
from rhapsody_cli.models.elements.containment.model_configuration import (  # noqa: F401
    RPConfiguration,
)
from rhapsody_cli.models.elements.containment.model_module import RPModule  # noqa: F401
from rhapsody_cli.models.elements.containment.model_node import RPNode  # noqa: F401
from rhapsody_cli.models.elements.containment.model_profile import RPProfile  # noqa: F401

__all__ = [
    "RPCollaboration",
    "RPComponent",
    "RPComponentInstance",
    "RPConfiguration",
    "RPModule",
    "RPNode",
    "IRPPackage",
    "RPProfile",
    "IRPProject",
]
