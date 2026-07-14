import uuid

import pytest

from rhapsody_cli.models.elements.classifiers import RPInterface
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPInterfaceIntegration:
    """Integration tests for RPInterface with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    @pytest.mark.xfail(
        reason="Rhapsody2.Application.1 does not expose 'addInterface' on a package (and "
        "addNewAggr('Interface') does not yield an Interface); RPPackage.add_interface raises. "
        "TODO: support Interface creation via the correct metaclass/owner in a future Rhapsody build.",
        strict=False,
    )
    def test_create_interface_in_package(self, test_project: RPProject) -> None:
        pkg_name = self._unique("IntPkg")
        iface_name = self._unique("MyInterface")
        pkg = self._create_package(test_project, pkg_name)
        try:
            iface = pkg.add_interface(iface_name)
            assert iface is not None
            assert isinstance(iface, RPInterface)
            assert iface.get_name() == iface_name
            assert iface.get_meta_class() == "Interface"
        finally:
            iface.delete_from_project()
