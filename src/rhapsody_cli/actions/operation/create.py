"""OperationCreateAction — split from operation_action.py."""

import argparse
import json
import logging
from pathlib import Path
from typing import Dict, List, Union, cast

from rhapsody_cli.actions.operation.base import AbstractOperationAction
from rhapsody_cli.actions.support import load_json_data
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class OperationCreateAction(AbstractOperationAction):
    """Create one or multiple operations.

    SWR_OP_00001: Operation Create Command
    SWR_OP_00007: External JSON File Support
    SWR_OP_00011: Returns Type Resolution
    SWR_OP_00012: Boolean Flag Support
    SWR_OP_00013: Bulk Creation Support
    """

    VALID_ATTRIBUTES = {
        "name",
        "body",
        "isAbstract",
        "isStatic",
        "isVirtual",
        "returns",
        "visibility",
        "arguments",
        "description",
    }

    def __init__(self) -> None:
        """Initialize the 'create' action."""
        super().__init__(command_id="create")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'create' subcommand and its arguments."""
        parser = sub_parser.add_parser("create", help="Create an operation")
        self.add_path_argument(parser, required=True, help_text="Parent classifier path")
        parser.add_argument("--input", default=None, help="JSON file with operation attributes")
        parser.add_argument("attributes", nargs="?", default=None, help="Inline JSON or JSON file path")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute operation creation."""
        super().execute(args)
        input_data = args.input if args.input else args.attributes
        if not input_data:
            raise CliExecutionError("Either --input or attributes argument must be provided")

        data = self._load_json_data(input_data)
        ops_data: List[Dict[str, object]] = data if isinstance(data, list) else [data]

        classifier = self._resolve_classifier(args.path)

        created: List[str] = []
        errors: List[str] = []
        for op_attrs in ops_data:
            try:
                name = self._create_single_operation(classifier, op_attrs, args.path)
                created.append(name)
            except CliExecutionError:
                raise
            except Exception as e:
                op_name = op_attrs.get("name", "unknown")
                self.logger.error("Failed to create operation '%s': %s", op_name, e)
                errors.append(cast(str, op_name))

        self._report_results(created, errors, len(ops_data))

    def _create_single_operation(self, classifier: IRPModelElement, op_attrs: Dict[str, object], parent_path: str) -> str:
        """Create a single operation and set its attributes. Returns the operation name."""
        name = str(op_attrs.get("name", ""))
        if not name:
            raise CliExecutionError("'name' is required in attributes")

        unknown = set(op_attrs.keys()) - self.VALID_ATTRIBUTES
        if unknown:
            self.logger.warning("Skipping unknown attributes: %s", unknown)

        operation = classifier.add_operation(name)  # type: ignore[attr-defined]
        self._set_attributes(classifier, operation, op_attrs)

        full_path = f"{parent_path}/{name}"
        self.logger.info("Created operation: %s", full_path)
        return name

    def _report_results(self, created: List[str], errors: List[str], total: int) -> None:
        """Log summary of creation results."""
        if errors and not created:
            raise CliExecutionError(f"Created 0/{total} operations; all failed")
        if errors:
            self.logger.info("Created %d/%d operations with %d error(s)", len(created), total, len(errors))

    def _load_json_data(self, attributes_input: str) -> Union[Dict[str, object], List[Dict[str, object]]]:
        """Load one operation object or a list of operation objects from JSON.

        SWR_OP_00007: External JSON File Support
        """
        if attributes_input.startswith("{") or attributes_input.startswith("["):
            try:
                data: object = json.loads(attributes_input)
                return self._normalize_operation_data(data)
            except json.JSONDecodeError as e:
                raise CliExecutionError(f"Invalid JSON: {e}") from e

        if not Path(attributes_input).exists():
            raise CliExecutionError(f"File not found: {attributes_input}")

        try:
            with open(attributes_input, encoding="utf-8") as f:
                file_data: object = json.load(f)
            return self._normalize_operation_data(file_data)
        except json.JSONDecodeError as e:
            raise CliExecutionError(f"Invalid JSON in file: {e}") from e
        except OSError as e:
            raise CliExecutionError(f"Failed to read file: {e}") from e

    def _load_json_data(self, attributes_input: str) -> Union[Dict[str, object], List[Dict[str, object]]]:
        """Load JSON data via the shared helper, then apply operation-shape normalization."""
        return self._normalize_operation_data(load_json_data(attributes_input))

    @staticmethod
    def _normalize_operation_data(data: object) -> Union[Dict[str, object], List[Dict[str, object]]]:
        """Validate the JSON root and each item in a bulk operation payload."""
        if isinstance(data, dict):
            return cast(Dict[str, object], data)
        if isinstance(data, list):
            operations: List[Dict[str, object]] = []
            for item in data:
                if not isinstance(item, dict):
                    raise CliExecutionError("Operation JSON must be an object or a list of objects")
                operations.append(cast(Dict[str, object], item))
            return operations
        raise CliExecutionError("Operation JSON must be an object or a list of objects")

    def _set_attributes(self, classifier: IRPModelElement, operation: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set validated attributes on operation."""
        if "name" in attrs:
            operation.name = cast(str, attrs["name"])
        if "body" in attrs:
            operation.body = cast(str, attrs["body"])  # type: ignore[attr-defined]
        if "description" in attrs:
            operation.description = cast(str, attrs["description"])
        if "visibility" in attrs:
            operation.visibility = cast(str, attrs["visibility"])  # type: ignore[attr-defined]
        if "arguments" in attrs:
            operation.set_arguments(attrs["arguments"])  # type: ignore[attr-defined]
        self._set_boolean_flags(operation, attrs)
        self._set_returns(classifier, operation, attrs)

    def _set_boolean_flags(self, operation: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set boolean flags isAbstract, isStatic, isVirtual.

        SWR_OP_00012: Boolean Flag Support
        """
        if "isAbstract" in attrs:
            operation.is_abstract = 1 if attrs["isAbstract"] else 0  # type: ignore[attr-defined]
        if "isStatic" in attrs:
            operation.is_static = 1 if attrs["isStatic"] else 0  # type: ignore[attr-defined]
        if "isVirtual" in attrs:
            operation.is_virtual = 1 if attrs["isVirtual"] else 0  # type: ignore[attr-defined]

    def _set_returns(self, classifier: IRPModelElement, operation: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Resolve and set the returns type.

        SWR_OP_00011: Returns Type Resolution
        """
        if "returns" in attrs:
            type_name = cast(str, attrs["returns"])
            owner = classifier.owner
            target = owner.find_nested_classifier_recursive(type_name)  # type: ignore[attr-defined]
            if target is None:
                raise CliExecutionError(f"Returns type '{type_name}' not found")
            operation.returns = target  # type: ignore[attr-defined]
