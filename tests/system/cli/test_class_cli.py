"""System tests for the `class` CLI command group.

Tests class CRUD lifecycle and link (generalization) via subprocess.

Path notes: Paths use "/" separator. Packages are created at root by
omitting --path. Class paths are "PkgName/ClassName".
"""

import json
import uuid

import pytest

from tests.system.cli.conftest import _run_cli, _unique_name


@pytest.mark.system
class TestClassCLI:
    """Test class CLI commands via subprocess."""

    @pytest.fixture(autouse=True)
    def _require_rhapsody(self, _require_rhapsody: None) -> None:
        """Skip these tests if no Rhapsody instance is available."""

    @staticmethod
    def _create_package(name: str) -> str:
        """Create a package at project root via CLI and return its path."""
        pkg_json = json.dumps({"name": name})
        result = _run_cli("package", "create", "--input", pkg_json)
        assert result.returncode == 0, f"Failed to create package: {result.stderr}"
        return name

    @staticmethod
    def _create_class(pkg_path: str, name: str) -> str:
        """Create a class via CLI and return its full path."""
        cls_json = json.dumps({"name": name})
        result = _run_cli("class", "create", "--path", pkg_path, "--input", cls_json)
        assert result.returncode == 0, f"Failed to create class: {result.stderr}"
        return f"{pkg_path}/{name}"

    def test_class_create_under_package(self, cli_project: str) -> None:
        """Test creating a class under a package."""
        pkg_name = _unique_name("Pkg")
        cls_name = _unique_name("Cls")
        pkg_path = self._create_package(pkg_name)

        try:
            cls_json = json.dumps({"name": cls_name})
            result = _run_cli("class", "create", "--path", pkg_path, "--input", cls_json)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify via list
            list_result = _run_cli("class", "list", "--path", pkg_path, "--format", "json")
            assert list_result.returncode == 0
            classes = json.loads(list_result.stdout)
            assert cls_name in classes
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_view_existing(self, cli_project: str) -> None:
        """Test viewing an existing class."""
        pkg_name = _unique_name("ViewPkg")
        cls_name = _unique_name("ViewCls")
        pkg_path = self._create_package(pkg_name)
        cls_path = self._create_class(pkg_path, cls_name)

        try:
            result = _run_cli("class", "view", "--path", cls_path, "--format", "json")
            assert result.returncode == 0, f"Failed: {result.stderr}"
            data = json.loads(result.stdout)
            assert data["name"] == cls_name
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_view_nonexistent(self, cli_project: str) -> None:
        """Test viewing a non-existent class returns error."""
        pkg_name = _unique_name("NoClsPkg")
        pkg_path = self._create_package(pkg_name)

        try:
            result = _run_cli("class", "view", "--path", f"{pkg_path}/NonExistent_{uuid.uuid4().hex[:8]}")
            assert result.returncode != 0
            assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_list_in_package(self, cli_project: str) -> None:
        """Test listing classes in a package."""
        pkg_name = _unique_name("ListPkg")
        cls1_name = _unique_name("Cls1")
        cls2_name = _unique_name("Cls2")
        pkg_path = self._create_package(pkg_name)
        self._create_class(pkg_path, cls1_name)
        self._create_class(pkg_path, cls2_name)

        try:
            result = _run_cli("class", "list", "--path", pkg_path, "--format", "json")
            assert result.returncode == 0
            classes = json.loads(result.stdout)
            assert cls1_name in classes
            assert cls2_name in classes
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_delete_existing(self, cli_project: str) -> None:
        """Test deleting an existing class."""
        pkg_name = _unique_name("DelPkg")
        cls_name = _unique_name("DelCls")
        pkg_path = self._create_package(pkg_name)
        cls_path = self._create_class(pkg_path, cls_name)

        try:
            result = _run_cli("class", "delete", "--path", cls_path)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify class is gone
            list_result = _run_cli("class", "list", "--path", pkg_path, "--format", "json")
            assert list_result.returncode == 0
            classes = json.loads(list_result.stdout)
            assert cls_name not in classes
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_delete_nonexistent(self, cli_project: str) -> None:
        """Test deleting a non-existent class returns error."""
        pkg_name = _unique_name("NoDelPkg")
        pkg_path = self._create_package(pkg_name)

        try:
            result = _run_cli("class", "delete", "--path", f"{pkg_path}/NonExistent_{uuid.uuid4().hex[:8]}")
            assert result.returncode != 0
            assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_link_generalization(self, cli_project: str) -> None:
        """Test adding a generalization link between classes."""
        pkg_name = _unique_name("LinkPkg")
        parent_cls_name = _unique_name("ParentCls")
        child_cls_name = _unique_name("ChildCls")
        pkg_path = self._create_package(pkg_name)
        self._create_class(pkg_path, parent_cls_name)
        child_path = self._create_class(pkg_path, child_cls_name)

        try:
            # Add generalization: child -> parent
            result = _run_cli("class", "link", "--path", child_path, "--add", parent_cls_name)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify by viewing child class
            view_result = _run_cli("class", "view", "--path", child_path, "--format", "json")
            assert view_result.returncode == 0
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_create_with_attributes(self, cli_project: str) -> None:
        """Test creating a class with attributes and operations in JSON."""
        pkg_name = _unique_name("AttrPkg")
        cls_name = _unique_name("AttrCls")
        pkg_path = self._create_package(pkg_name)

        try:
            cls_json = json.dumps({
                "name": cls_name,
                "attributes": ["attr1", "attr2"],
                "operations": ["op1"],
            })
            result = _run_cli("class", "create", "--path", pkg_path, "--input", cls_json)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify via view
            view_result = _run_cli("class", "view", "--path", f"{pkg_path}/{cls_name}", "--format", "json")
            assert view_result.returncode == 0
            data = json.loads(view_result.stdout)
            assert "attr1" in data["attributes"]
            assert "attr2" in data["attributes"]
            assert "op1" in data["operations"]
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_create_invalid_json(self, cli_project: str) -> None:
        """Test that invalid JSON input returns error."""
        pkg_name = _unique_name("BadJsonPkg")
        pkg_path = self._create_package(pkg_name)

        try:
            result = _run_cli("class", "create", "--path", pkg_path, "--input", "{invalid}")
            assert result.returncode != 0
            assert "json" in result.stderr.lower() or "error" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)
