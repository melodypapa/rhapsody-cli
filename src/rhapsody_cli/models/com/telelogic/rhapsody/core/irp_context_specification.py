"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPContextSpecification``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_values import IRPValueSpecification


def _cast_context_specification_dispatch(com_obj: object) -> object:
    """Cast a generic pywin model-element dispatch to IRPContextSpecification."""
    try:
        from win32com.client import CastTo, DispatchBaseClass
    except ImportError:
        return com_obj
    if isinstance(com_obj, DispatchBaseClass):
        return CastTo(com_obj, "IRPContextSpecification")
    return com_obj


class IRPContextSpecification(IRPValueSpecification):
    """Wraps ``IRPContextSpecification``: the exact context of an object.

    The context is a collection of strings giving the full path to the element
    together with a collection of indices disambiguating multiplicities. The
    JavaDoc accessor pairs are exposed by pywin32 as two read/write properties.
    """

    # IRPContextSpecification method parity checklist:
    # [x] multiplicities               [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] value                        [x] impl  [x] docstring  [x] unit test  [x] integration test (populated getter; setter live E_FAIL tracked in #202)
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)
    # [inherited] irp_value_specification methods (covered by irp_value_specification checklist)

    def __init__(self, com_obj: object) -> None:
        super().__init__(_cast_context_specification_dispatch(com_obj))

    @property
    def multiplicities(self) -> IRPCollection:
        """Returns the indices for each element in the ``value`` collection.

        Returns:
            A collection of indices given as strings.

        Reference:
            com.telelogic.rhapsody.core.IRPContextSpecification::getMultiplicities()
        """
        return IRPCollection(self.get_com_property(self._com, "multiplicities"))

    @multiplicities.setter
    def multiplicities(self, multiplicities: IRPCollection) -> None:
        """Specifies the indices for the elements in the ``value`` collection.

        Args:
            multiplicities: A collection of indices given as strings.

        Reference:
            com.telelogic.rhapsody.core.IRPContextSpecification::setMultiplicities(com.telelogic.rhapsody.core.IRPCollection multiplicities)
        """
        self.set_com_property(self._com, "multiplicities", multiplicities._com)

    @property
    def value(self) -> IRPCollection:
        """Returns the strings constituting the full path to the element.

        Returns:
            A collection of path strings.

        Reference:
            com.telelogic.rhapsody.core.IRPContextSpecification::getValue()
        """
        return IRPCollection(self.get_com_property(self._com, "value"))

    @value.setter
    def value(self, value: IRPCollection) -> None:
        """Specifies the strings constituting the full path to the element.

        Args:
            value: A collection of path strings.

        Reference:
            com.telelogic.rhapsody.core.IRPContextSpecification::setValue(com.telelogic.rhapsody.core.IRPCollection value)
        """
        self.set_com_property(self._com, "value", value._com)


IRPModelElement.register_wrapper("ContextSpecification", IRPContextSpecification)
