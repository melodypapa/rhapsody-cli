"""ProjectNewAction — split from project_action.py."""

import argparse

from rhapsody_cli.actions.abstract_action import RhapsodyContextAction
from rhapsody_cli.exceptions import RhapsodyConnectionError


class ProjectNewAction(RhapsodyContextAction):
    """New action - creates a new project."""

    def __init__(self) -> None:
        """Initialize the 'new' action."""
        super().__init__(command_id="new")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'new' subcommand and its arguments."""
        new_parser = sub_parser.add_parser("new", help="Create a new project")
        new_parser.add_argument("project_location", help="Location for the project")
        new_parser.add_argument("project_name", help="Name of the project")

    def execute(self, args: argparse.Namespace) -> None:
        """Create a new project."""
        project_location = args.project_location
        project_name = args.project_name
        try:
            app = self._connect_app()
            self._project = app.create_new_project(project_location, project_name)
            self.logger.info("Created project: %s at %s", project_name, project_location)
        except RhapsodyConnectionError as e:
            self._handle_connection_error(e, "Failed to create project")
        except Exception as e:
            self._handle_execution_error(e, f"Failed to create project '{project_name}'")
