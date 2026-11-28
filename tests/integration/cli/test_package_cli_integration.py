"""End-to-end integration tests for package CLI operations with a live Rhapsody instance.

These tests require a running Rhapsody instance (GUI or headless). The
``test_project`` fixture (from ``tests/integration/conftest.py``) automatically
creates and activates an isolated project at ``demos/test_project/`` before
these tests run, and cleans it up afterward — no manually-opened project is
required.

Run:
    pytest tests/integration/cli/test_package_cli_integration.py -v
"""

import json
import uuid
from typing import List

import pytest

from rhapsody_cli.cli.cli import build_registry, build_root_parser
from rhapsody_cli.exceptions.core import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestPackageCLIIntegration:
    """End-to-end tests for package CLI with live Rhapsody instance."""

    @pytest.fixture(autouse=True)
    def _use_test_project(self, test_project: IRPProject) -> None:
        """Ensure the isolated integration test_project is active for every test."""
        self.project = test_project

    @staticmethod
    def _run_command(argv: List[str]) -> None:
        """Run a CLI command end-to-end through the registry root parser."""
        parser = build_root_parser(build_registry())
        namespace = parser.parse_args(argv)
        namespace.entry.run(namespace)

    @staticmethod
    def _generate_unique_name(prefix: str = "TestPkg") -> str:
        """Generate a unique package name using a UUID suffix."""
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_create_and_delete_root_package(self) -> None:
        """E2E: Create a package at project root, verify it exists, delete it."""
        pkg_name = self._generate_unique_name("RootPkg")
        pkg_data = {"name": pkg_name}

        try:
            # Step 1: Create a package at project root
            self._run_command(["create", json.dumps(pkg_data)])

            # Step 2: Verify package exists via model API
            pkg_names = [p.name for p in self.project.packages]
            assert pkg_name in pkg_names, f"Package '{pkg_name}' should exist after creation"
        finally:
            # Step 3: Delete the package
            try:
                self._run_command(["delete", "--path", pkg_name])
            except Exception as e:
                print(f"Warning: Could not delete package {pkg_name}: {e}")

    def test_duplicate_package_detection_with_friendly_error(self) -> None:
        """E2E: Create a package, then try to create the same package again.

        Verify that the error message is user-friendly (not a raw COM exception).
        This tests SWR_PKG_0015: Duplicate package detection.
        """
        pkg_name = self._generate_unique_name("DupPkg")
        pkg_data = {"name": pkg_name}

        try:
            # Step 1: Create a package at project root
            self._run_command(["create", json.dumps(pkg_data)])

            # Step 1b: Verify package exists via model API
            pkg_names = [p.name for p in self.project.packages]
            assert pkg_name in pkg_names, f"Package '{pkg_name}' should exist after creation"

            # Step 2: Try to create the same package again
            # Should raise CliExecutionError with user-friendly message
            with pytest.raises(CliExecutionError, match="already exists") as exc_info:
                self._run_command(["create", json.dumps(pkg_data)])
            error_msg = str(exc_info.value)
            # Verify it's NOT the raw COM exception
            assert "-2147" not in error_msg, f"Error message should not contain raw COM error codes, got: {error_msg}"
            assert "Exception occurred" not in error_msg, f"Error message should not contain raw COM exception text, got: {error_msg}"

            # Step 2b: Verify there's still exactly one package (duplicate was rejected)
            pkg_names_after = [p.name for p in self.project.packages]
            matches = [n for n in pkg_names_after if n == pkg_name]
            assert len(matches) == 1, f"Should be exactly one package named '{pkg_name}', found {len(matches)}"
        finally:
            # Step 3: Clean up
            try:
                self._run_command(["delete", "--path", pkg_name])
            except Exception as e:
                print(f"Warning: Could not delete package {pkg_name}: {e}")

    def test_create_nested_package(self) -> None:
        """E2E: Create a nested package under a parent package."""
        parent_pkg_name = self._generate_unique_name("Parent")
        child_pkg_name = self._generate_unique_name("Child")
        parent_pkg_data = {"name": parent_pkg_name}
        child_pkg_data = {"name": child_pkg_name}

        try:
            # Step 1: Create parent package at project root
            self._run_command(["create", json.dumps(parent_pkg_data)])

            # Step 2: Create nested package under parent
            self._run_command(["create", json.dumps(child_pkg_data), "--path", parent_pkg_name])

            # Step 3: Verify nested package exists via model API
            pkgs = self.project.packages
            parent = next((p for p in pkgs if p.name == parent_pkg_name), None)
            assert parent is not None, f"Parent package '{parent_pkg_name}' should exist"
            child_names = [c.name for c in parent.packages]
            assert child_pkg_name in child_names, f"Child package '{child_pkg_name}' should exist under parent"
        finally:
            # Step 4: Clean up (delete child first, then parent)
            try:
                self._run_command(["delete", "--path", f"{parent_pkg_name}/{child_pkg_name}"])
            except Exception as e:
                print(f"Warning: Could not delete nested package: {e}")

            try:
                self._run_command(["delete", "--path", parent_pkg_name])
            except Exception as e:
                print(f"Warning: Could not delete parent package {parent_pkg_name}: {e}")

    def test_duplicate_nested_package_detection(self) -> None:
        """E2E: Create a nested package, try to create duplicate in same parent.

        Verify that duplicate detection works for nested packages too.
        """
        parent_pkg_name = self._generate_unique_name("ParentDup")
        child_pkg_name = self._generate_unique_name("ChildDup")
        parent_pkg_data = {"name": parent_pkg_name}
        child_pkg_data = {"name": child_pkg_name}

        try:
            # Step 1: Create parent package at project root
            self._run_command(["create", json.dumps(parent_pkg_data)])

            # Step 2: Create first nested package
            self._run_command(["create", json.dumps(child_pkg_data), "--path", parent_pkg_name])

            # Step 2b: Verify child exists via model API
            pkgs = self.project.packages
            parent = next((p for p in pkgs if p.name == parent_pkg_name), None)
            assert parent is not None, f"Parent package '{parent_pkg_name}' should exist"
            child_names = [c.name for c in parent.packages]
            assert child_pkg_name in child_names, f"Child package '{child_pkg_name}' should exist under parent"

            # Step 3: Try to create duplicate nested package
            with pytest.raises(CliExecutionError, match="already exists") as exc_info:
                self._run_command(["create", json.dumps(child_pkg_data), "--path", parent_pkg_name])
            error_msg = str(exc_info.value)
            # Verify it's NOT the raw COM exception
            assert "-2147" not in error_msg, f"Error message should not contain raw COM error codes, got: {error_msg}"

            # Step 3b: Verify there's still exactly one child (duplicate was rejected)
            child_names_after = [c.name for c in parent.packages]
            matches = [n for n in child_names_after if n == child_pkg_name]
            assert len(matches) == 1, f"Should be exactly one child named '{child_pkg_name}', found {len(matches)}"
        finally:
            # Step 4: Clean up
            try:
                self._run_command(["delete", "--path", f"{parent_pkg_name}/{child_pkg_name}"])
            except Exception as e:
                print(f"Warning: Could not delete nested package: {e}")

            try:
                self._run_command(["delete", "--path", parent_pkg_name])
            except Exception as e:
                print(f"Warning: Could not delete parent package {parent_pkg_name}: {e}")
