"""Element-related CLI commands using class-based architecture."""

from __future__ import annotations

import logging

import click

from rhapsody_cli.cli.context import RhapsodyContext
from rhapsody_cli.cli.formatters import OutputFormatter
from rhapsody_cli.exceptions import RhapsodyConnectionError

logger = logging.getLogger(__name__)

_NO_ACTIVE_INSTANCE_MESSAGE = (
    "No running Rhapsody instance found. Please open Rhapsody and a project first."
)


class BaseElementCommand(click.Command):
    """Base class for element commands."""

    pass


class AddElementCommand(BaseElementCommand):
    """Command: Add a new element to the project."""

    def __init__(self) -> None:
        super().__init__(
            name="add",
            help="Add a new element to the project.",
            callback=self.execute,
            params=[
                click.Option(
                    ["--type", "element_type"],
                    required=True,
                    help="Element type (class, actor, etc)",
                ),
                click.Option(["--name"], required=True, help="Element name"),
            ],
        )

    def execute(self, element_type: str, name: str) -> None:
        """Execute the add command."""
        ctx = RhapsodyContext()
        try:
            project = ctx.get_active_project()
        except RhapsodyConnectionError as e:
            logger.error("Failed to attach to Rhapsody: %s", e)
            click.echo(_NO_ACTIVE_INSTANCE_MESSAGE, err=True)
            raise click.Abort() from e

        try:
            root = project.getRoot()  # type: ignore[attr-defined]
            if element_type.lower() == "class":
                root.createClass(name)
            elif element_type.lower() == "actor":
                root.createActor(name)
            elif element_type.lower() == "package":
                root.createPackage(name)
            else:
                click.echo(f"Error: Unknown element type '{element_type}'", err=True)
                raise click.Abort()

            logger.info("Created %s: %s", element_type, name)
            click.echo(f"Created {element_type}: {name}")
        except click.Abort:
            raise
        except Exception as e:
            logger.error("Failed to create %s '%s': %s", element_type, name, e)
            click.echo(f"Error: {e}", err=True)
            raise click.Abort() from e


class ViewElementCommand(BaseElementCommand):
    """Command: View element details."""

    def __init__(self) -> None:
        super().__init__(
            name="view",
            help="View element details.",
            callback=self.execute,
            params=[
                click.Option(["--path"], required=True, help="Element path (e.g., Root::MyClass)"),
            ],
        )

    def execute(self, path: str) -> None:
        """Execute the view command."""
        ctx = RhapsodyContext()
        try:
            ctx.get_active_project()
        except RhapsodyConnectionError as e:
            logger.error("Failed to attach to Rhapsody: %s", e)
            click.echo(_NO_ACTIVE_INSTANCE_MESSAGE, err=True)
            raise click.Abort() from e

        try:
            data = {
                "path": path,
                "type": "unknown",
                "properties": {"status": "read-only for demo"},
            }

            if ctx.output_format == "json":
                output = OutputFormatter.json_format(data)
            else:
                rows = [["path", path], ["type", "unknown"]]
                output = OutputFormatter.table(["Property", "Value"], rows)

            click.echo(output)
        except click.Abort:
            raise
        except Exception as e:
            logger.error("Failed to view element '%s': %s", path, e)
            click.echo(f"Error: {e}", err=True)
            raise click.Abort() from e


class QueryElementCommand(BaseElementCommand):
    """Command: Query elements in active project."""

    def __init__(self) -> None:
        super().__init__(
            name="query",
            help="Query elements in active project.",
            callback=self.execute,
            params=[
                click.Option(["--filter"], default=None, help="Filter by type or name"),
            ],
        )

    def execute(self, filter: str) -> None:
        """Execute the query command."""
        ctx = RhapsodyContext()
        try:
            project = ctx.get_active_project()
        except RhapsodyConnectionError as e:
            logger.error("Failed to attach to Rhapsody: %s", e)
            click.echo(_NO_ACTIVE_INSTANCE_MESSAGE, err=True)
            raise click.Abort() from e

        try:
            root = project.getRoot()  # type: ignore[attr-defined]
            elements = root.getNestedElements()

            if ctx.output_format == "json":
                data = {
                    "elements": [
                        {
                            "name": elem.getName(),
                            "type": elem.getMetaClass(),
                        }
                        for elem in elements
                    ]
                }
                output = OutputFormatter.json_format(data)
            else:
                rows = [[elem.getName(), elem.getMetaClass()] for elem in elements]
                output = OutputFormatter.table(["Name", "Type"], rows)

            click.echo(output)
        except click.Abort:
            raise
        except Exception as e:
            logger.error("Failed to query elements: %s", e)
            click.echo(f"Error: {e}", err=True)
            raise click.Abort() from e


class ElementCommandGroup(click.Group):
    """Command group for element operations."""

    def __init__(self) -> None:
        super().__init__(
            name="element",
            help="Manage model elements.",
            invoke_without_command=False,
        )
        self.add_command(AddElementCommand())
        self.add_command(ViewElementCommand())
        self.add_command(QueryElementCommand())


element = ElementCommandGroup()
