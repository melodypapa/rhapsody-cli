"""Wrappers for Java package ``com.telelogic.rhapsody.core``.

Exports are resolved lazily: eagerly importing ``IRPClass`` here created a cycle
because its wrapper imports classifiers that in turn import this package.
"""

from importlib import import_module
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit import AddToModelMode, IRPUnit

_EXPORT_MODULES = {
    "AddToModelMode": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit",
    "IRPClass": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class",
    "IRPCollection": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection",
    "IRPUnit": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit",
}

__all__ = ["AddToModelMode", "IRPClass", "IRPCollection", "IRPUnit"]


def __getattr__(name: str) -> object:
    module_name = _EXPORT_MODULES.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    value = cast(object, getattr(import_module(module_name), name))
    globals()[name] = value
    return value
