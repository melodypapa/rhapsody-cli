"""Port-related CLI actions.

SWR_PORT_00001: Port Create Command
SWR_PORT_00002: Port Delete Command
SWR_PORT_00003: Port View Command
SWR_PORT_00004: Port List Command
SWR_PORT_00005: Port Update Command
SWR_PORT_00006: Path and Name Validation
SWR_PORT_00007: External JSON File Support
SWR_PORT_00008: Multi-Format Output
SWR_PORT_00009: Error Handling and Logging
SWR_PORT_00010: GUID Lookup Support
SWR_PORT_00011: PortContract Resolution
SWR_PORT_00012: IsBehavioral and IsReversed Support
SWR_PORT_00013: Bulk Creation Support
"""

import argparse
import json
import logging
from pathlib import Path
from typing import Dict, List, Union, cast

from rhapsody_cli.actions.abstract_action import ElementManagementAction, SessionAwareAction
from rhapsody_cli.cli.formatters import OutputFormatter
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.core import RPModelElement

logger = logging.getLogger(__name__)


class AbstractPortAction(SessionAwareAction, ElementManagementAction):
    """Base class for port actions with common path, name and GUID validation.

    SWR_PORT_00006: Path and Name Validation
    SWR_PORT_00009: Error Handling and Logging
    SWR_PORT_00010: GUID Lookup Support
    """

    def _resolve_classifier(self, path: str) -> RPModelElement:
        """Resolve a parent classifier path.

        Args:
            path: Classifier path to resolve.

        Returns:
            Classifier COM object.

        Raises:
            CliExecutionError: If path not found.
        """
        root = self._get_active_root()
        return self._resolve_container_or_element(root, path, resolve_element=True, operation=f"resolve classifier path '{path}'")

    def _resolve_port(self, classifier: RPModelElement, name: str) -> RPModelElement:
        """Find a port by name within a classifier by iterating getPorts().

        Args:
            classifier: The parent classifier COM object.
            name: The port name to find.

        Returns:
            Port COM object.

        Raises:
            CliExecutionError: If port not found.
        """
        ports = classifier.get_ports()  # type: ignore[attr-defined]
        for port in ports:
            if cast(RPModelElement, port).get_name() == name:
                return cast(RPModelElement, port)
        raise CliExecutionError(f"Port '{name}' not found in classifier")

    def _resolve_port_by_guid(self, guid: str) -> RPModelElement:
        """Locate a port by GUID and validate it's a Port element.

        SWR_PORT_00010: GUID Lookup Support

        Args:
            guid: GUID string in format 12345678-1234-1234-1234-123456789abc.

        Returns:
            Port COM object.

        Raises:
            CliExecutionError: If GUID not found or element is not a Port.
        """
        project = self._get_active_project()
        try:
            element = project.find_element_by_guid(guid)
        except Exception as e:
            self._handle_execution_error(e, f"Failed to locate port by GUID '{guid}'")

        if element is None:
            raise CliExecutionError(f"No element found with GUID '{guid}'")

        meta_class = element.get_meta_class()
        if meta_class != "Port":
            raise CliExecutionError(f"GUID '{guid}' does not resolve to a Port (found {meta_class})")

        return element


class PortCreateAction(AbstractPortAction):
    """Create one or multiple ports.

    SWR_PORT_00001: Port Create Command
    SWR_PORT_00007: External JSON File Support
    SWR_PORT_00011: PortContract Resolution
    SWR_PORT_00012: IsBehavioral and IsReversed Support
    SWR_PORT_00013: Bulk Creation Support
    """

    VALID_ATTRIBUTES = {
        "name",
        "isBehavioral",
        "isReversed",
        "portContract",
        "description",
    }

    def __init__(self) -> None:
        """Initialize the 'create' action."""
        super().__init__(command_id="create")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'create' subcommand and its arguments."""
        parser = sub_parser.add_parser("create", help="Create a port")
        self.add_path_argument(parser, required=True, help_text="Parent classifier path")
        parser.add_argument("--input", default=None, help="JSON file with port attributes")
        parser.add_argument("attributes", nargs="?", default=None, help="Inline JSON or JSON file path")
        self.add_verbose_argument(parser)

    def execute(self, args: argparse.Namespace) -> None:
        """Execute port creation."""
        super().execute(args)
        input_data = args.input if args.input else args.attributes
        if not input_data:
            raise CliExecutionError("Either --input or attributes argument must be provided")

        data = self._load_json_data(input_data)
        ports_data = data if isinstance(data, list) else [data]

        classifier = self._resolve_classifier(args.path)

        created: List[str] = []
        errors: List[str] = []
        for port_attrs in ports_data:
            try:
                name = self._create_single_port(classifier, port_attrs, args.path)
                created.append(name)
            except CliExecutionError:
                raise
            except Exception as e:
                port_name = port_attrs.get("name", "unknown")
                self.logger.error("Failed to create port '%s': %s", port_name, e)
                errors.append(cast(str, port_name))

        self._report_results(created, errors, len(ports_data))

    def _create_single_port(self, classifier: RPModelElement, port_attrs: Dict[str, object], parent_path: str) -> str:
        """Create a single port and set its attributes. Returns the port name."""
        name = str(port_attrs.get("name", ""))
        if not name:
            raise CliExecutionError("'name' is required in attributes")

        unknown = set(port_attrs.keys()) - self.VALID_ATTRIBUTES
        if unknown:
            self.logger.warning("Skipping unknown attributes: %s", unknown)

        port = classifier.add_port(name)  # type: ignore[attr-defined]
        self._set_attributes(classifier, port, port_attrs)

        full_path = f"{parent_path}/{name}"
        self.logger.info("Created port: %s", full_path)
        return name

    def _report_results(self, created: List[str], errors: List[str], total: int) -> None:
        """Log summary of creation results."""
        if errors and not created:
            raise CliExecutionError(f"Created 0/{total} ports; all failed")
        if errors:
            self.logger.info("Created %d/%d ports with %d error(s)", len(created), total, len(errors))

    def _load_json_data(self, attributes_input: str) -> Dict[str, object]:
        """Load JSON data from inline string or external file.

        SWR_PORT_00007: External JSON File Support
        """
        if attributes_input.startswith("{") or attributes_input.startswith("["):
            try:
                return cast(Dict[str, object], json.loads(attributes_input))
            except json.JSONDecodeError as e:
                raise CliExecutionError(f"Invalid JSON: {e}") from e

        if not Path(attributes_input).exists():
            raise CliExecutionError(f"File not found: {attributes_input}")

        try:
            with open(attributes_input, encoding="utf-8") as f:
                return cast(Dict[str, object], json.load(f))
        except json.JSONDecodeError as e:
            raise CliExecutionError(f"Invalid JSON in file: {e}") from e
        except OSError as e:
            raise CliExecutionError(f"Failed to read file: {e}") from e

    def _set_attributes(self, classifier: RPModelElement, port: RPModelElement, attrs: Dict[str, object]) -> None:
        """Set validated attributes on port."""
        if "name" in attrs:
            port.set_name(cast(str, attrs["name"]))
        if "description" in attrs:
            port.set_description(cast(str, attrs["description"]))
        self._set_boolean_flags(port, attrs)
        self._set_port_contract(classifier, port, attrs)

    def _set_boolean_flags(self, port: RPModelElement, attrs: Dict[str, object]) -> None:
        """Set boolean flags isBehavioral, isReversed.

        SWR_PORT_00012: IsBehavioral and IsReversed Support
        """
        if "isBehavioral" in attrs:
            port.set_is_behavioral(int(cast(Union[str, int], attrs["isBehavioral"])))  # type: ignore[attr-defined]
        if "isReversed" in attrs:
            port.set_is_reversed(int(cast(Union[str, int], attrs["isReversed"])))  # type: ignore[attr-defined]

    def _set_port_contract(self, classifier: RPModelElement, port: RPModelElement, attrs: Dict[str, object]) -> None:
        """Resolve and set the portContract.

        SWR_PORT_00011: PortContract Resolution
        """
        if "portContract" in attrs:
            contract_name = cast(str, attrs["portContract"])
            owner = classifier.get_owner()
            target = owner.find_nested_classifier_recursive(contract_name)  # type: ignore[attr-defined]
            if target is None:
                raise CliExecutionError(f"PortContract '{contract_name}' not found")
            port.set_port_contract(target)  # type: ignore[attr-defined]


class PortDeleteAction(AbstractPortAction):
    """Delete a port.

    SWR_PORT_00002: Port Delete Command
    SWR_PORT_00010: GUID Lookup Support
    """

    def __init__(self) -> None:
        """Initialize the 'delete' action."""
        super().__init__(command_id="delete")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'delete' subcommand and its arguments."""
        parser = sub_parser.add_parser("delete", help="Delete a port")
        self.add_path_argument(parser, required=False, help_text="Parent classifier path")
        parser.add_argument("--guid", default=None, help="Port GUID to delete")
        parser.add_argument("--name", default=None, help="Port name within classifier")
        self.add_verbose_argument(parser)

    def execute(self, args: argparse.Namespace) -> None:
        """Execute port deletion."""
        super().execute(args)
        has_path_name = args.path and args.name
        has_guid = args.guid is not None

        if has_path_name and has_guid:
            raise CliExecutionError("Only one of --path + --name or --guid may be specified")
        if not has_path_name and not has_guid:
            raise CliExecutionError("Either --path + --name or --guid must be specified")

        if has_guid:
            port = self._resolve_port_by_guid(args.guid)
            label = f"GUID '{args.guid}'"
        else:
            classifier = self._resolve_classifier(args.path)
            port = self._resolve_port(classifier, args.name)
            label = args.name

        try:
            port.delete_from_project()
            self.logger.info("Deleted port: %s", label)
        except Exception as e:
            self._handle_execution_error(e, f"Failed to delete port '{label}'")


class PortListAction(AbstractPortAction):
    """List ports on a classifier.

    SWR_PORT_00004: Port List Command
    SWR_PORT_00008: Multi-Format Output
    """

    def __init__(self) -> None:
        """Initialize the 'list' action."""
        super().__init__(command_id="list")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'list' subcommand and its arguments."""
        parser = sub_parser.add_parser("list", help="List ports on a classifier")
        self.add_path_argument(parser, required=True, help_text="Classifier path")
        parser.add_argument("--format", choices=["table", "json", "csv"], default="table", help="Output format")
        parser.add_argument("--output", default=None, help="Write output to file")
        self.add_verbose_argument(parser)

    def execute(self, args: argparse.Namespace) -> None:
        """Execute port list."""
        super().execute(args)
        classifier = self._resolve_classifier(args.path)

        try:
            port_names = self._collect_port_names(classifier)
            output = self._format_output(port_names, args.format)

            if args.output:
                self._write_to_file(args.output, output)
                self.logger.info("Wrote %d ports to: %s", len(port_names), args.output)
            else:
                # NOTE: Result data to stdout (not logger) so it stays safe for piping/redirection.
                print(output)
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, f"Failed to list ports in '{args.path}'")

    def _collect_port_names(self, classifier: RPModelElement) -> List[str]:
        """Collect names of ports on a classifier."""
        ports = classifier.get_ports()  # type: ignore[attr-defined]
        return [cast(RPModelElement, port).get_name() for port in ports]

    def _format_output(self, port_names: List[str], format_type: str) -> str:
        """Format output based on format parameter."""
        if format_type == "json":
            return OutputFormatter.json_format(port_names)
        elif format_type == "csv":
            table_rows = [[name] for name in port_names]
            return OutputFormatter.csv_format(["Name"], table_rows)
        else:
            table_rows = [[name] for name in port_names]
            return OutputFormatter.table(["Name"], table_rows)

    def _write_to_file(self, file_path: str, content: str) -> None:
        """Write content to file."""
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError as e:
            raise CliExecutionError(f"Failed to write file '{file_path}': {e}") from e


class PortViewAction(AbstractPortAction):
    """View port details.

    SWR_PORT_00003: Port View Command
    SWR_PORT_00008: Multi-Format Output
    SWR_PORT_00010: GUID Lookup Support
    """

    _VIEW_HEADERS = [
        "Name",
        "GUID",
        "Description",
        "IsBehavioral",
        "IsReversed",
        "PortContract",
        "MetaClass",
        "FullPath",
    ]
    _VIEW_KEYS = [
        "name",
        "guid",
        "description",
        "isBehavioral",
        "isReversed",
        "portContract",
        "metaClass",
        "fullPath",
    ]

    def __init__(self) -> None:
        """Initialize the 'view' action."""
        super().__init__(command_id="view")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'view' subcommand and its arguments."""
        parser = sub_parser.add_parser("view", help="View port details")
        self.add_path_argument(parser, required=False, help_text="Parent classifier path")
        parser.add_argument("--guid", default=None, help="Port GUID to view")
        parser.add_argument("--name", default=None, help="Port name within classifier")
        parser.add_argument("--format", choices=["table", "json", "csv"], default="table", help="Output format")
        parser.add_argument("--output", default=None, help="Write output to file")
        self.add_verbose_argument(parser)

    def execute(self, args: argparse.Namespace) -> None:
        """Execute port view."""
        super().execute(args)
        has_path_name = args.path and args.name
        has_guid = args.guid is not None

        if has_path_name and has_guid:
            raise CliExecutionError("Only one of --path + --name or --guid may be specified")
        if not has_path_name and not has_guid:
            raise CliExecutionError("Either --path + --name or --guid must be specified")

        if has_guid:
            port = self._resolve_port_by_guid(args.guid)
        else:
            classifier = self._resolve_classifier(args.path)
            port = self._resolve_port(classifier, args.name)

        try:
            data = self._collect_port_data(port)
            output = self._format_output(data, args.format)

            if args.output:
                self._write_to_file(args.output, output)
                self.logger.info("Wrote port details to: %s", args.output)
            else:
                # NOTE: Result data to stdout (not logger) so it stays safe for piping/redirection.
                print(output)
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, f"Failed to view port '{args.name or args.guid}'")

    def _collect_port_data(self, port: RPModelElement) -> Dict[str, object]:
        """Collect port details into a data dictionary.

        Normalizes boolean flags to int for clean JSON round-trip.
        """
        contract = port.get_port_contract()  # type: ignore[attr-defined]
        contract_name = cast(RPModelElement, contract).get_name() if contract is not None else ""
        return {
            "name": port.get_name(),
            "guid": port.get_guid(),
            "description": port.get_description(),
            "isBehavioral": int(port.get_is_behavioral()),  # type: ignore[attr-defined]
            "isReversed": int(port.get_is_reversed()),  # type: ignore[attr-defined]
            "portContract": contract_name,
            "metaClass": port.get_meta_class(),
            "fullPath": port.get_full_path_name(),
        }

    def _format_output(self, data: Dict[str, object], format_type: str) -> str:
        """Format output based on format parameter."""
        if format_type == "json":
            return OutputFormatter.json_format(data)
        elif format_type == "csv":
            data_row = [str(data[key]) for key in self._VIEW_KEYS]
            return OutputFormatter.csv_format(self._VIEW_HEADERS, [data_row])
        else:
            table_rows: List[List[str]] = [
                ["Name", str(data["name"])],
                ["GUID", str(data["guid"])],
                ["Description", str(data["description"])],
                ["IsBehavioral", str(data["isBehavioral"])],
                ["IsReversed", str(data["isReversed"])],
                ["PortContract", str(data["portContract"])],
                ["MetaClass", str(data["metaClass"])],
                ["FullPath", str(data["fullPath"])],
            ]
            return OutputFormatter.table(["Property", "Value"], table_rows)

    def _write_to_file(self, file_path: str, content: str) -> None:
        """Write content to file."""
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError as e:
            raise CliExecutionError(f"Failed to write file '{file_path}': {e}") from e


class PortUpdateAction(AbstractPortAction):
    """Update attributes of an existing port.

    SWR_PORT_00005: Port Update Command
    SWR_PORT_00007: External JSON File Support
    SWR_PORT_00010: GUID Lookup Support
    SWR_PORT_00011: PortContract Resolution
    SWR_PORT_00012: IsBehavioral and IsReversed Support
    """

    VALID_ATTRIBUTES = {
        "name",
        "isBehavioral",
        "isReversed",
        "portContract",
        "description",
    }

    def __init__(self) -> None:
        """Initialize the 'update' action."""
        super().__init__(command_id="update")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'update' subcommand and its arguments."""
        parser = sub_parser.add_parser("update", help="Update attributes of an existing port")
        self.add_path_argument(parser, required=False, help_text="Parent classifier path")
        parser.add_argument("--guid", default=None, help="Port GUID to update")
        parser.add_argument("--name", default=None, help="Port name within classifier")
        parser.add_argument("--input", default=None, help="JSON file with port attributes")
        parser.add_argument("attributes", nargs="?", default=None, help="Inline JSON or JSON file path")
        self.add_verbose_argument(parser)

    def execute(self, args: argparse.Namespace) -> None:
        """Execute port update."""
        super().execute(args)
        has_path_name = args.path and args.name
        has_guid = args.guid is not None

        if has_path_name and has_guid:
            raise CliExecutionError("Only one of --path + --name or --guid may be specified")
        if not has_path_name and not has_guid:
            raise CliExecutionError("Either --path + --name or --guid must be specified")

        if has_guid:
            port = self._resolve_port_by_guid(args.guid)
            classifier = port.get_owner()
        else:
            classifier = self._resolve_classifier(args.path)
            port = self._resolve_port(classifier, args.name)

        input_data = args.input if args.input else args.attributes
        if not input_data:
            raise CliExecutionError("Either --input or attributes argument must be provided")

        data = self._load_json_data(input_data)

        unknown = set(data.keys()) - self.VALID_ATTRIBUTES
        if unknown:
            self.logger.warning("Skipping unknown attributes: %s", unknown)

        self._set_attributes(classifier, port, data)

        self.logger.info("Successfully updated port: %s", port.get_name())

    def _load_json_data(self, attributes_input: str) -> Dict[str, object]:
        """Load JSON data from inline string or external file.

        SWR_PORT_00007: External JSON File Support
        """
        if attributes_input.startswith("{") or attributes_input.startswith("["):
            try:
                return cast(Dict[str, object], json.loads(attributes_input))
            except json.JSONDecodeError as e:
                raise CliExecutionError(f"Invalid JSON: {e}") from e

        if not Path(attributes_input).exists():
            raise CliExecutionError(f"File not found: {attributes_input}")

        try:
            with open(attributes_input, encoding="utf-8") as f:
                return cast(Dict[str, object], json.load(f))
        except json.JSONDecodeError as e:
            raise CliExecutionError(f"Invalid JSON in file: {e}") from e
        except OSError as e:
            raise CliExecutionError(f"Failed to read file: {e}") from e

    def _set_attributes(self, classifier: RPModelElement, port: RPModelElement, attrs: Dict[str, object]) -> None:
        """Set validated attributes on port (partial update)."""
        if "name" in attrs:
            port.set_name(cast(str, attrs["name"]))
        if "description" in attrs:
            port.set_description(cast(str, attrs["description"]))
        if "isBehavioral" in attrs:
            port.set_is_behavioral(int(cast(Union[str, int], attrs["isBehavioral"])))  # type: ignore[attr-defined]
        if "isReversed" in attrs:
            port.set_is_reversed(int(cast(Union[str, int], attrs["isReversed"])))  # type: ignore[attr-defined]
        if "portContract" in attrs:
            contract_name = cast(str, attrs["portContract"])
            owner = classifier.get_owner()
            target = owner.find_nested_classifier_recursive(contract_name)  # type: ignore[attr-defined]
            if target is None:
                raise CliExecutionError(f"PortContract '{contract_name}' not found")
            port.set_port_contract(target)  # type: ignore[attr-defined]
