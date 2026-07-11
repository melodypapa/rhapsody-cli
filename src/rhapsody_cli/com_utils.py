"""Standalone COM utility functions shared by application.py and models/core.py.

Provides ``call_com()``, ``get_method_or_property()``, and
``set_method_or_property()`` as module-level functions so that both
``RhapsodyApplication`` and element wrapper classes can use them without
inheriting from ``AbstractRPModelElement``.
"""

from typing import Any, Callable, TypeVar

from rhapsody_cli.exceptions import RhapsodyRuntimeException

try:
    import pywintypes
except ImportError:  # pragma: no cover - pywintypes is Windows-only
    pywintypes = None

T = TypeVar("T")


def call_com(func: Callable[[], T]) -> T:
    """Invoke a COM call, translating COM errors into RhapsodyRuntimeException."""
    try:
        return func()
    except Exception as exc:
        if pywintypes is not None and isinstance(exc, pywintypes.com_error):
            raise RhapsodyRuntimeException(str(exc)) from exc
        raise


def _get_method_or_property(com_obj: Any, method_name: str, prop_name: str) -> Any:
    """Read a value from ``com_obj``, preferring the Java-style method.

    Some Rhapsody COM automation Prog IDs (e.g. the Java-mirroring
    ``Rhapsody.Application``) expose model element attributes as methods
    (``getName()``, ``getGUID()``, ...), while others (e.g.
    ``Rhapsody2.Application.1``) expose the same data as bare COM
    properties (``name``, ``GUID``, ...). Prefer the method when present,
    and fall back to the bare property otherwise.
    """
    if hasattr(com_obj, method_name):
        return call_com(lambda: getattr(com_obj, method_name)())
    return call_com(lambda: getattr(com_obj, prop_name))


def _set_method_or_property(com_obj: Any, method_name: str, prop_name: str, value: Any) -> None:
    """Write a value to ``com_obj``, preferring the Java-style setter method.

    See :func:`_get_method_or_property` for why both forms exist.
    """
    if hasattr(com_obj, method_name):
        call_com(lambda: getattr(com_obj, method_name)(value))
    else:
        call_com(lambda: setattr(com_obj, prop_name, value))
