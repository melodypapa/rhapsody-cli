"""Integration tests for RPStereotype with live Rhapsody COM API.

Scope: only methods that RPStereotype owns (IRPStereotype::addMetaClass,
removeMetaClass, getOfMetaClass, getIcon, getIsNewTerm, setIsNewTerm).
``add_stereotype`` (an IRPModelElement method) is used only to create the
fixture; its behaviour is covered by test_core.py.
"""

import uuid

import pytest

from rhapsody_cli.models.elements.classifiers import RPStereotype
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPStereotypeIntegration:
    """Integration tests for RPStereotype with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_meta_class_add_get_remove(self, test_project: RPProject) -> None:
        pkg_name = self._unique("SterPkg")
        stereo_name = self._unique("MyStereotype")
        pkg = self._create_package(test_project, pkg_name)
        stereotype = pkg.add_stereotype(stereo_name, "Class")
        try:
            assert isinstance(stereotype, RPStereotype)
            # Created for "Class"; adding another applicable metaclass should grow the list.
            before = stereotype.get_of_meta_class()
            assert isinstance(before, str)
            stereotype.add_meta_class("Attribute")
            after_add = stereotype.get_of_meta_class()
            assert "Attribute" in after_add
            stereotype.remove_meta_class("Attribute")
            after_remove = stereotype.get_of_meta_class()
            assert "Attribute" not in after_remove
        finally:
            stereotype.delete_from_project()

    def test_is_new_term_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("SterPkg")
        stereo_name = self._unique("MyStereotype")
        pkg = self._create_package(test_project, pkg_name)
        stereotype = pkg.add_stereotype(stereo_name, "Class")
        try:
            assert stereotype.get_is_new_term() in (0, 1)
            stereotype.set_is_new_term(1)
            assert stereotype.get_is_new_term() == 1
            stereotype.set_is_new_term(0)
            assert stereotype.get_is_new_term() == 0
        finally:
            stereotype.delete_from_project()

    def test_get_icon_is_string(self, test_project: RPProject) -> None:
        pkg_name = self._unique("SterPkg")
        stereo_name = self._unique("MyStereotype")
        pkg = self._create_package(test_project, pkg_name)
        stereotype = pkg.add_stereotype(stereo_name, "Class")
        try:
            icon = stereotype.get_icon()
            assert isinstance(icon, str)
        finally:
            stereotype.delete_from_project()
