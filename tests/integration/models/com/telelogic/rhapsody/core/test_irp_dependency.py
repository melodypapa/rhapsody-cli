import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPDependency
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPDependencyIntegration:
    """Integration tests for IRPDependency's own members with a live dependency."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def _create_dependency(self, test_project: IRPProject) -> tuple[IRPPackage, IRPClass, IRPClass, IRPClass, IRPDependency]:
        pkg = test_project.add_package(self._unique("DepPkg"))
        dependent = pkg.add_class(self._unique("DepClient"))
        supplier = pkg.add_class(self._unique("DepSupplier"))
        other = pkg.add_class(self._unique("DepOther"))
        dependency = IRPDependency(dependent.add_dependency_to(supplier)._com)
        return pkg, dependent, supplier, other, dependency

    def test_dependent(self, test_project: IRPProject) -> None:
        pkg, dependent, _supplier, _other, dependency = self._create_dependency(test_project)
        try:
            assert dependency.dependent is not None
            assert dependency.dependent.name == dependent.name
        finally:
            pkg.delete_from_project()

    def test_depends_on(self, test_project: IRPProject) -> None:
        pkg, _dependent, supplier, _other, dependency = self._create_dependency(test_project)
        try:
            assert dependency.depends_on is not None
            assert dependency.depends_on.name == supplier.name
        finally:
            pkg.delete_from_project()

    def test_dependent_setter_replaces_the_client(self, test_project: IRPProject) -> None:
        pkg, _dependent, _supplier, other, dependency = self._create_dependency(test_project)
        try:
            dependency.dependent = other
            assert dependency.dependent is not None
            assert dependency.dependent.name == other.name
        finally:
            pkg.delete_from_project()

    def test_depends_on_setter_replaces_the_supplier(self, test_project: IRPProject) -> None:
        pkg, _dependent, _supplier, other, dependency = self._create_dependency(test_project)
        try:
            dependency.depends_on = other
            assert dependency.depends_on is not None
            assert dependency.depends_on.name == other.name
        finally:
            pkg.delete_from_project()

    def test_set_owner_without_changing_dependent_moves_the_owner(self, test_project: IRPProject) -> None:
        pkg, dependent, _supplier, other, dependency = self._create_dependency(test_project)
        try:
            dependency.set_owner_without_changing_dependent(other)
            assert dependency.owner is not None
            assert dependency.owner.name == other.name
            assert dependency.dependent is not None
            assert dependency.dependent.name == dependent.name
        finally:
            pkg.delete_from_project()

    def test_is_need_to_migrate_is_documented_unavailable(self, test_project: IRPProject) -> None:
        pkg, _dependent, _supplier, _other, dependency = self._create_dependency(test_project)
        try:
            with pytest.raises(NotImplementedError):
                dependency.is_need_to_migrate()
        finally:
            pkg.delete_from_project()

    def test_set_link_type_is_documented_unavailable(self, test_project: IRPProject) -> None:
        pkg, _dependent, _supplier, _other, dependency = self._create_dependency(test_project)
        try:
            with pytest.raises(NotImplementedError):
                dependency.set_link_type("Usage")
        finally:
            pkg.delete_from_project()
