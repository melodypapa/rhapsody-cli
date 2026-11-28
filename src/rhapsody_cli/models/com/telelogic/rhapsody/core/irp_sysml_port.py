"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPSysMLPort``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPLink
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_relation import IRPRelation


class IRPSysMLPort(IRPInstance):
    """Wraps ``IRPSysMLPort``: a flowport in a Rhapsody model.

    The JavaDoc accessor pairs are exposed by pywin32 as read/write properties;
    ``add_link`` remains a method.
    """

    # IRPSysMLPort method parity checklist:
    # [x] is_reversed                   [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] port_direction                [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] type                          [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_link                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_instance methods (covered by irp_instance checklist)
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)
    # [inherited] irp_relation methods (covered by irp_relation checklist)
    # [inherited] irp_unit methods (covered by irp_unit checklist)

    @property
    def is_reversed(self) -> int:
        """Checks whether the flowport is conjugated.

        Returns:
            1 if conjugated, 0 otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::getIsReversed()
        """
        return int(self.get_com_property(self._com, "isReversed"))

    @is_reversed.setter
    def is_reversed(self, is_reversed: int) -> None:
        """Specifies whether the flowport should be conjugated.

        Args:
            is_reversed: 1 to conjugate the flowport, 0 otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::setIsReversed(int isReversed)
        """
        self.set_com_property(self._com, "isReversed", is_reversed)

    @property
    def port_direction(self) -> str:
        """Returns the flowport direction.

        Returns:
            One of ``"In"``, ``"Out"``, or ``"InOut"``.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::getPortDirection()
        """
        return str(self.get_com_property(self._com, "portDirection"))

    @port_direction.setter
    def port_direction(self, port_direction: str) -> None:
        """Sets the flowport direction.

        Args:
            port_direction: One of ``"In"``, ``"Out"``, or ``"InOut"``.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::setPortDirection(java.lang.String portDirection)
        """
        self.set_com_property(self._com, "portDirection", port_direction)

    @property
    def type(self) -> IRPClassifier | None:
        """Returns the type specified for the flowport.

        Returns:
            The flowport type, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::getType()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier

        return cast(IRPClassifier, self.wrap(self.get_com_property(self._com, "type")))

    @type.setter
    def type(self, type_: IRPClassifier) -> None:
        """Sets the type of the flowport.

        Args:
            type_: The classifier to use as the flowport type.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::setType(com.telelogic.rhapsody.core.IRPClassifier type)
        """
        self.set_com_property(self._com, "type", type_._com)

    def add_link(self, from_part: IRPInstance, to_part: IRPInstance, assoc: IRPRelation | None, to_port: IRPSysMLPort, new_owner: IRPPackage) -> IRPLink:
        """Creates a link between flowports on two parts.

        Args:
            from_part: The "from" part for the link.
            to_part: The "to" part for the link.
            assoc: Pass ``None``; JavaDoc says the association is irrelevant
                for links between flowports.
            to_port: The "to" port for the link.
            new_owner: The package that should own the created link.

        Returns:
            The link that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::addLink(
                com.telelogic.rhapsody.core.IRPInstance fromPart,
                com.telelogic.rhapsody.core.IRPInstance toPart,
                com.telelogic.rhapsody.core.IRPRelation assoc,
                com.telelogic.rhapsody.core.IRPSysMLPort toPort,
                com.telelogic.rhapsody.core.IRPPackage newOwner)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPLink

        assoc_com = assoc._com if assoc is not None else None
        return cast(IRPLink, self.wrap(self.call_com(lambda: self._com.addLink(from_part._com, to_part._com, assoc_com, to_port._com, new_owner._com))))


IRPModelElement.register_wrapper("SysMLPort", IRPSysMLPort)
