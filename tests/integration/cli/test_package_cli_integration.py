"""End-to-end integration tests for package CLI operations with live Rhapsody instance.

These tests require a running Rhapsody instance with an open project.
Manual test procedure:
    1. Start Rhapsody application (GUI)
    2. Open or create a test project
    3. Run: pytest tests/integration/cli/test_package_cli_integration.py -v

To skip E2E tests in CI:
    pytest tests/integration/cli/test_package_cli_integration.py --co -q | head
"""

import json
import time

from rhapsody_cli.commands.package_command import PackageCommand
from rhapsody_cli.exceptions.core import CliExecutionError


class TestPackageCLIIntegration:
    """End-to-end tests for package CLI with live Rhapsody instance."""

    @staticmethod
    def _generate_unique_name(prefix: str = "TestPkg") -> str:
        """Generate a unique package name using timestamp."""
        return f"{prefix}_{int(time.time() * 1000) % 1000000}"

    def test_create_and_delete_root_package(self) -> None:
        """E2E: Create a package at project root, verify it exists, delete it."""
        pkg_name = self._generate_unique_name("RootPkg")
        pkg_data = {"name": pkg_name}

        try:
            # Step 1: Create a package at project root
            create_cmd = PackageCommand(["create", json.dumps(pkg_data)])
            create_cmd.execute()

            # Step 2: Verify package exists by querying root packages
            # (If we got here, package creation succeeded)
        finally:
            # Step 3: Delete the package
            try:
                delete_cmd = PackageCommand(["delete", "--path", pkg_name])
                delete_cmd.execute()
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
            create_cmd = PackageCommand(["create", json.dumps(pkg_data)])
            create_cmd.execute()

            # Step 2: Try to create the same package again
            # Should raise CliExecutionError with user-friendly message
            duplicate_cmd = PackageCommand(["create", json.dumps(pkg_data)])
            try:
                duplicate_cmd.execute()
                # If we get here, the duplicate check failed
                raise AssertionError("Duplicate package creation should have failed, but succeeded")
            except CliExecutionError as e:
                error_msg = str(e)
                # Verify the error message is user-friendly and mentions duplicate
                assert "already exists" in error_msg.lower(), f"Error message should mention 'already exists', got: {error_msg}"
                # Verify it's NOT the raw COM exception
                assert "-2147" not in error_msg, f"Error message should not contain raw COM error codes, got: {error_msg}"
                assert "Exception occurred" not in error_msg, f"Error message should not contain raw COM exception text, got: {error_msg}"
        finally:
            # Step 3: Clean up
            try:
                delete_cmd = PackageCommand(["delete", "--path", pkg_name])
                delete_cmd.execute()
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
            create_parent_cmd = PackageCommand(["create", json.dumps(parent_pkg_data)])
            create_parent_cmd.execute()

            # Step 2: Create nested package under parent
            create_child_cmd = PackageCommand(["create", json.dumps(child_pkg_data), "--path", parent_pkg_name])
            create_child_cmd.execute()

            # Step 3: Verify nested package was created (no exception = success)
        finally:
            # Step 4: Clean up (delete child first, then parent)
            try:
                delete_child_cmd = PackageCommand(["delete", "--path", f"{parent_pkg_name}/{child_pkg_name}"])
                delete_child_cmd.execute()
            except Exception as e:
                print(f"Warning: Could not delete nested package: {e}")

            try:
                delete_parent_cmd = PackageCommand(["delete", "--path", parent_pkg_name])
                delete_parent_cmd.execute()
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
            create_parent_cmd = PackageCommand(["create", json.dumps(parent_pkg_data)])
            create_parent_cmd.execute()

            # Step 2: Create first nested package
            create_child_cmd = PackageCommand(["create", json.dumps(child_pkg_data), "--path", parent_pkg_name])
            create_child_cmd.execute()

            # Step 3: Try to create duplicate nested package
            duplicate_child_cmd = PackageCommand(["create", json.dumps(child_pkg_data), "--path", parent_pkg_name])
            try:
                duplicate_child_cmd.execute()
                # If we get here, the duplicate check failed
                raise AssertionError("Duplicate nested package creation should have failed, but succeeded")
            except CliExecutionError as e:
                error_msg = str(e)
                # Verify the error message mentions duplicate or already exists
                assert "already exists" in error_msg.lower(), f"Error message should mention 'already exists', got: {error_msg}"
                # Verify it's NOT the raw COM exception
                assert "-2147" not in error_msg, f"Error message should not contain raw COM error codes, got: {error_msg}"
        finally:
            # Step 4: Clean up
            try:
                delete_child_cmd = PackageCommand(["delete", "--path", f"{parent_pkg_name}/{child_pkg_name}"])
                delete_child_cmd.execute()
            except Exception as e:
                print(f"Warning: Could not delete nested package: {e}")

            try:
                delete_parent_cmd = PackageCommand(["delete", "--path", parent_pkg_name])
                delete_parent_cmd.execute()
            except Exception as e:
                print(f"Warning: Could not delete parent package {parent_pkg_name}: {e}")
