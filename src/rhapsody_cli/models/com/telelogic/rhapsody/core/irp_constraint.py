"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPConstraint``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


def _cast_constraint_dispatch(com_obj: object) -> object:
    """Cast generic pywin model-element dispatches to the constraint interface."""
    try:
        from win32com.client import CastTo, DispatchBaseClass
    except ImportError:
        return com_obj
    if isinstance(com_obj, DispatchBaseClass):
        return CastTo(com_obj, "IRPConstraint")
    return com_obj


class IRPConstraint(IRPModelElement):
    """Wraps ``IRPConstraint``: a constraint element.

    The JavaDoc ``getConstraintsByMe`` accessor is exposed by pywin32 as a
    read-only ``constraintsByMe`` property.
    """

    # IRPConstraint method parity checklist:
    # [x] constraints_by_me              [x] impl  [x] docstring  [x] unit test  [x] integration test (empty-state; populated collection remains blocked)
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)

    @property
    def constraints_by_me(self) -> IRPCollection:
        """Returns all model elements affected by this constraint.

        Returns:
            The affected elements as an ``IRPCollection``.

        Reference:
            com.telelogic.rhapsody.core.IRPConstraint::getConstraintsByMe()
        """
        constraint_com = _cast_constraint_dispatch(self._com)
        return IRPCollection(self.get_com_property(constraint_com, "constraintsByMe"))


IRPModelElement.register_wrapper("Constraint", IRPConstraint)
