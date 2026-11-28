"""Tests for operation actions."""

from typing import Any, Tuple
from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.actions.abstract_action import ElementManagementAction
from rhapsody_cli.actions.operation import AbstractOperationAction
from rhapsody_cli.exceptions import CliExecutionError


class TestAbstractOperationAction:
    """Test AbstractOperationAction base class.

    SWR_OP_00006: Path and Name Validation
    SWR_OP_00009: Error Handling and Logging
    SWR_OP_00010: GUID Lookup Support
    """

    def test_resolve_classifier_success(self) -> None:
        """Test successful classifier resolution."""
        action = AbstractOperationAction()
        mock_classifier = MagicMock()
        mock_classifier.meta_class = "Class"

        with patch.object(ElementManagementAction, "_get_active_root", return_value=MagicMock()):
            with patch(
                "rhapsody_cli.actions.abstract_action.PathResolver.resolve_element",
                return_value=mock_classifier,
            ):
                result = action._resolve_classifier("Sensors/TemperatureSensor")
                assert result == mock_classifier

    def test_resolve_operation_success(self) -> None:
        """Test successful operation resolution by name within classifier."""
        action = AbstractOperationAction()
        mock_classifier = MagicMock()
        mock_op = MagicMock()
        mock_classifier.find_interface_item.return_value = mock_op

        result = action._resolve_operation(mock_classifier, "readValue")
        assert result == mock_op
        mock_classifier.find_interface_item.assert_called_once_with("readValue")

    def test_resolve_operation_not_found(self) -> None:
        """Test that missing operation raises CliExecutionError."""
        action = AbstractOperationAction()
        mock_classifier = MagicMock()
        mock_classifier.find_interface_item.return_value = None

        with pytest.raises(CliExecutionError) as exc_info:
            action._resolve_operation(mock_classifier, "missingOp")

        assert "Operation 'missingOp' not found" in str(exc_info.value)

    def test_resolve_operation_by_guid_success(self) -> None:
        """Test successful operation lookup by GUID."""
        action = AbstractOperationAction()
        mock_op = MagicMock()
        mock_op.meta_class = "Operation"

        mock_project = MagicMock()
        mock_project.find_element_by_guid.return_value = mock_op

        with patch.object(ElementManagementAction, "_get_active_project", return_value=mock_project):
            result = action._resolve_operation_by_guid("12345678-1234-1234-1234-123456789abc")
            assert result == mock_op
            mock_project.find_element_by_guid.assert_called_once_with("12345678-1234-1234-1234-123456789abc")

    def test_resolve_operation_by_guid_not_found(self) -> None:
        """Test GUID lookup fails when element is None."""
        action = AbstractOperationAction()
        mock_project = MagicMock()
        mock_project.find_element_by_guid.return_value = None

        with patch.object(ElementManagementAction, "_get_active_project", return_value=mock_project):
            with pytest.raises(CliExecutionError) as exc_info:
                action._resolve_operation_by_guid("12345678-1234-1234-1234-123456789abc")

            assert "No element found with GUID" in str(exc_info.value)

    def test_resolve_operation_by_guid_wrong_type(self) -> None:
        """Test GUID lookup fails for non-operation element."""
        action = AbstractOperationAction()
        mock_class = MagicMock()
        mock_class.meta_class = "Class"

        mock_project = MagicMock()
        mock_project.find_element_by_guid.return_value = mock_class

        with patch.object(ElementManagementAction, "_get_active_project", return_value=mock_project):
            with pytest.raises(CliExecutionError) as exc_info:
                action._resolve_operation_by_guid("12345678-1234-1234-1234-123456789abc")

            assert "does not resolve to an Operation" in str(exc_info.value)
            assert "found Class" in str(exc_info.value)


class TestOperationCreateAction:
    """Test OperationCreateAction.

    SWR_OP_00001: Operation Create Command
    SWR_OP_00007: External JSON File Support
    SWR_OP_00011: Returns Type Resolution
    SWR_OP_00012: Boolean Flag Support
    SWR_OP_00013: Bulk Creation Support
    """

    def _make_action_with_classifier(self) -> Tuple[Any, Any]:
        """Helper: build action and mock parent classifier."""
        from rhapsody_cli.actions.operation import OperationCreateAction

        action = OperationCreateAction()
        mock_classifier = MagicMock()
        return action, mock_classifier

    def test_create_single_operation_inline_json(self) -> None:
        """UTS_OP_00001: Test creating single operation with inline JSON."""
        action, mock_classifier = self._make_action_with_classifier()
        mock_op = MagicMock()
        mock_classifier.add_operation.return_value = mock_op

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            args = MagicMock()
            args.path = "Sensors/TemperatureSensor"
            args.input = None
            args.attributes = '{"name":"readValue","description":"Reads value"}'

            action.execute(args)

            mock_classifier.add_operation.assert_called_once_with("readValue")
            assert mock_op.description == "Reads value"

    def test_create_bulk_operations_from_file(self, tmp_path: Any) -> None:
        """UTS_OP_00002: Test creating multiple operations from JSON file."""
        action, mock_classifier = self._make_action_with_classifier()
        mock_op = MagicMock()
        mock_classifier.add_operation.return_value = mock_op

        json_file = tmp_path / "operations.json"
        json_file.write_text('[{"name":"readValue"},{"name":"setValue"}]', encoding="utf-8")

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            args = MagicMock()
            args.path = "Sensors/TemperatureSensor"
            args.input = str(json_file)
            args.attributes = None

            action.execute(args)

            assert mock_classifier.add_operation.call_count == 2

    def test_load_json_data_rejects_non_object_shapes(self, tmp_path: Any) -> None:
        from rhapsody_cli.actions.operation import OperationCreateAction

        action = OperationCreateAction()
        json_file = tmp_path / "invalid.json"

        for content in ('"scalar"', '[{"name":"valid"},"scalar"]'):
            json_file.write_text(content, encoding="utf-8")

            with pytest.raises(CliExecutionError, match="object or a list of objects"):
                action._load_json_data(str(json_file))

    def test_create_with_boolean_flags(self) -> None:
        """UTS_OP_00003: Test isAbstract/isStatic/isVirtual set via setIsX(1/0)."""
        action, mock_classifier = self._make_action_with_classifier()
        mock_op = MagicMock()
        mock_classifier.add_operation.return_value = mock_op

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            args = MagicMock()
            args.path = "Sensors/TemperatureSensor"
            args.input = None
            args.attributes = '{"name":"X","isAbstract":true,"isStatic":false,"isVirtual":true}'

            action.execute(args)

            assert mock_op.is_abstract == 1
            assert mock_op.is_static == 0
            assert mock_op.is_virtual == 1

    def test_create_with_returns_type(self) -> None:
        """UTS_OP_00004: Test returns type resolved via findNestedClassifierRecursive."""
        action, mock_classifier = self._make_action_with_classifier()
        mock_op = MagicMock()
        mock_classifier.add_operation.return_value = mock_op
        mock_owner = MagicMock()
        mock_type = MagicMock()
        mock_classifier.owner = mock_owner
        mock_owner.find_nested_classifier_recursive.return_value = mock_type

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            args = MagicMock()
            args.path = "Sensors/TemperatureSensor"
            args.input = None
            args.attributes = '{"name":"readValue","returns":"Temperature"}'

            action.execute(args)

            mock_owner.find_nested_classifier_recursive.assert_called_once_with("Temperature")
            assert mock_op.returns is mock_type

    def test_create_skips_unknown_attributes(self) -> None:
        """UTS_OP_00005: Test unknown attributes skipped with warning."""
        action, mock_classifier = self._make_action_with_classifier()
        mock_op = MagicMock()
        mock_classifier.add_operation.return_value = mock_op

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            args = MagicMock()
            args.path = "Sensors/TemperatureSensor"
            args.input = None
            args.attributes = '{"name":"X","unknown_field":"value"}'

            with patch.object(action.logger, "warning") as mock_warning:
                action.execute(args)

                mock_warning.assert_called_once()
                assert "unknown_field" in str(mock_warning.call_args)

    def test_create_missing_name_raises_error(self) -> None:
        """UTS_OP_00006: Test missing name raises CliExecutionError."""
        action, mock_classifier = self._make_action_with_classifier()

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            args = MagicMock()
            args.path = "Sensors/TemperatureSensor"
            args.input = None
            args.attributes = '{"description":"No name"}'

            with pytest.raises(CliExecutionError) as exc_info:
                action.execute(args)

            assert "'name' is required" in str(exc_info.value)


class TestOperationDeleteAction:
    """Test OperationDeleteAction.

    SWR_OP_00002: Operation Delete Command
    SWR_OP_00010: GUID Lookup Support
    """

    def test_delete_operation_by_path_and_name(self) -> None:
        """UTS_OP_00007: Test successful operation deletion by path + name."""
        from rhapsody_cli.actions.operation import OperationDeleteAction

        action = OperationDeleteAction()
        mock_classifier = MagicMock()
        mock_op = MagicMock()

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            with patch.object(action, "_resolve_operation", return_value=mock_op):
                args = MagicMock()
                args.path = "Sensors/TemperatureSensor"
                args.name = "readValue"
                args.guid = None

                action.execute(args)

                mock_classifier.delete_operation.assert_called_once_with(mock_op)

    def test_delete_operation_by_guid(self) -> None:
        """UTS_OP_00008: Test successful operation deletion by GUID."""
        from rhapsody_cli.actions.operation import OperationDeleteAction

        action = OperationDeleteAction()
        mock_op = MagicMock()
        mock_op.meta_class = "Operation"
        mock_owner = MagicMock()
        mock_op.owner = mock_owner

        with patch.object(action, "_resolve_operation_by_guid", return_value=mock_op):
            args = MagicMock()
            args.path = None
            args.name = None
            args.guid = "12345678-1234-1234-1234-123456789abc"

            action.execute(args)

            mock_owner.delete_operation.assert_called_once_with(mock_op)

    def test_delete_operation_guid_wrong_type(self) -> None:
        """UTS_OP_00009: Test that wrong type via --guid raises error."""
        from rhapsody_cli.actions.operation import OperationDeleteAction

        action = OperationDeleteAction()
        mock_class = MagicMock()
        mock_class.meta_class = "Class"

        mock_project = MagicMock()
        mock_project.find_element_by_guid.return_value = mock_class

        with patch.object(ElementManagementAction, "_get_active_project", return_value=mock_project):
            args = MagicMock()
            args.path = None
            args.name = None
            args.guid = "12345678-1234-1234-1234-123456789abc"

            with pytest.raises(CliExecutionError) as exc_info:
                action.execute(args)

            assert "does not resolve to an Operation" in str(exc_info.value)
            assert "found Class" in str(exc_info.value)

    def test_delete_requires_path_name_or_guid(self) -> None:
        """UTS_OP_00010: Test that either --path + --name or --guid is required."""
        from rhapsody_cli.actions.operation import OperationDeleteAction

        action = OperationDeleteAction()
        args = MagicMock()
        args.path = None
        args.name = None
        args.guid = None

        with pytest.raises(CliExecutionError) as exc_info:
            action.execute(args)

        assert "Either --path + --name or --guid must be specified" in str(exc_info.value)


class TestOperationViewAction:
    """Test OperationViewAction.

    SWR_OP_00003: Operation View Command
    SWR_OP_00008: Multi-Format Output
    SWR_OP_00010: GUID Lookup Support
    """

    def _make_mock_operation(self) -> MagicMock:
        """Helper: build a fully-populated mock operation."""
        mock_op = MagicMock()
        mock_op.meta_class = "Operation"
        mock_op.name = "readValue"
        mock_op.guid = "12345678-1234-1234-1234-123456789abc"
        mock_op.description = "Reads the value"
        mock_op.body = "return threshold;"
        mock_op.is_abstract = True
        mock_op.is_static = 0
        mock_op.is_virtual = 1
        mock_op.visibility = "public"
        mock_op.get_full_path_name.return_value = "Sensors/TemperatureSensor/readValue"

        mock_returns = MagicMock()
        mock_returns.name = "Temperature"
        mock_op.returns = mock_returns

        arg1 = MagicMock()
        arg1.name = "x"
        arg2 = MagicMock()
        arg2.name = "y"
        mock_op.arguments = [arg1, arg2]

        return mock_op

    def test_view_table_output(self, capsys: Any) -> None:
        """UTS_OP_00011: Test table format output."""
        from rhapsody_cli.actions.operation import OperationViewAction

        action = OperationViewAction()
        mock_op = self._make_mock_operation()

        with patch.object(action, "_resolve_classifier", return_value=MagicMock()):
            with patch.object(action, "_resolve_operation", return_value=mock_op):
                args = MagicMock()
                args.path = "Sensors/TemperatureSensor"
                args.name = "readValue"
                args.guid = None
                args.format = "table"
                args.output = None

                action.execute(args)

                captured = capsys.readouterr()
                assert "readValue" in captured.out
                assert "Property" in captured.out
                assert "Temperature" in captured.out

    def test_view_json_output_to_file(self, tmp_path: Any) -> None:
        """UTS_OP_00012: Test JSON output to file."""
        import json as json_module

        from rhapsody_cli.actions.operation import OperationViewAction

        action = OperationViewAction()
        mock_op = self._make_mock_operation()

        with patch.object(action, "_resolve_classifier", return_value=MagicMock()):
            with patch.object(action, "_resolve_operation", return_value=mock_op):
                output_file = tmp_path / "op.json"
                args = MagicMock()
                args.path = "Sensors/TemperatureSensor"
                args.name = "readValue"
                args.guid = None
                args.format = "json"
                args.output = str(output_file)

                action.execute(args)

                data = json_module.loads(output_file.read_text())
                assert data["name"] == "readValue"
                assert data["guid"] == "12345678-1234-1234-1234-123456789abc"
                assert data["description"] == "Reads the value"
                assert data["isAbstract"] == 1  # bool True normalized to int
                assert data["isStatic"] == 0
                assert data["isVirtual"] == 1
                assert data["returns"] == "Temperature"
                assert data["visibility"] == "public"
                assert data["body"] == "return threshold;"
                assert data["metaClass"] == "Operation"

    def test_view_csv_output(self, capsys: Any) -> None:
        """UTS_OP_00013: Test CSV format output."""
        from rhapsody_cli.actions.operation import OperationViewAction

        action = OperationViewAction()
        mock_op = self._make_mock_operation()

        with patch.object(action, "_resolve_classifier", return_value=MagicMock()):
            with patch.object(action, "_resolve_operation", return_value=mock_op):
                args = MagicMock()
                args.path = "Sensors/TemperatureSensor"
                args.name = "readValue"
                args.guid = None
                args.format = "csv"
                args.output = None

                action.execute(args)

                captured = capsys.readouterr()
                lines = captured.out.strip().split("\n")
                assert len(lines) == 2
                assert "Name,GUID" in lines[0]
                assert "readValue" in lines[1]

    def test_view_by_guid(self, capsys: Any) -> None:
        """UTS_OP_00014: Test viewing operation by GUID."""
        from rhapsody_cli.actions.operation import OperationViewAction

        action = OperationViewAction()
        mock_op = self._make_mock_operation()

        with patch.object(action, "_resolve_operation_by_guid", return_value=mock_op):
            args = MagicMock()
            args.path = None
            args.name = None
            args.guid = "12345678-1234-1234-1234-123456789abc"
            args.format = "table"
            args.output = None

            action.execute(args)

            captured = capsys.readouterr()
            assert "readValue" in captured.out


class TestOperationListAction:
    """Test OperationListAction.

    SWR_OP_00004: Operation List Command
    SWR_OP_00008: Multi-Format Output
    """

    def test_list_operations(self, capsys: Any) -> None:
        """UTS_OP_00015: Test listing operations on a classifier."""
        from rhapsody_cli.actions.operation import OperationListAction

        action = OperationListAction()
        mock_classifier = MagicMock()
        op1 = MagicMock()
        op1.name = "readValue"
        op2 = MagicMock()
        op2.name = "setValue"
        mock_classifier.operations = [op1, op2]

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            args = MagicMock()
            args.path = "Sensors/TemperatureSensor"
            args.format = "table"
            args.output = None

            action.execute(args)

            captured = capsys.readouterr()
            assert "readValue" in captured.out
            assert "setValue" in captured.out

    def test_list_empty(self, capsys: Any) -> None:
        """UTS_OP_00016: Test listing classifier with no operations."""
        from rhapsody_cli.actions.operation import OperationListAction

        action = OperationListAction()
        mock_classifier = MagicMock()
        mock_classifier.operations = []

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            args = MagicMock()
            args.path = "Sensors/TemperatureSensor"
            args.format = "table"
            args.output = None

            action.execute(args)

            capsys.readouterr()  # Should produce empty table (no data)

    def test_list_json_output(self, capsys: Any) -> None:
        """UTS_OP_00017: Test JSON output format."""
        import json as json_module

        from rhapsody_cli.actions.operation import OperationListAction

        action = OperationListAction()
        mock_classifier = MagicMock()
        op1 = MagicMock()
        op1.name = "readValue"
        op2 = MagicMock()
        op2.name = "setValue"
        mock_classifier.operations = [op1, op2]

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            args = MagicMock()
            args.path = "Sensors/TemperatureSensor"
            args.format = "json"
            args.output = None

            action.execute(args)

            captured = capsys.readouterr()
            data = json_module.loads(captured.out)
            assert data == ["readValue", "setValue"]


class TestOperationUpdateAction:
    """Test OperationUpdateAction.

    SWR_OP_00005: Operation Update Command
    SWR_OP_00010: GUID Lookup Support
    """

    def test_update_operation_by_path_and_name(self) -> None:
        """UTS_OP_00018: Test updating operation via --path + --name."""
        from rhapsody_cli.actions.operation import OperationUpdateAction

        action = OperationUpdateAction()
        mock_classifier = MagicMock()
        mock_op = MagicMock()

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            with patch.object(action, "_resolve_operation", return_value=mock_op):
                args = MagicMock()
                args.path = "Sensors/TemperatureSensor"
                args.name = "readValue"
                args.guid = None
                args.input = None
                args.attributes = '{"body":"return 42;"}'

                action.execute(args)

                assert mock_op.body == "return 42;"

    def test_update_operation_by_guid(self) -> None:
        """UTS_OP_00019: Test updating operation via --guid with type validation."""
        from rhapsody_cli.actions.operation import OperationUpdateAction

        action = OperationUpdateAction()
        mock_op = MagicMock()
        mock_op.meta_class = "Operation"

        with patch.object(action, "_resolve_operation_by_guid", return_value=mock_op):
            args = MagicMock()
            args.path = None
            args.name = None
            args.guid = "12345678-1234-1234-1234-123456789abc"
            args.input = None
            args.attributes = '{"visibility":"private"}'

            action.execute(args)

            assert mock_op.visibility == "private"

    def test_update_partial_update(self) -> None:
        """UTS_OP_00020: Test that partial update only modifies specified fields."""
        from rhapsody_cli.actions.operation import OperationUpdateAction

        action = OperationUpdateAction()
        mock_classifier = MagicMock()
        mock_op = MagicMock()

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            with patch.object(action, "_resolve_operation", return_value=mock_op):
                args = MagicMock()
                args.path = "Sensors/TemperatureSensor"
                args.name = "readValue"
                args.guid = None
                args.input = None
                args.attributes = '{"isAbstract":true}'

                action.execute(args)

                assert mock_op.is_abstract == 1
                assert "body" not in mock_op.__dict__
                assert "name" not in mock_op.__dict__

    def test_update_skips_unknown_fields(self) -> None:
        """UTS_OP_00021: Test that unknown fields are skipped with warning."""
        from rhapsody_cli.actions.operation import OperationUpdateAction

        action = OperationUpdateAction()
        mock_classifier = MagicMock()
        mock_op = MagicMock()

        with patch.object(action, "_resolve_classifier", return_value=mock_classifier):
            with patch.object(action, "_resolve_operation", return_value=mock_op):
                args = MagicMock()
                args.path = "Sensors/TemperatureSensor"
                args.name = "readValue"
                args.guid = None
                args.input = None
                args.attributes = '{"body":"new body","unknown_field":"value"}'

                with patch.object(action.logger, "warning") as mock_warning:
                    action.execute(args)

                    assert mock_op.body == "new body"
                    mock_warning.assert_called()
                    assert "unknown_field" in str(mock_warning.call_args)
