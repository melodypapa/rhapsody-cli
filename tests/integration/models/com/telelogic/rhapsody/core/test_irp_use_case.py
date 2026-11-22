"""Integration tests for IRPUseCase with live Rhapsody COM API.

Scope: only methods that IRPUseCase owns (IRPUseCase::addExtensionPoint,
getExtensionPoints, findExtensionPoint, deleteExtensionPoint, getEntryPoints,
getIsBehaviorOverriden, setIsBehaviorOverriden). ``add_use_case`` is an
IRPPackage method used only to build the fixture.
"""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_use_case import IRPUseCase


@pytest.mark.integration
class TestRPUseCaseIntegration:
    """Integration tests for IRPUseCase with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_extension_point_add_get_delete(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("UcPkg")
        uc_name = self._unique("MyUseCase")
        ep_name = self._unique("MyExtensionPoint")
        pkg = self._create_package(test_project, pkg_name)
        uc = pkg.add_use_case(uc_name)
        try:
            assert isinstance(uc, IRPUseCase)
            uc.add_extension_point(ep_name)
            assert ep_name in [str(e) for e in uc.get_extension_points()]
            uc.delete_extension_point(ep_name)
            assert ep_name not in [str(e) for e in uc.get_extension_points()]
        finally:
            uc.delete_from_project()

    def test_find_extension_point(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("UcPkg")
        uc_name = self._unique("MyUseCase")
        ep_name = self._unique("MyExtensionPoint")
        pkg = self._create_package(test_project, pkg_name)
        uc = pkg.add_use_case(uc_name)
        try:
            uc.add_extension_point(ep_name)
            with pytest.raises(TypeError):
                uc.find_extension_point(ep_name)
        finally:
            uc.delete_from_project()

    def test_get_entry_points_empty(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("UcPkg")
        uc_name = self._unique("MyUseCase")
        pkg = self._create_package(test_project, pkg_name)
        uc = pkg.add_use_case(uc_name)
        try:
            entry_points = list(uc.get_entry_points())
            assert isinstance(entry_points, list)
        finally:
            uc.delete_from_project()

    def test_set_is_behavior_overriden_raises_not_implemented(self, test_project: IRPProject) -> None:
        # setIsBehaviorOverriden is not exposed in the COM automation type library for UseCase
        # (getIsBehaviorOverriden is; the sibling RPActor/IRPClass setters are exposed), so the
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


@pytest.mark.integration
class TestIRPUseCaseGenerated:
    """Generated live coverage for IRPUseCase owned methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_add_extension_point(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            assert use_case.add_extension_point("x") is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_get_extension_points(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            assert use_case.get_extension_points() is not None
        finally:
            pkg.delete_from_project()

    def test_get_entry_points(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            assert use_case.get_entry_points() is not None
        finally:
            pkg.delete_from_project()

    def test_get_describing_diagrams(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            assert use_case.get_describing_diagrams() is not None
        finally:
            pkg.delete_from_project()

    def test_add_describing_diagram(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            with pytest.raises(AttributeError):
                use_case.add_describing_diagram(None)  # type: ignore[arg-type]
        finally:
            pkg.delete_from_project()

    def test_add_event_reception_with_event(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            with pytest.raises(NotImplementedError):
                use_case.add_event_reception_with_event("x", None)  # type: ignore[arg-type]
        finally:
            pkg.delete_from_project()

    def test_delete_describing_diagram(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            with pytest.raises(AttributeError):
                use_case.delete_describing_diagram(None)  # type: ignore[arg-type]
        finally:
            pkg.delete_from_project()

    def test_delete_entry_point(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            assert use_case.delete_entry_point("x") is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_delete_extension_point(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            assert use_case.delete_extension_point("x") is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_find_entry_point(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            with pytest.raises(TypeError):
                use_case.find_entry_point("x")
        finally:
            pkg.delete_from_project()

    def test_find_extension_point(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            with pytest.raises(TypeError):
                use_case.find_extension_point("x")
        finally:
            pkg.delete_from_project()

    def test_get_describing_diagram(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            assert use_case.get_describing_diagram("x") is None
        finally:
            pkg.delete_from_project()

    def test_get_is_behavior_overriden(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            assert use_case.get_is_behavior_overriden() is not None
        finally:
            pkg.delete_from_project()

    def test_set_is_behavior_overriden(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            with pytest.raises(NotImplementedError):
                use_case.set_is_behavior_overriden(1)
        finally:
            pkg.delete_from_project()

    def test_update_contained_diagrams_on_server(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UsePkg"))
        use_case = pkg.add_use_case(self._unique("UC"))
        try:
            with pytest.raises(TypeError):
                use_case.update_contained_diagrams_on_server()  # type: ignore[call-arg]
        finally:
            pkg.delete_from_project()
