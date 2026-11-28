"""Integration tests for IRPConfiguration with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component import IRPComponent
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_configuration import IRPConfiguration
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPConfigurationIntegration:
    """Integration tests for IRPConfiguration with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _configuration(project: IRPProject) -> tuple[IRPComponent, IRPConfiguration]:
        component = project.add_component(f"ConfigurationOwner_{uuid.uuid4().hex[:8]}")
        configuration = component.add_configuration(f"Config_{uuid.uuid4().hex[:8]}")
        return component, configuration

    def test_additional_sources(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            # No documented API populates this read-only configuration property.
            assert configuration.additional_sources in ("", None)
        finally:
            component.delete_from_project()

    def test_all_elements_in_instrumentation_scope(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            expected = int(configuration._com.allElementsInInstrumentationScope)
            assert expected in (0, 1)
            assert configuration.all_elements_in_instrumentation_scope == expected
        finally:
            component.delete_from_project()

    def test_build_set(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            expected = str(configuration._com.buildSet)
            assert expected
            assert configuration.build_set == expected
        finally:
            component.delete_from_project()

    def test_compiler_switches(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            expected = str(configuration._com.compilerSwitches)
            assert expected
            assert configuration.compiler_switches == expected
        finally:
            component.delete_from_project()

    def test_generate_code_for_actors(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            # No documented API populates this read-only configuration property.
            assert configuration.generate_code_for_actors in (0, 1)
        finally:
            component.delete_from_project()

    def test_include_path(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            # No documented API populates this read-only configuration property.
            assert configuration.include_path in ("", None)
        finally:
            component.delete_from_project()

    def test_initial_instances(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            # No documented API populates this read-only configuration property.
            assert len(list(configuration.initial_instances)) == 0
        finally:
            component.delete_from_project()

    def test_initialization_code(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            # No documented API populates this read-only configuration property.
            assert configuration.initialization_code in ("", None)
        finally:
            component.delete_from_project()

    def test_instrumentation_scope(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            # No documented API populates this read-only configuration property.
            assert len(list(configuration.instrumentation_scope)) == 0
        finally:
            component.delete_from_project()

    def test_instrumentation_type(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            expected = str(configuration._com.instrumentationType)
            assert expected
            assert configuration.instrumentation_type == expected
        finally:
            component.delete_from_project()

    def test_libraries(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            # No documented API populates this read-only configuration property.
            assert configuration.libraries in ("", None)
        finally:
            component.delete_from_project()

    def test_link_switches(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            expected = str(configuration._com.linkSwitches)
            assert expected
            assert configuration.link_switches == expected
        finally:
            component.delete_from_project()

    def test_scope_type(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            expected = str(configuration._com.scopeType)
            assert expected
            assert configuration.scope_type == expected
        finally:
            component.delete_from_project()

    def test_standard_headers(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            # No documented API populates this read-only configuration property.
            assert configuration.standard_headers in ("", None)
        finally:
            component.delete_from_project()

    def test_statechart_implementation(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            expected = str(configuration._com.statechartImplementation)
            assert expected
            assert configuration.statechart_implementation == expected
        finally:
            component.delete_from_project()

    def test_time_model(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            expected = str(configuration._com.timeModel)
            assert expected
            assert configuration.time_model == expected
        finally:
            component.delete_from_project()

    def test_unavailable_members_raise_before_dispatch(self, test_project: IRPProject) -> None:
        component, configuration = self._configuration(test_project)
        try:
            with pytest.raises(NotImplementedError):
                configuration.get_path()
            with pytest.raises(NotImplementedError):
                configuration.set_path("path")
        finally:
            component.delete_from_project()
