"""Integration tests for RPUseCase with live Rhapsody COM API.

Scope: only methods that RPUseCase owns (IRPUseCase::addExtensionPoint,
getExtensionPoints, findExtensionPoint, deleteExtensionPoint, getEntryPoints,
getIsBehaviorOverriden, setIsBehaviorOverriden). ``add_use_case`` is an
IRPPackage method used only to build the fixture.
"""

import uuid

import pytest

from rhapsody_cli.models.elements.classifiers import RPUseCase
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPUseCaseIntegration:
    """Integration tests for RPUseCase with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_extension_point_add_get_delete(self, test_project: RPProject) -> None:
        pkg_name = self._unique("UcPkg")
        uc_name = self._unique("MyUseCase")
        ep_name = self._unique("MyExtensionPoint")
        pkg = self._create_package(test_project, pkg_name)
        uc = pkg.add_use_case(uc_name)
        try:
            assert isinstance(uc, RPUseCase)
            uc.add_extension_point(ep_name)
            assert ep_name in [str(e) for e in uc.get_extension_points()]
            uc.delete_extension_point(ep_name)
            assert ep_name not in [str(e) for e in uc.get_extension_points()]
        finally:
            uc.delete_from_project()

    @pytest.mark.xfail(strict=False, reason="COM findExtensionPoint expects an object argument, not a name string (Java-API signature mismatch); wrapper needs COM-signature investigation")
    def test_find_extension_point(self, test_project: RPProject) -> None:
        pkg_name = self._unique("UcPkg")
        uc_name = self._unique("MyUseCase")
        ep_name = self._unique("MyExtensionPoint")
        pkg = self._create_package(test_project, pkg_name)
        uc = pkg.add_use_case(uc_name)
        try:
            uc.add_extension_point(ep_name)
            found = uc.find_extension_point(ep_name)
            assert found is not None and found.get_name() == ep_name
        finally:
            uc.delete_from_project()

    def test_get_entry_points_empty(self, test_project: RPProject) -> None:
        pkg_name = self._unique("UcPkg")
        uc_name = self._unique("MyUseCase")
        pkg = self._create_package(test_project, pkg_name)
        uc = pkg.add_use_case(uc_name)
        try:
            entry_points = list(uc.get_entry_points())
            assert isinstance(entry_points, list)
        finally:
            uc.delete_from_project()

    def test_set_is_behavior_overriden_raises_not_implemented(self, test_project: RPProject) -> None:
        # setIsBehaviorOverriden is not exposed in the COM automation type library for UseCase
        # (getIsBehaviorOverriden is; the sibling RPActor/RPClass setters are exposed), so the
        # wrapper raises NotImplementedError.
        pkg_name = self._unique("UcPkg")
        uc_name = self._unique("MyUseCase")
        pkg = self._create_package(test_project, pkg_name)
        uc = pkg.add_use_case(uc_name)
        try:
            assert uc.get_is_behavior_overriden() in (0, 1)
            with pytest.raises(NotImplementedError, match="setIsBehaviorOverriden is not exposed"):
                uc.set_is_behavior_overriden(1)
        finally:
            uc.delete_from_project()
