"""Regression tests for system-test fixture lifecycle ordering."""

import inspect

from tests.system.cli.conftest import cli_connection


def test_cli_connection_depends_on_rhapsody_owner() -> None:
    """Keep the Rhapsody owner alive until all CLI fixture teardown is done."""
    fixture_function = cli_connection.__wrapped__

    assert "rhapsody_instance" in inspect.signature(fixture_function).parameters
