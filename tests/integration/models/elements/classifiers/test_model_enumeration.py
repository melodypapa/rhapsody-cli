import uuid

import pytest

from rhapsody_cli.models.elements.classifiers import RPEnumeration
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPEnumerationIntegration:
    """Integration tests for RPEnumeration with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    @pytest.mark.xfail(
        reason="Rhapsody2.Application.1 does not expose 'addEnumeration' (or addNewAggr('Enumeration')) "
        "on a package; RPPackage.add_enumeration raises. TODO: support Enumeration creation via the "
        "correct metaclass/owner in a future Rhapsody build.",
        strict=False,
    )
    def test_create_enumeration_in_package(self, test_project: RPProject) -> None:
        pkg_name = self._unique("EnumPkg")
        enum_name = self._unique("MyEnum")
        pkg = self._create_package(test_project, pkg_name)
        try:
            enumeration = pkg.add_enumeration(enum_name)
            assert enumeration is not None
            assert isinstance(enumeration, RPEnumeration)
            assert enumeration.get_name() == enum_name
            assert enumeration.get_meta_class() == "Enumeration"
        finally:
            enumeration.delete_from_project()
