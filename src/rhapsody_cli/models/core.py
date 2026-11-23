"""Core wrapping machinery shared by all rhapsody_cli element wrappers.

``ComHelper.call_com()`` translates COM failures into ``RhapsodyRuntimeException``.
``ComHelper`` provides the shared COM helpers and is inherited only by
``IRPModelElement``, the base interface for every wrapped Rhapsody model
element (mirroring ``com.telelogic.rhapsody.core.IRPModelElement``).
``ComHelper.wrap()`` dispatches a raw COM object to its matching wrapper
class using a registry populated by each element module at import time.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, TypeVar

from rhapsody_cli.exceptions import RhapsodyRuntimeException

try:
    import pywintypes
except ImportError:  # pragma: no cover - pywintypes is Windows-only
    pywintypes = None

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


T = TypeVar("T")


class ComHelper:
    """Mixin providing the single COM boundary for ``IRPModelElement``.

    Not a Java interface and not instantiated directly: it owns COM error
    translation, property access, element wrapping and wrapper registration
    for ``IRPModelElement`` and every subclass that inherits from it.
    """

    #: Maps a Rhapsody ``getMetaClass()`` string (e.g. "Class", "Package") to the
    #: wrapper class that should represent it. Populated by each element module
    #: at import time via ``register_wrapper``. Unmapped meta classes fall back
    #: to ``IRPModelElement`` in ``ComHelper.wrap()``.
    _WRAPPER_REGISTRY: dict[str, type[IRPModelElement]] = {}

    @classmethod
    def register_wrapper(cls, meta_class: str, wrapper_cls: type[IRPModelElement]) -> None:
        """Register ``wrapper_cls`` as the wrapper for COM objects of ``meta_class``."""
        cls._WRAPPER_REGISTRY[meta_class] = wrapper_cls

    @classmethod
    def call_com(cls, func: Callable[[], T]) -> T:
        """Invoke a COM call, translating ``pywintypes.com_error`` into ``RhapsodyRuntimeException``."""
        try:
            return func()
        except Exception as exc:
            if pywintypes is not None and isinstance(exc, pywintypes.com_error):
                raise RhapsodyRuntimeException(str(exc)) from exc
            raise

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

        Some Rhapsody COM automation Prog IDs (e.g. the Java-mirroring
        ``Rhapsody.Application``) expose model element attributes as methods
        (``getName()``, ``getGUID()``, ...), while others (e.g.
        ``Rhapsody2.Application.1``) expose the same data as bare COM
        properties (``name``, ``GUID``, ...). Prefer the method when present,
        and fall back to the bare property otherwise.

        Returns ``Any`` because COM property values are dynamically typed.

        .. deprecated::
            Legacy dual-binding probe. Synced wrappers call exactly one
            pywin32-exposed member via :meth:`call_com` / :meth:`get_com_property`.
        """
        if hasattr(com_obj, method_name):
            return cls.call_com(lambda: getattr(com_obj, method_name)())
        return cls.call_com(lambda: getattr(com_obj, prop_name))

    @classmethod
    def _set_method_or_property(cls, com_obj: object, method_name: str, prop_name: str, value: object) -> None:
        """Write a value to ``com_obj``, preferring the Java-style setter method.

        .. deprecated::
            Legacy dual-binding probe. Synced wrappers use :meth:`set_com_property`.
        """
        if hasattr(com_obj, method_name):
            cls.call_com(lambda: getattr(com_obj, method_name)(value))
        else:
            cls.call_com(lambda: setattr(com_obj, prop_name, value))

    @classmethod
    def get_com_property(cls, com_obj: object, prop_name: str) -> Any:
        """Read one pywin32-exposed COM property (authoritative name; no fallback).

        The generated pywin32 interface (``docs/reports/pywin32_authority.json``)
        is the single source of truth for the member name and shape.
        """
        return cls.call_com(lambda: getattr(com_obj, prop_name))

    @classmethod
    def set_com_property(cls, com_obj: object, prop_name: str, value: object) -> None:
        """Write one pywin32-exposed COM property (authoritative name; no fallback).

        See :meth:`get_com_property` for the pywin32-authoritative naming rule.
        """
        cls.call_com(lambda: setattr(com_obj, prop_name, value))
