"""Helpers for building fake Rhapsody COM objects for unit tests.

These fakes stand in for real win32com dispatch objects so tests can run
without a licensed Rhapsody installation.
"""

from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pywintypes


def make_fake_element(meta_class: str, properties: Optional[Dict[str, Any]] = None, **method_returns: Any) -> MagicMock:
    """Build a fake COM object representing an IRPModelElement subtype.

    ``meta_class`` is the string returned by ``getMetaClass()`` (e.g.
    ``"Class"``, ``"Package"``, ``"Attribute"``), used by ``AbstractRPModelElement.wrap()`` to pick
    the correct wrapper class.

    ``method_returns`` maps method names to the value that mock method
    should return when called, e.g. ``getName="Foo"`` configures
    ``fake.getName()`` to return ``"Foo"``.

    ``properties`` maps pywin32 property names to the plain value a
    bare attribute read should return, e.g.
    ``properties={"isAbstract": 1}`` makes ``fake.isAbstract`` read as
    ``1`` (not a callable mock). Property-shaped wrappers read these
    via ``get_com_property`` / ``set_com_property``.
    """
    fake = MagicMock(name=f"FakeCom[{meta_class}]")
    fake.getMetaClass.return_value = meta_class
    for method_name, return_value in method_returns.items():
        getattr(fake, method_name).return_value = return_value
    for prop_name, prop_value in (properties or {}).items():
        setattr(fake, prop_name, prop_value)
    return fake


def make_fake_collection(items: List[Any]) -> MagicMock:
    """Build a fake COM object representing an IRPCollection."""

    def get_item(index: int) -> Any:
        if index <= 0:
            raise IndexError("IRPCollection indices are 1-based")
        return items[index - 1]

    fake = MagicMock(name="FakeCollection")
    fake.getCount.return_value = len(items)
    fake.getItem.side_effect = get_item
    return fake


def make_com_error(message: str = "Rhapsody COM failure") -> pywintypes.com_error:
    """Build a ``pywintypes.com_error`` matching what a failed COM call raises."""
    return pywintypes.com_error(-2147352567, message, None, None)
