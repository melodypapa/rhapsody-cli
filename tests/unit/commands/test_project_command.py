"""Tests for project actions and the ProjectCommand dispatcher."""

import argparse
import os
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.actions.project_action import (
    ProjectCloseAction,
    ProjectListAction,
    ProjectNewAction,
    ProjectOpenAction,
)
from rhapsody_cli.commands.project_command import ProjectCommand
from rhapsody_cli.exceptions import CliExecutionError


class TestProjectCommandDispatch:
    """Tests for the ProjectCommand group dispatcher."""

    def test_open_subcommand_dispatches(self) -> None:
        """Test: 'open' subcommand is parsed correctly."""
        cmd = ProjectCommand(["open", "MyProject.rpy"])
        assert cmd._subcommand == "open"

    def test_missing_subcommand_exits(self) -> None:
        """Test: no subcommand raises CliExecutionError."""
        with pytest.raises(CliExecutionError):
            ProjectCommand([])


class TestProjectOpenAction:
    """Tests for ProjectOpenAction."""

    def test_open_action_execute_signature(self) -> None:
        """Test: ProjectOpenAction has execute method."""
        action = ProjectOpenAction()
        assert hasattr(action, "execute")
        assert callable(action.execute)

    def test_open_action_calls_open_project_on_connected_app(self, tmp_path: Path) -> None:
        """Test: open action connects, then calls app.open_project() with the given path."""
        project_file = tmp_path / "MyProject.rpy"
        project_file.write_text("")
        action = ProjectOpenAction()
        args = argparse.Namespace(project_path=str(project_file), verbose=False)
        fake_project = MagicMock(name="FakeProject")
        fake_app = MagicMock(name="FakeApplication")
        fake_app.open_project.return_value = fake_project

        with patch.object(ProjectOpenAction, "_connect_app", return_value=fake_app):
            # pi-lens-ignore: python-sql-injection
            # AbstractAction.execute() is CLI action dispatch, not a DB sink.
            action.execute(args)

        fake_app.open_project.assert_called_once_with(str(project_file))
        assert action._project is fake_project

    def test_open_action_raises_for_missing_file_without_connecting(self) -> None:
        """COM openProject returns an empty project for a nonexistent file
        (Rhapsody then reports zero open projects); the action must fail fast
        with a clear error before touching COM (smoke test finding)."""
        action = ProjectOpenAction()
        args = argparse.Namespace(project_path="Z:/no/such/SmokeProj.rpyx", verbose=False)

        with patch.object(ProjectOpenAction, "_connect_app") as mock_connect:
            with pytest.raises(CliExecutionError, match="Project file not found"):
                # pi-lens-ignore: python-sql-injection
                # AbstractAction.execute() is CLI action dispatch, not a DB sink.
                action.execute(args)

        mock_connect.assert_not_called()


class TestProjectListAction:
    """Tests for ProjectListAction."""

    def test_list_action_prints_name_and_filename_for_each_project(self) -> None:
        """Regression test: the list action must call get_filename() (not the
        non-existent get_path()) on each project to render its table row."""
        action = ProjectListAction()
        args = argparse.Namespace(verbose=False)

        fake_project = MagicMock(name="FakeProject")
        fake_project.get_name.return_value = "MyProject"
        fake_project.get_filename.return_value = "C:/models/MyProject.rpyx"
        fake_app = MagicMock(name="FakeApplication")
        fake_app.get_projects.return_value = [fake_project]

        with patch.object(ProjectListAction, "_connect_app", return_value=fake_app):
            # Should not raise
            # pi-lens-ignore: python-sql-injection
            # AbstractAction.execute() is CLI action dispatch, not a DB sink.
            action.execute(args)

        fake_project.get_filename.assert_called_once_with()


class TestProjectCloseAction:
    """Tests for ProjectCloseAction."""

    def test_close_action_execute_signature(self) -> None:
        """Test: ProjectCloseAction has execute method."""
        action = ProjectCloseAction()
        assert hasattr(action, "execute")
        assert callable(action.execute)

    def test_close_action_does_nothing_when_no_project_cached(self) -> None:
        """Test: close is a no-op (does not raise) when no project has been opened yet."""
        action = ProjectCloseAction()
        args = argparse.Namespace(verbose=False)

        # pi-lens-ignore: python-sql-injection
        # AbstractAction.execute() is CLI action dispatch, not a DB sink.
        action.execute(args)  # Should not raise

        assert action._project is None

    def test_close_action_closes_and_clears_cached_project(self) -> None:
        """Test: close calls project.close() and clears the cached project."""
        action = ProjectCloseAction()
        args = argparse.Namespace(verbose=False)
        fake_project = MagicMock(name="FakeProject")
        action._project = fake_project

        # pi-lens-ignore: python-sql-injection
        # AbstractAction.execute() is CLI action dispatch, not a DB sink.
        action.execute(args)

        fake_project.close.assert_called_once_with()
        assert action._project is None


class TestProjectNewAction:
    """Tests for ProjectNewAction."""

    def test_new_action_calls_create_project_with_absolute_location(self, tmp_path: Path) -> None:
        """Test: new action delegates to app.create_new_project with an absolute location."""
        action = ProjectNewAction()
        args = argparse.Namespace(project_location=str(tmp_path), project_name="MyNewProject", verbose=False)
        fake_project = MagicMock(name="FakeProject")
        fake_app = MagicMock(name="FakeApplication")
        fake_app.create_new_project.return_value = fake_project

        with patch.object(ProjectNewAction, "_connect_app", return_value=fake_app):
            # pi-lens-ignore: python-sql-injection
            # AbstractAction.execute() is CLI action dispatch, not a DB sink.
            action.execute(args)

        fake_app.create_new_project.assert_called_once_with(str(tmp_path), "MyNewProject")
        assert action._project is fake_project

    def test_new_action_resolves_relative_location_to_absolute(self) -> None:
        """COM createNewProject fails with E_FAIL for relative locations; the
        action must pass an absolute path (smoke test finding)."""
        action = ProjectNewAction()
        args = argparse.Namespace(project_location="build/smoke", project_name="SmokeProj", verbose=False)
        fake_project = MagicMock(name="FakeProject")
        fake_app = MagicMock(name="FakeApplication")
        fake_app.create_new_project.return_value = fake_project

        with patch.object(ProjectNewAction, "_connect_app", return_value=fake_app):
            # pi-lens-ignore: python-sql-injection
            # AbstractAction.execute() is CLI action dispatch, not a DB sink.
            action.execute(args)

        called_location = fake_app.create_new_project.call_args[0][0]
        assert os.path.isabs(called_location)
        assert called_location.endswith(os.path.normpath("build/smoke"))


class TestProjectCommandRegistration:
    """Tests that ProjectCommand registers exactly the four active subcommands."""

    def test_get_actions_returns_four_actions(self) -> None:
        """ProjectCommand.get_actions() must return exactly 4 actions (export/import moved to top level)."""
        cmd = ProjectCommand(["open", "MyProject.rpy"])
        actions = cmd.get_actions()
        command_ids = [a.command_id for a in actions]

        assert command_ids == ["open", "list", "close", "new"]
