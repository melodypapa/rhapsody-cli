"""Main CLI entry point using argparse - PanGu style architecture."""

import argparse
import logging
import sys
from typing import Optional, Set

from rhapsody_cli.actions.abstract_action import AbstractAction
from rhapsody_cli.actions.package_action import PackageExportAction, PackageImportAction
from rhapsody_cli.actions.session_action import ConnectAction, DisconnectAction, StatusAction, VersionAction
from rhapsody_cli.cli.logging_config import CliLoggingConfigurator
from rhapsody_cli.commands.attribute_command import AttributeCommand
from rhapsody_cli.commands.class_command import ClassCommand
from rhapsody_cli.commands.operation_command import OperationCommand
from rhapsody_cli.commands.package_command import PackageCommand
from rhapsody_cli.commands.port_command import PortCommand
from rhapsody_cli.commands.project_command import ProjectCommand
from rhapsody_cli.exceptions import CliExecutionError

logger = logging.getLogger(__name__)

# Command groups that are temporarily suspended: implementations are retained
# (actions/, commands/ and their tests) but dispatch rejects them with an
# explicit notice. Re-enable by removing the name here, from _usage(), and
# re-adding the dispatch/get_actions() wiring.
SUSPENDED_COMMANDS: Set[str] = {"attribute", "operation", "port"}


def main() -> None:
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        _usage("")

    command_name = sys.argv[1]
    command_args = sys.argv[2:]

    # Check for help
    if command_name in ("-h", "--help"):
        _usage("")

    # Suspended commands: reject with an explicit notice before any dispatch
    if command_name in SUSPENDED_COMMANDS:
        # NOTE: Suspension notice to stderr (mirrors usage-on-error behavior).
        print(f"rhapsody-cli: command '{command_name}' is temporarily suspended.", file=sys.stderr)
        print("Active commands: connect, disconnect, status, version, export, import, project, package, class", file=sys.stderr)
        sys.exit(2)

    # Check for verbose flag in args and configure logging
    verbose = "-v" in command_args or "--verbose" in command_args
    CliLoggingConfigurator(verbose=verbose).configure()

    # Check for output format flag
    output_format = "table"
    if "--format" in command_args:
        idx = command_args.index("--format")
        if idx + 1 < len(command_args):
            output_format = command_args[idx + 1]

    try:
        # Single-level commands (no AbstractCommand wrapper)
        action: AbstractAction
        if command_name == "connect":
            action = ConnectAction()
            # Parse args for connect
            parser = argparse.ArgumentParser(prog="rhapsody-cli connect")
            parser.add_argument("--timeout", type=int, help="Session timeout in minutes")
            parser.add_argument("--attach-only", action="store_true", help="Only attach to existing instance")
            parser.add_argument("--no-gui", action="store_true", help="Keep GUI hidden")
            parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
            parsed_args = parser.parse_args(command_args)
            action.execute(parsed_args)
            return

        elif command_name == "disconnect":
            action = DisconnectAction()
            parser = argparse.ArgumentParser(prog="rhapsody-cli disconnect")
            parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
            parsed_args = parser.parse_args(command_args)
            action.execute(parsed_args)
            return

        elif command_name == "status":
            action = StatusAction()
            parser = argparse.ArgumentParser(prog="rhapsody-cli status")
            parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
            parsed_args = parser.parse_args(command_args)
            action.execute(parsed_args)
            return

        elif command_name == "version":
            action = VersionAction()
            parser = argparse.ArgumentParser(prog="rhapsody-cli version")
            parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
            parsed_args = parser.parse_args(command_args)
            action.execute(parsed_args)
            return

        elif command_name == "export":
            action = PackageExportAction()
            parser = argparse.ArgumentParser(prog="rhapsody-cli export")
            parser.add_argument("--path", default=None, help="Path to package (defaults to root)")
            parser.add_argument("--file", required=True, help="Output YAML file path")
            parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
            parsed_args = parser.parse_args(command_args)
            # pi-lens-ignore: python-sql-injection
            # AbstractAction.execute() is the CLI action-dispatch method (no SQL in this layer).
            action.execute(parsed_args)
            return

        elif command_name == "import":
            action = PackageImportAction()
            parser = argparse.ArgumentParser(prog="rhapsody-cli import")
            parser.add_argument("--path", default=None, help="Path to target package (defaults to root)")
            parser.add_argument("--file", required=True, help="Input YAML file path")
            parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
            parsed_args = parser.parse_args(command_args)
            # pi-lens-ignore: python-sql-injection
            # AbstractAction.execute() is the CLI action-dispatch method (no SQL in this layer).
            action.execute(parsed_args)
            return

        # Two-level commands (existing)
        cmd: Optional[object] = None

        if command_name == "class":
            cmd = ClassCommand(command_args)
        elif command_name == "attribute":
            cmd = AttributeCommand(command_args)
        elif command_name == "package":
            cmd = PackageCommand(command_args)
        elif command_name == "operation":
            cmd = OperationCommand(command_args)
        elif command_name == "port":
            cmd = PortCommand(command_args)
        elif command_name == "project":
            cmd = ProjectCommand(command_args)
        else:
            _usage(f"Unknown command: {command_name}")

        # Execute the command
        if cmd and hasattr(cmd, "execute"):
            cmd.execute(output_format=output_format)

    except KeyboardInterrupt:
        # NOTE: Terminal feedback for interactive Ctrl+C; print() to stdout
        # with a leading newline to clear the ^C echo. Logger would add
        # timestamps/levels that clutter this one-word message.
        print("\nInterrupted")
        sys.exit(130)
    except SystemExit:
        raise
    except CliExecutionError as e:
        # The single legitimate place sys.exit() is called for our own
        # errors: all CLI actions/commands raise CliExecutionError instead
        # of calling sys.exit() directly.
        logger.error(str(e))
        sys.exit(e.exit_code)
    except Exception as e:
        logger.error("Command failed: %s", e)
        sys.exit(1)


def _usage(error: str) -> None:
    """Print usage message and exit."""
    commands_text = "Single-Level Commands:\n"
    commands_text += "  connect     Connect to Rhapsody\n"
    commands_text += "  disconnect  Disconnect from Rhapsody\n"
    commands_text += "  status      Show connection status\n"
    commands_text += "  version     Show CLI version\n"
    commands_text += "  export      Export a package to a YAML file\n"
    commands_text += "  import      Import a YAML file into a package\n\n"
    commands_text += "Two-Level Commands:\n"
    commands_text += "  class       Manage classes\n"
    commands_text += "  package     Manage packages\n"
    commands_text += "  project     Manage projects\n\n"
    commands_text += "Suspended Commands (temporarily disabled, implementations retained):\n"
    commands_text += "  attribute   Manage attributes\n"
    commands_text += "  operation   Manage operations\n"
    commands_text += "  port        Manage ports\n"
    options_text = "Global Options:\n"
    options_text += "  --format <format>   Output format (table, json, csv). Default: table\n"
    options_text += "  -v|--verbose        Enable debug logging\n"
    options_text += "  -h|--help          Show this help message\n"

    message = "Usage:\n  rhapsody-cli <command> [options]\n\n"
    message += commands_text + "\n" + options_text

    if error != "":
        # NOTE: Usage/error output to stderr (mirrors argparse's help-on-error behavior).
        print(f"Error: {error}\n", file=sys.stderr)
        print(message, file=sys.stderr)
    else:
        # NOTE: Help/usage output to stdout (mirrors argparse's --help behavior).
        print(message)
    sys.exit(2 if error else 0)


if __name__ == "__main__":
    main()
