"""Core wrapping machinery shared by all rhapsody_cli element wrappers.

``AbstractRPModelElement.call_com()`` translates COM failures into ``RhapsodyRuntimeException``.
``AbstractRPModelElement`` is the abstract base class providing common utilities.
``IRPModelElement`` is the base interface for every wrapped Rhapsody model
element, mirroring ``com.telelogic.rhapsody.core.IRPModelElement``.
``AbstractRPModelElement.wrap()`` dispatches a raw COM object to its matching wrapper class using
a registry populated by each element module at import time.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, TypeVar

from rhapsody_cli import com_utils

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


T = TypeVar("T")


class AbstractRPModelElement:
    """Abstract base class providing common utilities for all Rhapsody element wrappers.

    Implements class methods for COM interaction, element wrapping, and registry management.
    """

    #: Maps a Rhapsody ``getMetaClass()`` string (e.g. "Class", "Package") to the
    #: wrapper class that should represent it. Populated by each element module
    #: at import time via ``register_wrapper``. Unmapped meta classes fall back
    #: to ``IRPModelElement`` in ``AbstractRPModelElement.wrap()``.
    _WRAPPER_REGISTRY: dict[str, type[IRPModelElement]] = {}

    @classmethod
    def register_wrapper(cls, meta_class: str, wrapper_cls: type[IRPModelElement]) -> None:
        """Register ``wrapper_cls`` as the wrapper for COM objects of ``meta_class``."""
        cls._WRAPPER_REGISTRY[meta_class] = wrapper_cls

    @classmethod
    def call_com(cls, func: Callable[[], T]) -> T:
        """Invoke a COM call, translating COM errors into RhapsodyRuntimeException.

        Forwards to :func:`rhapsody_cli.com_utils.call_com`.
        """
        return com_utils.call_com(func)

    @classmethod
    def _wrap_if_element(cls, value: Any) -> Any:
        """Wrap ``value`` if it looks like a Rhapsody model element."""
        if hasattr(value, "getMetaClass") or hasattr(value, "metaClass"):
            return cls.wrap(value)
        return value

    @classmethod
    def wrap(cls, com_obj: object) -> IRPModelElement | None:
        """Wrap a raw Rhapsody COM model element in its matching wrapper class.

        Args:
            com_obj: A raw COM object from Rhapsody API, or None.

        Returns:
            An IRPModelElement (or specific subclass) wrapping the COM object,
            or None if com_obj is None. None typically indicates a search/find
            operation returned no result (e.g., findNestedElement not found).
        """
        if com_obj is None:
            return None  # Truthfully return None instead of wrapping it
        meta_class = str(cls.get_com_property(com_obj, "metaClass"))
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

        wrapper_cls = cls._WRAPPER_REGISTRY.get(meta_class, IRPModelElement)
        return wrapper_cls(com_obj)

    @classmethod
    def _get_method_or_property(cls, com_obj: object, method_name: str, prop_name: str) -> Any:
        """Read a value from ``com_obj``, preferring the Java-style method.

        Forwards to :func:`rhapsody_cli.com_utils._get_method_or_property`.
        """
        return com_utils._get_method_or_property(com_obj, method_name, prop_name)

    @classmethod
    def _set_method_or_property(cls, com_obj: object, method_name: str, prop_name: str, value: object) -> None:
        """Write a value to ``com_obj``, preferring the Java-style setter method.

        Forwards to :func:`rhapsody_cli.com_utils._set_method_or_property`.

        .. deprecated:: Legacy dual-binding probe; synced wrappers use :meth:`get_com_property` / :meth:`set_com_property`.
        """
        com_utils._set_method_or_property(com_obj, method_name, prop_name, value)

    @classmethod
    def get_com_property(cls, com_obj: object, prop_name: str) -> Any:
        """Read one pywin32-exposed COM property (authoritative name; no fallback).

        Forwards to :func:`rhapsody_cli.com_utils.get_com_property`.
        """
        return com_utils.get_com_property(com_obj, prop_name)

    @classmethod
    def set_com_property(cls, com_obj: object, prop_name: str, value: object) -> None:
        """Write one pywin32-exposed COM property (authoritative name; no fallback).

        Forwards to :func:`rhapsody_cli.com_utils.set_com_property`.
        """
        com_utils.set_com_property(com_obj, prop_name, value)
