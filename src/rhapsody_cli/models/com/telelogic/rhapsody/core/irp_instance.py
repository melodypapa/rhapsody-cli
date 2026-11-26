"""Wraps ``com.telelogic.rhapsody.core.IRPInstance``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_relation import IRPRelation

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation


class IRPInstance(IRPRelation):
    """Wraps ``IRPInstance``: represents an instance in the model."""

    # IRPInstance method parity checklist (typelib authority 2026-11-26):
    # [x] add_relation_to_the_whole        method            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_all_nested_elements          JavaDoc-only      NotImplementedError stub (documented_unavailable)  [x] unit test  [ ] integration test
    # [x] get_attribute_value              method            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_attribute_value              method            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_in_links                     method            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_out_links                    method            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] instantiated_by                  property (get/set) [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_list_of_initializer_arguments method           [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_explicit                     method            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_implicit                     method            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_initializer_argument_value   method            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] update_contained_diagrams_on_server JavaDoc-only   NotImplementedError stub (documented_unavailable)  [x] unit test  [ ] integration test
    # No deprecated methods in IRPInstance.

    def get_all_nested_elements(self) -> IRPCollection:
        """Returns a collection of all the model elements that are directly under the object.

        This method should be used instead of the inherited ``getNestedElements``
        method, because the latter does not return a complete list in the case
        of implicit objects.

        Raises:
            NotImplementedError: The Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::getAllNestedElements()
        """
        raise NotImplementedError("getAllNestedElements is not exposed in the Rhapsody COM automation type library.")

    def get_attribute_value(self, attribute_name: str) -> str:
        """Gets the value of an attribute on the instance.

        Args:
            attribute_name: The name of the attribute.

        Returns:
            The attribute value as a string.

        Raises:
            RhapsodyRuntimeException: if the attribute value cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::getAttributeValue(java.lang.String attName)
        """
        return self.call_com(lambda: str(self._com.getAttributeValue(attribute_name)))

    def set_attribute_value(self, attribute_name: str, attribute_value: str) -> None:
        """Sets the value of an attribute on the instance.

        Args:
            attribute_name: The name of the attribute.
            attribute_value: The new value to set.

        Raises:
            RhapsodyRuntimeException: if the attribute value cannot be set.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::setAttributeValue(java.lang.String attName, java.lang.String attValue)
        """
        self.call_com(lambda: self._com.setAttributeValue(attribute_name, attribute_value))

    def get_in_links(self) -> IRPCollection:
        """Returns all incoming links to this instance.

        Returns:
            An ``IRPCollection`` of incoming link elements.

        Raises:
            RhapsodyRuntimeException: if the incoming links cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::getInLinks()
        """
        return IRPCollection(self.call_com(lambda: self._com.getInLinks()))

    def get_out_links(self) -> IRPCollection:
        """Returns all outgoing links from this instance.

        Returns:
            An ``IRPCollection`` of outgoing link elements.

        Raises:
            RhapsodyRuntimeException: if the outgoing links cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::getOutLinks()
        """
        return IRPCollection(self.call_com(lambda: self._com.getOutLinks()))

    def add_relation_to_the_whole(self, rel_name: str) -> IRPRelation:
        """Adds a relation to the whole for this instance.

        Args:
            rel_name: The name of the relation to add.

        Returns:
            The wrapped ``IRPRelation`` created.

        Raises:
            RhapsodyRuntimeException: if the relation cannot be added.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::addRelationToTheWhole(java.lang.String relName)
        """
        return cast(IRPRelation, self.wrap(self.call_com(lambda: self._com.addRelationToTheWhole(rel_name))))

    @property
    def instantiated_by(self) -> IRPOperation:
        """The operation that instantiates this instance (``getInstantiatedBy`` / ``setInstantiatedBy``).

        Raises:
            RhapsodyRuntimeException: if the instantiating operation cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::getInstantiatedBy()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation

        return cast(IRPOperation, self.wrap(self.get_com_property(self._com, "instantiatedBy")))

    @instantiated_by.setter
    def instantiated_by(self, instantiated_by: IRPOperation) -> None:
        """Sets the operation that instantiates this instance.

        Args:
            instantiated_by: The operation (``IRPOperation``) that instantiates this instance.

        Raises:
            RhapsodyRuntimeException: if the instantiating operation cannot be set.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::setInstantiatedBy(com.telelogic.rhapsody.core.IRPOperation instantiatedBy)
        """
        self.set_com_property(self._com, "instantiatedBy", instantiated_by._com)

    def get_list_of_initializer_arguments(self) -> IRPCollection:
        """Returns the list of initializer arguments for this instance.

        Returns:
            An ``IRPCollection`` of initializer argument elements.

        Raises:
            RhapsodyRuntimeException: if the initializer arguments cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::getListOfInitializerArguments()
        """
        return IRPCollection(self.call_com(lambda: self._com.getListOfInitializerArguments()))

    def set_explicit(self) -> None:
        """Sets the instance to be explicit.

        Raises:
            RhapsodyRuntimeException: if the instance cannot be set explicit.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::setExplicit()
        """
        self.call_com(lambda: self._com.setExplicit())

    def set_implicit(self) -> None:
        """Sets the instance to be implicit.

        Raises:
            RhapsodyRuntimeException: if the instance cannot be set implicit.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::setImplicit()
        """
        self.call_com(lambda: self._com.setImplicit())

    def set_initializer_argument_value(self, arg_name: str, arg_value: str) -> None:
        """Sets the value of an initializer argument on the instance.

        Args:
            arg_name: The name of the initializer argument.
            arg_value: The new value to set.

        Raises:
            RhapsodyRuntimeException: if the initializer argument value cannot be set.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::setInitializerArgumentValue(java.lang.String argName, java.lang.String argValue)
        """
        self.call_com(lambda: self._com.setInitializerArgumentValue(arg_name, arg_value))

    def update_contained_diagrams_on_server(self, enforce_update: int) -> int:
        """Updates the views on the Rhapsody Model Manager server for all diagrams.

        Args:
            enforce_update: ``0`` to update only if changes were made,
                ``1`` to update regardless.

        Raises:
            NotImplementedError: The Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPInstance::updateContainedDiagramsOnServer(int enforceUpdate)
        """
        raise NotImplementedError("updateContainedDiagramsOnServer is not exposed in the Rhapsody COM automation type library.")


IRPModelElement.register_wrapper("Instance", IRPInstance)
# Also register "Object" metaClass (used in live Rhapsody for instance elements)
# See: https://github.com/melodypapa/rhapsody-cli/issues/96
IRPModelElement.register_wrapper("Object", IRPInstance)
