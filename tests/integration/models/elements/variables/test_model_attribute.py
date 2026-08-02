"""Integration tests for RPAttribute with live Rhapsody COM API.

Scope: only methods that RPAttribute owns (the 12 is_*/multiplicity/visibility
getters and setters declared on IRPAttribute). Parent-class behaviour
(IRPVariable::set_declaration / get_type / set_default_value, IRPClassifier::
add_attribute) is exercised in its own integration tests; here
``add_attribute`` is used purely to obtain an RPAttribute instance.
"""

import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.variables import RPAttribute


@pytest.mark.integration
class TestRPAttributeIntegration:
    """Integration tests for RPAttribute with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_is_static_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            assert isinstance(attr, RPAttribute)
            assert attr.get_is_static() is False
            attr.set_is_static(True)
            assert attr.get_is_static() is True
            attr.set_is_static(False)
            assert attr.get_is_static() is False
        finally:
            test_class.delete_from_project()

    def test_is_constant_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            assert attr.get_is_constant() in (0, 1)
            attr.set_is_constant(True)
            assert attr.get_is_constant() == 1
            attr.set_is_constant(False)
            assert attr.get_is_constant() == 0
        finally:
            test_class.delete_from_project()

    def test_is_ordered_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            assert attr.get_is_ordered() in (0, 1)
            attr.set_is_ordered(True)
            assert attr.get_is_ordered() == 1
            attr.set_is_ordered(False)
            assert attr.get_is_ordered() == 0
        finally:
            test_class.delete_from_project()

    def test_is_reference_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            assert attr.get_is_reference() in (0, 1)
            attr.set_is_reference(True)
            assert attr.get_is_reference() == 1
            attr.set_is_reference(False)
            assert attr.get_is_reference() == 0
        finally:
            test_class.delete_from_project()

    def test_multiplicity_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            attr.set_multiplicity("0..*")
            assert attr.get_multiplicity() == "0..*"
        finally:
            test_class.delete_from_project()

    def test_visibility_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            attr.set_visibility("private")
            assert attr.get_visibility() == "private"
        finally:
            test_class.delete_from_project()
