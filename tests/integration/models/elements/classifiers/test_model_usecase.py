import uuid

import pytest

from rhapsody_cli.models.elements.classifiers import RPUseCase
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPUseCaseIntegration:
    """Integration tests for RPUseCase with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_create_usecase_in_package(self, test_project: RPProject) -> None:
        pkg_name = self._unique("UcPkg")
        uc_name = self._unique("MyUseCase")
        pkg = self._create_package(test_project, pkg_name)
        try:
            uc = pkg.add_use_case(uc_name)
            assert uc is not None
            assert isinstance(uc, RPUseCase)
            assert uc.get_name() == uc_name
            assert uc.get_meta_class() == "UseCase"
        finally:
            uc.delete_from_project()
