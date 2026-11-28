"""Tests for pure CLI action helpers (actions.support).

The helpers preserve the exact error-message contracts of the per-file
implementations they consolidate (characterization rule).
"""

from pathlib import Path

import pytest

from rhapsody_cli.actions.support import load_json_data, write_text_file
from rhapsody_cli.exceptions import CliExecutionError


class TestLoadJsonData:
    def test_inline_json_object(self) -> None:
        assert load_json_data('{"name":"Temp"}') == {"name": "Temp"}

    def test_inline_json_list(self) -> None:
        assert load_json_data('[{"name":"A"}]') == [{"name": "A"}]

    def test_inline_json_invalid_raises_with_contract_message(self) -> None:
        with pytest.raises(CliExecutionError, match="Invalid JSON:"):
            load_json_data("{not json")

    def test_json_file_reference(self, tmp_path: Path) -> None:
        f = tmp_path / "attrs.json"
        f.write_text('{"name":"FromFile"}')
        assert load_json_data(str(f)) == {"name": "FromFile"}

    def test_missing_file_raises_with_contract_message(self, tmp_path: Path) -> None:
        with pytest.raises(CliExecutionError, match="File not found:"):
            load_json_data(str(tmp_path / "nope.json"))

    def test_invalid_file_json_raises_with_contract_message(self, tmp_path: Path) -> None:
        f = tmp_path / "bad.json"
        f.write_text("{not json")
        with pytest.raises(CliExecutionError, match="Invalid JSON in file:"):
            load_json_data(str(f))


class TestWriteTextFile:
    def test_writes_content(self, tmp_path: Path) -> None:
        target = tmp_path / "out.txt"
        write_text_file(str(target), "hello")
        assert target.read_text() == "hello"

    def test_write_failure_raises_with_contract_message(self, tmp_path: Path) -> None:
        with pytest.raises(CliExecutionError, match="Failed to write file"):
            # Writing a path whose parent is a FILE makes open() fail with NotADirectoryError (OSError).
            blocker = tmp_path / "blocker"
            blocker.write_text("i am a file")
            write_text_file(str(blocker / "out.txt"), "x")
