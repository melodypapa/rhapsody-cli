"""Wrapper for ``com.telelogic.rhapsody.core.IRPCollection``.

Canonical module for :class:`IRPCollection`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_collection.md``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator

from rhapsody_cli import com_utils

if TYPE_CHECKING:
    from rhapsody_cli.models.core import IRPModelElement


class IRPCollection:
    """Wraps ``IRPCollection``: an iterable/indexable container of elements."""

    # IRPCollection method parity checklist:
    # [x] get_count  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_item  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_item  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_graphical_item  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] to_list  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_size  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] remove  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_string  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_model_element  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] empty  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_integer  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # No deprecated IRPCollection methods.

    def __init__(self, com_obj: Any) -> None:
        self._com = com_obj

    def get_count(self) -> int:
        """Returns the number of elements in the collection.

        Returns:
            The number of elements in the collection as an integer.

        Reference:
            com.telelogic.rhapsody.core.IRPCollection::getCount()
        """
        return int(com_utils.get_com_property(self._com, "Count"))

    def get_item(self, index: int) -> Any:
        """Returns the element at the specified index in the collection.

        Args:
            index: The 1-based position of the element to retrieve.

        Returns:
            The wrapped element at the given index.

        Raises:
            RhapsodyRuntimeException: if the element at the given index
                cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPCollection::getItem(int)
        """
        raw_item = com_utils.call_com(lambda: self._com.Item(index))
        from rhapsody_cli.models.core import AbstractRPModelElement

        return AbstractRPModelElement._wrap_if_element(raw_item)

    def add_item(self, element: IRPModelElement) -> None:
        """Adds an element to the collection.

        Args:
            element: The model element to add to the collection.

        Raises:
            RhapsodyRuntimeException: if the element cannot be added to
                the collection.

        Reference:
            com.telelogic.rhapsody.core.IRPCollection::addItem(com.telelogic.rhapsody.core.IRPModelElement)
        """
        com_utils.call_com(lambda: self._com.addItem(element._com))

    def add_graphical_item(self, item: IRPModelElement) -> None:
        """Adds a graphical item to the collection.

        Args:
            item: The graphical model element to add.

        Raises:
            RhapsodyRuntimeException: If the operation fails.

        Reference:
            com.telelogic.rhapsody.core.IRPCollection::addGraphicalItem(com.telelogic.rhapsody.core.IRPModelElement)
        """
        com_utils.call_com(lambda: self._com.addGraphicalItem(item._com))

    def to_list(self) -> list[Any]:
        """Converts the collection to a Python list.

        Returns:
            A Python list containing all elements in the collection.

        Reference:
            com.telelogic.rhapsody.core.IRPCollection::toList()
        """
        return list(self)

    def set_size(self, size: int) -> None:
        """Sets the size of the collection.

        Args:
            size: The new size for the collection.

        Raises:
            RhapsodyRuntimeException: If the operation fails.

        Reference:
            com.telelogic.rhapsody.core.IRPCollection::setSize(int)
        """
        com_utils.call_com(lambda: self._com.setSize(size))

    def remove(self, index: int) -> None:
        """Removes the element at the specified index.

        Args:
            index: The 1-based index of the element to remove.

        Raises:
            RhapsodyRuntimeException: If the operation fails.

        Reference:
            com.telelogic.rhapsody.core.IRPCollection::remove(int)
        """
        com_utils.call_com(lambda: self._com.remove(index))

    def set_string(self, index: int, value: str) -> None:
        """Sets a string value at the specified index.

        Args:
            index: The 1-based index where to set the value.
            value: The string value to set.

        Raises:
            RhapsodyRuntimeException: If the operation fails.

        Reference:
            com.telelogic.rhapsody.core.IRPCollection::setString(int, java.lang.String)
        """
        com_utils.call_com(lambda: self._com.setString(index, value))

    def set_model_element(self, index: int, element: IRPModelElement) -> None:
        """Sets a model element at the specified index.

        Args:
            index: The 1-based index where to set the element.
            element: The model element to set.

        Raises:
            RhapsodyRuntimeException: If the operation fails.

        Reference:
            com.telelogic.rhapsody.core.IRPCollection::setModelElement(int, com.telelogic.rhapsody.core.IRPModelElement)
        """
        com_utils.call_com(lambda: self._com.setModelElement(index, element._com))

    def empty(self) -> None:
        """Removes all elements from the collection.

        Raises:
            RhapsodyRuntimeException: If the operation fails.

        Reference:
            com.telelogic.rhapsody.core.IRPCollection::empty()
        """
        com_utils.call_com(lambda: self._com.empty())

    def set_integer(self, index: int, value: int) -> None:
        """Sets an integer value at the specified index.

        Args:
            index: The 1-based index where to set the value.
            value: The integer value to set.

        Raises:
            RhapsodyRuntimeException: If the operation fails.

        Reference:
            com.telelogic.rhapsody.core.IRPCollection::setInteger(int, int)
        """
        com_utils.call_com(lambda: self._com.setInteger(index, value))

    def __len__(self) -> int:
        return self.get_count()

    def __getitem__(self, index: Any) -> Any:
        if isinstance(index, slice):
            return [self.get_item(i + 1) for i in range(*index.indices(len(self)))]
        if index < 0:
            raise IndexError("negative indices are not supported")
        return self.get_item(index + 1)

    def __iter__(self) -> Iterator[Any]:
        for index in range(1, len(self) + 1):
            yield self.get_item(index)
