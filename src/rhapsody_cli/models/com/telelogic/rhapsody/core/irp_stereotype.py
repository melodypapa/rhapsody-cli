"""Wraps ``com.telelogic.rhapsody.core.IRPStereotype``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPStereotype(IRPClassifier):
    """Represents a stereotype in a Rhapsody model."""

    # JavaDoc-owned method parity: add/remove metaclass and three pywin32
    # properties. IRPClassifier, IRPUnit and IRPModelElement members are inherited.

    def add_meta_class(self, meta_class: str) -> None:
        """Adds one metaclass to the stereotype's applicable metaclasses.

        Args:
            meta_class: Name of the metaclass to add. Add multiple metaclasses
                with separate calls.

        Reference:
            com.telelogic.rhapsody.core.IRPStereotype::addMetaClass(java.lang.String metaClass)
        """
        self.call_com(lambda: self._com.addMetaClass(meta_class))

    @property
    def icon(self) -> str:
        """Returns the full path of the image file associated with this stereotype.

        Reference:
            com.telelogic.rhapsody.core.IRPStereotype::getIcon()
        """
        return str(self.get_com_property(self._com, "icon"))

    @property
    def is_new_term(self) -> int:
        """Indicates whether this stereotype is a new-term stereotype.

        Returns:
            ``1`` if this is a new-term stereotype, otherwise ``0``.

        Reference:
            com.telelogic.rhapsody.core.IRPStereotype::getIsNewTerm()
        """
        return int(self.get_com_property(self._com, "isNewTerm"))

    @is_new_term.setter
    def is_new_term(self, is_new_term: int) -> None:
        """Sets whether this stereotype is a new-term stereotype.

        Args:
            is_new_term: ``1`` to mark it as a new-term stereotype; ``0`` to
                make it an ordinary stereotype.

        Reference:
            com.telelogic.rhapsody.core.IRPStereotype::setIsNewTerm(int isNewTerm)
        """
        self.set_com_property(self._com, "isNewTerm", is_new_term)

    @property
    def of_meta_class(self) -> str:
        """Returns the applicable metaclass names as a comma-separated string.

        Reference:
            com.telelogic.rhapsody.core.IRPStereotype::getOfMetaClass()
        """
        return str(self.get_com_property(self._com, "ofMetaClass"))

    def remove_meta_class(self, meta_class: str) -> None:
        """Removes one metaclass from the stereotype's applicable metaclasses.

        Args:
            meta_class: Name of the metaclass to remove. Remove multiple
                metaclasses with separate calls.

        Reference:
            com.telelogic.rhapsody.core.IRPStereotype::removeMetaClass(java.lang.String metaClass)
        """
        self.call_com(lambda: self._com.removeMetaClass(meta_class))


IRPModelElement.register_wrapper("Stereotype", IRPStereotype)
