"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPFlow``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_other_model import IRPSysMLPort
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port import IRPPort


class IRPFlow(IRPModelElement):
    """Wraps ``IRPFlow``: a flow between two model elements in an activity diagram.

    The pywin32 binding exposes the JavaDoc getters and setters of this
    interface as COM properties, so the Python surface uses ``@property``
    accessors rather than ``get_*`` / ``set_*`` methods.
    """

    # IRPFlow method parity checklist:
    # [x] conveyed                     [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] direction                    [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] end1                         [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] end1_port                    [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] end1_sys_ml_port             [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] end2                         [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] end2_port                    [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] end2_sys_ml_port             [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_conveyed                 [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] remove_conveyed              [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_end1_via_port            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_end1_via_sys_ml_port     [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_end2_via_port            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_end2_via_sys_ml_port     [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)

    @property
    def conveyed(self) -> IRPCollection:
        """Returns the conveyed elements of the flow.

        Returns:
            The conveyed elements of the flow.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::getConveyed()
        """
        return IRPCollection(self.get_com_property(self._com, "conveyed"))

    @property
    def direction(self) -> str:
        """Returns the direction of the flow.

        Returns:
            One of ``"toEnd1"``, ``"toEnd2"``, or ``"bidirectional"``.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::getDirection()
        """
        return str(self.get_com_property(self._com, "direction"))

    @direction.setter
    def direction(self, direction: str) -> None:
        """Specifies the direction to use for the flow.

        Args:
            direction: One of ``"toEnd1"``, ``"toEnd2"``, or ``"bidirectional"``.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::setDirection(java.lang.String direction)
        """
        self.set_com_property(self._com, "direction", direction)

    @property
    def end1(self) -> IRPModelElement | None:
        """Returns the first end of the flow.

        Returns:
            The model element at the first end, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::getEnd1()
        """
        return self.wrap(self.get_com_property(self._com, "end1"))

    @end1.setter
    def end1(self, end1: IRPModelElement) -> None:
        """Sets the first end of the flow.

        Args:
            end1: The model element to set as the first end.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::setEnd1(com.telelogic.rhapsody.core.IRPModelElement end1)
        """
        self.set_com_property(self._com, "end1", end1._com)

    @property
    def end1_port(self) -> IRPPort:
        """Returns the port at the first end of the flow.

        Returns:
            The port at the first end of the flow.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::getEnd1Port()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port import IRPPort

        return cast(IRPPort, self.wrap(self.get_com_property(self._com, "end1Port")))

    @property
    def end1_sys_ml_port(self) -> IRPSysMLPort:
        """Returns the SysML port at the first end of the flow.

        Returns:
            The SysML port at the first end of the flow.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::getEnd1SysMLPort()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_other_model import IRPSysMLPort

        return cast(IRPSysMLPort, self.wrap(self.get_com_property(self._com, "end1SysMLPort")))

    @property
    def end2(self) -> IRPModelElement | None:
        """Returns the second end of the flow.

        Returns:
            The model element at the second end, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::getEnd2()
        """
        return self.wrap(self.get_com_property(self._com, "end2"))

    @end2.setter
    def end2(self, end2: IRPModelElement) -> None:
        """Sets the second end of the flow.

        Args:
            end2: The model element to set as the second end.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::setEnd2(com.telelogic.rhapsody.core.IRPModelElement end2)
        """
        self.set_com_property(self._com, "end2", end2._com)

    @property
    def end2_port(self) -> IRPPort:
        """Returns the port at the second end of the flow.

        Returns:
            The port at the second end of the flow.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::getEnd2Port()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port import IRPPort

        return cast(IRPPort, self.wrap(self.get_com_property(self._com, "end2Port")))

    @property
    def end2_sys_ml_port(self) -> IRPSysMLPort:
        """Returns the SysML port at the second end of the flow.

        Returns:
            The SysML port at the second end of the flow.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::getEnd2SysMLPort()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_other_model import IRPSysMLPort

        return cast(IRPSysMLPort, self.wrap(self.get_com_property(self._com, "end2SysMLPort")))

    def add_conveyed(self, p_element: IRPModelElement) -> None:
        """Adds a conveyed element to the flow.

        Args:
            p_element: The model element to add as conveyed.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::addConveyed(com.telelogic.rhapsody.core.IRPModelElement pElement)
        """
        self.call_com(lambda: self._com.addConveyed(p_element._com))

    def remove_conveyed(self, p_element: IRPModelElement) -> None:
        """Removes a conveyed element from the flow.

        Args:
            p_element: The model element to remove from the conveyed collection.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::removeConveyed(com.telelogic.rhapsody.core.IRPModelElement pElement)
        """
        self.call_com(lambda: self._com.removeConveyed(p_element._com))

    def set_end1_via_port(self, p_instance: IRPInstance, p_port: IRPPort) -> None:
        """Sets the first end of the flow via a port.

        Args:
            p_instance: The instance to set as the first end.
            p_port: The port to use for the connection.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::setEnd1ViaPort(com.telelogic.rhapsody.core.IRPInstance pInstance, com.telelogic.rhapsody.core.IRPPort pPort)
        """
        self.call_com(lambda: self._com.setEnd1ViaPort(p_instance._com, p_port._com))

    def set_end1_via_sys_ml_port(self, p_instance: IRPInstance, p_sys_m_l_port: IRPSysMLPort) -> None:
        """Sets the first end of the flow via a SysML port.

        Args:
            p_instance: The instance to set as the first end.
            p_sys_m_l_port: The SysML port to use for the connection.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::setEnd1ViaSysMLPort(com.telelogic.rhapsody.core.IRPInstance pInstance, com.telelogic.rhapsody.core.IRPSysMLPort pSysMLPort)
        """
        self.call_com(lambda: self._com.setEnd1ViaSysMLPort(p_instance._com, p_sys_m_l_port._com))

    def set_end2_via_port(self, p_instance: IRPInstance, p_port: IRPPort) -> None:
        """Sets the second end of the flow via a port.

        Args:
            p_instance: The instance to set as the second end.
            p_port: The port to use for the connection.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::setEnd2ViaPort(com.telelogic.rhapsody.core.IRPInstance pInstance, com.telelogic.rhapsody.core.IRPPort pPort)
        """
        self.call_com(lambda: self._com.setEnd2ViaPort(p_instance._com, p_port._com))

    def set_end2_via_sys_ml_port(self, p_instance: IRPInstance, p_sys_m_l_port: IRPSysMLPort) -> None:
        """Sets the second end of the flow via a SysML port.

        Args:
            p_instance: The instance to set as the second end.
            p_sys_m_l_port: The SysML port to use for the connection.

        Reference:
            com.telelogic.rhapsody.core.IRPFlow::setEnd2ViaSysMLPort(com.telelogic.rhapsody.core.IRPInstance pInstance, com.telelogic.rhapsody.core.IRPSysMLPort pSysMLPort)
        """
        self.call_com(lambda: self._com.setEnd2ViaSysMLPort(p_instance._com, p_sys_m_l_port._com))


IRPModelElement.register_wrapper("Flow", IRPFlow)
