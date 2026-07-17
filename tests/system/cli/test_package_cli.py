"""System tests for the `package` CLI command group.

Tests package CRUD lifecycle via subprocess against a live Rhapsody project.

Path notes: Paths use "/" separator. The project name is NOT a valid path
segment — omit --path to create at root. `package list/view/delete` require
a Package path (not Project), so root-level packages are verified via
`package view`, not `package list`.
"""

import json
import uuid

import pytest

from tests.system.cli.conftest import _run_cli, _unique_name


@pytest.mark.system
class TestPackageCLI:
    """Test package CLI commands via subprocess."""

    @pytest.fixture(autouse=True)
    def _require_rhapsody(self, _require_rhapsody: None) -> None:
        """Skip these tests if no Rhapsody instance is available."""

    @staticmethod
    def _create_root_package(name: str) -> str:
        """Create a package at project root via CLI and return its path.

        Args:
            name: Package name to create.

        Returns:
            Package path (just the name, since root-level packages have no parent prefix).
        """
        pkg_json = json.dumps({"name": name})
        result = _run_cli("package", "create", "--input", pkg_json)
        assert result.returncode == 0, f"Failed to create root package: {result.stderr}"
        return name

    @staticmethod
    def _create_nested_package(parent_path: str, name: str) -> str:
        """Create a nested package under a parent via CLI and return its path.

        Args:
            parent_path: Parent package path (e.g., "ParentPkg").
            name: Package name to create.

        Returns:
            Full path of the created package (e.g., "ParentPkg/ChildPkg").
        """
        pkg_json = json.dumps({"name": name})
        result = _run_cli("package", "create", "--path", parent_path, "--input", pkg_json)
        assert result.returncode == 0, f"Failed to create nested package: {result.stderr}"
        return f"{parent_path}/{name}"

    def test_package_create_at_root(self, cli_project: str) -> None:
        """Test creating a package at project root (omit --path)."""
        pkg_name = _unique_name("Pkg")
        pkg_json = json.dumps({"name": pkg_name})

        # Omit --path to create at project root
        result = _run_cli("package", "create", "--input", pkg_json)
        assert result.returncode == 0, f"Failed: {result.stderr}"

        # Verify via package view (package list cannot operate on project root)
        view_result = _run_cli("package", "view", "--path", pkg_name, "--format", "json")
        assert view_result.returncode == 0, f"View failed: {view_result.stderr}"
        data = json.loads(view_result.stdout)
        assert data["name"] == pkg_name

        # Cleanup
        _run_cli("package", "delete", "--path", pkg_name)

    def test_package_create_nested(self, cli_project: str) -> None:
        """Test creating a nested package under another package."""
        parent_name = _unique_name("ParentPkg")
        child_name = _unique_name("ChildPkg")

        try:
            # Create parent at root
            parent_path = self._create_root_package(parent_name)

            # Create child under parent
            self._create_nested_package(parent_path, child_name)

            # Verify child appears in parent's list
            list_result = _run_cli("package", "list", "--path", parent_path, "--format", "json")
            assert list_result.returncode == 0
            packages = json.loads(list_result.stdout)
            assert child_name in packages
        finally:
            # Cleanup parent (deletes children too)
            _run_cli("package", "delete", "--path", parent_name)

    def test_package_view_existing(self, cli_project: str) -> None:
        """Test viewing an existing package."""
        pkg_name = _unique_name("ViewPkg")
        pkg_path = self._create_root_package(pkg_name)

        try:
            result = _run_cli("package", "view", "--path", pkg_path, "--format", "json")
            assert result.returncode == 0, f"Failed: {result.stderr}"
            data = json.loads(result.stdout)
            assert data["name"] == pkg_name
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_package_view_nonexistent(self, cli_project: str) -> None:
        """Test viewing a non-existent package returns error."""
        result = _run_cli("package", "view", "--path", f"NonExistentPkg_{uuid.uuid4().hex[:8]}")
        assert result.returncode != 0
        assert "error" in result.stderr.lower() or "not found" in result.stderr.lower() or "failed" in result.stderr.lower()

    def test_package_list_in_package(self, cli_project: str) -> None:
        """Test listing nested packages within a package."""
        parent_name = _unique_name("ListParent")
        child1_name = _unique_name("Child1")
        child2_name = _unique_name("Child2")

        try:
            parent_path = self._create_root_package(parent_name)
            self._create_nested_package(parent_path, child1_name)
            self._create_nested_package(parent_path, child2_name)

            result = _run_cli("package", "list", "--path", parent_path, "--format", "json")
            assert result.returncode == 0
            packages = json.loads(result.stdout)
            assert child1_name in packages
            assert child2_name in packages
        finally:
            _run_cli("package", "delete", "--path", parent_name)

    def test_package_delete_existing(self, cli_project: str) -> None:
        """Test deleting an existing package."""
        pkg_name = _unique_name("DelPkg")
        pkg_path = self._create_root_package(pkg_name)

        result = _run_cli("package", "delete", "--path", pkg_path)
        assert result.returncode == 0, f"Failed: {result.stderr}"

        # Verify package is gone
        view_result = _run_cli("package", "view", "--path", pkg_path)
        assert view_result.returncode != 0

    def test_package_delete_nonexistent(self, cli_project: str) -> None:
        """Test deleting a non-existent package returns error."""
        result = _run_cli("package", "delete", "--path", f"NonExistentDel_{uuid.uuid4().hex[:8]}")
        assert result.returncode != 0
        assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()

    def test_package_create_invalid_json(self, cli_project: str) -> None:
        """Test that invalid JSON input returns error."""
        result = _run_cli("package", "create", "--input", "{invalid json}")
        assert result.returncode != 0
        assert "json" in result.stderr.lower() or "error" in result.stderr.lower()
