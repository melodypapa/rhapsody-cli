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
    """Integration tests for IRPAssociationClass with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_owned_properties_via_wrapped_com_object(self, test_project: IRPProject) -> None:
        """Create a real association class and exercise its owned properties.

        ``IRPModelElement.add_association`` (JavaDoc: "Creates an association
        class using the specified IRPRelation elements") is the documented way
        to build the fixture: create two classes, relate them, take the two
        relation ends, and turn that association into an association class.
        """
        pkg = self._create_package(test_project, self._unique("AssocPkg"))
        try:
            class_a = pkg.add_class(self._unique("AssocClsA"))
            class_b = pkg.add_class(self._unique("AssocClsB"))
            end1 = class_a.add_relation_to(class_b, "", "Association", "1", "", "Association", "1", "")
            end2 = end1.get_inverse()

            assoc = pkg.add_association(end1, end2, self._unique("AssocClass"))

            assert isinstance(assoc, IRPAssociationClass)
            assert assoc.end1 in (end1, end2)
            assert assoc.end2 in (end1, end2)
            assert assoc.end1 != assoc.end2

            original_is_class = assoc.is_class
            assert original_is_class in (0, 1)
            toggled_is_class = 0 if original_is_class == 1 else 1
            assoc.is_class = toggled_is_class
            assert assoc.is_class == toggled_is_class
            assoc.is_class = original_is_class
            assert assoc.is_class == original_is_class
        finally:
            pkg.delete_from_project()
