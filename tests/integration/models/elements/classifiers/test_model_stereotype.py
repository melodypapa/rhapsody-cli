"""Integration tests for RPStereotype with live Rhapsody COM API.

Scope: only methods that RPStereotype owns (IRPStereotype::addMetaClass,
removeMetaClass, getOfMetaClass, getIcon, getIsNewTerm, setIsNewTerm).
The stereotype fixture is created on a class via ``add_stereotype`` (an
IRPModelElement method) — its behaviour is covered by test_core.py.
"""

import uuid
from typing import Tuple

import pytest

from rhapsody_cli.models.elements.classifiers import RPClass, RPStereotype
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

    def _create_stereotype(self, pkg: RPPackage, stereo_name: str) -> Tuple[RPClass, RPStereotype]:
        # addStereotype(name, "Class") succeeds when applied to a Class element; applying a
        # "Class"-scoped stereotype directly to a Package raises a COM error in this build.
        # The owning class is returned so cleanup can delete it before the stereotype
        # (a stereotype cannot be delete_from_project'd while still applied to a class).
        test_class = pkg.add_class(self._unique("SterCls"))
        stereotype = test_class.add_stereotype(stereo_name, "Class")
        assert isinstance(stereotype, RPStereotype)
        return test_class, stereotype

    def test_meta_class_add_get_remove(self, test_project: RPProject) -> None:
        pkg_name = self._unique("SterPkg")
        stereo_name = self._unique("MyStereotype")
        pkg = self._create_package(test_project, pkg_name)
        test_class, stereotype = self._create_stereotype(pkg, stereo_name)
        try:
            # Created scoped to "Class"; adding another applicable metaclass should grow the list.
            before = stereotype.get_of_meta_class()
            assert isinstance(before, str)
            stereotype.add_meta_class("Attribute")
            after_add = stereotype.get_of_meta_class()
            assert "Attribute" in after_add
            stereotype.remove_meta_class("Attribute")
            after_remove = stereotype.get_of_meta_class()
            assert "Attribute" not in after_remove
        finally:
            test_class.delete_from_project()
            stereotype.delete_from_project()

    def test_set_is_new_term_raises_not_implemented(self, test_project: RPProject) -> None:
        # setIsNewTerm is not exposed in the COM automation type library for stereotypes
        # (getIsNewTerm is), so the wrapper raises NotImplementedError — mirrors RPClass.set_is_abstract.
        pkg_name = self._unique("SterPkg")
        stereo_name = self._unique("MyStereotype")
        pkg = self._create_package(test_project, pkg_name)
        test_class, stereotype = self._create_stereotype(pkg, stereo_name)
        try:
            assert stereotype.get_is_new_term() in (0, 1)
            with pytest.raises(NotImplementedError, match="setIsNewTerm is not exposed"):
                stereotype.set_is_new_term(1)
        finally:
            test_class.delete_from_project()
            stereotype.delete_from_project()

    def test_get_icon_is_string(self, test_project: RPProject) -> None:
        pkg_name = self._unique("SterPkg")
        stereo_name = self._unique("MyStereotype")
        pkg = self._create_package(test_project, pkg_name)
        test_class, stereotype = self._create_stereotype(pkg, stereo_name)
        try:
            icon = stereotype.get_icon()
            assert isinstance(icon, str)
        finally:
            test_class.delete_from_project()
            stereotype.delete_from_project()
