"""System tests for the `operation` CLI command group.

Tests operation CRUD lifecycle via subprocess against a live Rhapsody project.

Path notes: Paths use "/" separator. Operation view/delete require TWO
args: --path <class_path> AND --name <op_name> (or --guid). They do NOT
accept a combined element path.
"""

import json
import uuid

import pytest

from tests.system.cli.conftest import _run_cli, _unique_name


@pytest.mark.system
class TestOperationCLI:
    """Test operation CLI commands via subprocess."""

    @pytest.fixture(autouse=True)
    def _require_rhapsody(self, _require_rhapsody: None) -> None:
        """Skip these tests if no Rhapsody instance is available."""

    @staticmethod
    def _create_package_and_class(pkg_name: str, cls_name: str) -> tuple[str, str]:
        """Create a package at root and a class under it.

        Returns:
            Tuple of (pkg_path, cls_path). Both use "/" separator.
        """
        pkg_json = json.dumps({"name": pkg_name})
        result = _run_cli("package", "create", "--input", pkg_json)
        assert result.returncode == 0, f"Failed to create package: {result.stderr}"
        pkg_path = pkg_name

        cls_json = json.dumps({"name": cls_name})
        result = _run_cli("class", "create", "--path", pkg_path, "--input", cls_json)
        assert result.returncode == 0, f"Failed to create class: {result.stderr}"
        cls_path = f"{pkg_path}/{cls_name}"
        return pkg_path, cls_path

    def test_operation_create_under_class(self, cli_project: str) -> None:
        """Test creating an operation under a class."""
        pkg_name = _unique_name("OpPkg")
        cls_name = _unique_name("OpCls")
        op_name = _unique_name("myOp")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            op_json = json.dumps({"name": op_name})
            result = _run_cli("operation", "create", "--path", cls_path, "--input", op_json)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify via list
            list_result = _run_cli("operation", "list", "--path", cls_path, "--format", "json")
            assert list_result.returncode == 0
            operations = json.loads(list_result.stdout)
            assert op_name in operations
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_operation_view_existing(self, cli_project: str) -> None:
        """Test viewing an existing operation via --path + --name."""
        pkg_name = _unique_name("ViewPkg")
        cls_name = _unique_name("ViewCls")
        op_name = _unique_name("viewOp")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            op_json = json.dumps({"name": op_name})
            _run_cli("operation", "create", "--path", cls_path, "--input", op_json)

            # View uses --path <class_path> --name <op_name> (NOT a combined path)
            result = _run_cli("operation", "view", "--path", cls_path, "--name", op_name, "--format", "json")
            assert result.returncode == 0, f"Failed: {result.stderr}"
            data = json.loads(result.stdout)
            assert data["name"] == op_name
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_operation_view_nonexistent(self, cli_project: str) -> None:
        """Test viewing a non-existent operation returns error."""
        pkg_name = _unique_name("NoOpPkg")
        cls_name = _unique_name("NoOpCls")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            # View uses --path + --name (not a combined path)
            result = _run_cli(
                "operation", "view",
                "--path", cls_path,
                "--name", f"NonExistent_{uuid.uuid4().hex[:8]}",
            )
            assert result.returncode != 0
            assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_operation_list_in_class(self, cli_project: str) -> None:
        """Test listing operations in a class."""
        pkg_name = _unique_name("ListPkg")
        cls_name = _unique_name("ListCls")
        op1_name = _unique_name("op1")
        op2_name = _unique_name("op2")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            _run_cli("operation", "create", "--path", cls_path, "--input", json.dumps({"name": op1_name}))
            _run_cli("operation", "create", "--path", cls_path, "--input", json.dumps({"name": op2_name}))

            result = _run_cli("operation", "list", "--path", cls_path, "--format", "json")
            assert result.returncode == 0
            operations = json.loads(result.stdout)
            assert op1_name in operations
            assert op2_name in operations
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_operation_delete_existing(self, cli_project: str) -> None:
        """Test deleting an existing operation via --path + --name."""
        pkg_name = _unique_name("DelPkg")
        cls_name = _unique_name("DelCls")
        op_name = _unique_name("delOp")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            _run_cli("operation", "create", "--path", cls_path, "--input", json.dumps({"name": op_name}))

            # Delete uses --path <class_path> --name <op_name> (NOT a combined path)
            result = _run_cli("operation", "delete", "--path", cls_path, "--name", op_name)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify operation is gone
            list_result = _run_cli("operation", "list", "--path", cls_path, "--format", "json")
            assert list_result.returncode == 0
            operations = json.loads(list_result.stdout)
            assert op_name not in operations
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_operation_delete_nonexistent(self, cli_project: str) -> None:
        """Test deleting a non-existent operation returns error."""
        pkg_name = _unique_name("NoDelPkg")
        cls_name = _unique_name("NoDelCls")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            # Delete uses --path + --name
            result = _run_cli(
                "operation", "delete",
                "--path", cls_path,
                "--name", f"NonExistent_{uuid.uuid4().hex[:8]}",
            )
            assert result.returncode != 0
            assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_operation_create_invalid_json(self, cli_project: str) -> None:
        """Test that invalid JSON input returns error."""
        pkg_name = _unique_name("BadJsonPkg")
        cls_name = _unique_name("BadJsonCls")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            result = _run_cli("operation", "create", "--path", cls_path, "--input", "{invalid}")
            assert result.returncode != 0
            assert "json" in result.stderr.lower() or "error" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)
