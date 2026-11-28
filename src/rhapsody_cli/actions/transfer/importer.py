"""Root ``import`` command — imports a YAML file into a package.

SWR_XCH_001: Import/Export CLI Actions
"""

import argparse

from rhapsody_cli.actions.abstract_action import RootCommandAction
from rhapsody_cli.actions.package.base import AbstractPackageAction
from rhapsody_cli.exceptions import CliExecutionError, RhapsodyConnectionError
from rhapsody_cli.exchange.importer import RhapsodyImporter
from rhapsody_cli.exchange.yaml_utils import RhapsodyYaml


class ImportAction(RootCommandAction, AbstractPackageAction):
    """Action for the root ``import`` command — imports a YAML file into a package."""

    def __init__(self) -> None:
        super().__init__(command_id="import")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'import' subcommand and its arguments."""
        parser = sub_parser.add_parser(self.command_id, help="Import a YAML file into a package")
        self.add_path_argument(parser, required=False, help_text="Path to target package (defaults to root)")
        parser.add_argument("--file", required=True, help="Input YAML file path")

    def execute(self, args: argparse.Namespace) -> None:
        """Import the given YAML file into the resolved package, then save."""
        super().execute(args)
        try:
            app = self._connect_app()
            package = self._resolve_and_validate_package(args.path)
            yaml_io = RhapsodyYaml()
            data = yaml_io.read(args.file)
            importer = RhapsodyImporter(app=app)
            importer.import_template(data, package)
            app.save_all()
            self.logger.info("Imported %s into package", args.file)
        except RhapsodyConnectionError as e:
            self._handle_connection_error(e, "import package")
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, "import package")
