from pathlib import Path

import pytest

import scripts.validate_model_api as validator
from scripts.pywin32_authority import (
    AuthorityData,
    build_authority,
    build_authority_from_typelib,
    export_catalog_from_reports,
    load_authority,
    write_authority,
)


def _package_report(root: Path, name: str) -> Path:
    report_dir = root / "com" / "telelogic" / "rhapsody" / "core"
    report_dir.mkdir(parents=True, exist_ok=True)
    return report_dir / name


def test_export_catalog_from_reports_extracts_names_and_kinds(tmp_path: Path) -> None:
    report = _package_report(tmp_path, "IRPExample_api_report.md")
    report.write_text(
        "# Rhapsody API Validation: IRPExample\n"
        "| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| — | — | addItem (method); Count (property) | PYWIN32_ONLY_MEMBER | Review. |\n",
        encoding="utf-8",
    )

    assert export_catalog_from_reports(tmp_path) == {"IRPExample": {"addItem": "method", "Count": "property"}}


def test_build_authority_starts_with_empty_exception_maps(tmp_path: Path) -> None:
    _package_report(tmp_path, "IRPExample_api_report.md").write_text(
        "| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |\n" "| --- | --- | --- | --- | --- |\n" "| — | — | addItem (method) | PYWIN32_ONLY_MEMBER | Review. |\n",
        encoding="utf-8",
    )

    data = build_authority(tmp_path)

    assert data["catalog"] == {"IRPExample": {"addItem": "method"}}
    assert data["documented_aliases"] == {}
    assert data["documented_unavailable"] == {}


def test_build_authority_from_typelib_uses_registered_members(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    _package_report(tmp_path, "IRPExample_api_report.md").write_text("", encoding="utf-8")
    monkeypatch.setattr(validator, "collect_registered_pywin32_members", lambda interface_name: {"isFoo": "method", "Bar": "property"})

    data = build_authority_from_typelib(tmp_path)

    assert data["catalog"] == {"IRPExample": {"isFoo": "method", "Bar": "property"}}
    assert data["documented_aliases"] == {}
    assert data["documented_unavailable"] == {}


def test_load_authority_reports_missing_snapshot(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="Could not load pywin32 authority"):
        load_authority(tmp_path / "missing.json")


def test_load_authority_round_trip(tmp_path: Path) -> None:
    target = tmp_path / "authority.json"
    data = AuthorityData(
        catalog={"IRPExample": {"addItem": "method"}},
        documented_aliases={"IRPExample": {"get_add": "addItem"}},
        documented_unavailable={"IRPExample": ["toList"]},
    )

    write_authority(data, target)

    assert load_authority(target) == data
