# IRPClass Binding Fixes and Python Property Migration — Combined Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring `docs/reports/IRPClass_api_report.md` to zero actionable deviations under pywin32-authoritative rules, and in the same deliverable replace `RPClass`'s own `get_is_*` / `set_is_*` methods with snake_case Python `@property` accessors.

**Architecture:** A committed pywin32 authority snapshot (name → kind per interface, plus documented aliases and unavailable members) plus an offline `--source authority` validator mode classify expected Java-vs-pywin32 differences as informational. Wrapper COM calls are corrected to use exposed members, the one IRPClass-owned wrapper calling an unavailable COM member is removed, and RPClass's 10 own flag methods become 6 properties. Callers in the CLI layer, unit tests, and integration tests migrate together so the tree stays green.

**Tech Stack:** Python 3.8+ stdlib (`ast`, `json`, `argparse`, `pathlib`, `typing.TypedDict`, `@property`), pytest, ruff/black/mypy strict, Markdown reports.

---

## Deviation inventory and proposal by type

`docs/reports/IRPClass_api_report.md` has **83 deviation rows**:

| Rows | Deviation type | Proposed solution |
|---:|---|---|
| 56 | `ACCESSOR_ALIAS_MISMATCH` + `METHOD_PROPERTY_MISMATCH` | Informational — Java getters vs pywin32 properties, already handled by the binding helpers. |
| 10 | `PYTHON_ONLY_MEMBER` | Keep documented stubs/helpers; informational. |
| 6 | `MISSING_PYTHON_WRAPPER` | OSLC members documented unsupported; design-manager members go to backlog #121. |
| 3 | `COM_MEMBER_NOT_EXPOSED` | Fix `BinaryID`, `CMHeader`, and call `isOfMetaClass` directly (Task 4). |
| 2 | `PYWIN32_ONLY_MEMBER` | Backlog (signatures need makepy verification). |
| 2 | `PYTHON_METHOD_NAME_MISMATCH` | `get_description_html` documented as alias; `get_is_abstract` disappears in the property migration. |
| 2 | `PYWIN32_MEMBER_MISSING` | Remove `RPClass.update_contained_diagrams_on_server`; inherited `get_rmm_url` documented unavailable. |
| 1 | `JAVA_ONLY_MEMBER` | Covered by the existing documented `NotImplementedError` stub. |
| 1 | `MISSING_PYTHON_WRAPPER` (stereotype) | Backlog. |
| 1 | `ACCESSOR_ALIAS_MISMATCH` (`getUnitPath`) | Document getter as unavailable; keep setter. |

**Ordering:** removal (Task 3) → COM fixes (Task 4) → property migration (Tasks 5–7) → report regeneration (Task 8). Regenerating last ensures the final report reflects property names.

## Scope and non-goals

**In scope:** IRPClass report; RPClass's 10 own flag methods → 6 properties; CLI `class_action.py`; unit and integration tests for RPClass; validator authority mode and authority snapshot.

**Out of scope:** the other 11 interfaces; `RPModelElement`/`RPUnit` inherited methods; other classes' getters/setters; adding the 8 backlog wrappers; renaming public methods to COM names.

**Python naming rule:** snake_case methods and UPPERCASE constants per `docs/CODE_GUIDELINES.md`. COM names (`BinaryID`, `isAbstract`, `getBinaryID`) are **string arguments only**, never Python identifiers.

## File structure

| File | Responsibility |
|---|---|
| `scripts/pywin32_authority.py` (new) | Load/write authority JSON; export catalog from reports. |
| `docs/reports/pywin32_authority.json` (new) | pywin32 name → kind, documented aliases and unavailable Java names. |
| `scripts/validate_model_api.py` (modify) | `--source authority`, deviation/informational/backlog split, report sections. |
| `tests/unit/test_pywin32_authority.py` (new) | Catalog export and authority round-trip. |
| `tests/unit/test_validate_model_api.py` (modify) | Authority post-processing and report guard. |
| `src/rhapsody_cli/models/core.py` (modify) | `BinaryID`, `CMHeader`, `isOfMetaClass` call sites. |
| `tests/unit/models/test_core.py` (modify) | TDD tests for those call sites. |
| `src/rhapsody_cli/models/elements/classifiers/model_class.py` (modify) | Remove one unavailable method; 10 flag methods → 6 properties; checklist. |
| `tests/unit/models/elements/classifiers/test_model_class.py` (modify) | Removal guard; property tests. |
| `src/rhapsody_cli/actions/class_action.py` (modify) | Attribute access instead of flag methods. |
| `tests/integration/models/elements/classifiers/test_model_class.py` (modify) | Remove obsolete test; property attribute access. |
| `tests/integration/models/test_core.py` (modify) | xfail updates for binding fixes. |
| `docs/reports/IRPClass_api_report.md` (regenerate) | Final proof of zero actionable deviations. |
| `docs/CODE_GUIDELINES.md` (modify) | pywin32-authoritative rule and scoped refactor rule. |

## Preflight

Work on branch `docs/pywin32-authoritative-bindings` (PR #122). The separate property branch/plan is retired; tracking issue #123 points back here.

```bash
git switch docs/pywin32-authoritative-bindings
git fetch origin
```

---

### Task 1: Committed pywin32 authority module and snapshot

**Files:** `scripts/pywin32_authority.py`, `tests/unit/test_pywin32_authority.py`, `docs/reports/pywin32_authority.json`

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

- [ ] **Step 2: Run tests to verify failure**

`pytest tests/unit/test_pywin32_authority.py -q` → `ModuleNotFoundError`.

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

- [ ] **Step 4: Run tests to verify they pass**

`pytest tests/unit/test_pywin32_authority.py -q` → 3 passed.

- [ ] **Step 5: Generate, verify and commit**

```bash
python scripts/pywin32_authority.py
python -c 'import json; d=json.load(open("docs/reports/pywin32_authority.json")); print(d["catalog"]["IRPClass"]["isAbstract"], d["catalog"]["IRPClass"]["BinaryID"])'
git add scripts/pywin32_authority.py tests/unit/test_pywin32_authority.py docs/reports/pywin32_authority.json
git commit -m "feat: add committed pywin32 authority snapshot"
```

Expected print: `property property`.

---

### Task 2: Validator authority mode and classification

**Files:** `scripts/validate_model_api.py`, `tests/unit/test_validate_model_api.py`

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
            "get_description_html() -> descriptionHTML; get_description_html() -> getDescriptionHTML",
            "getDescriptionHTML (method)",
            "descriptionHTML (property)",
            "PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH",
            "Rename the Python method.",
        )
    ]

    deviations, informational, backlog = validator.apply_pywin32_authority(
        rows, "IRPClass", _authority(aliases={"IRPClass": {"get_description_html": "description_html"}})
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

Extend the existing parser test with `assert default_args.source == "typelib"`.

- [ ] **Step 2: Run tests to verify failure**

`pytest tests/unit/test_validate_model_api.py -q -k 'authority or argument_parser'` → failures.

- [ ] **Step 3: Add the authority import and post-processing**

Add after the existing scripts import:

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

After the `Deviations by status` block insert:

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

After the comparison table insert:

```python
    if authoritative:
        _append_report_table(lines, "## Expected Binding Differences", informational_rows or [])
        _append_report_table(lines, "## Wrapper Backlog", backlog_rows or [])
```

- [ ] **Step 5: Add `--source` and rewire `main`**

Add to `build_arg_parser` before `--path`:

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

`pytest tests/unit/test_validate_model_api.py -q` → all pass.

```bash
git add scripts/validate_model_api.py tests/unit/test_validate_model_api.py
git commit -m "feat: validate wrappers against committed pywin32 authority"
```

---

### Task 3: Remove the IRPClass wrapper calling an unavailable member

**Files:** `model_class.py`, `tests/unit/models/elements/classifiers/test_model_class.py`

- [ ] **Step 1: Write the failing guard**

Add to `test_model_class.py`:

```python
def test_class_does_not_expose_unavailable_server_diagram_update() -> None:
    assert not hasattr(RPClass, "update_contained_diagrams_on_server")
```

- [ ] **Step 2: Run it to verify failure**

`pytest tests/unit/models/elements/classifiers/test_model_class.py -q -k unavailable_server_diagram` → 1 failure.

- [ ] **Step 3: Remove the method, old test and checklist row**

Delete from `model_class.py`:

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

Delete from `test_model_class.py`:

```python
def test_class_update_contained_diagrams_on_server_delegates_to_com() -> None:
    fake = make_fake_element("Class", updateContainedDiagramsOnServer=3)
    klass = RPClass(fake)

    assert klass.update_contained_diagrams_on_server(1) == 3

    fake.updateContainedDiagramsOnServer.assert_called_once_with(1)
```

Replace the checklist row with:

```python
    # update_contained_diagrams_on_server: unavailable in Rhapsody2.Application.1 type library; wrapper removed.
```

- [ ] **Step 4: Verify and commit**

`pytest tests/unit/models/elements/classifiers/test_model_class.py -q` → pass.

```bash
git add src/rhapsody_cli/models/elements/classifiers/model_class.py tests/unit/models/elements/classifiers/test_model_class.py
git commit -m "fix: remove RPClass update_contained_diagrams_on_server (not in pywin32)"
```

---

### Task 4: Fix the three COM calls exposed under different names

**Files:** `src/rhapsody_cli/models/core.py`, `tests/unit/models/test_core.py`

- [ ] **Step 1: Write failing tests**

Replace `test_model_element_get_binary_id_returns_bytes` with:

```python
def test_model_element_get_binary_id_falls_back_to_pywin32_binaryid_property() -> None:
    fake = MagicMock(spec=["BinaryID"])
    fake.BinaryID = b"\x01\x02\x03"
    element = RPModelElement(fake)

    assert element.get_binary_id() == b"\x01\x02\x03"
```

Add:

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

Replace `test_model_element_get_is_of_meta_class_returns_int` with:

```python
def test_model_element_get_is_of_meta_class_calls_pywin32_member() -> None:
    fake = MagicMock(spec=["isOfMetaClass"])
    fake.isOfMetaClass.return_value = 1
    element = RPModelElement(fake)

    assert element.get_is_of_meta_class("Class") == 1
    fake.isOfMetaClass.assert_called_once_with("Class")
```

- [ ] **Step 2: Run tests to verify failure**

`pytest tests/unit/models/test_core.py -q -k 'binary_id or cm_header or is_of_meta_class'` → 4 failures.

- [ ] **Step 3: Implement**

In `get_binary_id` replace the return with:

```python
        return bytes(AbstractRPModelElement._get_method_or_property(self._com, "getBinaryID", "BinaryID"))
```

In `get_cm_header` replace the return with:

```python
        return str(AbstractRPModelElement._get_method_or_property(self._com, "getCMHeader", "CMHeader"))
```

In `set_cm_header` replace the call with:

```python
        AbstractRPModelElement._set_method_or_property(self._com, "setCMHeader", "CMHeader", cm_header)
```

In `get_is_of_meta_class` replace the return with:

```python
        return int(AbstractRPModelElement.call_com(lambda: self._com.isOfMetaClass(meta_class)))
```

A getter/property helper is not usable for `isOfMetaClass`: pywin32 exposes it as a method, so the helper would return the bound method without invoking it.

- [ ] **Step 4: Verify and commit**

`pytest tests/unit/models/test_core.py -q` → pass.

```bash
git add src/rhapsody_cli/models/core.py tests/unit/models/test_core.py
git commit -m "fix: call pywin32-exposed BinaryID, CMHeader and isOfMetaClass members"
```

---

### Task 5: Failing unit tests for RPClass properties

**Files:** `tests/unit/models/elements/classifiers/test_model_class.py`

- [ ] **Step 1: Replace the flag-method tests with property tests**

Replace `test_class_get_is_abstract_delegates_to_com` with:

```python
def test_class_is_abstract_property_delegates_to_com() -> None:
    fake = make_fake_element("Class", getIsAbstract=1)
    klass = RPClass(fake)

    assert klass.is_abstract is True
```

Replace the five `test_class_get_is_*_delegates_to_com` tests (active, behavior_overriden, composite, final, reactive) with:

```python
def test_class_is_active_property_delegates_to_com() -> None:
    fake = make_fake_element("Class", getIsActive=1)
    klass = RPClass(fake)

    assert klass.is_active == 1


def test_class_is_behavior_overriden_property_delegates_to_com() -> None:
    fake = make_fake_element("Class", getIsBehaviorOverriden=0)
    klass = RPClass(fake)

    assert klass.is_behavior_overriden == 0


def test_class_is_composite_property_delegates_to_com() -> None:
    fake = make_fake_element("Class", getIsComposite=1)
    klass = RPClass(fake)

    assert klass.is_composite == 1


def test_class_is_final_property_delegates_to_com() -> None:
    fake = make_fake_element("Class", getIsFinal=0)
    klass = RPClass(fake)

    assert klass.is_final == 0


def test_class_is_reactive_property_delegates_to_com() -> None:
    fake = make_fake_element("Class", getIsReactive=1)
    klass = RPClass(fake)

    assert klass.is_reactive == 1
```

Replace the four setter tests with:

```python
def test_class_is_abstract_setter_raises_not_implemented() -> None:
    fake = make_fake_element("Class")
    klass = RPClass(fake)

    with pytest.raises(NotImplementedError):
        klass.is_abstract = True

    fake.setIsAbstract.assert_not_called()


def test_class_is_active_setter_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    klass = RPClass(fake)

    klass.is_active = 0

    fake.setIsActive.assert_called_once_with(0)


def test_class_is_behavior_overriden_setter_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    klass = RPClass(fake)

    klass.is_behavior_overriden = 1

    fake.setIsBehaviorOverriden.assert_called_once_with(1)


def test_class_is_final_setter_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    klass = RPClass(fake)

    klass.is_final = 1

    fake.setIsFinal.assert_called_once_with(1)
```

- [ ] **Step 2: Run tests to verify failure**

`pytest tests/unit/models/elements/classifiers/test_model_class.py -q -k 'is_abstract or is_active or is_behavior_overriden or is_composite or is_final or is_reactive'` → failures.

- [ ] **Step 3: Commit the failing tests**

```bash
git add tests/unit/models/elements/classifiers/test_model_class.py
git commit -m "test(unit): expect RPClass boolean flags as properties"
```

---

### Task 6: Implement the six RPClass properties

**Files:** `src/rhapsody_cli/models/elements/classifiers/model_class.py`

- [ ] **Step 1: Replace `get_is_abstract` and `set_is_abstract`**

```python
    @property
    def is_abstract(self) -> bool:
        """Checks whether this class is abstract."""
        return bool(AbstractRPModelElement._get_method_or_property(self._com, "getIsAbstract", "isAbstract"))

    @is_abstract.setter
    def is_abstract(self, is_abstract: bool) -> None:
        """Unimplemented: the COM write is accepted but never persists."""
        raise NotImplementedError("RPClass.is_abstract setter is unimplemented: Rhapsody2.Application.1 accepts the write but never persists it.")
```

`bool` is used for both getter and setter because mypy strict requires a compatible setter type; the Java-style `int` callers are migrated in Task 7.

- [ ] **Step 2: Replace the other getter/setter pairs**

```python
    @property
    def is_active(self) -> int:
        """``1`` if the class runs on its own thread, ``0`` if sequential."""
        return int(AbstractRPModelElement._get_method_or_property(self._com, "getIsActive", "isActive"))

    @is_active.setter
    def is_active(self, is_active: int) -> None:
        """Set to ``1`` for active, ``0`` for sequential."""
        AbstractRPModelElement._set_method_or_property(self._com, "setIsActive", "isActive", is_active)

    @property
    def is_behavior_overriden(self) -> int:
        """``1`` if the class does not inherit its base statechart behavior, else ``0``."""
        return int(AbstractRPModelElement._get_method_or_property(self._com, "getIsBehaviorOverriden", "isBehaviorOverriden"))

    @is_behavior_overriden.setter
    def is_behavior_overriden(self, is_behavior_overriden: int) -> None:
        """Set to ``1`` to not inherit the base statechart behavior, ``0`` to inherit."""
        AbstractRPModelElement._set_method_or_property(self._com, "setIsBehaviorOverriden", "isBehaviorOverriden", is_behavior_overriden)

    @property
    def is_composite(self) -> int:
        """``1`` if the class is a composite class, ``0`` otherwise."""
        return int(AbstractRPModelElement._get_method_or_property(self._com, "getIsComposite", "isComposite"))

    @property
    def is_final(self) -> int:
        """``1`` if the class is final, ``0`` otherwise."""
        return int(AbstractRPModelElement._get_method_or_property(self._com, "getIsFinal", "isFinal"))

    @is_final.setter
    def is_final(self, new_val: int) -> None:
        """Set to ``1`` to make the class final, ``0`` otherwise."""
        AbstractRPModelElement._set_method_or_property(self._com, "setIsFinal", "isFinal", new_val)

    @property
    def is_reactive(self) -> int:
        """``1`` if the class has a statechart or activity diagram, ``0`` otherwise."""
        return int(AbstractRPModelElement._get_method_or_property(self._com, "getIsReactive", "isReactive"))
```

- [ ] **Step 3: Update the parity checklist**

Replace the ten `get_is_*` / `set_is_*` checklist rows with six `is_*` rows marked `[x] impl (property)`.

- [ ] **Step 4: Verify and commit**

`pytest tests/unit/models/elements/classifiers/test_model_class.py -q` → pass.

```bash
git add src/rhapsody_cli/models/elements/classifiers/model_class.py
git commit -m "refactor: expose RPClass boolean flags as Python properties"
```

---

### Task 7: Migrate CLI and integration call sites

**Files:** `src/rhapsody_cli/actions/class_action.py`, `tests/integration/models/elements/classifiers/test_model_class.py`, `tests/integration/models/test_core.py`

- [ ] **Step 1: Migrate `class_action.py`**

Apply these replacements (keep existing `# type: ignore[attr-defined]` comments):

```python
cls.set_is_abstract(1 if attrs["isAbstract"] else 0)  →  cls.is_abstract = bool(attrs["isAbstract"])
cls.set_is_final(1 if attrs["isFinal"] else 0)        →  cls.is_final = 1 if attrs["isFinal"] else 0
cls.set_is_active(1 if attrs["isActive"] else 0)      →  cls.is_active = 1 if attrs["isActive"] else 0
cls.set_is_abstract(1 if value else 0)                →  cls.is_abstract = bool(value)
cls.set_is_final(1 if value else 0)                   →  cls.is_final = 1 if value else 0
cls.set_is_active(1 if value else 0)                  →  cls.is_active = 1 if value else 0
int(cls.get_is_abstract())                            →  int(cls.is_abstract)
int(cls.get_is_active())                              →  int(cls.is_active)
int(cls.get_is_final())                               →  int(cls.is_final)
int(cls.get_is_composite())                           →  int(cls.is_composite)
int(cls.get_is_reactive())                            →  int(cls.is_reactive)
```

Do not touch `operation_action.py` — `RPOperation` keeps its methods.

- [ ] **Step 2: Migrate RPClass integration tests**

In `tests/integration/models/elements/classifiers/test_model_class.py`, replace `test_class.get_is_abstract()` → `test_class.is_abstract`, `get_is_active()` → `is_active`, `get_is_behavior_overriden()` → `is_behavior_overriden`, `get_is_composite()` → `is_composite`, `get_is_final()` → `is_final`, `get_is_reactive()` → `is_reactive`, and setter calls with assignments. For abstract, keep the failure expectation:

```python
            with pytest.raises(NotImplementedError):
                test_class.is_abstract = True
```

- [ ] **Step 3: Update binding-related integration tests**

Delete the xfailed `test_update_contained_diagrams_on_server` test from the RPClass integration file. In `tests/integration/models/test_core.py`: remove the xfail decorator from `test_get_is_of_meta_class_class`, and retitle the `get_rmm_url` xfail reason to reference `documented_unavailable`.

- [ ] **Step 4: Verify and commit**

```bash
pytest tests/unit/actions -q
pytest tests/integration/models/elements/classifiers/test_model_class.py tests/integration/models/test_core.py --collect-only -q
git add src/rhapsody_cli/actions/class_action.py tests/integration/models/elements/classifiers/test_model_class.py tests/integration/models/test_core.py
git commit -m "refactor: migrate CLI and integration tests to RPClass properties"
```

---

### Task 8: Document exceptions, regenerate the final report, and guard it

**Files:** `docs/reports/pywin32_authority.json`, `docs/reports/IRPClass_api_report.md`, `tests/unit/test_validate_model_api.py`

- [ ] **Step 1: Fill the authority exceptions**

Edit the two exception maps (currently `{}` after Task 1):

```json
  "documented_aliases": {
    "IRPClass": {
      "get_description_html": "description_html"
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

No `get_is_abstract` alias: after Task 6 the Python name is already the canonical `is_abstract`.

- [ ] **Step 2: Regenerate the report**

```bash
python scripts/validate_model_api.py IRPClass --source authority --path docs/reports
```

Expected exit `0`. Verify zero actionable rows:

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

- [ ] **Step 3: Guard the property/method shape**

```bash
python - <<'PY'
import ast
import json
from pathlib import Path

catalog = json.loads(Path("docs/reports/pywin32_authority.json").read_text(encoding="utf-8"))["catalog"]["IRPClass"]
properties = {name for name, kind in catalog.items() if "property" in kind}
sources = [Path("src/rhapsody_cli/models/core.py"), Path("src/rhapsody_cli/models/elements/classifiers/model_class.py")]
violations: list = []
for source in sources:
    tree = ast.parse(source.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        base = node.func.value
        if isinstance(base, ast.Attribute) and base.attr == "_com" and isinstance(base.value, ast.Name) and base.value.id == "self" and node.func.attr in properties:
            violations.append(f"{source}:{node.lineno}: {node.func.attr}()")
assert not violations, violations
print("IRPClass: no property-shaped pywin32 member called as a method")
PY
```

- [ ] **Step 4: Add the report guard test**

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

`pytest tests/unit/test_validate_model_api.py -q -k irpclass_report` → 1 passed.

- [ ] **Step 5: Commit**

```bash
git add docs/reports/pywin32_authority.json docs/reports/IRPClass_api_report.md tests/unit/test_validate_model_api.py
git commit -m "docs: regenerate IRPClass report after binding and property fixes"
```

---

### Task 9: Guidelines, quality gate and push

**Files:** `docs/CODE_GUIDELINES.md`

- [ ] **Step 1: Add the rule**

Insert before `## Questions?`:

```markdown
## pywin32 Bindings Are Authoritative

The generated pywin32 interface from the registered `Rhapsody2 1.0` type library is the source of truth for COM member names and shapes. Java getters vs pywin32 properties are informational, not defects.

- Confirm COM member names and kinds in `docs/reports/pywin32_authority.json`.
- Call method-shaped members with `call_com(lambda: self._com.methodName(...))`.
- Read/write property-shaped members with `_get_method_or_property` / `_set_method_or_property`, Java name first and pywin32 name second. COM names are string arguments only.
- Python-facing names follow this document: snake_case methods and UPPERCASE constants. Where a class is migrated to `@property`, its name is the snake_case canonical member name.
- Remove wrappers calling members absent from pywin32, or keep a documented `NotImplementedError` stub listed in `documented_unavailable`.
- Property/method refactors are scoped to one class at a time; do not reshape the shared wrapper hierarchy for one interface's deviations.
- Regenerate the affected report with `python scripts/validate_model_api.py <IRPInterface> --source authority --path docs/reports` and require zero rows under `## Comparison details`.
```

- [ ] **Step 2: Install deps and run the gate**

```bash
pip install -e ".[dev,cli]"
ruff check src/ tests/ scripts/ && black --check src/ tests/ scripts/ && mypy src/ tests/ scripts/ && pytest tests/unit/
```

On macOS/Linux use a temporary `pywintypes` stub:

```bash
STUB=$(mktemp -d); printf 'class com_error(Exception):\n    def __init__(self, *args):\n        self.args = args\n        super().__init__(*args)\n' > "$STUB/pywintypes.py"; PYTHONPATH="${STUB}:src" python -m pytest tests/unit/ -q; rm -rf "$STUB"
```

- [ ] **Step 3: Commit and push**

```bash
git add docs/CODE_GUIDELINES.md
git commit -m "docs: document pywin32-authoritative bindings and scoped property migration"
git push
```

---

## Self-review

**Coverage:** all 83 IRPClass deviation rows have a treatment; removal precedes fixes; property migration precedes final report regeneration so the report reflects the final API; unit, CLI, integration, and report tests are all included.

**Placeholder scan:** every code-changing step includes complete replacement code; no TBD steps.

**Type consistency:** `AuthorityData` is defined once and used identically in Tasks 1, 2, 8. `is_abstract` is `bool` on getter and setter (mypy strict), other flags are `int` on both sides; CLI output keeps `int(...)`. No `Any` annotations and no Python 3.9-only APIs.

**Breaking change:** callers of the ten removed RPClass methods must use attributes. This is intentional, tracked in issue #123, and scoped to one class; the other 11 interfaces and the shared base are untouched.
