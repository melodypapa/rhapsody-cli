import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPGeneralization
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestRPGeneralizationIntegration:
    """Integration tests for IRPGeneralization with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_create_generalization(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("GenPkg")
        parent_name = self._unique("Parent")
        child_name = self._unique("Child")
        pkg = self._create_package(test_project, pkg_name)
        parent = pkg.add_class(parent_name)
        child = pkg.add_class(child_name)
        try:
            child.add_generalization(parent)
            gen = child.find_generalization(parent_name)
            assert gen is not None
            assert isinstance(gen, IRPGeneralization)
            assert gen.meta_class == "Generalization"
            assert gen.get_base_class() == parent
        finally:
            child.delete_from_project()
            parent.delete_from_project()
