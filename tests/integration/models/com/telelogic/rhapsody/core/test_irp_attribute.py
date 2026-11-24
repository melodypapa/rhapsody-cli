"""Integration tests for IRPAttribute with live Rhapsody COM API.

Scope: only methods that IRPAttribute owns (the 12 is_*/multiplicity/visibility
getters and setters declared on IRPAttribute). Parent-class behaviour
(IRPVariable::set_declaration / get_type / set_default_value, IRPClassifier::
add_attribute) is exercised in its own integration tests; here
``add_attribute`` is used purely to obtain an IRPAttribute instance.
"""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestRPAttributeIntegration:
    """Integration tests for IRPAttribute with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_is_static_roundtrip(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            assert isinstance(attr, IRPAttribute)
            assert attr.is_static is False
            attr.is_static = True
            assert attr.is_static is True
            attr.is_static = False
            assert attr.is_static is False
        finally:
            test_class.delete_from_project()

    def test_is_constant_roundtrip(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            assert attr.is_constant in (0, 1)
            attr.is_constant = True
            assert attr.is_constant == 1
            attr.is_constant = False
            assert attr.is_constant == 0
        finally:
            test_class.delete_from_project()

    def test_is_ordered_roundtrip(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            assert attr.is_ordered in (0, 1)
            attr.is_ordered = True
            assert attr.is_ordered == 1
            attr.is_ordered = False
            assert attr.is_ordered == 0
        finally:
            test_class.delete_from_project()

    def test_is_reference_roundtrip(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            assert attr.is_reference in (0, 1)
            attr.is_reference = True
            assert attr.is_reference == 1
            attr.is_reference = False
            assert attr.is_reference == 0
        finally:
            test_class.delete_from_project()

    def test_multiplicity_roundtrip(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            attr.multiplicity = "0..*"
            assert attr.multiplicity == "0..*"
        finally:
            test_class.delete_from_project()

    def test_visibility_roundtrip(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            attr.visibility = "private"
            assert attr.visibility == "private"
        finally:
            test_class.delete_from_project()
