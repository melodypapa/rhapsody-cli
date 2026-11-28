"""ProjectExportAction — split from project_action.py."""

import argparse

from rhapsody_cli.actions.abstract_action import RhapsodyContextAction
from rhapsody_cli.exceptions import CliExecutionError, RhapsodyConnectionError
from rhapsody_cli.exchange.exporter import RhapsodyExporter
from rhapsody_cli.exchange.yaml_utils import RhapsodyYaml


class ProjectExportAction(RhapsodyContextAction):
    """Action for `project export` — exports the active project to a YAML file.

    SWR_XCH_001: Import/Export CLI Actions
    """

    def __init__(self) -> None:
        super().__init__(command_id="export")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        parser = sub_parser.add_parser(self.command_id, help="Export the active project to a YAML file")
        parser.add_argument("--file", required=True, help="Output YAML file path")

    def execute(self, args: argparse.Namespace) -> None:
        try:
            project = self._get_active_project()
            app = self._connect_app()
            exporter = RhapsodyExporter(app=app)
            data = exporter.export(project)
            yaml_io = RhapsodyYaml()
            yaml_io.write(args.file, data)
            self.logger.info("Exported project to %s", args.file)
        except RhapsodyConnectionError as e:
            self._handle_connection_error(e, "export project")
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, "export project")
