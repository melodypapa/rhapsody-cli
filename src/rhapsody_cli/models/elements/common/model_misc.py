"""Miscellaneous model element wrappers — RPComment, RPConstraint, RPEnumerationLiteral."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class RPEnumerationLiteral(IRPModelElement):
    """Wraps ``IRPEnumerationLiteral``: a literal value in an enumeration."""

    # IRPEnumerationLiteral method parity checklist:
    # [x] get_value  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_value  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklists)
    # No deprecated IRPEnumerationLiteral methods.

    def get_value(self) -> str:
        """Returns the value of the enumeration literal.

        Returns:
            The enumeration literal value as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPEnumerationLiteral::getValue()
        """
        return str(self._get_method_or_property(self._com, "getValue", "value"))

    def set_value(self, value: str) -> None:
        """Sets the value of the enumeration literal.

        Args:
            value: The value to set.

        Reference:
            com.telelogic.rhapsody.core.IRPEnumerationLiteral::setValue(java.lang.String value)
        """
        self.call_com(lambda: self._com.setValue(value))


IRPModelElement.register_wrapper("EnumerationLiteral", RPEnumerationLiteral)


class RPComment(IRPModelElement):
    """Wraps ``IRPComment``: a free-text comment element."""

    # IRPComment method parity checklist:
    # [inherited] irp_model_element methods (covered by rp_model_element checklists)
    # No deprecated IRPComment methods.

    pass


IRPModelElement.register_wrapper("Comment", RPComment)


class RPConstraint(IRPModelElement):
    """Wraps ``IRPConstraint``: a constraint element."""

    # IRPConstraint method parity checklist:
    # [x] get_constraints_by_me  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklists)
    # No deprecated IRPConstraint methods.

    def get_constraints_by_me(self) -> IRPCollection:
        """Returns the collection of elements constrained by this constraint.

        Returns:
            An ``IRPCollection`` of model elements constrained by this constraint.

        Reference:
            com.telelogic.rhapsody.core.IRPConstraint::getConstraintsByMe()
        """
        return IRPCollection(self._get_method_or_property(self._com, "getConstraintsByMe", "constraintsByMe"))


IRPModelElement.register_wrapper("Constraint", RPConstraint)
