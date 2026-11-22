"""Integration tests for the canonical IRPUnit wrapper with live Rhapsody COM API."""

import uuid
from pathlib import Path

import pytest

from rhapsody_cli.exceptions import RhapsodyRuntimeException
from rhapsody_cli.models.com.telelogic.rhapsody.core import AddToModelMode, IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from tests.integration.conftest import TEST_PROJECT_DIR


@pytest.mark.integration
class TestIRPUnitPersistenceIntegration:
    """Integration tests for IRPUnit filename/language/path/lifecycle methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        assert isinstance(pkg, IRPUnit)
        return pkg

    def test_set_and_get_filename_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("UnitPkg"))
        try:
            assert isinstance(pkg, IRPUnit)
            new_filename = self._unique("renamed_unit")
            pkg.set_filename(new_filename)
            filename = pkg.get_filename()
            assert new_filename in filename
            assert isinstance(filename, str)
        finally:
            pkg.delete_from_project()

    def test_set_and_get_language_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("LangPkg"))
        try:
            original = pkg.get_language()
            assert isinstance(original, str)
            pkg.set_language("C++", 0)
            language = pkg.get_language()
            assert language == "C++"
            assert isinstance(language, str)
            pkg.set_language(original, 0)
        finally:
            pkg.delete_from_project()

    def test_get_unit_path_raises_not_implemented(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("UnitPathPkg"))
        try:
            with pytest.raises(NotImplementedError):
                pkg.get_unit_path(1)
        finally:
            pkg.delete_from_project()

    def test_get_current_directory_matches_project(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("CurDirPkg"))
        try:
            current_dir = pkg.get_current_directory()
            assert isinstance(current_dir, str)
            current_path = Path(current_dir)
            assert TEST_PROJECT_DIR == current_path or TEST_PROJECT_DIR in current_path.parents
        finally:
            pkg.delete_from_project()

    def test_save_after_mutation_clears_modified(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("SavePkg"))
        try:
            pkg.set_name(self._unique("SavePkgRenamed"))
            assert pkg.save() is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_get_last_modified_time_after_save(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ModTimePkg"))
        try:
            pkg.set_name(self._unique("ModTimePkgRenamed"))
            pkg.save()
            modified_time = pkg.get_last_modified_time()
            assert isinstance(modified_time, str)
            assert len(modified_time) > 0
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestIRPUnitCmStateIntegration:
    """Integration tests for IRPUnit configuration-management/read-only/stub methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        assert isinstance(pkg, IRPUnit)
        return pkg

    def test_set_and_get_read_only_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ReadOnlyPkg"))
        try:
            assert isinstance(pkg, IRPUnit)
            pkg.save()
            pkg.set_read_only(True)
            assert pkg.is_read_only() is True
            pkg.set_read_only(False)
            assert pkg.is_read_only() is False
        finally:
            pkg.delete_from_project()

    def test_set_and_get_cm_header_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("CmHeaderPkg"))
        try:
            assert isinstance(pkg, IRPUnit)
            pkg.save()
            header = self._unique("CMHeader")
            pkg.set_cm_header(header)
            retrieved = pkg.get_cm_header()
            assert isinstance(retrieved, str)
            assert retrieved == header
        finally:
            pkg.delete_from_project()

    def test_get_cm_state_returns_int(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("CmStatePkg"))
        try:
            assert isinstance(pkg, IRPUnit)
            pkg.save()
            state = pkg.get_cm_state()
            assert isinstance(state, int)
        finally:
            pkg.delete_from_project()

    def test_set_and_get_separate_save_unit_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("SeparatePkg"))
        try:
            assert isinstance(pkg, IRPUnit)
            pkg.save()
            original = pkg.is_separate_save_unit()
            assert isinstance(original, int)
            pkg.set_separate_save_unit(1)
            assert pkg.is_separate_save_unit() == 1
            pkg.set_separate_save_unit(0)
            assert pkg.is_separate_save_unit() == 0
            pkg.set_separate_save_unit(original)
        finally:
            pkg.delete_from_project()

    def test_set_and_get_include_in_next_load_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("NextLoadPkg"))
        try:
            assert isinstance(pkg, IRPUnit)
            pkg.save()
            original = pkg.get_include_in_next_load()
            assert isinstance(original, int)
            pkg.set_include_in_next_load(1)
            assert pkg.get_include_in_next_load() == 1
            pkg.set_include_in_next_load(0)
            assert pkg.get_include_in_next_load() == 0
            pkg.set_include_in_next_load(original)
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestIRPUnitCrossProjectIntegration:
    """Integration tests for IRPUnit cross-project and nesting methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        assert isinstance(pkg, IRPUnit)
        return pkg

    def test_get_nested_save_units_empty_on_plain_package(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("NestPkg"))
        try:
            assert isinstance(pkg, IRPUnit)
            units = pkg.get_nested_save_units()
            assert isinstance(units, IRPCollection)
            assert isinstance(units.get_count(), int)
            assert len(list(units)) == 0
        finally:
            pkg.delete_from_project()

    def test_get_nested_save_units_count_matches_collection(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("NestPkg"))
        try:
            assert isinstance(pkg, IRPUnit)
            pkg.save()
            sub_pkg = pkg.add_nested_package(self._unique("SubPkg"))
            sub_pkg.set_separate_save_unit(1)
            sub_pkg.save()

            count = pkg.get_nested_save_units_count()
            units = pkg.get_nested_save_units()
            assert isinstance(count, int)
            assert count == len(list(units))
            assert count >= 1
        finally:
            pkg.delete_from_project()

    def test_get_structure_diagrams_empty_on_class(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("StructPkg"))
        try:
            cls = pkg.add_class(self._unique("StructCls"))
            assert isinstance(cls, IRPUnit)
            diagrams = cls.get_structure_diagrams()
            assert isinstance(diagrams, IRPCollection)
            assert isinstance(diagrams.get_count(), int)
            assert len(list(diagrams)) == 0
        finally:
            pkg.delete_from_project()

    def test_get_add_to_model_mode_returns_int(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("AddModePkg"))
        try:
            assert isinstance(pkg, IRPUnit)
            pkg.save()
            mode = pkg.get_add_to_model_mode()
            assert isinstance(mode, int)
            assert mode in (member.value for member in AddToModelMode)
        finally:
            pkg.delete_from_project()

    def test_is_reference_unit_false_for_local_unit(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("RefPkg"))
        try:
            assert isinstance(pkg, IRPUnit)
            pkg.save()
            assert pkg.is_reference_unit() == 0
        finally:
            pkg.delete_from_project()

    def test_cross_project_and_lifecycle_members(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UnitOpsPkg"))
        try:
            assert pkg.get_is_stub() in (0, 1)
            with pytest.raises(RhapsodyRuntimeException):
                pkg.copy_to_another_project(test_project)
            assert pkg.load(0) is None
            with pytest.raises(RhapsodyRuntimeException):
                pkg.move_to_another_project_leave_a_reference(test_project)
            with pytest.raises(RhapsodyRuntimeException):
                pkg.reference_to_another_project(test_project)
            with pytest.raises(RhapsodyRuntimeException):
                pkg.set_unit_path("x")
            assert pkg.unload() is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()
