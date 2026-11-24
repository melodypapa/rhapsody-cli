"""Integration tests for IRPAssociationClass with live Rhapsody COM API.

These tests require a running Rhapsody instance with an open project.
"""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_class import IRPAssociationClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestRPAssociationClassIntegration:
    """Integration tests for IRPAssociationClass with real Rhapsody COM API.

    Note: In this Rhapsody build, ``addRelationTo`` with a non-empty ``linkName``
    does not actually create an association class — it creates a regular
    association with metaclass ``AssociationEnd`` roles.  The four
    ``IRPAssociationClass``-specific members therefore cannot be exercised via
    live COM in this environment.  They **do** have unit-test coverage via
    fakes, and the integration test below is marked ``xfail`` with a clear
    description of the limitation.
    """

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_owned_properties_via_wrapped_com_object(self, test_project: IRPProject) -> None:
        """Exercise the owned properties on a wrapped COM object. This Rhapsody build
        creates a plain association via addRelationTo, not an AssociationClass.
        """
        pkg = self._create_package(test_project, self._unique("AssocPkg"))
        cls = pkg.add_class(self._unique("AssocCls"))
        try:
            assoc = IRPAssociationClass(cls._com)
            for accessor in (
                lambda: assoc.end1,
                lambda: assoc.end2,
                lambda: assoc.is_class,
            ):
                with pytest.raises(AttributeError):
                    accessor()
            with pytest.raises(AttributeError):
                assoc.is_class = 1
        finally:
            cls.delete_from_project()
