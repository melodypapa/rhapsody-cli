"""Tests for element command classes."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from click.testing import CliRunner

from rhapsody_cli.cli.commands.element import ElementCommandGroup
from rhapsody_cli.cli.context import RhapsodyContext
from rhapsody_cli.exceptions import RhapsodyConnectionError


class TestElementCommandGroup:
    """Tests for ElementCommandGroup."""

    def test_element_group_has_add_command(self) -> None:
        """Test: ElementCommandGroup includes add command."""
        group = ElementCommandGroup()
        assert "add" in group.commands
        assert group.commands["add"].name == "add"

    def test_element_group_has_view_command(self) -> None:
        """Test: ElementCommandGroup includes view command."""
        group = ElementCommandGroup()
        assert "view" in group.commands
        assert group.commands["view"].name == "view"

    def test_element_group_has_query_command(self) -> None:
        """Test: ElementCommandGroup includes query command."""
        group = ElementCommandGroup()
        assert "query" in group.commands
        assert group.commands["query"].name == "query"

    def test_element_group_name_is_element(self) -> None:
        """Test: ElementCommandGroup name is 'element'."""
        group = ElementCommandGroup()
        assert group.name == "element"

    def test_element_group_has_help(self) -> None:
        """Test: ElementCommandGroup has help text."""
        group = ElementCommandGroup()
        assert group.help is not None
        assert "element" in group.help.lower()


class TestAddElementCommand:
    """Tests for AddElementCommand."""

    def test_add_command_name_is_add(self) -> None:
        """Test: add command name is 'add'."""
        group = ElementCommandGroup()
        add_cmd = group.commands["add"]
        assert add_cmd.name == "add"

    def test_add_command_has_help(self) -> None:
        """Test: add command has help text."""
        group = ElementCommandGroup()
        add_cmd = group.commands["add"]
        assert add_cmd.help is not None
        assert "add" in add_cmd.help.lower()


class TestViewElementCommand:
    """Tests for ViewElementCommand."""

    def test_view_command_name_is_view(self) -> None:
        """Test: view command name is 'view'."""
        group = ElementCommandGroup()
        view_cmd = group.commands["view"]
        assert view_cmd.name == "view"

    def test_view_command_has_help(self) -> None:
        """Test: view command has help text."""
        group = ElementCommandGroup()
        view_cmd = group.commands["view"]
        assert view_cmd.help is not None
        assert "view" in view_cmd.help.lower()


class TestQueryElementCommand:
    """Tests for QueryElementCommand."""

    def test_query_command_name_is_query(self) -> None:
        """Test: query command name is 'query'."""
        group = ElementCommandGroup()
        query_cmd = group.commands["query"]
        assert query_cmd.name == "query"

    def test_query_command_has_help(self) -> None:
        """Test: query command has help text."""
        group = ElementCommandGroup()
        query_cmd = group.commands["query"]
        assert query_cmd.help is not None
        assert "query" in query_cmd.help.lower()


class TestAddElementCommandAttachBehavior:
    """Tests for AddElementCommand attaching to the live Rhapsody instance."""

    def test_add_command_creates_class_on_active_project(self) -> None:
        """Test: add --type class calls createClass on the active project's root."""
        runner = CliRunner()
        group = ElementCommandGroup()

        fake_root = MagicMock(name="FakeRoot")
        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            result = runner.invoke(group, ["add", "--type", "class", "--name", "Foo"])

        assert result.exit_code == 0
        fake_root.createClass.assert_called_once_with("Foo")
        assert "Created class: Foo" in result.output

    def test_add_command_reports_no_running_instance(self) -> None:
        """Test: add command reports a clear message when no Rhapsody is running."""
        runner = CliRunner()
        group = ElementCommandGroup()

        with patch.object(
            RhapsodyContext,
            "get_active_project",
            side_effect=RhapsodyConnectionError("No running Rhapsody instance found"),
        ):
            result = runner.invoke(group, ["add", "--type", "class", "--name", "Foo"])

        assert result.exit_code != 0
        assert (
            "No running Rhapsody instance found. Please open Rhapsody and a project first."
            in result.output
        )


class TestQueryElementCommandAttachBehavior:
    """Tests for QueryElementCommand attaching to the live Rhapsody instance."""

    def test_query_command_lists_elements_from_active_project(self) -> None:
        """Test: query command lists elements from the active project's root."""
        runner = CliRunner()
        group = ElementCommandGroup()

        fake_element = MagicMock(name="FakeElement")
        fake_element.getName.return_value = "MyClass"
        fake_element.getMetaClass.return_value = "Class"

        fake_root = MagicMock(name="FakeRoot")
        fake_root.getNestedElements.return_value = [fake_element]

        fake_project = MagicMock(name="FakeProject")
        fake_project.getRoot.return_value = fake_root

        def fake_get_active_project(self: RhapsodyContext) -> MagicMock:
            self.project = fake_project
            return fake_project

        with patch.object(RhapsodyContext, "get_active_project", fake_get_active_project):
            result = runner.invoke(group, ["query"])

        assert result.exit_code == 0
        assert "MyClass" in result.output

    def test_query_command_reports_no_running_instance(self) -> None:
        """Test: query command reports a clear message when no Rhapsody is running."""
        runner = CliRunner()
        group = ElementCommandGroup()

        with patch.object(
            RhapsodyContext,
            "get_active_project",
            side_effect=RhapsodyConnectionError("No running Rhapsody instance found"),
        ):
            result = runner.invoke(group, ["query"])

        assert result.exit_code != 0
        assert (
            "No running Rhapsody instance found. Please open Rhapsody and a project first."
            in result.output
        )
