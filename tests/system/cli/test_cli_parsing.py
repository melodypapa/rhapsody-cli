"""CLI parsing and argument validation tests.

These tests do NOT require a running Rhapsody instance — they test
the CLI's argument parsing, help output, and error handling.
"""

import pytest

from tests.system.cli.conftest import _run_cli


@pytest.mark.system
class TestCLIParsing:
    """Test CLI argument parsing, help, and error messages."""

    def test_cli_help_command(self) -> None:
        """Test that --help returns 0 and shows usage."""
        result = _run_cli("--help")
        assert result.returncode == 0
        assert "Usage:" in result.stdout or "usage:" in result.stdout.lower()

    def test_cli_no_arguments_shows_usage(self) -> None:
        """Test that running with no arguments shows usage and exits 0."""
        result = _run_cli()
        # main._usage("") prints usage to stdout and exits 0 (no error)
        assert result.returncode == 0
        assert "Usage:" in result.stdout or "usage:" in result.stdout.lower()

    def test_cli_invalid_command(self) -> None:
        """Test that unknown commands are rejected."""
        result = _run_cli("invalid_command_xyz")
        assert result.returncode != 0
        assert "Unknown command" in result.stderr or "invalid choice" in result.stderr.lower() or "Error" in result.stderr

    def test_cli_verbose_flag_accepted(self) -> None:
        """Test that --verbose flag is accepted at subcommand level."""
        result = _run_cli("class", "list", "--path", "DummyPkg", "--verbose")
        # May fail with Rhapsody error, but should not have unrecognized arguments
        assert "unrecognized arguments" not in result.stderr.lower()

    def test_class_create_missing_path(self) -> None:
        """Test that class create without --path shows usage error."""
        result = _run_cli("class", "create")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_class_create_missing_input(self) -> None:
        """Test that class create with --path but no input shows error."""
        result = _run_cli("class", "create", "--path", "TestProject::Pkg")
        assert result.returncode != 0
        # Should complain about missing input data
        assert "input" in result.stderr.lower() or "attributes" in result.stderr.lower() or "error" in result.stderr.lower()

    def test_class_delete_missing_arguments(self) -> None:
        """Test that class delete without --path or --guid shows error."""
        result = _run_cli("class", "delete")
        assert result.returncode != 0
        assert "error" in result.stderr.lower() or "usage" in result.stderr.lower()

    def test_package_delete_missing_path(self) -> None:
        """Test that package delete without --path shows usage error."""
        result = _run_cli("package", "delete")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_attribute_create_missing_path(self) -> None:
        """Test that attribute create without --path shows usage error."""
        result = _run_cli("attribute", "create")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_operation_create_missing_path(self) -> None:
        """Test that operation create without --path shows usage error."""
        result = _run_cli("operation", "create")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_port_create_missing_path(self) -> None:
        """Test that port create without --path shows usage error."""
        result = _run_cli("port", "create")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_project_open_missing_arguments(self) -> None:
        """Test that project open without project_path shows usage error."""
        result = _run_cli("project", "open")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_project_new_missing_arguments(self) -> None:
        """Test that project new without arguments shows usage error."""
        result = _run_cli("project", "new")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_class_list_with_invalid_format(self) -> None:
        """Test that invalid --format value is rejected."""
        result = _run_cli("class", "list", "--path", "Dummy", "--format", "xml")
        assert result.returncode != 0
        assert "invalid choice" in result.stderr.lower() or "usage" in result.stderr.lower()

    def test_class_view_missing_path_and_guid(self) -> None:
        """Test that class view without --path or --guid shows error."""
        result = _run_cli("class", "view")
        assert result.returncode != 0
        assert "error" in result.stderr.lower() or "usage" in result.stderr.lower()
