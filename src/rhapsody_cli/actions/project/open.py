"""ProjectOpenAction — split from project_action.py."""

import argparse

from rhapsody_cli.actions.abstract_action import RhapsodyContextAction
from rhapsody_cli.exceptions import RhapsodyConnectionError


class ProjectOpenAction(RhapsodyContextAction):
    """Open action - opens a project file."""

    def __init__(self) -> None:
        """Initialize the 'open' action."""
        super().__init__(command_id="open")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'open' subcommand and its arguments."""
        open_parser = sub_parser.add_parser("open", help="Open a project file")
        open_parser.add_argument("project_path", help="Path to the project file")

    def execute(self, args: argparse.Namespace) -> None:
        """Open a project file."""
        project_path = args.project_path
        try:
            app = self._connect_app()
            self._project = app.open_project(project_path)
            self.logger.info("Opened project: %s", project_path)
        except RhapsodyConnectionError as e:
            self._handle_connection_error(e, "Failed to open project")
        except Exception as e:
            self._handle_execution_error(e, f"Failed to open project '{project_path}'")
