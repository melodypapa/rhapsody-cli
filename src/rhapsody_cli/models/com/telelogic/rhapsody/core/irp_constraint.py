"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPConstraint``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPConstraint(IRPModelElement):
    """Wraps ``IRPConstraint``: a constraint element.

    The JavaDoc ``getConstraintsByMe`` accessor is exposed by pywin32 as a
    read-only ``constraintsByMe`` property.
    """

    # IRPConstraint method parity checklist:
    # [x] constraints_by_me              [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)

    @property
    def constraints_by_me(self) -> IRPCollection:
        """Returns all model elements affected by this constraint.

        Returns:
            The affected elements as an ``IRPCollection``.

        Reference:
            com.telelogic.rhapsody.core.IRPConstraint::getConstraintsByMe()
        """
        return IRPCollection(self.get_com_property(self._com, "constraintsByMe"))


IRPModelElement.register_wrapper("Constraint", IRPConstraint)
