"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPFlowItem``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPFlowItem(IRPClassifier):
    """Wraps ``IRPFlowItem``: represents item flows in Rhapsody models.

    The JavaDoc ``getRepresented`` accessor is exposed by pywin32 as a
    ``represented`` property.
    """

    # IRPFlowItem method parity checklist:
    # [x] represented                   [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_represented               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] remove_represented            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_classifier methods (covered by irp_classifier checklist)
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)
    # [inherited] irp_unit methods (covered by irp_unit checklist)

    @property
    def represented(self) -> IRPCollection:
        """Returns the information elements represented by the item flow.

        Returns:
            The represented elements as an ``IRPCollection``.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowItem::getRepresented()
        """
        return IRPCollection(self.get_com_property(self._com, "represented"))

    def add_represented(self, p_element: IRPModelElement) -> None:
        """Adds an element to the represented-information collection.

        Args:
            p_element: The element to add.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowItem::addRepresented(com.telelogic.rhapsody.core.IRPModelElement pElement)
        """
        self.call_com(lambda: self._com.addRepresented(p_element._com))

    def remove_represented(self, p_element: IRPModelElement) -> None:
        """Removes an element from the represented-information collection.

        Args:
            p_element: The element to remove.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowItem::removeRepresented(com.telelogic.rhapsody.core.IRPModelElement pElement)
        """
        self.call_com(lambda: self._com.removeRepresented(p_element._com))


IRPModelElement.register_wrapper("FlowItem", IRPFlowItem)
