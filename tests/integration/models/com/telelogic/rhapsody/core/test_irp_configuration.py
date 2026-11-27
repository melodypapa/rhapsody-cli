"""Integration tests for IRPConfiguration with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_configuration import IRPConfiguration
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPConfigurationIntegration:
    """Integration tests for IRPConfiguration with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _configuration(pkg: IRPPackage) -> tuple[IRPPackage, IRPConfiguration]:
        element = pkg.add_new_aggr("Configuration", f"Config_{uuid.uuid4().hex[:8]}")
        configuration = IRPConfiguration(element._com)
        assert isinstance(configuration, IRPConfiguration)
        return pkg, configuration

    def test_additional_sources(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Additional_SourcesPkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.additional_sources in ("", None)
        finally:
            pkg.delete_from_project()

    def test_all_elements_in_instrumentation_scope(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("All_Elements_In_Instrumentation_ScopePkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert len(list(configuration.all_elements_in_instrumentation_scope)) == 0
        finally:
            pkg.delete_from_project()

    def test_build_set(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Build_SetPkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.build_set in ("", None)
        finally:
            pkg.delete_from_project()

    def test_compiler_switches(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Compiler_SwitchesPkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.compiler_switches in ("", None)
        finally:
            pkg.delete_from_project()

    def test_generate_code_for_actors(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Generate_Code_For_ActorsPkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.generate_code_for_actors in (0, 1)
        finally:
            pkg.delete_from_project()

    def test_include_path(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Include_PathPkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.include_path in ("", None)
        finally:
            pkg.delete_from_project()

    def test_initial_instances(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Initial_InstancesPkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert len(list(configuration.initial_instances)) == 0
        finally:
            pkg.delete_from_project()

    def test_initialization_code(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Initialization_CodePkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.initialization_code in ("", None)
        finally:
            pkg.delete_from_project()

    def test_instrumentation_scope(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Instrumentation_ScopePkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert len(list(configuration.instrumentation_scope)) == 0
        finally:
            pkg.delete_from_project()

    def test_instrumentation_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Instrumentation_TypePkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.instrumentation_type in (0, 1)
        finally:
            pkg.delete_from_project()

    def test_libraries(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("LibrariesPkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.libraries in ("", None)
        finally:
            pkg.delete_from_project()

    def test_link_switches(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Link_SwitchesPkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.link_switches in ("", None)
        finally:
            pkg.delete_from_project()

    def test_scope_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Scope_TypePkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.scope_type in (0, 1)
        finally:
            pkg.delete_from_project()

    def test_standard_headers(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Standard_HeadersPkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.standard_headers in ("", None)
        finally:
            pkg.delete_from_project()

    def test_statechart_implementation(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Statechart_ImplementationPkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.statechart_implementation in (0, 1)
        finally:
            pkg.delete_from_project()

    def test_time_model(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Time_ModelPkg"))
        try:
            _, configuration = self._configuration(pkg)
            # No documented API populates this read-only configuration property.
            assert configuration.time_model in (0, 1)
        finally:
            pkg.delete_from_project()

    def test_unavailable_members_raise_before_dispatch(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UnavailablePkg"))
        try:
            _, configuration = self._configuration(pkg)
            with pytest.raises(NotImplementedError):
                configuration.get_path()
            with pytest.raises(NotImplementedError):
                configuration.set_path("path")
        finally:
            pkg.delete_from_project()
