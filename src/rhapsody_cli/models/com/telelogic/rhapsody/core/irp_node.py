"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPNode``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component_instance import IRPComponentInstance


class IRPNode(IRPUnit):
    """Wraps ``IRPNode``: a node that extends ``IRPUnit``.

    The JavaDoc accessor pairs are exposed by pywin32 as read/write
    ``CPUtype`` and read-only ``componentInstances`` properties.
    """

    # IRPNode method parity checklist:
    # [x] cpu_type                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] component_instances           [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_component_instance        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] delete_component_instance     [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] find_component_instance       [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_unit / irp_model_element methods (covered by their checklists)

    @property
    def cpu_type(self) -> str:
        """Returns the CPU type of the node.

        Reference:
            com.telelogic.rhapsody.core.IRPNode::getCPUtype()
        """
        return str(self.get_com_property(self._com, "CPUtype"))

    @cpu_type.setter
    def cpu_type(self, value: str) -> None:
        """Sets the CPU type of the node.

        Reference:
            com.telelogic.rhapsody.core.IRPNode::setCPUtype(java.lang.String value)
        """
        self.set_com_property(self._com, "CPUtype", value)

    @property
    def component_instances(self) -> IRPCollection:
        """Returns all component instances in the node.

        Reference:
            com.telelogic.rhapsody.core.IRPNode::getComponentInstances()
        """
        return IRPCollection(self.get_com_property(self._com, "componentInstances"))

    def add_component_instance(self, name: str) -> IRPComponentInstance:
        """Adds a component instance to the node.

        Args:
            name: The name of the new component instance.

        Returns:
            The component instance created.

        Reference:
            com.telelogic.rhapsody.core.IRPNode::addComponentInstance(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component_instance import IRPComponentInstance

        return cast(IRPComponentInstance, self.wrap(self.call_com(lambda: self._com.addComponentInstance(name))))

    def delete_component_instance(self, instance: IRPComponentInstance) -> None:
        """Deletes a component instance from the node.

        Args:
            instance: The component instance to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPNode::deleteComponentInstance(IRPComponentInstance instance)
        """
        self.call_com(lambda: self._com.deleteComponentInstance(instance._com))

    def find_component_instance(self, name: str) -> IRPComponentInstance | None:
        """Finds a component instance by name.

        Args:
            name: The name to look up.

        Returns:
            The matching instance, or None if not found.

        Reference:
            com.telelogic.rhapsody.core.IRPNode::findComponentInstance(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component_instance import IRPComponentInstance

        result = self.call_com(lambda: self._com.findComponentInstance(name))
        if result is None:
            return None
        return cast(IRPComponentInstance, self.wrap(result))


IRPModelElement.register_wrapper("Node", IRPNode)
