# Pywin32-Authoritative Binding Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the committed pywin32 type-library snapshot the source of truth for COM member names/shapes, and bring the two pilot wrappers (`RPCollection`, `RhapsodyApplication`) to zero actionable binding deviations in their validation reports.

**Architecture:** The existing validator (`scripts/validate_model_api.py`) compares three sources (Java Javadoc, wrapper AST, pywin32 generated interface) and currently counts Java-vs-pywin32 getter/property differences as deviations. This plan adds a committed JSON authority file (pywin32 catalog + documented exceptions), an offline `--source authority` mode, and a post-processing split that separates actionable deviations from expected informational differences and a wrapper backlog. Then it fixes the two wrappers' COM calls to use the names/kinds the pywin32 interface actually exposes, using the project's existing `_get_method_or_property` / `_set_method_or_property` fallback pattern.

**Tech Stack:** Python 3.8+ stdlib (`ast`, `json`, `argparse`, `pathlib`, `typing.TypedDict`), pytest, ruff/black/mypy, Markdown reports. Windows CI has pywin32; macOS/Linux needs the temporary `pywintypes` stub documented in Task 6.

---

## Scope and non-goals

**In scope:**
- Commit an offline pywin32 authority snapshot generated from the 12 existing reports.
- Validator `--source authority` mode and deviation classification under that mode.
- Fix the two real binding bugs in `RhapsodyApplication` (`getBuildNo`, `getOMROOT` called directly instead of via the exposed `BuildNo`/`OMROOT` properties).
- Document the intentional `get_version` alias and the Java-only members in `RPCollection` / `RhapsodyApplication` so they stop being false positives.
- Regenerate the two pilot reports; require zero rows under `## Comparison details`.
- Add a code-guideline entry so future wrappers follow the pywin32-authoritative rule.

**Explicitly out of scope (follow-up plans, one per interface):**
- Adding the 201 `MISSING_PYTHON_WRAPPER` and 34 `PYWIN32_ONLY_MEMBER` wrappers. These need method signatures from the generated makepy source on Windows; the reports contain names only. They will be listed in `## Wrapper Backlog` in the regenerated reports and tracked in the authority file.
- Touching the other 10 interfaces.
- Renaming public Python methods (breaking change) or deleting Java-only wrappers. Per decision, Java-only members are kept as documented compatibility fallbacks.

**Reference data (aggregated from the 12 reports, 967 rows):**

| Status | Count | Treatment in this plan |
|---|---|---|
| `ACCESSOR_ALIAS_MISMATCH` | 628 | Informational (expected with pywin32) |
| `METHOD_PROPERTY_MISMATCH` | 600 | Informational (expected with pywin32) |
| `MISSING_PYTHON_WRAPPER` | 201 | Wrapper backlog |
| `PYTHON_ONLY_MEMBER` | 89 | Informational (local facade helpers) |
| `COM_MEMBER_NOT_EXPOSED` | 40 | Actionable — fix wrapper COM call |
| `PYWIN32_ONLY_MEMBER` | 34 | Wrapper backlog |
| `PYWIN32_MEMBER_MISSING` | 31 | Actionable unless in `documented_java_only` |
| `PYTHON_METHOD_NAME_MISMATCH` | 19 | Actionable unless in `documented_aliases` |
| `JAVA_ONLY_MEMBER` | 3 | Actionable unless in `documented_java_only` |

Pilot-specific actionable rows: `IRPApplication` has 2 `COM_MEMBER_NOT_EXPOSED`, 1 `PYTHON_METHOD_NAME_MISMATCH`, 1 `JAVA_ONLY_MEMBER`; `IRPCollection` has 1 `PYWIN32_MEMBER_MISSING`, 1 `JAVA_ONLY_MEMBER`.

## File structure

| File | Responsibility |
|---|---|
| `scripts/pywin32_authority.py` (new) | Load/write the committed authority JSON; export the catalog from generated reports. |
| `docs/reports/pywin32_authority.json` (new, generated + edited) | Authoritative pywin32 name→kind map per interface, plus documented aliases and Java-only exceptions. |
| `scripts/validate_model_api.py` (modify) | Add `--source authority`, split rows into deviations/informational/backlog, render new sections. |
| `tests/unit/test_pywin32_authority.py` (new) | Unit tests for catalog export and authority round-trip. |
| `tests/unit/test_validate_model_api.py` (modify) | Unit tests for authority post-processing and offline mode. |
| `src/rhapsody_cli/application.py` (modify) | Use `BuildNo`/`OMROOT` property fallbacks; document `get_version` alias and Java-only member. |
| `tests/unit/test_application.py` (modify) | TDD tests for the two fallback paths. |
| `src/rhapsody_cli/models/core.py` (modify) | Document `RPCollection.add_graphical_item` as a Java-only fallback. |
| `docs/reports/IRPApplication_api_report.md`, `docs/reports/IRPCollection_api_report.md` (regenerate) | Proof of zero actionable deviations. |
| `docs/CODE_GUIDELINES.md` (modify) | "pywin32 Bindings Are Authoritative" section. |

## Preflight

Create the feature branch (project rules forbid committing to `main`):

```bash
git switch main
git pull --ff-only origin main
git switch -c fix/pywin32-authoritative-bindings
```

---

### Task 1: Committed pywin32 authority module and snapshot

**Files:**
- Create: `scripts/pywin32_authority.py`
- Create: `tests/unit/test_pywin32_authority.py`
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
    assert data["documented_java_only"] == {}


def test_load_authority_round_trip(tmp_path: Path) -> None:
    target = tmp_path / "authority.json"
    data = AuthorityData(
        catalog={"IRPExample": {"addItem": "method"}},
        documented_aliases={"IRPExample": {"get_add": "addItem"}},
        documented_java_only={"IRPExample": ["toList"]},
    )

    write_authority(data, target)

    assert load_authority(target) == data
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/unit/test_pywin32_authority.py -q`
Expected: collection error / `ModuleNotFoundError: No module named 'scripts.pywin32_authority'`.

- [ ] **Step 3: Write the implementation**

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
    documented_java_only: Dict[str, List[str]]


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
        documented_java_only={},
    )


def load_authority(path: Path = AUTHORITY_PATH) -> AuthorityData:
    """Load the committed authority snapshot."""
    data = json.loads(path.read_text(encoding="utf-8"))
    return AuthorityData(
        catalog=data["catalog"],
        documented_aliases=data["documented_aliases"],
        documented_java_only=data["documented_java_only"],
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

- [ ] **Step 5: Generate and commit the authority snapshot**

Run: `python scripts/pywin32_authority.py`

Verify the snapshot contains the two pilots:

```bash
python -c 'import json; d=json.load(open("docs/reports/pywin32_authority.json")); print(len(d["catalog"]), d["catalog"]["IRPApplication"]["version"], d["catalog"]["IRPCollection"]["Count"])'
```

Expected output: `12 method property`.

Commit:

```bash
git add scripts/pywin32_authority.py tests/unit/test_pywin32_authority.py docs/reports/pywin32_authority.json
git commit -m "feat: add committed pywin32 authority snapshot"
```

---

### Task 2: Validator authority mode and deviation classification

**Files:**
- Modify: `scripts/validate_model_api.py:9-12` (imports/aliases), `:295-354` (classification post-processing), `:394-476` (rendering), `:479-522` (parser/main)
- Modify: `tests/unit/test_validate_model_api.py:303-315` (parser test) and add four tests

- [ ] **Step 1: Write the failing tests**

Append to `tests/unit/test_validate_model_api.py`:

```python
from typing import Dict, List, Optional

from scripts.pywin32_authority import AuthorityData


def _authority(
    aliases: Optional[Dict[str, Dict[str, str]]] = None,
    java_only: Optional[Dict[str, List[str]]] = None,
) -> AuthorityData:
    return AuthorityData(
        catalog={},
        documented_aliases=aliases or {},
        documented_java_only=java_only or {},
    )


def test_apply_pywin32_authority_demotes_expected_differences() -> None:
    rows = [
        (
            "get_build_no() -> getBuildNo; get_build_no() -> BuildNo",
            "getBuildNo (method)",
            "BuildNo (property)",
            "ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Use a property-aware getter/setter fallback.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(rows, "IRPApplication", _authority())

    assert deviations == []
    assert informational == rows
    assert backlog == []


def test_apply_pywin32_authority_suppresses_documented_alias() -> None:
    rows = [
        (
            "get_version() -> version",
            "version (method)",
            "version (method)",
            "PYTHON_METHOD_NAME_MISMATCH",
            "Rename the Python method.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(
        rows, "IRPApplication", _authority(aliases={"IRPApplication": {"get_version": "version"}})
    )

    assert (deviations, informational, backlog) == ([], [], [])


def test_apply_pywin32_authority_suppresses_documented_java_only_member() -> None:
    rows = [
        (
            "add_graphical_item() -> addGraphicalItem",
            "addGraphicalItem (method)",
            "—",
            "PYWIN32_MEMBER_MISSING",
            "Use a member exposed by the registered type library.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(
        rows, "IRPCollection", _authority(java_only={"IRPCollection": ["addGraphicalItem"]})
    )

    assert (deviations, informational, backlog) == ([], [], [])


def test_apply_pywin32_authority_keeps_unexposed_member_as_deviation() -> None:
    rows = [
        (
            "get_build_no() -> getBuildNo",
            "getBuildNo (method)",
            "BuildNo (property)",
            "COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH",
            "Use the BuildNo property.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(rows, "IRPApplication", _authority())

    assert deviations == [
        (
            "get_build_no() -> getBuildNo",
            "getBuildNo (method)",
            "BuildNo (property)",
            "COM_MEMBER_NOT_EXPOSED",
            "Use the BuildNo property.",
        )
    ]
    assert informational == []
    assert backlog == []


def test_main_authority_source_reports_backlog_without_typelib(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(validator, "load_authority", lambda: _authority(catalog={"IRPApplication": {"version": "method"}}))
    monkeypatch.setattr(validator, "collect_java_signatures", lambda interface_name, docs_root: {"version": {"IRPApplication.version()"}})
    monkeypatch.setattr(validator, "collect_java_members", lambda interface_name, docs_root: {"version"})
    monkeypatch.setattr(validator, "collect_python_members", lambda interface_name, models_root: {"version": {"version() -> version"}})

    assert validator.main(["IRPApplication", "--source", "authority"]) == 0

    report = (tmp_path / "IRPApplication_api_report.md").read_text(encoding="utf-8")
    assert "## Expected Binding Differences" in report
    assert "## Wrapper Backlog" in report
    assert "No deviations require changes." in report
```

Also extend the existing parser test `test_argument_parser_requires_one_interface_and_optional_report_directory` by adding one line after `assert default_args.path is None`:

```python
    assert default_args.source == "typelib"
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/unit/test_validate_model_api.py -q -k 'authority or argument_parser'`
Expected: failures for missing `validator.apply_pywin32_authority` and `source` argument.

- [ ] **Step 3: Add the authority import and post-processing function**

Add this import after line 9 in `scripts/validate_model_api.py`:

```python
from scripts.pywin32_authority import AuthorityData, load_authority
```

Add these aliases after `_HELPER_NAMES` (line 12):

```python
Rows = List[Tuple[str, str, str, str, str]]
_AUTHORITY_INFO_STATUSES = {"ACCESSOR_ALIAS_MISMATCH", "METHOD_PROPERTY_MISMATCH", "PYTHON_ONLY_MEMBER"}
_AUTHORITY_BACKLOG_STATUSES = {"MISSING_PYTHON_WRAPPER", "PYWIN32_ONLY_MEMBER"}
```

Insert this function immediately before `build_deviation_rows` (line 357):

```python
def apply_pywin32_authority(rows: Rows, interface_name: str, authority: AuthorityData) -> Tuple[Rows, Rows, Rows]:
    """Split raw deviations into actionable, informational, and backlog rows."""
    deviations: Rows = []
    informational: Rows = []
    backlog: Rows = []
    aliases = authority["documented_aliases"].get(interface_name, {})
    java_only = set(authority["documented_java_only"].get(interface_name, []))

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
            if status in {"JAVA_ONLY_MEMBER", "PYWIN32_MEMBER_MISSING"}:
                java_names = {entry[: -len(" (method)")] for entry in row[1].split("; ") if entry.endswith(" (method)")}
                if java_names and java_names.issubset(java_only):
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

- [ ] **Step 4: Add the new report sections**

Insert this helper immediately before `render_markdown_report` (line 410):

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

Change the `render_markdown_report` signature (lines 410-417) to:

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

After the block that appends `Deviations by status` (ends at line 436), insert:

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

After the comparison-table rows and the `if not rows` placeholder (ends at line 451), insert:

```python
    if authoritative:
        _append_report_table(lines, "## Expected Binding Differences", informational_rows or [])
        _append_report_table(lines, "## Wrapper Backlog", backlog_rows or [])
```

- [ ] **Step 5: Add `--source` and rewire `main`**

In `build_arg_parser` (line 479), add this argument before the `--path` argument:

```python
    parser.add_argument(
        "--source",
        choices=("typelib", "authority"),
        default="typelib",
        help="pywin32 member source: registered type library (Windows) or committed authority snapshot (offline)",
    )
```

Replace `main` (lines 490-522) with:

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

- [ ] **Step 6: Run tests and verify**

Run: `python -m pytest tests/unit/test_validate_model_api.py -q`
Expected: all tests pass, including the four new ones and the extended parser test.

- [ ] **Step 7: Commit**

```bash
git add scripts/validate_model_api.py tests/unit/test_validate_model_api.py
git commit -m "feat: validate wrappers against committed pywin32 authority"
```

---

### Task 3: Fix RhapsodyApplication COM calls that pywin32 does not expose

**Files:**
- Modify: `tests/unit/test_application.py:269-274` and `:285-290` (add fallback tests)
- Modify: `src/rhapsody_cli/application.py:263-275` (`get_build_no`) and `:285-297` (`get_omroot`)

- [ ] **Step 1: Write the failing tests**

Add these two tests next to the existing `test_get_build_no_returns_string` and `test_get_omroot_returns_string` in `tests/unit/test_application.py`:

```python
def test_get_build_no_falls_back_to_buildno_property() -> None:
    fake_app = MagicMock(spec=["BuildNo"])
    fake_app.BuildNo = "12345"
    app = RhapsodyApplication(fake_app)

    assert app.get_build_no() == "12345"


def test_get_omroot_falls_back_to_omroot_property() -> None:
    fake_app = MagicMock(spec=["OMROOT"])
    fake_app.OMROOT = "C:/Rhapsody/OMROOT"
    app = RhapsodyApplication(fake_app)

    assert app.get_omroot() == "C:/Rhapsody/OMROOT"
```

Keep the two existing method-style tests unchanged — both binding shapes must work.

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/unit/test_application.py -q -k 'build_no or omroot'`
Expected: 2 failures, because the fake objects have no `getBuildNo` / `getOMROOT`.

- [ ] **Step 3: Implement the property fallbacks**

Replace the body of `get_build_no` (currently line 275) with:

```python
        return str(com_utils._get_method_or_property(self._com, "getBuildNo", "BuildNo"))
```

Add to its docstring, above `Raises:`:

```python
        The authenticated pywin32 type library exposes this value as the
        ``BuildNo`` property, not as ``getBuildNo()``; the Java-style method
        is tried first for other binding styles.
```

Replace the body of `get_omroot` (currently line 297) with:

```python
        return str(com_utils._get_method_or_property(self._com, "getOMROOT", "OMROOT"))
```

Add to its docstring, above `Raises:`:

```python
        The authenticated pywin32 type library exposes this value as the
        ``OMROOT`` property, not as ``getOMROOT()``; the Java-style method
        is tried first for other binding styles.
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python -m pytest tests/unit/test_application.py -q`
Expected: all tests pass (method-style and property-style).

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/application.py tests/unit/test_application.py
git commit -m "fix: read BuildNo and OMROOT through pywin32 property fallbacks"
```

---

### Task 4: Document intentional exceptions and regenerate pilot reports

**Files:**
- Modify: `docs/reports/pywin32_authority.json` (add `documented_aliases` / `documented_java_only`)
- Modify: `src/rhapsody_cli/application.py:255-261` (`get_version` docstring) and `:240-242` (`close_all_projects` needs no change — listed as informational only)
- Modify: `src/rhapsody_cli/models/core.py:2269-2281` (`add_graphical_item` docstring)
- Regenerate: `docs/reports/IRPApplication_api_report.md`, `docs/reports/IRPCollection_api_report.md`

- [ ] **Step 1: Add the documented exceptions to the authority file**

Edit `docs/reports/pywin32_authority.json` so the two empty maps become:

```json
  "documented_aliases": {
    "IRPApplication": {
      "get_version": "version"
    }
  },
  "documented_java_only": {
    "IRPApplication": [
      "getPlugInWindow"
    ],
    "IRPCollection": [
      "addGraphicalItem",
      "toList"
    ]
  }
```

Do not edit the `catalog` map — it is generated from pywin32 and must stay untouched.

- [ ] **Step 2: Document the alias and the Java-only fallback in code**

In `src/rhapsody_cli/application.py`, add this note to the `get_version` docstring (before `Returns:`):

```python
        Note:
            ``get_version`` is a documented alias for the authenticated
            pywin32 member ``version``. It is intentionally not renamed.
```

In `src/rhapsody_cli/models/core.py`, add this note to the `add_graphical_item` docstring (before `Reference:`):

```python
        Note:
            The authenticated pywin32 type library does not expose
            ``addGraphicalItem``. This method is retained as a Java-API
            compatibility fallback; it is listed in
            ``documented_java_only`` in the authority snapshot.
```

- [ ] **Step 3: Regenerate both pilot reports offline**

Run:

```bash
python scripts/validate_model_api.py IRPApplication --source authority --path docs/reports
python scripts/validate_model_api.py IRPCollection --source authority --path docs/reports
```

Expected: both commands exit `0` (no actionable deviations).

Verify:

```bash
python - <<'PY'
from pathlib import Path
for name in ("IRPApplication", "IRPCollection"):
    text = Path(f"docs/reports/{name}_api_report.md").read_text(encoding="utf-8")
    section = text.split("## Comparison details", 1)[1].split("## Expected Binding Differences", 1)[0]
    rows = [line for line in section.splitlines() if line.startswith("| ") and "Python model wrapper" not in line and "---" not in line]
    assert rows == [], (name, rows)
    print(name, "zero actionable deviations")
PY
```

Expected output:

```
IRPApplication zero actionable deviations
IRPCollection zero actionable deviations
```

Also confirm the backlog is visible:

```bash
grep -c '^| ' docs/reports/IRPApplication_api_report.md
```

Expected: a non-zero count (informational + backlog rows are retained in their own sections).

- [ ] **Step 4: Add a guard test that the pilot reports stay clean**

Add to `tests/unit/test_validate_model_api.py`:

```python
def test_pilot_reports_have_no_actionable_deviations() -> None:
    from pathlib import Path

    reports_root = Path(__file__).resolve().parents[2] / "docs" / "reports"
    for interface_name in ("IRPApplication", "IRPCollection"):
        text = (reports_root / f"{interface_name}_api_report.md").read_text(encoding="utf-8")
        section = text.split("## Comparison details", 1)[1].split("## Expected Binding Differences", 1)[0]
        rows = [
            line
            for line in section.splitlines()
            if line.startswith("| ") and "Python model wrapper" not in line and "---" not in line
        ]
        assert rows == [], (interface_name, rows)
```

Run: `python -m pytest tests/unit/test_validate_model_api.py -q -k pilot_reports`
Expected: 1 passed.

- [ ] **Step 5: Commit**

```bash
git add docs/reports/pywin32_authority.json docs/reports/IRPApplication_api_report.md docs/reports/IRPCollection_api_report.md src/rhapsody_cli/application.py src/rhapsody_cli/models/core.py tests/unit/test_validate_model_api.py
git commit -m "docs: regenerate pilot reports with zero binding deviations"
```

---

### Task 5: Record the rule in the code guidelines

**Files:**
- Modify: `docs/CODE_GUIDELINES.md` (insert before `## Questions?` at line 1010)

- [ ] **Step 1: Add the guideline section**

Insert this section immediately before `## Questions?`:

```markdown
## pywin32 Bindings Are Authoritative

The generated pywin32 interface from the registered `Rhapsody2 1.0` type library is the source of truth for COM member names and shapes. Java Javadoc describes a different (Java-style) API and may show `getX`/`setX` methods where pywin32 exposes a bare `X` property; those differences are expected and are reported as informational, not as defects.

- Confirm each COM member's exact name and kind in `docs/reports/pywin32_authority.json`.
- Call method-shaped members with `com_utils.call_com(lambda: self._com.methodName(...))`.
- Read/write property-shaped members with `_get_method_or_property` / `_set_method_or_property`, Java-style name first and pywin32 name second. This keeps both binding styles working.
- Keep Java-only wrappers as documented compatibility fallbacks and add the member to `documented_java_only` in the authority file.
- Document intentional Python-name aliases in `documented_aliases` rather than renaming public methods.
- After changing a wrapper, regenerate its report with `python scripts/validate_model_api.py <IRPInterface> --source authority --path docs/reports` and require zero rows under `## Comparison details`.
- New supported-but-unwrapped members belong in `## Wrapper Backlog`; add them in a follow-up plan with signatures verified against the generated makepy source on Windows.
```

- [ ] **Step 2: Verify the Markdown renders correctly**

Run: `grep -n 'pywin32 Bindings Are Authoritative' docs/CODE_GUIDELINES.md`
Expected: one matching line.

- [ ] **Step 3: Commit**

```bash
git add docs/CODE_GUIDELINES.md
git commit -m "docs: document pywin32-authoritative binding rule"
```

---

### Task 6: Full quality gate

**Files:** none (verification only)

- [ ] **Step 1: Install dev dependencies if needed**

Run: `pip install -e ".[dev,cli]"`
Expected: pytest, pytest-cov, ruff, black, mypy, tabulate, rich available.

- [ ] **Step 2: Run the quality gate**

On Windows (CI), run directly:

```bash
ruff check src/ tests/ scripts/ && black --check src/ tests/ scripts/ && mypy src/ tests/ scripts/ && pytest tests/unit/
```

On macOS/Linux, `pywintypes` is unavailable; inject a temporary stub without modifying the repo:

```bash
STUB=$(mktemp -d); printf 'class com_error(Exception):\n    def __init__(self, *args):\n        self.args = args\n        super().__init__(*args)\n' > "$STUB/pywintypes.py"; PYTHONPATH="${STUB}:src" python -m pytest tests/unit/ -q; rm -rf "$STUB"
```

Expected: all unit tests pass, lint/format/type checks clean.

- [ ] **Step 3: Confirm the branch is clean and list the commits**

```bash
git status --short
git log --oneline origin/main..HEAD
```

Expected: clean working tree and five commits (authority module, validator mode, application fixes, regenerated reports, guidelines).

---

## Self-review

**Spec coverage:** The pywin32-authoritative requirement is implemented in Task 1 (catalog + exceptions), Task 2 (classification/render), Task 3 (real binding bugs), Task 4 (exceptions + regenerated reports), Task 5 (rule). The two pilot interfaces are fully covered: all their actionable rows are either fixed (`COM_MEMBER_NOT_EXPOSED`, `PYTHON_METHOD_NAME_MISMATCH`, `PYWIN32_MEMBER_MISSING`, `JAVA_ONLY_MEMBER`) or explicitly moved to informational/backlog. The 10 other interfaces and the 235 new-wrapper items are explicitly deferred with a visible backlog — a conscious scope decision confirmed with the user.

**Placeholder scan:** No "TBD"/"TODO"/"similar to Task N" steps. Every code-changing step includes the complete code. Generated JSON content is produced by a committed script with an exact verification command rather than pasted wholesale.

**Type consistency:** `AuthorityData` is defined once in Task 1 and used unchanged in Tasks 2 and 4. `apply_pywin32_authority(rows, interface_name, authority)` has one signature used by all four tests and by `main`. `Rows = List[Tuple[str, str, str, str, str]]` matches `build_deviation_rows`' return type. No `Any` annotations. `scripts/pywin32_authority.py` uses no Python 3.9-only APIs (`removesuffix` was replaced with slicing) to honor the py3.8 target.
