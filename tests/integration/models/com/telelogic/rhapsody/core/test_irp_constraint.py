"""Integration tests for IRPConstraint with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_constraint import IRPConstraint
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPConstraintIntegration:
    """Integration tests for IRPConstraint with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_constraints_by_me_empty_state(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ConstraintPkg"))
        try:
            element = pkg.add_new_aggr("Constraint", self._unique("Constraint"))
            constraint = IRPConstraint(element._com)
            assert isinstance(constraint, IRPConstraint)
            # JavaDoc exposes only getConstraintsByMe; no documented API attaches
            # a constrained element. Tracked as a P0 blocker in the sync ledger.
            assert len(list(constraint.constraints_by_me)) == 0
        finally:
            pkg.delete_from_project()
