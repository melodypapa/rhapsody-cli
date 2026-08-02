"""Wraps ``com.telelogic.rhapsody.core.IRPStereotype``."""

from typing import TYPE_CHECKING

from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.classifiers.model_classifier import RPClassifier

if TYPE_CHECKING:
    pass


class RPStereotype(RPClassifier):
    """Wraps ``IRPStereotype``: a stereotype that extends ``IRPClassifier``."""

    # IRPStereotype method parity checklist:
    # [ ] add_meta_class  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_icon  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_is_new_term  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_of_meta_class  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] remove_meta_class  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] set_is_new_term (unimplemented -- raises NotImplementedError; getter works via COM)  [ ] impl  [x] docstring  [x] unit test  [x] integration test
    # [inherited] irp_classifier / irp_unit / irp_model_element methods (covered by rp_classifier / rp_unit / rp_model_element checklists)
    # No deprecated IRPStereotype methods.

    def add_meta_class(self, meta_class: str) -> None:
        """Adds a metaclass to the stereotype's applicable metaclasses.

        Args:
            meta_class: The metaclass name to add (e.g., 'Class', 'Attribute').

        Reference:
            com.telelogic.rhapsody.core.IRPStereotype::addMetaClass(java.lang.String metaClass)
        """
        AbstractRPModelElement.call_com(lambda: self._com.addMetaClass(meta_class))

    def get_icon(self) -> str:
        """Returns the path to the icon file used for this stereotype.

        Returns:
            The path to the icon file as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPStereotype::getIcon()
        """
        return str(AbstractRPModelElement._get_method_or_property(self._com, "getIcon", "icon"))

    def get_is_new_term(self) -> int:
        """Checks whether this stereotype is marked as a "new term".

        Returns:
            ``1`` if this is a new term stereotype, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPStereotype::getIsNewTerm()
        """
        return int(AbstractRPModelElement._get_method_or_property(self._com, "getIsNewTerm", "isNewTerm"))

    def get_of_meta_class(self) -> str:
        """Returns the names of the metaclasses that the stereotype can be applied to.

        Returns:
            The metaclass names as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPStereotype::getOfMetaClass()
        """
        return str(AbstractRPModelElement._get_method_or_property(self._com, "getOfMetaClass", "ofMetaClass"))

    def remove_meta_class(self, meta_class: str) -> None:
        """Removes a metaclass from the stereotype's applicable metaclasses.

        Args:
            meta_class: The metaclass name to remove.

        Reference:
            com.telelogic.rhapsody.core.IRPStereotype::removeMetaClass(java.lang.String metaClass)
        """
        AbstractRPModelElement.call_com(lambda: self._com.removeMetaClass(meta_class))

    def set_is_new_term(self, is_new_term: int) -> None:
        """Sets whether this stereotype is marked as a "new term".

        Args:
            is_new_term: ``1`` to mark as new term, ``0`` otherwise.

        Raises:
            NotImplementedError: Always. Under Rhapsody2.Application.1 the
                ``setIsNewTerm`` method is not exposed in the COM automation
                type library for stereotypes (the getter ``getIsNewTerm`` is
                exposed and works). Marked unimplemented rather than failing
                with a raw COM ``AttributeError`` at runtime.

        Reference:
            com.telelogic.rhapsody.core.IRPStereotype::setIsNewTerm(int isNewTerm)
        """
        raise NotImplementedError(
            "RPStereotype.set_is_new_term is unimplemented: setIsNewTerm is not exposed in the " "Rhapsody COM automation type library (get_is_new_term works). See docstring for details."
        )


AbstractRPModelElement.register_wrapper("Stereotype", RPStereotype)
