"""Miscellaneous model element wrappers — IRPComment, IRPConstraint."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPComment(IRPModelElement):
    """Wraps ``IRPComment``: a free-text comment element."""

    # IRPComment method parity checklist:
    # [inherited] irp_model_element methods (covered by rp_model_element checklists)
    # No deprecated IRPComment methods.

    pass


IRPModelElement.register_wrapper("Comment", IRPComment)


class IRPConstraint(IRPModelElement):
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


IRPModelElement.register_wrapper("Constraint", IRPConstraint)
