"""Wrappers for ``com.telelogic.rhapsody.core.IRPPort``.

Canonical module for :class:`IRPPort`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_port.md``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.elements.relations.model_instance import RPInstance

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass


class IRPPort(RPInstance):
    """Wraps ``IRPPort``: represents a port on a classifier in the model."""

    # IRPPort method parity checklist:
    # [x] add_provided_interface      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_required_interface      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_behavioral               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_reversed                 [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] port_contract               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] provided_interfaces         [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] required_interfaces         [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] remove_provided_interface   [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] remove_required_interface   [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_contract (deprecated, use port_contract) [x] impl [x] docstring [x] unit test  [ ] integration test
    # [x] set_contract (deprecated, use port_contract) [x] impl [x] docstring [x] unit test  [ ] integration test

    @property
    def is_behavioral(self) -> int:
        """Checks whether the port is a behavioral port.

        Returns:
            ``1`` if the port is behavioral, ``0`` otherwise.

        Raises:
            RhapsodyRuntimeException: if the property cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::getIsBehavioral()
        """
        return int(self.get_com_property(self._com, "isBehavioral"))

    @is_behavioral.setter
    def is_behavioral(self, is_behavioral: int) -> None:
        """Specifies whether the port should be a behavioral port.

        Args:
            is_behavioral: ``1`` to make the port behavioral, ``0`` otherwise.

        Raises:
            RhapsodyRuntimeException: if the property cannot be set.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::setIsBehavioral(int isBehavioral)
        """
        self.set_com_property(self._com, "isBehavioral", is_behavioral)

    @property
    def is_reversed(self) -> int:
        """Checks whether the port's direction is reversed.

        Returns:
            ``1`` if the port is reversed, ``0`` otherwise.

        Raises:
            RhapsodyRuntimeException: if the property cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::getIsReversed()
        """
        return int(self.get_com_property(self._com, "isReversed"))

    @is_reversed.setter
    def is_reversed(self, is_reversed: int) -> None:
        """Specifies whether the port's direction should be reversed.

        Args:
            is_reversed: ``1`` to reverse the port, ``0`` otherwise.

        Raises:
            RhapsodyRuntimeException: if the property cannot be set.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::setIsReversed(int isReversed)
        """
        self.set_com_property(self._com, "isReversed", is_reversed)

    @property
    def port_contract(self) -> IRPClass:
        """Returns the contract defined for the port.

        Returns:
            The wrapped ``IRPClass`` used as the port's contract.

        Raises:
            RhapsodyRuntimeException: if the contract cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::getPortContract()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass

        return cast(IRPClass, self.wrap(self.get_com_property(self._com, "portContract")))

    @port_contract.setter
    def port_contract(self, port_contract: IRPModelElement) -> None:
        """Specifies the contract to use for the port.

        Args:
            port_contract: The class (``IRPClass``) to use as the port's contract.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::setPortContract(com.telelogic.rhapsody.core.IRPClass portContract)
        """
        self.set_com_property(self._com, "portContract", port_contract._com)

    @property
    def provided_interfaces(self) -> IRPCollection:
        """Returns the interfaces provided by the port.

        Returns:
            An ``IRPCollection`` of provided interface classes.

        Raises:
            RhapsodyRuntimeException: if the provided interfaces cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::getProvidedInterfaces()
        """
        return IRPCollection(self.get_com_property(self._com, "providedInterfaces"))

    def add_provided_interface(self, new_val: IRPModelElement) -> None:
        """Adds a provided interface to the port.

        Args:
            new_val: The class (``IRPClass``) to add as a provided interface.

        Raises:
            RhapsodyRuntimeException: if the provided interface cannot be added.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::addProvidedInterface(com.telelogic.rhapsody.core.IRPClass newVal)
        """
        self.call_com(lambda: self._com.addProvidedInterface(new_val._com))

    def remove_provided_interface(self, new_val: IRPModelElement) -> None:
        """Removes a provided interface from the port.

        Args:
            new_val: The class (``IRPClass``) to remove from the provided interfaces.

        Raises:
            RhapsodyRuntimeException: if the provided interface cannot be removed.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::removeProvidedInterface(com.telelogic.rhapsody.core.IRPClass newVal)
        """
        self.call_com(lambda: self._com.removeProvidedInterface(new_val._com))

    @property
    def required_interfaces(self) -> IRPCollection:
        """Returns the interfaces required by the port.

        Returns:
            An ``IRPCollection`` of required interface classes.

        Raises:
            RhapsodyRuntimeException: if the required interfaces cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::getRequiredInterfaces()
        """
        return IRPCollection(self.get_com_property(self._com, "requiredInterfaces"))

    def add_required_interface(self, new_val: IRPModelElement) -> None:
        """Adds a required interface to the port.

        Args:
            new_val: The class (``IRPClass``) to add as a required interface.

        Raises:
            RhapsodyRuntimeException: if the required interface cannot be added.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::addRequiredInterface(com.telelogic.rhapsody.core.IRPClass newVal)
        """
        self.call_com(lambda: self._com.addRequiredInterface(new_val._com))

    def remove_required_interface(self, new_val: IRPModelElement) -> None:
        """Removes a required interface from the port.

        Args:
            new_val: The class (``IRPClass``) to remove from the required interfaces.

        Raises:
            RhapsodyRuntimeException: if the required interface cannot be removed.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::removeRequiredInterface(com.telelogic.rhapsody.core.IRPClass newVal)
        """
        self.call_com(lambda: self._com.removeRequiredInterface(new_val._com))

    def get_contract(self) -> IRPClass:
        """Return the port contract using the deprecated API name.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::getContract()
        """
        raise NotImplementedError("getContract is not exposed in the Rhapsody COM automation type library.")

    def set_contract(self, contract: IRPClass) -> None:
        """Set the port contract using the deprecated API name.

        Args:
            contract: The class to use as the port's contract.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPPort::setContract(com.telelogic.rhapsody.core.IRPClass contract)
        """
        raise NotImplementedError("setContract is not exposed in the Rhapsody COM automation type library.")


IRPModelElement.register_wrapper("Port", IRPPort)
