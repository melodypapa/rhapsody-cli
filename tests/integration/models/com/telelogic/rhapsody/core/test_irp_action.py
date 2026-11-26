"""Integration tests for IRPAction with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_action import IRPAction
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPActionIntegration:
    """Integration tests for IRPAction with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _action(pkg: IRPPackage) -> tuple[IRPPackage, IRPAction]:
        owner = pkg.add_class(pkg.name + "_Owner")
        statechart = owner.add_statechart()
        root = statechart.root_state
        assert root is not None
        source = root.add_state(f"Source_{uuid.uuid4().hex[:8]}")
        target = root.add_state(f"Target_{uuid.uuid4().hex[:8]}")
        transition = source.add_transition(target)
        action = transition.set_its_action("doSomething();")
        assert isinstance(action, IRPAction)
        return pkg, action

    def test_body(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ActionPkg"))
        try:
            _, action = self._action(pkg)
            assert action.body == "doSomething();"
        finally:
            pkg.delete_from_project()

    def test_body_setter(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ActionSetterPkg"))
        try:
            _, action = self._action(pkg)
            updated = "doOther();"
            action.body = updated
            assert action.body == updated
        finally:
            pkg.delete_from_project()
