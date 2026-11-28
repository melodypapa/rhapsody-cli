"""Pure helpers shared by CLI actions (no COM, no session; file I/O only).

These consolidate the per-file ``_load_json_data``/``_write_to_file`` copies.
They preserve the exact error-message contracts of the implementations they
replaced — actions may assert on those messages.
"""

import json
import logging
from pathlib import Path
from typing import cast

from rhapsody_cli.exceptions import CliExecutionError

logger = logging.getLogger(__name__)


def load_json_data(attributes_input: str) -> object:
    """Load JSON data from an inline string or an external file.

    Resolution order (identical to the per-file implementations this
    consolidates): a string starting with ``{`` or ``[`` is parsed inline;
    anything else is treated as a file path.

    Args:
        attributes_input: Inline JSON text, or a path to a JSON file.

    Returns:
        The parsed JSON value (object or list, per caller's contract).

    Raises:
        CliExecutionError: "Invalid JSON: ..." for bad inline text,
            "File not found: ..." for a missing path, "Invalid JSON in
            file: ..." for unreadable file contents, "Failed to read
            file: ..." for OS-level read errors.
    """
    if attributes_input.startswith("{") or attributes_input.startswith("["):
        try:
            return json.loads(attributes_input)
        except json.JSONDecodeError as e:
            raise CliExecutionError(f"Invalid JSON: {e}") from e

    if not Path(attributes_input).exists():
        raise CliExecutionError(f"File not found: {attributes_input}")

    try:
        with open(attributes_input, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise CliExecutionError(f"Invalid JSON in file: {e}") from e
    except OSError as e:
        raise CliExecutionError(f"Failed to read file: {e}") from e


def load_json_mapping(attributes_input: str) -> "dict[str, object]":
    """Load a JSON object (mapping) via :func:`load_json_data` and cast it.

    Args:
        attributes_input: Inline JSON object text, or a path to a JSON file
            containing an object.

    Returns:
        The parsed JSON mapping.
    """
    return cast("dict[str, object]", load_json_data(attributes_input))


def write_text_file(file_path: str, content: str) -> None:
    """Write text content to a file (UTF-8).

    Args:
        file_path: Destination file path.
        content: Text content to write.

    Raises:
        CliExecutionError: "Failed to write file '<path>': ..." on OS errors.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except OSError as e:
        raise CliExecutionError(f"Failed to write file '{file_path}': {e}") from e
