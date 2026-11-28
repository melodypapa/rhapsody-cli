"""ProjectListAction — split from project_action.py."""

import argparse

from rhapsody_cli.actions.abstract_action import RhapsodyContextAction


class ProjectListAction(RhapsodyContextAction):
    """List action - lists open projects."""

    def __init__(self) -> None:
        """Initialize the 'list' action."""
        super().__init__(command_id="list")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'list' subcommand and its arguments."""
        sub_parser.add_parser("list", help="List open projects")

    def execute(self, args: argparse.Namespace) -> None:
        """List open projects."""
        try:
            app = self._connect_app()
            projects = app.projects

            if not projects or len(projects) == 0:
                self.logger.info("No open projects")
                return

            rows = [[proj.name, proj.filename] for proj in projects]

            # NOTE: This is the command's result data (not a status/log
            # message), so it is written directly to stdout via print()
            # rather than the logger, to keep it safe for piping/redirection.
            # force_table=True preserves the table-only contract; JSON output
            # for `project list` is a separate future enhancement.
            self._print_formatted_output(data={}, headers=["Name", "Path"], table_rows=rows, force_table=True)
        except Exception as e:
            self._handle_execution_error(e, "Failed to list projects")
