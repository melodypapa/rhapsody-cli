"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPSwimlane``."""

from __future__ import annotations

from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPSwimlane(IRPModelElement):
    """Wraps ``IRPSwimlane``: represents swimlanes in an activity diagram.

    JavaDoc accessors exposed by pywin32 as properties are surfaced as
    ``@property`` members; ``add_swimlane`` remains a method.
    """

    # IRPSwimlane method parity checklist:
    # [x] contents                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] represents                    [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] swimlanes                     [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_swimlane                  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)

    @property
    def contents(self) -> IRPCollection:
        """Returns the elements contained in the swimlane.

        Returns:
            The contained elements as an ``IRPCollection``.

        Reference:
            com.telelogic.rhapsody.core.IRPSwimlane::getContents()
        """
        return IRPCollection(self.get_com_property(self._com, "contents"))

    @property
    def represents(self) -> IRPModelElement | None:
        """Returns the model element represented by the swimlane.

        Returns:
            The represented model element, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPSwimlane::getRepresents()
        """
        return self.wrap(self.get_com_property(self._com, "represents"))

    @represents.setter
    def represents(self, represents: IRPModelElement) -> None:
        """Specifies the model element that the swimlane represents.

        Args:
            represents: The model element to represent.

        Reference:
            com.telelogic.rhapsody.core.IRPSwimlane::setRepresents(com.telelogic.rhapsody.core.IRPModelElement represents)
        """
        self.set_com_property(self._com, "represents", represents._com)

    @property
    def swimlanes(self) -> IRPCollection:
        """Returns the swimlanes nested under this swimlane.

        Returns:
            The nested swimlanes as an ``IRPCollection``.

        Reference:
            com.telelogic.rhapsody.core.IRPSwimlane::getSwimlanes()
        """
        return IRPCollection(self.get_com_property(self._com, "swimlanes"))

    def add_swimlane(self, name: str) -> IRPSwimlane:
        """Adds a nested swimlane (for internal use).

        Args:
            name: The name of the new swimlane.

        Returns:
            The swimlane that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPSwimlane::addSwimlane(java.lang.String name)
        """
        return cast(IRPSwimlane, self.wrap(self.call_com(lambda: self._com.addSwimlane(name))))


IRPModelElement.register_wrapper("Swimlane", IRPSwimlane)
