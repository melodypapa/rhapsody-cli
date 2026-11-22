"""Wrappers for ``com.telelogic.rhapsody.core.IRPInterfaceItem``.

Canonical module for :class:`IRPInterfaceItem`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_interface_item.md``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.core import AbstractRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_argument import IRPArgument


class IRPInterfaceItem(IRPClassifier):
    """Wraps ``IRPInterfaceItem``: the base interface for operation-like
    elements that carry an argument list and signature (e.g. operations,
    triggers).
    """

    # IRPInterfaceItem method parity checklist:
    # [x] add_argument  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_argument_before_position  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_arguments  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_signature  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_signature_no_arg_names  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_signature_no_arg_types  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] match_on_signature  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [inherited] irp_classifier / irp_unit / irp_model_element methods (covered by rp_classifier / rp_unit / rp_model_element checklists)
    # No deprecated IRPInterfaceItem methods.

    def add_argument(self, new_val: str) -> IRPArgument:
        """Adds a new argument to the end of the argument list.

        Only the name is taken from the supplied string; the argument's type
        defaults to ``int``. To change the type, use the returned
        ``IRPArgument`` object's type setter.

        Args:
            new_val: The name to use for the new argument.

        Returns:
            The wrapped ``IRPArgument`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPInterfaceItem::addArgument(java.lang.String newVal)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_argument import IRPArgument

        return cast(IRPArgument, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.addArgument(new_val))))

    def add_argument_before_position(self, new_val: str, pos: int) -> IRPArgument:
        """Adds a new argument at the specified position in the argument list.

        As with :meth:`add_argument`, only the name is taken from the supplied
        string and the argument's type defaults to ``int``; change the type via
        the returned ``IRPArgument`` object's type setter.

        Args:
            new_val: The name to use for the new argument.
            pos: The 1-based position at which to insert the new argument.

        Returns:
            The wrapped ``IRPArgument`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPInterfaceItem::addArgumentBeforePosition(java.lang.String newVal, int pos)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_argument import IRPArgument

        return cast(IRPArgument, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.addArgumentBeforePosition(new_val, pos))))

    def get_arguments(self) -> IRPCollection:
        """Returns all the arguments for the operation.

        Returns:
            An ``IRPCollection`` of ``IRPArgument`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPInterfaceItem::getArguments()
        """
        return IRPCollection(AbstractRPModelElement.get_com_property(self._com, "arguments"))

    def get_signature(self) -> str:
        """Returns the signature of the operation.

        Returns:
            The full signature string, including argument names and types.

        Reference:
            com.telelogic.rhapsody.core.IRPInterfaceItem::getSignature()
        """
        return str(AbstractRPModelElement.get_com_property(self._com, "signature"))

    def get_signature_no_arg_names(self) -> str:
        """Returns the signature of the operation without the argument names.

        Returns:
            The signature string with argument types but no argument names.

        Reference:
            com.telelogic.rhapsody.core.IRPInterfaceItem::getSignatureNoArgNames()
        """
        return str(AbstractRPModelElement.call_com(lambda: self._com.getSignatureNoArgNames()))

    def get_signature_no_arg_types(self) -> str:
        """Returns the signature of the operation without the argument types.

        Returns:
            The signature string with argument names but no argument types.

        Reference:
            com.telelogic.rhapsody.core.IRPInterfaceItem::getSignatureNoArgTypes()
        """
        return str(AbstractRPModelElement.call_com(lambda: self._com.getSignatureNoArgTypes()))

    def match_on_signature(self, item: IRPInterfaceItem) -> bool:
        """Compares the signature of this operation with another operation's signature.

        This is useful when moving an operation from one class to another,
        because Rhapsody raises an exception if an operation with an identical
        signature already exists in the target class.

        Args:
            item: The other interface item to compare signatures with.

        Returns:
            ``True`` if the signatures match, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPInterfaceItem::matchOnSignature(com.telelogic.rhapsody.core.IRPInterfaceItem Item)
        """
        return bool(AbstractRPModelElement.call_com(lambda: self._com.matchOnSignature(item._com)))


AbstractRPModelElement.register_wrapper("InterfaceItem", IRPInterfaceItem)
