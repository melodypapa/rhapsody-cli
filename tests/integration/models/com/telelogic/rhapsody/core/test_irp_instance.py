import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPInstanceIntegration:
    """Integration tests for IRPInstance's own documented-unavailable stubs with a live instance."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_instance(test_project: IRPProject, pkg_name: str, cls_name: str, inst_name: str) -> tuple[IRPPackage, IRPClass, IRPInstance]:
        pkg = test_project.add_package(pkg_name)
        cls = pkg.add_class(cls_name)
        instance = IRPInstance(cls.add_new_aggr("Instance", inst_name)._com)
        return pkg, cls, instance

    def test_get_all_nested_elements_is_documented_unavailable(self, test_project: IRPProject) -> None:
        pkg, _cls, instance = self._create_instance(test_project, self._unique("StubPkg"), self._unique("StubCls"), self._unique("StubInst"))
        try:
            with pytest.raises(NotImplementedError):
                instance.get_all_nested_elements()
        finally:
            pkg.delete_from_project()

    def test_update_contained_diagrams_on_server_is_documented_unavailable(self, test_project: IRPProject) -> None:
        pkg, _cls, instance = self._create_instance(test_project, self._unique("StubPkg"), self._unique("StubCls"), self._unique("StubInst"))
        try:
            with pytest.raises(NotImplementedError):
                instance.update_contained_diagrams_on_server(1)
        finally:
            pkg.delete_from_project()
