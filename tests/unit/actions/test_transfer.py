"""Tests for the root-level export/import commands (SWR_XCH_001).

UTS_XCH_00088: root export action writes YAML file.
UTS_XCH_00089: root import action reads YAML and imports into package.
"""

from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.actions.transfer.export import ExportAction
from rhapsody_cli.actions.transfer.importer import ImportAction
from rhapsody_cli.exceptions import CliExecutionError


class TestExportAction:
    """UTS_XCH_00088: root export action writes YAML file."""

    def test_export_writes_yaml_file(self) -> None:
        action = ExportAction()
        fake_app = MagicMock(name="FakeApplication")
        fake_package = MagicMock(name="FakePackage")
        payload = {"version": 1, "project": "P", "rhapsody-model": []}

        with patch("rhapsody_cli.actions.transfer.export.RhapsodyExporter") as mock_exporter_cls:
            with patch("rhapsody_cli.actions.transfer.export.RhapsodyYaml") as mock_yaml_cls:
                mock_exporter = MagicMock()
                mock_exporter_cls.return_value = mock_exporter
                mock_exporter.export.return_value = payload

                args = MagicMock()
                args.path = "Sensors"
                args.file = "sensors.yaml"

                with patch.object(action, "_connect_app", return_value=fake_app), patch.object(action, "_resolve_and_validate_package", return_value=fake_package):
                    action.execute(args)

                mock_exporter_cls.assert_called_once_with(app=fake_app)
                mock_exporter.export.assert_called_once_with(fake_package)
                mock_yaml_cls.return_value.write.assert_called_once_with("sensors.yaml", payload)

    def test_export_raises_on_unresolved_package(self) -> None:
        action = ExportAction()
        fake_app = MagicMock(name="FakeApplication")

        with patch("rhapsody_cli.actions.transfer.export.RhapsodyExporter"), patch("rhapsody_cli.actions.transfer.export.RhapsodyYaml"):
            args = MagicMock()
            args.path = "Nonexistent"
            args.file = "out.yaml"

            with patch.object(action, "_connect_app", return_value=fake_app), patch.object(
                action,
                "_resolve_and_validate_package",
                side_effect=CliExecutionError("package not found"),
            ):
                with pytest.raises(CliExecutionError, match="package not found"):
                    action.execute(args)


class TestImportAction:
    """UTS_XCH_00089: root import action reads YAML and imports into package."""

    def test_import_reads_yaml_and_calls_import_template(self) -> None:
        action = ImportAction()
        fake_app = MagicMock(name="FakeApplication")
        fake_package = MagicMock(name="FakePackage")
        payload: dict[str, Any] = {"version": 1, "project": "P", "rhapsody-model": []}

        with patch("rhapsody_cli.actions.transfer.importer.RhapsodyYaml") as mock_yaml_cls:
            with patch("rhapsody_cli.actions.transfer.importer.RhapsodyImporter") as mock_importer_cls:
                mock_yaml = MagicMock()
                mock_yaml_cls.return_value = mock_yaml
                mock_yaml.read.return_value = payload

                mock_importer = MagicMock()
                mock_importer_cls.return_value = mock_importer

                args = MagicMock()
                args.path = "Sensors"
                args.file = "sensors.yaml"

                with patch.object(action, "_connect_app", return_value=fake_app), patch.object(action, "_resolve_and_validate_package", return_value=fake_package):
                    action.execute(args)

                mock_yaml_cls.assert_called_once()
                mock_yaml.read.assert_called_once_with("sensors.yaml")
                mock_importer_cls.assert_called_once_with(app=fake_app)
                mock_importer.import_template.assert_called_once_with(payload, fake_package)
                fake_app.save_all.assert_called_once()

    def test_import_raises_on_unresolved_package(self) -> None:
        action = ImportAction()
        fake_app = MagicMock(name="FakeApplication")

        with patch("rhapsody_cli.actions.transfer.importer.RhapsodyYaml"), patch("rhapsody_cli.actions.transfer.importer.RhapsodyImporter"):
            args = MagicMock()
            args.path = "Nonexistent"
            args.file = "in.yaml"

            with patch.object(action, "_connect_app", return_value=fake_app), patch.object(
                action,
                "_resolve_and_validate_package",
                side_effect=CliExecutionError("package not found"),
            ):
                with pytest.raises(CliExecutionError, match="package not found"):
                    action.execute(args)
