"""Wrappers for Java package ``com.telelogic.rhapsody.core``.

Exports are resolved lazily: eagerly importing ``IRPClass`` here created a cycle
because its wrapper imports classifiers that in turn import this package.
"""

from importlib import import_module
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application import IRPApplication
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_argument import IRPArgument
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_class import IRPAssociationClass
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port import IRPPort
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_type import IRPType
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit import AddToModelMode, IRPUnit
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_use_case import IRPUseCase

_EXPORT_MODULES = {
    "AddToModelMode": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit",
    "IRPArgument": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_argument",
    "IRPAssociationClass": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_class",
    "IRPAttribute": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute",
    "IRPClass": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class",
    "IRPInterfaceItem": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item",
    "IRPClassifier": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier",
    "IRPCollection": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection",
    "IRPModelElement": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element",
    "IRPOperation": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation",
    "IRPPackage": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package",
    "IRPPort": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port",
    "IRPProject": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project",
    "IRPType": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_type",
    "IRPUseCase": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_use_case",
    "IRPUnit": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit",
    "IRPApplication": "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application",
}

__all__ = [
    "AddToModelMode",
    "IRPApplication",
    "IRPArgument",
    "IRPAssociationClass",
    "IRPAttribute",
    "IRPClass",
    "IRPClassifier",
    "IRPCollection",
    "IRPModelElement",
    "IRPOperation",
    "IRPPackage",
    "IRPPort",
    "IRPProject",
    "IRPType",
    "IRPUnit",
    "IRPUseCase",
]


def __getattr__(name: str) -> object:
    module_name = _EXPORT_MODULES.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    value = cast(object, getattr(import_module(module_name), name))
    globals()[name] = value
    return value
