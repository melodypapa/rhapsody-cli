import uuid
from typing import cast

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPActorIntegration:
    """Integration tests for IRPActor with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_is_behavior_overriden(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("BehPkg")
        actor_name = self._unique("BehActor")
        pkg = self._create_package(test_project, pkg_name)
        try:
            actor = pkg.add_actor(actor_name)
            assert actor.is_behavior_overriden is False
            actor.is_behavior_overriden = True
            assert actor.is_behavior_overriden is True
            actor.is_behavior_overriden = False
            assert actor.is_behavior_overriden is False
        finally:
            pkg.delete_from_project()

    def test_update_contained_diagrams_on_server_is_documented_unavailable(self, test_project: IRPProject) -> None:
        """JavaDoc declares updateContainedDiagramsOnServer(int), but the registered IRPActor typelib/catalog expose no member; the stub raises before dispatch."""
        package = self._create_package(test_project, self._unique("ActorDiagramServerPkg"))
        actor = package.add_actor(self._unique("ActorDiagramServer"))
        try:
            with pytest.raises(NotImplementedError):
                actor.update_contained_diagrams_on_server(0)
        finally:
            pkg.delete_from_project()

    def test_add_event_reception_with_event(self, test_project: IRPProject) -> None:
        """JavaDoc defines addEventReceptionWithEvent(name, event), but the IRPActor typelib/catalog expose no member; the stub raises before dispatch."""
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPEvent

        pkg_name = self._unique("ActorEvPkg")
        actor_name = self._unique("EvActor")
        event_name = self._unique("MyEvent")
        reception_name = self._unique("onMyEvent")
        pkg = self._create_package(test_project, pkg_name)
        try:
            actor = pkg.add_actor(actor_name)
            event = pkg.add_event(event_name)
            with pytest.raises(NotImplementedError, match="addEventReceptionWithEvent is not exposed by the registered pywin32 interface"):
                actor.add_event_reception_with_event(reception_name, cast(IRPEvent, event))
        finally:
            pkg.delete_from_project()
