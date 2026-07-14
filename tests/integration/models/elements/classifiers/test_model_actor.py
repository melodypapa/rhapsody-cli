import uuid

import pytest

from rhapsody_cli.models.elements.classifiers import RPActor
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPActorIntegration:
    """Integration tests for RPActor with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_create_actor_in_package(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ActorPkg")
        actor_name = self._unique("TestActor")
        pkg = self._create_package(test_project, pkg_name)
        try:
            actor = pkg.add_actor(actor_name)
            assert actor is not None
            assert isinstance(actor, RPActor)
            assert actor.get_name() == actor_name
            assert actor.get_meta_class() == "Actor"
            actors = pkg.get_actors()
            assert actor in list(actors)
        finally:
            actor.delete_from_project()

    def test_actor_behavior_override(self, test_project: RPProject) -> None:
        pkg_name = self._unique("BehPkg")
        actor_name = self._unique("BehActor")
        pkg = self._create_package(test_project, pkg_name)
        try:
            actor = pkg.add_actor(actor_name)
            assert actor.get_is_behavior_overriden() is False
            actor.set_is_behavior_overriden(True)
            assert actor.get_is_behavior_overriden() is True
            actor.set_is_behavior_overriden(False)
            assert actor.get_is_behavior_overriden() is False
        finally:
            actor.delete_from_project()

    def test_actor_owner(self, test_project: RPProject) -> None:
        pkg_name = self._unique("OwnPkg")
        actor_name = self._unique("OwnActor")
        pkg = self._create_package(test_project, pkg_name)
        try:
            actor = pkg.add_actor(actor_name)
            owner = actor.get_owner()
            assert owner is not None
            assert owner.get_name() == pkg_name
            assert isinstance(owner, RPPackage)
        finally:
            actor.delete_from_project()
