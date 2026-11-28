"""PackageDeleteAction — split from package_action.py."""

import argparse
import logging

from rhapsody_cli.actions.package.base import AbstractPackageAction

logger = logging.getLogger(__name__)


class PackageDeleteAction(AbstractPackageAction):
    """Delete a package.

    SWR_PKG_0002: Package Delete Command
    """

    def __init__(self) -> None:
        """Initialize the 'delete' action."""
        super().__init__(command_id="delete")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'delete' subcommand and its arguments."""
        parser = sub_parser.add_parser("delete", help="Delete a package")
        self.add_path_argument(parser, required=True, help_text="Package path to delete")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute package deletion."""
        super().execute(args)
        self.logger.info("Starting package deletion...")
        self.logger.info("Resolving package path '%s'...", args.path)
        package = self._resolve_and_validate_package(args.path)

        try:
            self.logger.info("Deleting package '%s'...", args.path)
            package.delete_from_project()
            self.logger.info("Successfully deleted package '%s'", args.path)
        except Exception as e:
            self._handle_execution_error(e, f"Failed to delete package '{args.path}'")
