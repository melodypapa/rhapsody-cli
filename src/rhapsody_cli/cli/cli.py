"""Main CLI entry point: registry-driven root parser (PanGu style)."""

import argparse
import logging
import sys
from typing import Dict, Protocol

from rhapsody_cli.actions.session import ConnectAction, DisconnectAction, StatusAction, VersionAction
from rhapsody_cli.actions.transfer import ExportAction, ImportAction
from rhapsody_cli.cli.logging_config import CliLoggingConfigurator
from rhapsody_cli.commands.attribute_command import AttributeCommand
from rhapsody_cli.commands.class_command import ClassCommand
from rhapsody_cli.commands.operation_command import OperationCommand
from rhapsody_cli.commands.package_command import PackageCommand
from rhapsody_cli.commands.port_command import PortCommand
from rhapsody_cli.commands.project_command import ProjectCommand
from rhapsody_cli.exceptions import CliExecutionError

logger = logging.getLogger(__name__)


class CliEntry(Protocol):
    """A top-level CLI command: registers a subparser and runs from the namespace."""

    def register(self, subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Create this entry's subparser under the root subparsers action."""
        ...

    def run(self, namespace: argparse.Namespace) -> None:
        """Execute this entry using values from the parsed namespace."""
        ...


def build_registry() -> Dict[str, CliEntry]:
    """Build the top-level command registry (name -> entry instance)."""
    return {
        "connect": ConnectAction(),
        "disconnect": DisconnectAction(),
        "status": StatusAction(),
        "version": VersionAction(),
        "export": ExportAction(),
        "import": ImportAction(),
        "class": ClassCommand(),
        "attribute": AttributeCommand(),
        "operation": OperationCommand(),
        "package": PackageCommand(),
        "port": PortCommand(),
        "project": ProjectCommand(),
    }


def build_root_parser(commands: Dict[str, CliEntry]) -> argparse.ArgumentParser:
    """Build the root parser with global flags and every registered command.

    Args:
        commands: The command registry from build_registry().

    Returns:
        The fully wired root ArgumentParser. Every subparser carries a
        ``set_defaults(entry=...)`` pointing at its registry entry, so the
        parsed namespace selects the dispatcher.
    """
    parser = argparse.ArgumentParser(prog="rhapsody-cli", description="Rhapsody CLI")
    parser.add_argument("--format", choices=["table", "json", "csv"], default="table", help="Output format (global; use before the command)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
    subparsers = parser.add_subparsers(dest="command", required=True, metavar="<command>")
    for entry in commands.values():
        entry.register(subparsers)
    for name, sub_parser in subparsers.choices.items():
        sub_parser.set_defaults(entry=commands[name])
    return parser


def main() -> None:
    """Main CLI entry point."""
    root_parser = build_root_parser(build_registry())
    namespace = root_parser.parse_args()
    CliLoggingConfigurator(verbose=namespace.verbose).configure()
    try:
        namespace.entry.run(namespace)
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


if __name__ == "__main__":
    main()
