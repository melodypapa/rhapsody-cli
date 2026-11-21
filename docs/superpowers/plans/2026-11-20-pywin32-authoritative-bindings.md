# IRPClass Pywin32 Binding Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring `docs/reports/IRPClass_api_report.md` to zero actionable deviations, removing wrappers that call COM members the authenticated pywin32 interface does not expose **first**, then fixing the members it does expose under different names.

**Architecture:** The validator (`scripts/validate_model_api.py`) compares Java Javadoc, wrapper AST, and the pywin32 generated interface. This plan adds a committed authority snapshot (pywin32 name → kind per interface, plus documented aliases and documented-unavailable members) and an offline `--source authority` mode. `IRPClass` (`src/rhapsody_cli/models/elements/classifiers/model_class.py`) is the only target report; several root causes live in the inherited `RPModelElement` (`src/rhapsody_cli/models/core.py`) and are fixed there because they cannot be fixed in the child class.

**Tech Stack:** Python 3.8+ stdlib (`ast`, `json`, `argparse`, `pathlib`, `typing.TypedDict`), pytest, ruff/black/mypy, Markdown reports. Windows CI has pywin32 and live Rhapsody; macOS/Linux needs the temporary `pywintypes` stub documented in Task 7.

---

## IRPClass deviation inventory and proposed solution by type

`docs/reports/IRPClass_api_report.md` has **83 deviation rows**. Each row type and its proposed treatment:

| # | Rows | Deviation type | Root cause (IRPClass-specific) | Proposed solution |
|---|---:|---|---|---|
| 1 | 56 | `ACCESSOR_ALIAS_MISMATCH` + `METHOD_PROPERTY_MISMATCH` | Java `getX`/`setX` methods vs pywin32 `x` properties; wrappers already use `_get_method_or_property` | **No code change.** Classify as informational — expected once pywin32 is authoritative. |
| 2 | 10 | `PYTHON_ONLY_MEMBER` | 4 local helpers (`is_a_template`, `is_modified`, `is_reference_unit`, `is_remote`); 5 `NotImplementedError` stubs (`add_event_reception_with_event`, `create_oslc_link`, `delete_oslc_link`, `get_oslc_links`, `set_description_html`); `set_is_abstract` documented stub | Keep as-is; classify informational. Stubs are deliberate, documented unavailable APIs — **do not delete** the rationale. List their Java names in `documented_unavailable`. |
| 3 | 5 | `MISSING_PYTHON_WRAPPER` | pywin32 exposes `createOSLCLink`, `deleteOSLCLink`, `getOSLCLinks`, `lockOnDesignManager`, `unlockOnDesignManager`; no callable wrapper | Do **not** add wrappers in this plan. The three OSLC members are already documented as unsupported (see #2); `lockOnDesignManager`/`unlockOnDesignManager` go to the wrapper backlog with signature verification on Windows. |
| 4 | 2 | `COM_MEMBER_NOT_EXPOSED` + alias/property | `get_binary_id` falls back to `binaryID` but pywin32 exposes `BinaryID`; `get_cm_header`/`set_cm_header` fall back to `cMHeader` but pywin32 exposes `CMHeader` | **Fix** the fallback names in `core.py` to `BinaryID` / `CMHeader` (TDD in Task 4). |
| 5 | 2 | `PYWIN32_ONLY_MEMBER` | pywin32 exposes `deleteActivityDiagram`, `deleteStatechart`; no wrapper | Wrapper backlog — signatures must be verified against generated makepy source. No change now. |
| 6 | 2 | `PYTHON_METHOD_NAME_MISMATCH` + alias/property | `get_description_html` and `get_is_abstract` are snake_case of the Java getters, but canonicalisation expects the property-shaped names `description_html` / `is_abstract` | **Document aliases** in the authority file; no public rename (breaking change). Task 5. |
| 7 | 2 | `PYWIN32_MEMBER_MISSING` | `RPClass.update_contained_diagrams_on_server` calls `updateContainedDiagramsOnServer` (not in pywin32); inherited `RPModelElement.get_rmm_url` calls `getRmmUrl` (not in pywin32) | **Remove first:** delete `RPClass.update_contained_diagrams_on_server` and its unit test (Task 3). `get_rmm_url` lives on the shared base — cannot be removed in an IRPClass-only change; list `getRmmUrl` in `documented_unavailable` and track base removal in #121. |
| 8 | 1 | `JAVA_ONLY_MEMBER` | `addEventReceptionWithEvent` exists only in Java | Already covered by #2: wrapper is a documented `NotImplementedError` stub. Classify informational, no wrapper added. |
| 9 | 1 | `COM_MEMBER_NOT_EXPOSED` + alias | `get_is_of_meta_class` calls `getIsOfMetaClass`; pywin32 exposes `isOfMetaClass (method)` | **Fix** to call `self._com.isOfMetaClass(meta_class)` directly (Task 4). A getter/property helper would return the bound method without invoking it. |
| 10 | 1 | `MISSING_PYTHON_WRAPPER` + alias/property | Java `getStereotype`/`setStereotype` vs pywin32 `stereotype` property; no wrapper | Backlog: add a `get_stereotype` wrapper only after verifying the pywin32 property is readable. No change now. |
| 11 | 1 | `ACCESSOR_ALIAS_MISMATCH` | `get_unit_path` calls `getUnitPath` (not in pywin32); `set_unit_path` matches pywin32 `setUnitPath (method)` | Keep setter; getter is unavailable on the authenticated binding. Document `getUnitPath` in `documented_unavailable`. Informational. |

**Priority:** Task 3 (removal of the unavailable RPClass member) runs before any fix or backlog work.

## Property vs method refactor — IRPClass only

This plan does **not** refactor property/method handling across the wrapper hierarchy. The shared helpers (`com_utils._get_method_or_property` / `_set_method_or_property`, `com_utils.py:31-58`) already implement the dual binding correctly, and the 56 getter/property rows in the IRPClass report are that pattern working as intended. Scope is limited to COM call sites **visible in the IRPClass report**.

| Shape in `IRPClass_api_report.md` | Correct wrapper form | IRPClass application |
|---|---|---|
| pywin32 member is a `property` (e.g. `BinaryID`, `CMHeader`, `isAbstract`, `activityDiagram`) | `_get_method_or_property(self._com, "getX", "x")` / `_set_method_or_property(...)`, Java name first, pywin32 name second | Already used by the 56 rows; only `BinaryID` and `CMHeader` have the wrong pywin32 name and are fixed in Task 4 |
| pywin32 member is a `method` (e.g. `isOfMetaClass`) | direct `com_utils.call_com(lambda: self._com.isOfMetaClass(...))` | `get_is_of_meta_class` is fixed in Task 4 — a getter/property helper would return the bound method without calling it |
| pywin32 member absent (e.g. `updateContainedDiagramsOnServer`, `getRmmUrl`) | remove the wrapper, or keep a documented `NotImplementedError` stub | `RPClass.update_contained_diagrams_on_server` removed in Task 3; inherited `get_rmm_url` documented in Task 5 |

**Explicit non-goals of this scoped consideration:**
- Python-facing names follow `docs/CODE_GUIDELINES.md` — snake_case methods (`get_binary_id`, `get_is_abstract`), UPPERCASE constants. The camelCase/PascalCase COM names in the table (`BinaryID`, `isAbstract`, `getBinaryID`) are **string arguments only**, never Python method or attribute names.
- No changes to property/method handling for the other 11 interfaces.
- No new validator status for "property called as method"; a one-off guard in Task 5 verifies the IRPClass-visible case. A generic validator check can be a follow-up in #121.

## Scope and non-goals

**In scope:**
- Offline pywin32 authority snapshot and validator authority mode (needed to classify the IRPClass report).
- Remove the IRPClass-owned wrapper that calls a pywin32-unavailable COM member.
- Fix the three IRPClass-visible COM calls that pywin32 exposes under different names (`BinaryID`, `CMHeader`, `isOfMetaClass`).
- Document intentional aliases and documented-unavailable members so IRPClass has zero actionable rows.
- Regenerate and guard `docs/reports/IRPClass_api_report.md`.

**Out of scope:**
- The other 11 interfaces and their reports.
- Deleting `RPModelElement` stubs (`create_oslc_link`, `delete_oslc_link`, `get_oslc_links`, `set_description_html`, `get_rmm_url`) — shared base class, tracked in #121.
- Removing `RPClass.set_is_abstract` — it is an intentional, documented `NotImplementedError` backed by a verified Rhapsody persistence bug.
- Adding any of the 8 new wrappers (`lockOnDesignManager`, `unlockOnDesignManager`, `getStereotype`, `deleteActivityDiagram`, `deleteStatechart`, etc.) — signature verification required; backlog in #121.
- Renaming public methods.

## File structure

| File | Responsibility |
|---|---|
| `scripts/pywin32_authority.py` (new) | Load/write authority JSON; export catalog from generated reports. |
| `docs/reports/pywin32_authority.json` (new, generated + edited) | pywin32 name→kind per interface, documented aliases, documented-unavailable Java names. |
| `scripts/validate_model_api.py` (modify) | `--source authority`, row split into deviations/informational/backlog, new report sections. |
| `tests/unit/test_pywin32_authority.py` (new) | Catalog export and authority round-trip tests. |
| `tests/unit/test_validate_model_api.py` (modify) | Authority post-processing tests and IRPClass report guard. |
| `src/rhapsody_cli/models/elements/classifiers/model_class.py` (modify) | Remove `update_contained_diagrams_on_server`; update parity checklist. |
| `tests/unit/models/elements/classifiers/test_model_class.py` (modify) | Remove old delegation test; add removal guard. |
| `src/rhapsody_cli/models/core.py` (modify) | `BinaryID`, `CMHeader`, `isOfMetaClass` call sites. |
| `tests/unit/models/test_core.py` (modify) | TDD tests for the three call-site changes. |
| `tests/integration/models/elements/classifiers/test_model_class.py` (modify) | Remove the integration test for the deleted IRPClass method. |
| `tests/integration/models/test_core.py` (modify) | Remove obsolete xfail, retitle documented-unavailable xfail; live verification of Task 4 call sites. |
| `docs/reports/IRPClass_api_report.md` (regenerate) | Proof of zero actionable deviations. |
| `docs/CODE_GUIDELINES.md` (modify) | "pywin32 Bindings Are Authoritative" rule. |

## Preflight

The feature branch `docs/pywin32-authoritative-bindings` already exists and PR #122 is open. Continue on it:

```bash
git switch docs/pywin32-authoritative-bindings
git fetch origin
```

---

### Task 1: Committed pywin32 authority module and snapshot

**Files:**
- Create: `scripts/pywin32_authority.py`, `tests/unit/test_pywin32_authority.py`
- Generate: `docs/reports/pywin32_authority.json`

- [ ] **Step 1: Write the failing tests**

Create `tests/unit/test_pywin32_authority.py`:

```python
from pathlib import Path

from scripts.pywin32_authority import (
    AuthorityData,
    build_authority,
    export_catalog_from_reports,
    load_authority,
    write_authority,
)


def test_export_catalog_from_reports_extracts_names_and_kinds(tmp_path: Path) -> None:
    report = tmp_path / "IRPExample_api_report.md"
    report.write_text(
        "# Rhapsody API Validation: IRPExample\n"
        "| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| — | — | addItem (method); Count (property) | PYWIN32_ONLY_MEMBER | Review. |\n",
        encoding="utf-8",
    )

    assert export_catalog_from_reports(tmp_path) == {"IRPExample": {"addItem": "method", "Count": "property"}}


def test_build_authority_starts_with_empty_exception_maps(tmp_path: Path) -> None:
    (tmp_path / "IRPExample_api_report.md").write_text(
        "| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| — | — | addItem (method) | PYWIN32_ONLY_MEMBER | Review. |\n",
        encoding="utf-8",
    )

    data = build_authority(tmp_path)

    assert data["catalog"] == {"IRPExample": {"addItem": "method"}}
    assert data["documented_aliases"] == {}
    assert data["documented_unavailable"] == {}


def test_load_authority_round_trip(tmp_path: Path) -> None:
    target = tmp_path / "authority.json"
    data = AuthorityData(
        catalog={"IRPExample": {"addItem": "method"}},
        documented_aliases={"IRPExample": {"get_add": "addItem"}},
        documented_unavailable={"IRPExample": ["toList"]},
    )

    write_authority(data, target)

    assert load_authority(target) == data
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/unit/test_pywin32_authority.py -q`
Expected: `ModuleNotFoundError: No module named 'scripts.pywin32_authority'`.

- [ ] **Step 3: Implement the module**

Create `scripts/pywin32_authority.py`:

```python
"""Committed pywin32 authority snapshot and documented binding exceptions."""

import argparse
import json
from pathlib import Path
from typing import Dict, List, TypedDict

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_PATH = REPOSITORY_ROOT / "docs" / "reports" / "pywin32_authority.json"
_REPORT_SUFFIX = "_api_report.md"


class AuthorityData(TypedDict):
    catalog: Dict[str, Dict[str, str]]
    documented_aliases: Dict[str, Dict[str, str]]
    documented_unavailable: Dict[str, List[str]]


def export_catalog_from_reports(reports_dir: Path) -> Dict[str, Dict[str, str]]:
    """Read the pywin32 column of generated reports into an offline catalog."""
    catalog: Dict[str, Dict[str, str]] = {}
    for report_path in sorted(reports_dir.glob("*" + _REPORT_SUFFIX)):
        interface_name = report_path.name[: -len(_REPORT_SUFFIX)]
        members: Dict[str, str] = {}
        for line in report_path.read_text(encoding="utf-8").splitlines():
            if not line.startswith("| ") or line.startswith("| Python model wrapper") or line.startswith("| ---"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) < 5:
                continue
            for entry in cells[2].split("; "):
                if entry == "—":
                    continue
                name, separator, kind_with_paren = entry.rpartition(" (")
                if not separator or not kind_with_paren.endswith(")"):
                    continue
                members[name] = kind_with_paren[:-1]
        catalog[interface_name] = members
    return catalog


def build_authority(reports_dir: Path) -> AuthorityData:
    """Build a fresh authority file with no documented exceptions yet."""
    return AuthorityData(
        catalog=export_catalog_from_reports(reports_dir),
        documented_aliases={},
        documented_unavailable={},
    )


def load_authority(path: Path = AUTHORITY_PATH) -> AuthorityData:
    """Load the committed authority snapshot."""
    data = json.loads(path.read_text(encoding="utf-8"))
    return AuthorityData(
        catalog=data["catalog"],
        documented_aliases=data["documented_aliases"],
        documented_unavailable=data["documented_unavailable"],
    )


def write_authority(data: AuthorityData, path: Path) -> None:
    """Write the authority snapshot as stable, reviewable JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Export the pywin32 catalog from generated validation reports")
    parser.add_argument("--reports-dir", type=Path, default=REPOSITORY_ROOT / "docs" / "reports")
    parser.add_argument("--output", type=Path, default=AUTHORITY_PATH)
    args = parser.parse_args()
    write_authority(build_authority(args.reports_dir), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python -m pytest tests/unit/test_pywin32_authority.py -q`
Expected: 3 passed.

- [ ] **Step 5: Generate and commit the snapshot**

```bash
python scripts/pywin32_authority.py
python -c 'import json; d=json.load(open("docs/reports/pywin32_authority.json")); print(d["catalog"]["IRPClass"]["isAbstract"], d["catalog"]["IRPClass"]["BinaryID"])'
```

Expected: `property property`.

```bash
git add scripts/pywin32_authority.py tests/unit/test_pywin32_authority.py docs/reports/pywin32_authority.json
git commit -m "feat: add committed pywin32 authority snapshot"
```

---

### Task 2: Validator authority mode and classification

**Files:**
- Modify: `scripts/validate_model_api.py`, `tests/unit/test_validate_model_api.py`

- [ ] **Step 1: Write the failing tests**

Append to `tests/unit/test_validate_model_api.py`:

```python
from typing import Dict, List, Optional

from scripts.pywin32_authority import AuthorityData


def _authority(
    aliases: Optional[Dict[str, Dict[str, str]]] = None,
    unavailable: Optional[Dict[str, List[str]]] = None,
) -> AuthorityData:
    return AuthorityData(
        catalog={},
        documented_aliases=aliases or {},
        documented_unavailable=unavailable or {},
    )


def test_apply_pywin32_authority_demotes_expected_differences() -> None:
    rows = [
        (
            "get_activity_diagram() -> activityDiagram; get_activity_diagram() -> getActivityDiagram",
            "getActivityDiagram (method)",
            "activityDiagram (property)",
            "ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Use a property-aware getter/setter fallback.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(rows, "IRPClass", _authority())

    assert deviations == []
    assert informational == rows
    assert backlog == []


def test_apply_pywin32_authority_suppresses_documented_alias() -> None:
    rows = [
        (
            "get_is_abstract() -> getIsAbstract; get_is_abstract() -> isAbstract",
            "getIsAbstract (method)",
            "isAbstract (property)",
            "PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Rename the Python method.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(
        rows, "IRPClass", _authority(aliases={"IRPClass": {"get_is_abstract": "is_abstract"}})
    )

    assert deviations == []
    assert informational == rows
    assert backlog == []


def test_apply_pywin32_authority_suppresses_documented_unavailable_member() -> None:
    rows = [
        (
            "get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl",
            "getRmmUrl (method)",
            "—",
            "PYWIN32_MEMBER_MISSING",
            "Use a member exposed by the registered type library.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(
        rows, "IRPClass", _authority(unavailable={"IRPClass": ["getRmmUrl"]})
    )

    assert (deviations, informational, backlog) == ([], [], [])


def test_apply_pywin32_authority_keeps_unexposed_member_as_deviation() -> None:
    rows = [
        (
            "get_binary_id() -> binaryID; get_binary_id() -> getBinaryID",
            "getBinaryID (method)",
            "BinaryID (property)",
            "COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Use the BinaryID property.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(rows, "IRPClass", _authority())

    assert deviations == [
        (
            "get_binary_id() -> binaryID; get_binary_id() -> getBinaryID",
            "getBinaryID (method)",
            "BinaryID (property)",
            "COM_MEMBER_NOT_EXPOSED",
            "Use the BinaryID property.",
        )
    ]
    assert informational == []
    assert backlog == []


def test_main_authority_source_reports_backlog_without_typelib(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(validator, "load_authority", lambda: _authority(catalog={"IRPClass": {"isAbstract": "property"}}))
    monkeypatch.setattr(validator, "collect_java_signatures", lambda interface_name, docs_root: {"isAbstract": {"IRPClass.isAbstract()"}})
    monkeypatch.setattr(validator, "collect_java_members", lambda interface_name, docs_root: {"isAbstract"})
    monkeypatch.setattr(validator, "collect_python_members", lambda interface_name, models_root: {"isAbstract": {"is_abstract() -> isAbstract"}})

    assert validator.main(["IRPClass", "--source", "authority"]) == 0

    report = (tmp_path / "IRPClass_api_report.md").read_text(encoding="utf-8")
    assert "## Expected Binding Differences" in report
    assert "## Wrapper Backlog" in report
    assert "No deviations require changes." in report
```

Extend the existing parser test `test_argument_parser_requires_one_interface_and_optional_report_directory` with:

```python
    assert default_args.source == "typelib"
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/unit/test_validate_model_api.py -q -k 'authority or argument_parser'`
Expected: failures for missing `apply_pywin32_authority` and `source`.

- [ ] **Step 3: Add imports, aliases, and post-processing**

Add after the existing `scripts` import in `scripts/validate_model_api.py`:

```python
from scripts.pywin32_authority import AuthorityData, load_authority
```

Add after `_HELPER_NAMES`:

```python
Rows = List[Tuple[str, str, str, str, str]]
_AUTHORITY_INFO_STATUSES = {"ACCESSOR_ALIAS_MISMATCH", "METHOD_PROPERTY_MISMATCH", "PYTHON_ONLY_MEMBER", "JAVA_ONLY_MEMBER"}
_AUTHORITY_BACKLOG_STATUSES = {"MISSING_PYTHON_WRAPPER", "PYWIN32_ONLY_MEMBER"}
```

Insert before `build_deviation_rows`:

```python
def apply_pywin32_authority(rows: Rows, interface_name: str, authority: AuthorityData) -> Tuple[Rows, Rows, Rows]:
    """Split raw deviations into actionable, informational, and backlog rows."""
    deviations: Rows = []
    informational: Rows = []
    backlog: Rows = []
    aliases = authority["documented_aliases"].get(interface_name, {})
    unavailable = set(authority["documented_unavailable"].get(interface_name, []))

    for row in rows:
        statuses = row[3].split("; ")
        remaining: List[str] = []
        for status in statuses:
            if status in _AUTHORITY_INFO_STATUSES:
                continue
            if status == "PYTHON_METHOD_NAME_MISMATCH":
                wrapper_names = {label.split("()", maxsplit=1)[0] for label in row[0].split("; ") if label != "—"}
                if wrapper_names and all(name in aliases for name in wrapper_names):
                    continue
            if status == "PYWIN32_MEMBER_MISSING":
                java_names = {entry[: -len(" (method)")] for entry in row[1].split("; ") if entry.endswith(" (method)")}
                if java_names and java_names.issubset(unavailable):
                    continue
            remaining.append(status)

        if any(status in _AUTHORITY_BACKLOG_STATUSES for status in remaining):
            backlog.append(row)
        elif remaining:
            deviations.append((row[0], row[1], row[2], "; ".join(remaining), row[4]))
        elif any(status in _AUTHORITY_INFO_STATUSES for status in statuses):
            informational.append(row)

    return deviations, informational, backlog
```

- [ ] **Step 4: Add report sections**

Insert before `render_markdown_report`:

```python
def _append_report_table(lines: List[str], heading: str, rows: Rows) -> None:
    lines.extend(["", heading, "", "| Python model wrapper | Java API | pywin32 | Status | Recommended change |", "| --- | --- | --- | --- | --- |"])
    if not rows:
        lines.append("| — | — | — | — | — |")
        return
    for row in rows:
        escaped_cells = [cell.replace("|", "\\|").replace("\n", "<br>") for cell in row]
        lines.append("| " + " | ".join(escaped_cells) + " |")
```

Change the `render_markdown_report` signature to:

```python
def render_markdown_report(
    interface_name: str,
    rows: Rows,
    wrapper_class: str,
    wrapper_path: str,
    java_signatures: Dict[str, Set[str]],
    member_counts: Tuple[int, int, int],
    authoritative: bool = False,
    informational_rows: Optional[Rows] = None,
    backlog_rows: Optional[Rows] = None,
) -> str:
```

After the `Deviations by status` block, insert:

```python
    if authoritative:
        lines.extend(
            [
                "",
                f"- Informational binding differences (expected): `{len(informational_rows or [])}`",
                f"- Wrapper backlog (supported members without wrappers): `{len(backlog_rows or [])}`",
            ]
        )
```

After the comparison-table rows / empty placeholder, insert:

```python
    if authoritative:
        _append_report_table(lines, "## Expected Binding Differences", informational_rows or [])
        _append_report_table(lines, "## Wrapper Backlog", backlog_rows or [])
```

- [ ] **Step 5: Add `--source` and rewire `main`**

Add to `build_arg_parser` before the `--path` argument:

```python
    parser.add_argument(
        "--source",
        choices=("typelib", "authority"),
        default="typelib",
        help="pywin32 member source: registered type library (Windows) or committed authority snapshot (offline)",
    )
```

Replace `main` with:

```python
def main(argv: Optional[List[str]] = None) -> int:
    args = build_arg_parser().parse_args(argv)
    authority = load_authority()
    repository_root = Path(__file__).resolve().parents[1]
    docs_root = repository_root / "docs" / "java_api" / "com" / "telelogic" / "rhapsody" / "core"
    models_root = repository_root / "src" / "rhapsody_cli" / "models"
    report_directory = args.path or Path.cwd()
    report_path = report_directory / f"{args.java_interface}_api_report.md"

    try:
        wrapper_class, wrapper_source = resolve_python_wrapper(args.java_interface, models_root)
        java_members = collect_java_members(args.java_interface, docs_root)
        java_signatures = collect_java_signatures(args.java_interface, docs_root)
        python_members = collect_python_members(args.java_interface, models_root)
        if args.source == "authority":
            pywin32_members = authority["catalog"].get(args.java_interface)
            if pywin32_members is None:
                raise ValueError(f"No pywin32 authority snapshot for {args.java_interface}")
        else:
            pywin32_members = collect_registered_pywin32_members(args.java_interface)
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    raw_rows = build_deviation_rows(python_members, java_members, pywin32_members)
    if args.source == "authority":
        rows, informational_rows, backlog_rows = apply_pywin32_authority(raw_rows, args.java_interface, authority)
    else:
        rows, informational_rows, backlog_rows = raw_rows, [], []

    try:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        python_method_names = {label.split("()", maxsplit=1)[0] for labels in python_members.values() for label in labels}
        member_counts = (len(python_method_names), len(java_members), len(pywin32_members))
        wrapper_path = wrapper_source.relative_to(repository_root).as_posix()
        markdown = render_markdown_report(
            args.java_interface,
            rows,
            wrapper_class,
            wrapper_path,
            java_signatures,
            member_counts,
            authoritative=(args.source == "authority"),
            informational_rows=informational_rows,
            backlog_rows=backlog_rows,
        )
        report_path.write_text(markdown, encoding="utf-8")
    except OSError as exc:
        print(f"Error writing Markdown report to {report_path}: {exc}", file=sys.stderr)
        return 2

    return 0 if not rows else 1
```

- [ ] **Step 6: Run tests and commit**

Run: `python -m pytest tests/unit/test_validate_model_api.py -q`
Expected: all tests pass.

```bash
git add scripts/validate_model_api.py tests/unit/test_validate_model_api.py
git commit -m "feat: validate wrappers against committed pywin32 authority"
```

---

### Task 3: Remove the IRPClass wrapper that calls an unavailable pywin32 member

**Files:**
- Modify: `src/rhapsody_cli/models/elements/classifiers/model_class.py:448-464` and its checklist at `:40`
- Modify: `tests/unit/models/elements/classifiers/test_model_class.py:331-336`

- [ ] **Step 1: Write the failing removal guard**

Add to `tests/unit/models/elements/classifiers/test_model_class.py`:

```python
def test_class_does_not_expose_unavailable_server_diagram_update() -> None:
    assert not hasattr(RPClass, "update_contained_diagrams_on_server")
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python -m pytest tests/unit/models/elements/classifiers/test_model_class.py -q -k unavailable_server_diagram`
Expected: 1 failure — the method still exists.

- [ ] **Step 3: Remove the method, its old test, and its checklist entry**

Delete this method from `model_class.py`:

```python
    def update_contained_diagrams_on_server(self, enforce_update: int) -> int:
        """Updates the views on the Rhapsody Model Manager server for all diagrams.

        Args:
            enforce_update: ``0`` to update only if changes were made,
                ``1`` to update regardless.

        Returns:
            The number of views updated, ``0`` if no update needed, ``-1`` on failure.

        Raises:
            RhapsodyRuntimeException: if the server update fails.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::updateContainedDiagramsOnServer(int enforceUpdate)
        """
        return int(AbstractRPModelElement.call_com(lambda: self._com.updateContainedDiagramsOnServer(enforce_update)))
```

Delete this test from `test_model_class.py`:

```python
def test_class_update_contained_diagrams_on_server_delegates_to_com() -> None:
    fake = make_fake_element("Class", updateContainedDiagramsOnServer=3)
    klass = RPClass(fake)

    assert klass.update_contained_diagrams_on_server(1) == 3

    fake.updateContainedDiagramsOnServer.assert_called_once_with(1)
```

Delete this checklist line from `model_class.py`:

```python
    # [x] update_contained_diagrams_on_server [x] impl [x] docstring [x] unit test  [x] integration test
```

Replace it with:

```python
    # update_contained_diagrams_on_server: unavailable in Rhapsody2.Application.1 type library; wrapper removed.
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `python -m pytest tests/unit/models/elements/classifiers/test_model_class.py -q`
Expected: all tests pass.

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/models/elements/classifiers/model_class.py tests/unit/models/elements/classifiers/test_model_class.py
git commit -m "fix: remove RPClass update_contained_diagrams_on_server (not in pywin32)"
```

---

### Task 4: Fix the three IRPClass-visible COM calls that pywin32 exposes under different names

**Files:**
- Modify: `tests/unit/models/test_core.py:708-713`, `:875-880`, plus new CMHeader tests
- Modify: `src/rhapsody_cli/models/core.py:661-671`, `:1861-1871`, `:2102-2111`, `:882-894`

- [ ] **Step 1: Write the failing tests**

Replace the existing `test_model_element_get_binary_id_returns_bytes` (lines 708-713) with:

```python
def test_model_element_get_binary_id_falls_back_to_pywin32_binaryid_property() -> None:
    fake = MagicMock(spec=["BinaryID"])
    fake.BinaryID = b"\x01\x02\x03"
    element = RPModelElement(fake)

    assert element.get_binary_id() == b"\x01\x02\x03"
```

Add next to it:

```python
def test_model_element_get_cm_header_falls_back_to_pywin32_cmheader_property() -> None:
    fake = MagicMock(spec=["CMHeader"])
    fake.CMHeader = "header-1"
    element = RPModelElement(fake)

    assert element.get_cm_header() == "header-1"


def test_model_element_set_cm_header_falls_back_to_pywin32_cmheader_property() -> None:
    fake = MagicMock(spec=[])
    element = RPModelElement(fake)

    element.set_cm_header("header-2")

    assert fake.CMHeader == "header-2"
```

Replace the existing `test_model_element_get_is_of_meta_class_returns_int` (lines 875-880) with:

```python
def test_model_element_get_is_of_meta_class_calls_pywin32_member() -> None:
    fake = MagicMock(spec=["isOfMetaClass"])
    fake.isOfMetaClass.return_value = 1
    element = RPModelElement(fake)

    assert element.get_is_of_meta_class("Class") == 1
    fake.isOfMetaClass.assert_called_once_with("Class")
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/unit/models/test_core.py -q -k 'binary_id or cm_header or is_of_meta_class'`
Expected: 4 failures — no `BinaryID`, `CMHeader`, or `isOfMetaClass` attributes on the fakes.

- [ ] **Step 3: Implement the call-site changes**

In `get_binary_id` (`core.py:671`), replace the return with:

```python
        return bytes(AbstractRPModelElement._get_method_or_property(self._com, "getBinaryID", "BinaryID"))
```

Add to its docstring:

```python
        The authenticated pywin32 type library exposes this as the
        ``BinaryID`` property; ``getBinaryID`` is tried first for other bindings.
```

In `get_cm_header` (`core.py:1871`), replace the return with:

```python
        return str(AbstractRPModelElement._get_method_or_property(self._com, "getCMHeader", "CMHeader"))
```

In `set_cm_header` (`core.py:2111`), replace the call with:

```python
        AbstractRPModelElement._set_method_or_property(self._com, "setCMHeader", "CMHeader", cm_header)
```

Add the same pywin32-name note to both docstrings.

In `get_is_of_meta_class` (`core.py:894`), replace the return with:

```python
        return int(AbstractRPModelElement.call_com(lambda: self._com.isOfMetaClass(meta_class)))
```

Add to its docstring:

```python
        The pywin32 binding exposes ``isOfMetaClass`` as a method. A getter/
        property helper is not usable here because it would return the bound
        method without calling it.
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python -m pytest tests/unit/models/test_core.py -q`
Expected: all tests pass.

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/models/core.py tests/unit/models/test_core.py
git commit -m "fix: call pywin32-exposed BinaryID, CMHeader and isOfMetaClass members"
```

---

### Task 5: Document IRPClass aliases/unavailable members and regenerate the report

**Files:**
- Modify: `docs/reports/pywin32_authority.json`
- Regenerate: `docs/reports/IRPClass_api_report.md`
- Modify: `tests/unit/test_validate_model_api.py` (guard test)

- [ ] **Step 1: Add the documented exceptions**

Edit `docs/reports/pywin32_authority.json` so the two exception maps (currently empty `{}` after Task 1) become:

```json
    "documented_aliases": {
      "IRPClass": {
        "get_description_html": "description_html",
        "get_is_abstract": "is_abstract"
      }
    },
    "documented_unavailable": {
      "IRPClass": [
        "addEventReceptionWithEvent",
        "createOSLCLink",
        "deleteOSLCLink",
        "getOSLCLinks",
        "getRmmUrl",
        "getUnitPath",
        "setDescriptionHTML",
        "setIsAbstract",
        "updateContainedDiagramsOnServer"
      ]
    }
```

Do not edit the `catalog` map.

- [ ] **Step 2: Regenerate the IRPClass report offline**

```bash
python scripts/validate_model_api.py IRPClass --source authority --path docs/reports
```

Expected: exit code `0`.

Verify with:

```bash
python - <<'PY'
from pathlib import Path
text = Path("docs/reports/IRPClass_api_report.md").read_text(encoding="utf-8")
section = text.split("## Comparison details", 1)[1].split("## Expected Binding Differences", 1)[0]
rows = [line for line in section.splitlines() if line.startswith("| ") and "Python model wrapper" not in line and "---" not in line]
assert rows == [], rows
print("IRPClass: zero actionable deviations")
PY
```

Expected: `IRPClass: zero actionable deviations`.

Then guard the IRPClass-visible property/method shapes (no generic validator change):

```bash
python - <<'PY'
import ast
import json
from pathlib import Path

catalog = json.loads(Path("docs/reports/pywin32_authority.json").read_text(encoding="utf-8"))["catalog"]["IRPClass"]
properties = {name for name, kind in catalog.items() if "property" in kind}
sources = [
    Path("src/rhapsody_cli/models/core.py"),
    Path("src/rhapsody_cli/models/elements/classifiers/model_class.py"),
]
violations: list = []
for source in sources:
    tree = ast.parse(source.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        base = node.func.value
        if (
            isinstance(base, ast.Attribute)
            and base.attr == "_com"
            and isinstance(base.value, ast.Name)
            and base.value.id == "self"
            and node.func.attr in properties
        ):
            violations.append(f"{source}:{node.lineno}: {node.func.attr}()")
assert not violations, violations
print("IRPClass: no property-shaped pywin32 member called as a method")
PY
```

Expected: `IRPClass: no property-shaped pywin32 member called as a method`. If it fails, the listed call site must use `_get_method_or_property` instead of `self._com.X()`.

- [ ] **Step 3: Add the guard test**

Add to `tests/unit/test_validate_model_api.py`:

```python
def test_irpclass_report_has_no_actionable_deviations() -> None:
    reports_root = Path(__file__).resolve().parents[2] / "docs" / "reports"
    text = (reports_root / "IRPClass_api_report.md").read_text(encoding="utf-8")
    section = text.split("## Comparison details", 1)[1].split("## Expected Binding Differences", 1)[0]
    rows = [
        line
        for line in section.splitlines()
        if line.startswith("| ") and "Python model wrapper" not in line and "---" not in line
    ]
    assert rows == [], rows
```

Run: `python -m pytest tests/unit/test_validate_model_api.py -q -k irpclass_report`
Expected: 1 passed.

- [ ] **Step 4: Commit**

```bash
git add docs/reports/pywin32_authority.json docs/reports/IRPClass_api_report.md tests/unit/test_validate_model_api.py
git commit -m "docs: regenerate IRPClass report with zero binding deviations"
```

---

### Task 6: Integration tests for IRPClass and live COM verification

**Files:**
- Modify: `tests/integration/models/elements/classifiers/test_model_class.py:309-317`
- Modify: `tests/integration/models/test_core.py:1344-1359` and `:1273`
- Verify only (no edit): `tests/integration/models/test_core.py:1321-1330`, `:1760-1771`

- [ ] **Step 1: Delete the integration test for the removed method**

Delete this xfailed test from `tests/integration/models/elements/classifiers/test_model_class.py`:

```python
    @pytest.mark.xfail(strict=False, reason="IRPClass COM dispatch does not expose updateContainedDiagramsOnServer (AttributeError) though declared in the Java API")
    def test_update_contained_diagrams_on_server(self, test_project: RPProject) -> None:
        pkg_name = self._unique("SrvPkg")
        class_name = self._unique("SrvCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            test_class.update_contained_diagrams_on_server(0)
        finally:
            test_class.delete_from_project()
```

This is required by the integration scope rule: the file targets `RPClass` and asserts only its own methods; the method no longer exists.

- [ ] **Step 2: Remove the now-obsolete xfail on `get_is_of_meta_class`**

Task 4 changes the COM call to `isOfMetaClass`, which is the member pywin32 actually exposes. Replace the decorator line:

```python
    @pytest.mark.xfail(strict=False, reason="IRPModelElement.getIsOfMetaClass not exposed via COM dispatch (AttributeError: addClass.getIsOfMetaClass)")
```

with nothing, leaving the test body unchanged:

```python
    def test_get_is_of_meta_class_class(self, test_project: RPProject) -> None:
        pkg = self._create_package(test_project, self._unique("IsOfPkg"))
        try:
            cls = pkg.add_class(self._unique("IsOfCls"))
            result = cls.get_is_of_meta_class("Class")
            assert result

            not_result = cls.get_is_of_meta_class("Package")
            assert not not_result
        finally:
            pkg.delete_from_project()
```

- [ ] **Step 3: Retitle the xfail for `get_rmm_url`**

`get_rmm_url` is inherited and intentionally retained as a documented-unavailable wrapper (Task 5), so the live call still cannot succeed. Replace only the reason string:

```python
    @pytest.mark.xfail(strict=False, reason="getRmmUrl is listed in documented_unavailable; the pywin32 interface does not expose it")
```

Keep the test body unchanged.

- [ ] **Step 4: Collection verification (no Rhapsody required)**

```bash
pytest tests/integration/models/elements/classifiers/test_model_class.py tests/integration/models/test_core.py --collect-only -q
```

Expected: collection succeeds; `test_update_contained_diagrams_on_server` is absent from the collected list.

- [ ] **Step 5: Live verification on Windows/CI only**

These are the real proof that the pywin32 names chosen in Task 4 work against a live Rhapsody instance; they cannot run on macOS/Linux:

```bash
pytest tests/integration/models/test_core.py -k "get_binary_id or get_cm_header or get_is_of_meta_class" -v
pytest tests/integration/models/elements/classifiers/test_model_class.py -k "get_is_abstract" -v
```

Expected: `test_get_binary_id`, `test_set_and_get_cm_header_roundtrip`, and `test_get_is_of_meta_class_class` pass (the last one as a normal pass, not `xfail`); `get_is_abstract` is unaffected.

- [ ] **Step 6: Commit**

```bash
git add tests/integration/models/elements/classifiers/test_model_class.py tests/integration/models/test_core.py
git commit -m "test: align IRPClass integration tests with pywin32 bindings"
```

---

### Task 7: Record the rule and run the quality gate

**Files:**
- Modify: `docs/CODE_GUIDELINES.md` (insert before `## Questions?`)

- [ ] **Step 1: Add the guideline**

```markdown
## pywin32 Bindings Are Authoritative

The generated pywin32 interface from the registered `Rhapsody2 1.0` type library is the source of truth for COM member names and shapes. Java Javadoc may show `getX`/`setX` methods where pywin32 exposes a bare `X` property; those differences are informational, not defects.

- Confirm each COM member's exact name and kind in `docs/reports/pywin32_authority.json`.
- Call method-shaped members with `call_com(lambda: self._com.methodName(...))`.
- Read/write property-shaped members with `_get_method_or_property` / `_set_method_or_property`, Java-style name first and pywin32 name second. COM names are string arguments only; Python-facing names follow `docs/CODE_GUIDELINES.md` (snake_case methods, UPPERCASE constants), e.g. `get_binary_id` wraps `BinaryID`.
- If pywin32 does not expose a member at all, remove the wrapper that calls it (or keep a documented `NotImplementedError` stub) and add its Java name to `documented_unavailable`.
- Document intentional Python-name aliases in `documented_aliases` instead of renaming public methods.
- After changing a wrapper, regenerate its report with `python scripts/validate_model_api.py <IRPInterface> --source authority --path docs/reports` and require zero rows under `## Comparison details`.
- Property/method refactoring is scoped to the members visible in the report being fixed (here: IRPClass). Do not reshape the shared wrapper hierarchy for one interface's deviations.
```

- [ ] **Step 2: Install dev dependencies (if not already installed)**

```bash
pip install -e ".[dev,cli]"
```

The `cli` extra provides `tabulate` and `rich`; without it `pytest tests/unit/` fails during collection on `tests/unit/commands/*`.

- [ ] **Step 3: Run the quality gate**

On Windows/CI:

```bash
ruff check src/ tests/ scripts/ && black --check src/ tests/ scripts/ && mypy src/ tests/ scripts/ && pytest tests/unit/
```

On macOS/Linux (temporary stub, no repo changes):

```bash
STUB=$(mktemp -d); printf 'class com_error(Exception):\n    def __init__(self, *args):\n        self.args = args\n        super().__init__(*args)\n' > "$STUB/pywintypes.py"; PYTHONPATH="${STUB}:src" python -m pytest tests/unit/ -q; rm -rf "$STUB"
```

Expected: all tests pass; lint/format/type checks clean.

- [ ] **Step 4: Commit and push**

```bash
git add docs/CODE_GUIDELINES.md
git commit -m "docs: document pywin32-authoritative binding rule"
git push
```

Expected: PR #122 updates automatically.

---

## Self-review

**Spec coverage:** IRPClass is the only target report. All 11 deviation types from the inventory have an explicit proposal (table above) and a task that implements or consciously defers it. The "remove unavailable first" instruction is Task 3, ahead of all fixes. The property/method consideration is explicitly scoped to IRPClass-visible call sites, with a decision table and a one-off guard in Task 5 — no hierarchy-wide refactor. Shared-base limitations (`get_rmm_url`, OSLC stubs, `setDescriptionHTML`) are documented rather than silently left broken, and tracked in #121.

**Placeholder scan:** No TBD/TODO steps. Every code-changing step contains the complete code. Generated JSON is produced by a committed script with a verification command.

**Test coverage:** Unit tests cover every code change (validator classification, authority round-trip, removal guard, three call-site fixes, IRPClass report guard). Integration tests are explicitly handled in Task 6: the removed method's integration test is deleted, the obsolete `get_is_of_meta_class` xfail is removed, the `get_rmm_url` xfail reason is retitled, and the live `BinaryID`/`CMHeader` tests are the Windows-only proof of Task 4. Collection is verifiable offline; execution is CI-only per the project rules.

**Type consistency:** `AuthorityData` (catalog, documented_aliases, documented_unavailable) is defined once in Task 1 and used unchanged in Tasks 2 and 5. `apply_pywin32_authority(rows, interface_name, authority)` has one signature used by all tests and `main`. `Rows` matches `build_deviation_rows`' return type. No `Any` annotations; no Python 3.9-only APIs (py3.8 target honored).

**Deferred work:** The 8 new wrappers and the shared-base removals stay in tracking issue #121. The plan does not claim IRPClass functionality is complete — only that its report has zero actionable deviations under the pywin32-authoritative classification.
