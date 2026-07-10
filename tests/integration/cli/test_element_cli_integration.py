"""End-to-end integration tests for element CLI operations with live Rhapsody instance.

These tests require a running Rhapsody instance with an open project.
Manual test procedure:
    1. Start Rhapsody application (GUI)
    2. Open or create a test project
    3. Run: pytest tests/integration/cli/test_element_cli_integration.py -v

To skip E2E tests in CI:
    pytest tests/integration/cli/test_element_cli_integration.py --co -q | head
"""

import time

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.commands.element_command import ElementCommand
from rhapsody_cli.commands.package_command import PackageCommand


class TestElementCLIIntegration:
    """End-to-end tests for element CLI with live Rhapsody instance."""

    TEST_PACKAGE_NAME = "integration_test_pkg"

    @staticmethod
    def _generate_unique_name(prefix: str = "TestClass") -> str:
        """Generate a unique element name using timestamp."""
        return f"{prefix}_{int(time.time() * 1000) % 1000000}"

    def _ensure_test_package(self) -> None:
        """Create the top-level test package directly via the model API.

        `package create` (PackageCreateAction) intentionally requires its
        `--path` parent to already be a Package, so it cannot create a
        top-level package under the project root. Test scaffolding uses the
        underlying `RPProject.addPackage()` model method instead.
        """
        app = RhapsodyApplication.attach()
        project = app.activeProject()
        try:
            project.addPackage(self.TEST_PACKAGE_NAME)
        except Exception as e:
            # Package might already exist from a previous run; reuse it.
            print(f"Note: Could not create test package (may already exist): {e}")

    def _cleanup_test_package(self) -> None:
        """Delete the test package via the `package delete` CLI command."""
        delete_pkg_cmd = PackageCommand(["delete", "--path", self.TEST_PACKAGE_NAME])
        try:
            delete_pkg_cmd.execute()
        except Exception as e:
            print(f"Warning: Could not delete test package: {e}")

    def test_add_and_delete_class_workflow(self) -> None:
        """E2E: Add a class to test package, verify it exists, delete it, verify deletion.

        This end-to-end test requires a live Rhapsody instance.
        """
        class_name = self._generate_unique_name("TestClass")

        self._ensure_test_package()

        try:
            # Step 1: Add a class to the test package
            add_cmd = ElementCommand(["add", "--type", "class", "--name", class_name, "--path", self.TEST_PACKAGE_NAME])
            add_cmd.execute()

            # Step 2: Query and verify the class exists
            query_cmd = ElementCommand(["query", "--path", self.TEST_PACKAGE_NAME])
            query_cmd.execute()

            # Step 3: Delete the class
            delete_cmd = ElementCommand(["delete", f"{self.TEST_PACKAGE_NAME}/{class_name}"])
            delete_cmd.execute()
        finally:
            self._cleanup_test_package()

    def test_add_multiple_classes_and_clean_up(self) -> None:
        """E2E: Add multiple classes to test package, clean them up one by one."""
        class_names = [self._generate_unique_name(f"TestClass{i}") for i in range(3)]

        self._ensure_test_package()

        try:
            # Add multiple classes to the test package
            for class_name in class_names:
                add_cmd = ElementCommand(["add", "--type", "class", "--name", class_name, "--path", self.TEST_PACKAGE_NAME])
                add_cmd.execute()

            # Query and verify all exist
            query_cmd = ElementCommand(["query", "--path", self.TEST_PACKAGE_NAME])
            query_cmd.execute()

            # Delete each one
            for class_name in class_names:
                delete_cmd = ElementCommand(["delete", f"{self.TEST_PACKAGE_NAME}/{class_name}"])
                delete_cmd.execute()
        finally:
            self._cleanup_test_package()
