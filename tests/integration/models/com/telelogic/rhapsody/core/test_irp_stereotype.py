"""Live integration tests for the JavaDoc-owned IRPStereotype API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPStereotype
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPStereotypeIntegration:
    """Exercise stereotype-owned behavior using a real project stereotype."""

    @staticmethod
    def _unique(prefix: str) -> str:
        return f"{prefix}_{uuid.uuid4().hex}"

    def _create_stereotype(self, project: IRPProject, prefix: str = "Stereotype") -> tuple[IRPPackage, IRPStereotype]:
        package = project.add_package(self._unique(f"{prefix}Pkg"))
        stereotype = package.add_stereotype(self._unique(prefix), "Package")
        return package, stereotype

    @staticmethod
    def _metaclasses(stereotype: IRPStereotype) -> set[str]:
        return {name.strip() for name in stereotype.of_meta_class.split(",") if name.strip()}

    def test_add_meta_class(self, test_project: IRPProject) -> None:
        package, stereotype = self._create_stereotype(test_project, "AddMetaClass")
        try:
            stereotype.add_meta_class("Class")

            assert "Class" in self._metaclasses(stereotype)
        finally:
            package.delete_from_project()

    def test_icon_empty_for_stereotype_without_custom_icon(self, test_project: IRPProject) -> None:
        """The JavaDoc getIcon API returns the associated image-file path.

        The registered typelib exposes ``icon`` as read-only and declares no
        setter. A newly created stereotype has no custom icon and returns an
        empty path. This empty-state case is additional only; the populated
        getter fixture remains blocked because no documented API assigns an icon.
        """
        package, stereotype = self._create_stereotype(test_project, "Icon")
        try:
            assert stereotype.icon == ""
        finally:
            package.delete_from_project()

    def test_is_new_term(self, test_project: IRPProject) -> None:
        package, stereotype = self._create_stereotype(test_project, "NewTerm")
        try:
            stereotype.is_new_term = 1
            assert stereotype.is_new_term == 1

            stereotype.is_new_term = 0
            assert stereotype.is_new_term == 0
        finally:
            package.delete_from_project()

    def test_of_meta_class(self, test_project: IRPProject) -> None:
        package, stereotype = self._create_stereotype(test_project, "OfMetaClass")
        try:
            stereotype.add_meta_class("Class")

            assert {"Package", "Class"}.issubset(self._metaclasses(stereotype))
        finally:
            package.delete_from_project()

    def test_remove_meta_class(self, test_project: IRPProject) -> None:
        package, stereotype = self._create_stereotype(test_project, "RemoveMetaClass")
        try:
            stereotype.add_meta_class("Class")
            assert "Class" in self._metaclasses(stereotype)

            stereotype.remove_meta_class("Class")

            assert "Class" not in self._metaclasses(stereotype)
        finally:
            package.delete_from_project()
