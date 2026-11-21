"""Wrappers for Java package ``com.telelogic.rhapsody.core``.

Exports are resolved lazily: eagerly importing ``IRPClass`` here created a cycle
because its wrapper imports classifiers that in turn import this package.
"""

from importlib import import_module
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

_EXPORT_MODULES = {
    "IRPClass": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class",
    "IRPCollection": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection",
}

__all__ = ["IRPClass", "IRPCollection"]


def __getattr__(name: str) -> object:
    module_name = _EXPORT_MODULES.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    value = cast(object, getattr(import_module(module_name), name))
    globals()[name] = value
    return value
