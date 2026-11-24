"""Wrappers for ``com.telelogic.rhapsody.core.IRPAssociationClass``.

Canonical module for :class:`IRPAssociationClass`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_association_class.md``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from rhapsody_cli.models.elements.relations.model_relation import RPRelation

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPAssociationClass(IRPClass):
    """Wraps ``IRPAssociationClass``: an association class that extends ``IRPClass``."""

    # IRPAssociationClass method parity checklist:
    # [x] end1  [x] impl  [x] docstring  [ ] unit test  [x] integration test
    # [x] end2  [x] impl  [x] docstring  [ ] unit test  [x] integration test
    # [x] is_class  [x] impl  [x] docstring  [ ] unit test  [x] integration test
    # [inherited] irp_class / irp_classifier / irp_unit / irp_model_element methods (covered by rp_class / rp_classifier / rp_unit / rp_model_element checklists)
    # No deprecated IRPAssociationClass methods.

    @property
    def end1(self) -> RPRelation:
        """Returns the first end of the association.

        Returns:
            The wrapped relation representing the first end.

        Reference:
            com.telelogic.rhapsody.core.IRPAssociationClass::getEnd1()
        """
        from rhapsody_cli.models.elements.relations.model_relation import RPRelation

        return cast(RPRelation, self.wrap(self.get_com_property(self._com, "end1")))

    @property
    def end2(self) -> RPRelation:
        """Returns the second end of the association.

        Returns:
            The wrapped relation representing the second end.

        Reference:
            com.telelogic.rhapsody.core.IRPAssociationClass::getEnd2()
        """
        from rhapsody_cli.models.elements.relations.model_relation import RPRelation

        return cast(RPRelation, self.wrap(self.get_com_property(self._com, "end2")))

    @property
    def is_class(self) -> int:
        """Checks whether this association class is also a class.

        Returns:
            ``1`` if this is also a class, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAssociationClass::getIsClass()
        """
        return int(self.get_com_property(self._com, "isClass"))

    @is_class.setter
    def is_class(self, is_class: int) -> None:
        """Sets whether this association class is also a class.

        Args:
            is_class: ``1`` to mark as a class, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAssociationClass::setIsClass(int isClass)
        """
        self.set_com_property(self._com, "isClass", is_class)


IRPModelElement.register_wrapper("AssociationClass", IRPAssociationClass)
