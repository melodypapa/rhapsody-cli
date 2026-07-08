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
            
            # Find or use a suitable container
            container = root
            
            # For classes and actors, try to use the Default package if it exists
            if element_type.lower() in ("class", "actor"):
                nested_elements = root.getNestedElements()
                for elem in nested_elements:
                    if elem.getName() == "Default" and elem.getMetaClass() == "Package":
                        container = elem
                        break
            
            if element_type.lower() == "class":
                container.addClass(name)
            elif element_type.lower() == "actor":
                container.addActor(name)
            elif element_type.lower() == "package":
                container.addNestedPackage(name) if container != root else root.addPackage(name)
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

    def execute(self, **kwargs: object) -> None:
        """Execute the query command."""
        filter_str = kwargs.get("filter")
        if filter_str is not None:
            filter_str = str(filter_str)

        ctx = RhapsodyContext()
        try:
            project = ctx.get_active_project()
        except RhapsodyConnectionError as e:
            logger.error("Failed to attach to Rhapsody: %s", e)
            click.echo(_NO_ACTIVE_INSTANCE_MESSAGE, err=True)
            raise click.Abort() from e

        try:
            root = project.getRoot()  # type: ignore[attr-defined]
            elements = list(root.getNestedElements())
            
            # Also search in the Default package for classes
            for elem in root.getNestedElements():
                if elem.getName() == "Default" and elem.getMetaClass() == "Package":
                    try:
                        elements.extend(list(elem.getNestedElements()))
                    except Exception:
                        pass  # If we can't get nested elements, just skip

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


class DeleteElementCommand(BaseElementCommand):
    """Command: Delete an element from the project."""

    def __init__(self) -> None:
        super().__init__(
            name="delete",
            help="Delete an element from the project.",
            callback=self.execute,
            params=[
                click.Option(
                    ["--path"],
                    required=True,
                    help="Element path (e.g., Root::MyClass)",
                ),
            ],
        )

    def execute(self, **kwargs: object) -> None:
        """Execute the delete command."""
        path = str(kwargs.get("path", ""))

        ctx = RhapsodyContext()
        try:
            project = ctx.get_active_project()
        except RhapsodyConnectionError as e:
            logger.error("Failed to attach to Rhapsody: %s", e)
            click.echo(_NO_ACTIVE_INSTANCE_MESSAGE, err=True)
            raise click.Abort() from e

        try:
            root = project.getRoot()  # type: ignore[attr-defined]

            # Parse path to extract parent path and element name
            path_parts = path.split("::")
            if len(path_parts) < 2:
                msg = f"Error: Invalid path format '{path}'. Use 'Root::ElementName'"
                click.echo(msg, err=True)
                raise click.Abort()

            element_name = path_parts[-1]
            parent_path_parts = path_parts[:-1]

            # Navigate to parent container
            parent = root
            for part in parent_path_parts[1:]:  # Skip 'Root'
                nested = parent.getNestedElements()
                found = None
                for elem in nested:
                    if elem.getName() == part:
                        found = elem
                        break
                if not found:
                    click.echo(f"Error: Parent path not found: {part}", err=True)
                    raise click.Abort()
                parent = found

            # Find and delete the element
            nested = parent.getNestedElements()
            element_to_delete = None
            for elem in nested:
                if elem.getName() == element_name:
                    element_to_delete = elem
                    break
            
            # If not found in parent and parent is root, try Default package
            if not element_to_delete and parent == root:
                for elem in parent.getNestedElements():
                    if elem.getName() == "Default" and elem.getMetaClass() == "Package":
                        parent = elem
                        nested = parent.getNestedElements()
                        for elem_in_default in nested:
                            if elem_in_default.getName() == element_name:
                                element_to_delete = elem_in_default
                                break
                        break

            if not element_to_delete:
                click.echo(f"Error: Element '{element_name}' not found at path '{path}'", err=True)
                raise click.Abort()

            # Try to delete using different methods based on element type
            meta_class = element_to_delete.getMetaClass()
            deleted = False

            # Try direct delete method first (if available)
            if hasattr(element_to_delete._com, "delete"):
                element_to_delete._com.delete()
                deleted = True
            else:
                # Fall back to parent container methods
                if meta_class == "Class":
                    parent._com.deleteClass(element_to_delete._com)
                    deleted = True
                elif meta_class == "Actor":
                    parent._com.deleteActor(element_to_delete._com)
                    deleted = True
                elif meta_class == "Package":
                    parent._com.deletePackage(element_to_delete._com)
                    deleted = True

            if not deleted:
                click.echo(f"Error: Unable to delete element of type '{meta_class}'", err=True)
                raise click.Abort()

            logger.info("Deleted %s: %s", meta_class, element_name)
            click.echo(f"Deleted {meta_class.lower()}: {element_name}")
        except click.Abort:
            raise
        except Exception as e:
            logger.error("Failed to delete element at path '%s': %s", path, e)
            click.echo(f"Error: {e}", err=True)
            raise click.Abort() from e


class ElementCommandGroup(click.Group):
    """Command group for element operations."""

    def __init__(self) -> None:
        super().__init__(
            name="element",
            help="Manage model elements.",
            invoke_without_command=False,
            params=[
                click.Option(
                    ["--verbose", "-v"],
                    is_flag=True,
                    default=False,
                    help="Enable DEBUG-level logging (default: INFO).",
                ),
            ],
        )
        self.add_command(AddElementCommand())
        self.add_command(ViewElementCommand())
        self.add_command(QueryElementCommand())
        self.add_command(DeleteElementCommand())

    def invoke(self, ctx: click.Context) -> object:
        """Override invoke to configure logging based on verbose flag."""
        from rhapsody_cli.cli.logging_config import CliLoggingConfigurator
        
        verbose = ctx.params.get("verbose", False)
        CliLoggingConfigurator(verbose=verbose).configure()
        return super().invoke(ctx)


element = ElementCommandGroup()
