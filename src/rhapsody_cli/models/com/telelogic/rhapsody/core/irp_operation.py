"""Wrappers for ``com.telelogic.rhapsody.core.IRPOperation``.

Canonical module for :class:`IRPOperation`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_operation.md``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_argument import IRPArgument
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flowchart import IRPFlowchart


class IRPOperation(IRPInterfaceItem):
    """Wraps ``IRPOperation``: represents an operation or method in a classifier."""

    # IRPOperation method parity checklist:
    # [x] body  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] create_auto_flow_chart  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] delete_argument  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_flowchart  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] flowchart  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_implementation_signature  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_return_type_declaration  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [ ] initializer  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] is_abstract  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [ ] is_cg_derived  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] is_const  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] is_ctor  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] is_dtor  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] is_final  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] is_inline  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] is_static  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [ ] is_trigger  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] is_virtual  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] returns  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_return_type_declaration  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [ ] update_contained_diagrams_on_server  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] visibility  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [inherited] irp_interface_item / irp_classifier / irp_unit / irp_model_element methods (covered by rp_interface_item / rp_classifier / rp_unit / rp_model_element checklists)
    # No deprecated IRPOperation methods.

    @property
    def body(self) -> str:
        """Returns the body/implementation of the operation.

        Returns:
            The operation's body code as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getBody()
        """
        return str(self.get_com_property(self._com, "body"))

    @body.setter
    def body(self, body: str) -> None:
        """Sets the body/implementation of the operation.

        Args:
            body: The body code to set.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::setBody(java.lang.String body)
        """
        self.set_com_property(self._com, "body", body)

    @property
    def is_abstract(self) -> bool:
        """Checks whether this operation is abstract.

        Returns:
            ``True`` if the operation is abstract, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getIsAbstract()
        """
        return bool(self.get_com_property(self._com, "isAbstract"))

    @is_abstract.setter
    def is_abstract(self, is_abstract: int) -> None:
        """Sets whether this operation is abstract.

        Args:
            is_abstract: ``1`` to mark the operation as abstract, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::setIsAbstract(boolean isAbstract)
        """
        self.set_com_property(self._com, "isAbstract", is_abstract)

    @property
    def is_static(self) -> bool:
        """Checks whether this operation is static.

        Returns:
            ``True`` if the operation is static, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getIsStatic()
        """
        return bool(self.get_com_property(self._com, "isStatic"))

    @is_static.setter
    def is_static(self, is_static: int) -> None:
        """Sets whether this operation is static.

        Args:
            is_static: ``1`` to mark the operation as static, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::setIsStatic(boolean isStatic)
        """
        self.set_com_property(self._com, "isStatic", is_static)

    @property
    def is_virtual(self) -> bool:
        """Checks whether this operation is virtual (for C++ or C# classes).

        Returns:
            ``True`` if the operation is virtual, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getIsVirtual()
        """
        return bool(self.get_com_property(self._com, "isVirtual"))

    @is_virtual.setter
    def is_virtual(self, is_virtual: int) -> None:
        """Sets whether this operation is virtual (for C++ or C# classes).

        Args:
            is_virtual: ``1`` to mark the operation as virtual, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::setIsVirtual(boolean isVirtual)
        """
        self.set_com_property(self._com, "isVirtual", is_virtual)

    @property
    def returns(self) -> IRPClassifier:
        """Returns the type specification for the operation's return value.

        Returns:
            The wrapped return type element.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getReturns()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier

        return cast(IRPClassifier, self.wrap(self.get_com_property(self._com, "returns")))

    @returns.setter
    def returns(self, returns: IRPClassifier) -> None:
        """Sets the return type of the operation to an existing classifier.

        Args:
            returns: The wrapped ``IRPClassifier`` to use as the return type.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::setReturns(com.telelogic.rhapsody.core.IRPClassifier returns)
        """
        self.set_com_property(self._com, "returns", returns._com)

    def get_return_type_declaration(self) -> str:
        """Returns the on-the-fly return type declaration for the operation.

        Returns:
            The return type declaration as a string (e.g. ``"int"``).

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getReturnTypeDeclaration()
        """
        return str(self.call_com(lambda: self._com.getReturnTypeDeclaration()))

    def create_auto_flow_chart(self) -> None:
        """Automatically generates a flowchart for the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::createAutoFlowChart()
        """
        self.call_com(lambda: self._com.createAutoFlowChart())

    def set_return_type_declaration(self, new_val: str) -> None:
        """Specifies an on-the-fly return type declaration for the operation.

        Args:
            new_val: The on-the-fly type declaration (e.g. ``"int"``), reusing
                a matching existing type if found.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::setReturnTypeDeclaration(java.lang.String newVal)
        """
        self.call_com(lambda: self._com.setReturnTypeDeclaration(new_val))

    def delete_argument(self, argument: IRPArgument) -> None:
        """Deletes the specified argument from the operation.

        Args:
            argument: The wrapped argument to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::deleteArgument(com.telelogic.rhapsody.core.IRPArgument argument)
        """
        self.call_com(lambda: self._com.deleteArgument(argument._com))

    def delete_flowchart(self) -> None:
        """Deletes the flowchart associated with the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::deleteFlowchart()
        """
        self.call_com(lambda: self._com.deleteFlowchart())

    @property
    def flowchart(self) -> IRPFlowchart:
        """Returns the flowchart associated with the operation.

        Returns:
            The wrapped flowchart representing the operation's flowchart.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getFlowchart()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flowchart import IRPFlowchart

        return cast(IRPFlowchart, self.wrap(self.get_com_property(self._com, "flowchart")))

    @flowchart.setter
    def flowchart(self, flowchart: IRPFlowchart) -> None:
        """Sets the flowchart associated with the operation.

        Args:
            flowchart: The wrapped activity diagram to set as the flowchart.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::setFlowchart(com.telelogic.rhapsody.core.IRPActivityDiagram flowchart)
        """
        self.set_com_property(self._com, "flowchart", flowchart._com)

    def get_implementation_signature(self) -> str:
        """Returns the implementation signature of the operation.

        Returns:
            The implementation signature as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getImplementationSignature()
        """
        return str(self.call_com(lambda: self._com.getImplementationSignature()))

    @property
    def initializer(self) -> str:
        """Returns the initializer for the operation.

        Returns:
            The initializer as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getInitializer()
        """
        return str(self.get_com_property(self._com, "initializer"))

    @initializer.setter
    def initializer(self, initializer: str) -> None:
        """Sets the initializer for the operation.

        Args:
            initializer: The initializer string to set.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::setInitializer(java.lang.String initializer)
        """
        self.set_com_property(self._com, "initializer", initializer)

    @property
    def is_cg_derived(self) -> int:
        """Checks whether the operation's code is derived from code generation.

        Returns:
            ``1`` if the operation is code-generated derived, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getIsCgDerived()
        """
        return int(self.get_com_property(self._com, "isCgDerived"))

    @property
    def is_const(self) -> int:
        """Checks whether the operation is const (C++).

        Returns:
            ``1`` if the operation is const, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getIsConst()
        """
        return int(self.get_com_property(self._com, "isConst"))

    @is_const.setter
    def is_const(self, is_const: int) -> None:
        """Sets whether the operation is const (C++).

        Args:
            is_const: ``1`` to mark the operation as const, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::setIsConst(int isConst)
        """
        self.set_com_property(self._com, "isConst", is_const)

    @property
    def is_ctor(self) -> int:
        """Checks whether the operation is a constructor.

        Returns:
            ``1`` if the operation is a constructor, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getIsCtor()
        """
        return int(self.get_com_property(self._com, "isCtor"))

    @property
    def is_dtor(self) -> int:
        """Checks whether the operation is a destructor.

        Returns:
            ``1`` if the operation is a destructor, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getIsDtor()
        """
        return int(self.get_com_property(self._com, "isDtor"))

    @property
    def is_final(self) -> int:
        """Checks whether the operation is final.

        Returns:
            ``1`` if the operation is final, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getIsFinal()
        """
        return int(self.get_com_property(self._com, "isFinal"))

    @is_final.setter
    def is_final(self, is_final: int) -> None:
        """Sets whether the operation is final.

        Args:
            is_final: ``1`` to mark the operation as final, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::setIsFinal(int isFinal)
        """
        self.set_com_property(self._com, "isFinal", is_final)

    @property
    def is_inline(self) -> int:
        """Checks whether the operation is inline.

        Returns:
            ``1`` if the operation is inline, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getIsInline()
        """
        return int(self.get_com_property(self._com, "isInline"))

    @property
    def is_trigger(self) -> int:
        """Checks whether the operation is used as a trigger.

        Returns:
            ``1`` if the operation is a trigger, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getIsTrigger()
        """
        return int(self.get_com_property(self._com, "isTrigger"))

    @property
    def visibility(self) -> str:
        """Returns the visibility of the operation.

        Returns:
            The visibility string (e.g. ``"public"``, ``"private"``).

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::getVisibility()
        """
        return str(self.get_com_property(self._com, "visibility"))

    @visibility.setter
    def visibility(self, visibility: str) -> None:
        """Sets the visibility of the operation.

        Args:
            visibility: The visibility string to set (e.g. ``"public"``, ``"private"``).

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::setVisibility(java.lang.String visibility)
        """
        self.set_com_property(self._com, "visibility", visibility)

    def update_contained_diagrams_on_server(self, enforce_update: int) -> int:
        """Updates the contained diagrams on the server.

        Args:
            enforce_update: Whether to update views regardless of recent changes.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPOperation::updateContainedDiagramsOnServer(int enforceUpdate)
        """
        raise NotImplementedError("updateContainedDiagramsOnServer is not exposed in the Rhapsody COM automation type library.")


IRPModelElement.register_wrapper("Operation", IRPOperation)
