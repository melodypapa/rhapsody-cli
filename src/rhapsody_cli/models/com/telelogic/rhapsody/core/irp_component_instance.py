"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPComponentInstance``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component import IRPComponent
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_node import IRPNode


class IRPComponentInstance(IRPInstance):
    """Wraps ``IRPComponentInstance``: a component instance extending ``IRPInstance``.

    The JavaDoc accessors are exposed by pywin32 as read/write ``componentType``
    and read-only ``node`` properties.
    """

    # IRPComponentInstance method parity checklist:
    # [x] component_type               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] node                         [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_instance / irp_relation / irp_unit / irp_model_element methods

    @property
    def component_type(self) -> IRPComponent | None:
        """Returns the component type of this instance.

        Reference:
            com.telelogic.rhapsody.core.IRPComponentInstance::getComponentType()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component import IRPComponent

        return cast(IRPComponent, self.wrap(self.get_com_property(self._com, "componentType")))

    @component_type.setter
    def component_type(self, component: IRPComponent) -> None:
        """Sets the component type of this instance.

        Reference:
            com.telelogic.rhapsody.core.IRPComponentInstance::setComponentType(IRPComponent component)
        """
        self.set_com_property(self._com, "componentType", component._com)

    @property
    def node(self) -> IRPNode | None:
        """Returns the node containing this component instance.

        Reference:
            com.telelogic.rhapsody.core.IRPComponentInstance::getNode()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_node import IRPNode

        return cast(IRPNode, self.wrap(self.get_com_property(self._com, "node")))


IRPModelElement.register_wrapper("ComponentInstance", IRPComponentInstance)
