"""Integration tests for RPStatechart with live Rhapsody COM API.

Scope: only methods that RPStatechart owns (IRPStatechart::createGraphics,
closeDiagram, getRootState, getItsClass, getIsMainBehavior, ...).
``add_statechart`` is an IRPClassifier method used only to build the fixture
(its coverage is in test_model_classifier.py).
"""

import uuid

import pytest

from rhapsody_cli.models.core import RPModelElement
from rhapsody_cli.models.elements.classifiers import RPClass, RPStatechart
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPStatechartIntegration:
    """Integration tests for RPStatechart with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_get_its_class_returns_owning_class(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ScPkg")
        class_name = self._unique("ScCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            sc = test_class.add_statechart()
            assert isinstance(sc, RPStatechart)
            owner = sc.get_its_class()
            assert isinstance(owner, RPClass)
            assert owner.get_name() == class_name
        finally:
            test_class.delete_from_project()

    def test_get_is_main_behavior(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ScPkg")
        class_name = self._unique("ScCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            sc = test_class.add_statechart()
            assert sc.get_is_main_behavior() in (0, 1)
        finally:
            test_class.delete_from_project()

    def test_get_root_state(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ScPkg")
        class_name = self._unique("ScCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            sc = test_class.add_statechart()
            root = sc.get_root_state()
            assert root is not None
            assert isinstance(root, RPModelElement)
        finally:
            test_class.delete_from_project()

    def test_create_graphics_then_close_diagram(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ScPkg")
        class_name = self._unique("ScCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            sc = test_class.add_statechart()
            sc.create_graphics()  # no return value; verify it does not raise
            sc.close_diagram()  # no return value; verify it does not raise
        finally:
            test_class.delete_from_project()
