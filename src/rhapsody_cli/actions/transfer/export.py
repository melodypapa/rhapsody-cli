"""Root ``export`` command — exports a package to a YAML file.

SWR_XCH_001: Import/Export CLI Actions
"""

import argparse

from rhapsody_cli.actions.abstract_action import RootCommandAction
from rhapsody_cli.actions.package.base import AbstractPackageAction
from rhapsody_cli.exceptions import CliExecutionError, RhapsodyConnectionError
from rhapsody_cli.exchange.exporter import RhapsodyExporter
from rhapsody_cli.exchange.yaml_utils import RhapsodyYaml


class ExportAction(RootCommandAction, AbstractPackageAction):
    """Action for the root ``export`` command — exports a package to a YAML file."""

    def __init__(self) -> None:
        super().__init__(command_id="export")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'export' subcommand and its arguments."""
        parser = sub_parser.add_parser(self.command_id, help="Export a package to a YAML file")
        self.add_path_argument(parser, required=False, help_text="Path to package (defaults to root)")
        parser.add_argument("--file", required=True, help="Output YAML file path")

    def execute(self, args: argparse.Namespace) -> None:
        """Export the resolved package to the given YAML file."""
        super().execute(args)
        try:
            app = self._connect_app()
            package = self._resolve_and_validate_package(args.path)
            exporter = RhapsodyExporter(app=app)
            data = exporter.export(package)
            yaml_io = RhapsodyYaml()
            yaml_io.write(args.file, data)
            self.logger.info("Exported package to %s", args.file)
        except RhapsodyConnectionError as e:
            self._handle_connection_error(e, "export package")
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, "export package")
