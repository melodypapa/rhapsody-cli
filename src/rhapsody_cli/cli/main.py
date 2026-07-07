"""Main CLI entry point."""

from __future__ import annotations

import click

from rhapsody_cli.cli.commands.element import element as element_cmd
from rhapsody_cli.cli.commands.io import io as io_cmd
from rhapsody_cli.cli.context import RhapsodyContext
from rhapsody_cli.cli.logging_config import CliLoggingConfigurator

# NOTE: The `project` sub-command is temporarily disabled. Users open Rhapsody
# projects manually via the Rhapsody GUI; `element` commands attach to that
# running instance's active project instead. Re-enable by importing
# `project as project_cmd` from `rhapsody_cli.cli.commands.project` and adding
# `cli.add_command(project_cmd)` below.


@click.group()
@click.option(
    "--output",
    type=click.Choice(["table", "json", "csv"]),
    default="table",
    help="Output format",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    default=False,
    help="Enable DEBUG-level logging (default: INFO).",
)
@click.pass_context
def cli(ctx: click.Context, output: str, verbose: bool) -> None:
    """Rhapsody model CLI tool for browsing and managing models."""
    CliLoggingConfigurator(verbose=verbose).configure()
    if ctx.obj is None:
        ctx.obj = RhapsodyContext()
    ctx.obj.output_format = output


cli.add_command(element_cmd)
cli.add_command(io_cmd)


if __name__ == "__main__":
    cli()
