"""rhapsody_cli models package - wrappers for all Rhapsody model elements."""

from importlib import import_module

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit import IRPUnit
from rhapsody_cli.models.core import ComHelper

__all__ = [
    "ComHelper",
    "IRPCollection",
    "IRPModelElement",
    "IRPUnit",
    "register_all_wrappers",
]


def register_all_wrappers() -> None:
    """Import every core wrapper module so their meta-class registrations exist.

    Wrapper modules call ``IRPModelElement.register_wrapper`` at import time.
    A bare ``import rhapsody_cli`` used to load only a few modules, so CLI
    subprocesses resolved elements such as Class, Attribute, Operation and Port
    to plain ``IRPModelElement`` and lost their domain-specific methods.
    """
    from rhapsody_cli.models.com.telelogic.rhapsody.core import _EXPORT_MODULES

    for module_name in _EXPORT_MODULES.values():
        import_module(module_name)
