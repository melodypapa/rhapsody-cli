"""ProjectImportAction — split from project_action.py."""

import argparse

from rhapsody_cli.actions.abstract_action import RhapsodyContextAction
from rhapsody_cli.exceptions import CliExecutionError, RhapsodyConnectionError
from rhapsody_cli.exchange.importer import RhapsodyImporter
from rhapsody_cli.exchange.yaml_utils import RhapsodyYaml


class ProjectImportAction(RhapsodyContextAction):
    """Action for `project import` — imports a YAML file into the active project.

    SWR_XCH_001: Import/Export CLI Actions
    """

    def __init__(self) -> None:
        super().__init__(command_id="import")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        parser = sub_parser.add_parser(self.command_id, help="Import a YAML file into the active project")
        parser.add_argument("--file", required=True, help="Input YAML file path")

    def execute(self, args: argparse.Namespace) -> None:
        try:
            project = self._get_active_project()
            app = self._connect_app()
            yaml_io = RhapsodyYaml()
            data = yaml_io.read(args.file)
            importer = RhapsodyImporter(app=app)
            importer.import_template(data, project)
            app.save_all()
            self.logger.info("Imported %s into project", args.file)
        except RhapsodyConnectionError as e:
            self._handle_connection_error(e, "import project")
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, "import project")
