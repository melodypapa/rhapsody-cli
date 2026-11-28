"""ProjectCloseAction — split from project_action.py."""

import argparse

from rhapsody_cli.actions.abstract_action import RhapsodyContextAction


class ProjectCloseAction(RhapsodyContextAction):
    """Close action - closes the active project."""

    def __init__(self) -> None:
        """Initialize the 'close' action."""
        super().__init__(command_id="close")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'close' subcommand and its arguments."""
        sub_parser.add_parser("close", help="Close active project")

    def execute(self, args: argparse.Namespace) -> None:
        """Close active project."""
        try:
            if self._project is None:
                self.logger.info("No active project")
                return
            self._project.close()
            self._project = None
            self.logger.info("Project closed")
        except Exception as e:
            self._handle_execution_error(e, "Failed to close project")
