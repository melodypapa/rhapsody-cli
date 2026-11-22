# Integration Test Review Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close every gap from the 2026-11-23 integration-suite review so the suite actually proves the pywin32 COM bindings work: enforce marker/pin hygiene in `verify_sync`, convert exception pins to authentic live assertions (Windows-gated), replace the `IRPAssociationClass` broken-binding test, and remove dead fixtures/literals.

**Architecture:** Two hard phases. **Phase 1 runs offline on this Mac** (skill-tooling enforcement, fixture/literal cleanup, one fully-worked pin conversion with wrapper+unit+integration code complete; live verification deferred to Phase 2). **Phase 2 requires Windows + live Rhapsody** — it is a repeatable per-method conversion recipe plus the full worklist, gated by `verify_sync` per interface. Legacy `elements/` modules are explicitly out of scope (they ride their future sync runs).

**Tech Stack:** pytest (unit fakes offline; live COM on Windows), AST-based skill tooling (`sync_tools.py`/`verify_sync.py`), pywin32 COM via `rhapsody_cli` wrappers.

**Base branch:** `fix/signature-validation-review` (stacked on PR #134). Phase 1 work goes on a new branch `fix/integration-review-offline` cut from it. Phase 2 executes on a Windows machine after PRs #132/#134 and the `feature/skill-review-fixes` → `main` merge, on a branch cut from the reconciled main.

---

## Phase 1 — Offline (this Mac)

### Task 1: Add a skip/xfail marker scan to `verify_sync` (TDD)

The review proved `verify_sync` has no marker scan: `test_irp_association_class.py` carried a stale "marked xfail" docstring through every gate. Model-class unit and integration tests must never use `pytest.mark.skip` / `xfail` / `pytest.skip(...)` (SKILL §4).

**Files:**
- Modify: `.agents/skills/rhapsody-sync/scripts/sync_tools.py` (new function + wiring into `verify_sync_artifacts`)
- Test: `.agents/skills/rhapsody-sync/tests/test_sync_tools.py`

- [ ] **Step 1: Write the failing tests**

Append to `.agents/skills/rhapsody-sync/tests/test_sync_tools.py`:

```python
def test_verify_integration_test_markers_flags_skip_and_xfail() -> None:
    """SKILL §4: model-class tests must run and pass — skip/xfail markers,
    including class-level markers and pytest.skip calls, must be flagged."""
    tools = _load_sync_tools()
    bad = '''
import pytest

@pytest.mark.xfail(reason="flaky COM")
class TestThing:
    @pytest.mark.skipif(True, reason="no fixture")
    def test_a(self):
        pass

    def test_b(self):
        pytest.skip("not available")
'''
    issues = tools.verify_integration_test_markers(bad)
    assert len(issues) == 3
    assert any("xfail" in i for i in issues)
    assert any("skipif" in i for i in issues)
    assert any("pytest.skip" in i for i in issues)


def test_verify_integration_test_markers_clean_file_passes() -> None:
    tools = _load_sync_tools()
    ok = '''
import pytest

class TestThing:
    def test_a(self):
        with pytest.raises(NotImplementedError):
            wrapper.java_only_method()
'''
    assert tools.verify_integration_test_markers(ok) == []


def test_verify_sync_artifacts_flags_xfail_marker_in_mirrored_test(tmp_path: Path) -> None:
    """verify_sync_artifacts scans the mirrored unit and integration files for
    skip/xfail markers and fails the interface when any is present."""
    tools = _load_sync_tools()
    root = _write_fixture_project(tmp_path / "repo", _VALID_RST_API_REFERENCE)
    report = _write_report(root)
    integration_test = root / "tests" / "integration" / "models" / Path(*_REPORT_PACKAGE_PARTS) / "test_model_thing.py"
    integration_test.write_text("import pytest\n\n@pytest.mark.xfail(reason='stale')\ndef test_thing():\n    pass\n", encoding="utf-8")

    issues = tools.verify_sync_artifacts(root, "IRPThing", report)

    assert any("xfail" in issue and "integration" in issue.lower() for issue in issues)
```

- [ ] **Step 2: Run to verify the new tests fail**

Run: `python3 -m pytest -o addopts= .agents/skills/rhapsody-sync/tests -q -k "markers"`
Expected: 3 failed (AttributeError: no attribute `verify_integration_test_markers`; the artifacts test finds no issue), the rest untouched.

- [ ] **Step 3: Implement the marker scanner and wire it in**

In `.agents/skills/rhapsody-sync/scripts/sync_tools.py`, add after `verify_integration_exception_catches`:

```python
def verify_integration_test_markers(test_source: str) -> List[str]:
    """Model-class tests must run and pass: no skip/xfail markers (SKILL §4).

    Flags pytest.mark.skip / skipif / xfail decorators on test functions and
    classes plus pytest.skip() / pytest.xfail() calls in the body.
    """
    issues: List[str] = []
    tree = ast.parse(test_source)
    marker_names = {"skip", "skipif", "xfail"}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            for deco in node.decorator_list:
                target = deco.func if isinstance(deco, ast.Call) else deco
                name = getattr(target, "attr", None) or getattr(target, "id", None)
                if name in marker_names:
                    issues.append(f"{name} marker on {node.name} (line {node.lineno}) — SKILL §4 forbids skipped model-class tests")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in ("skip", "xfail"):
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "pytest":
                issues.append(f"pytest.{node.func.attr} call at line {node.lineno} — SKILL §4 forbids skipped model-class tests")
    return issues
```

In `verify_sync_artifacts`, inside the existing `for label, test_base in (("Unit", "unit"), ("Integration", "integration")):` loop, extend the `elif` chain so both mirrored files are marker-scanned (add after the existing `wrapper_class not in test_path` check, keeping the Integration-only exception scan separate):

```python
        elif wrapper_class not in test_path.read_text(encoding="utf-8"):
            issues.append(f"{label} test file does not exercise {wrapper_class}: {test_path}")
        else:
            issues.extend(f"{label} test: {issue}" for issue in verify_integration_test_markers(test_path.read_text(encoding="utf-8")))
            if label == "Integration":
                issues.extend(verify_integration_exception_catches(test_path.read_text(encoding="utf-8")))
```

(Replace the previous `elif label == "Integration":` branch with the `else:` block above so both layers get the marker scan.)

- [ ] **Step 4: Run to verify the tests pass**

Run: `python3 -m pytest -o addopts= .agents/skills/rhapsody-sync/tests -q`
Expected: all pass (baseline 31 + 3 new = 34).

- [ ] **Step 5: Commit**

```bash
git add .agents/skills/rhapsody-sync/scripts/sync_tools.py .agents/skills/rhapsody-sync/tests/test_sync_tools.py
git commit -m "feat(sync): verify_sync scans mirrored tests for skip/xfail markers"
```

### Task 2: Add an all-integration hygiene sweep (TDD)

`verify_sync` only inspects one interface's mirrored files, so pins in legacy files (e.g. `test_model_actor.py`) escape. Add a report-only sweep over every model integration test file, exposed as `verify_sync.py --scan-all-integration`.

**Files:**
- Modify: `.agents/skills/rhapsody-sync/scripts/sync_tools.py` (new `scan_integration_hygiene`)
- Modify: `.agents/skills/rhapsody-sync/scripts/verify_sync.py` (new `--scan-all-integration` flag)
- Test: `.agents/skills/rhapsody-sync/tests/test_sync_tools.py`

- [ ] **Step 1: Write the failing tests**

```python
def test_scan_integration_hygiene_reports_issues_across_all_model_files(tmp_path: Path) -> None:
    """The sweep reports disallowed exception pins, try/except handlers and
    skip/xfail markers for every model integration test file, attributed per file."""
    tools = _load_sync_tools()
    pkg = tmp_path / "tests" / "integration" / "models" / "com" / "example"
    pkg.mkdir(parents=True)
    (pkg / "__init__.py").write_text("", encoding="utf-8")
    (pkg / "test_pinned.py").write_text(
        "import pytest\n\ndef test_a():\n    with pytest.raises(RhapsodyRuntimeException):\n        wrapper.method()\n",
        encoding="utf-8",
    )
    (pkg / "test_marked.py").write_text(
        "import pytest\n\n@pytest.mark.skip(reason='stale')\ndef test_b():\n    pass\n",
        encoding="utf-8",
    )
    (pkg / "test_clean.py").write_text("def test_c():\n    assert True\n", encoding="utf-8")

    issues = tools.scan_integration_hygiene(tmp_path)

    assert any("test_pinned.py" in i and "RhapsodyRuntimeException" in i for i in issues)
    assert any("test_marked.py" in i and "skip" in i for i in issues)
    assert not any("test_clean.py" in i for i in issues)
```

- [ ] **Step 2: Run to verify it fails**

Run: `python3 -m pytest -o addopts= .agents/skills/rhapsody-sync/tests -q -k hygiene`
Expected: 1 failed (AttributeError: no attribute `scan_integration_hygiene`).

- [ ] **Step 3: Implement**

In `sync_tools.py`:

```python
def scan_integration_hygiene(root: Path) -> List[str]:
    """Report-only sweep of every model integration test file.

    Flags disallowed exception assertions, try/except handlers, and skip/xfail
    markers in all test files under tests/integration/models/, attributed per
    file so interfaces can claim their own fixes.
    """
    issues: List[str] = []
    models_tests = root / "tests" / "integration" / "models"
    if not models_tests.is_dir():
        return issues
    for path in sorted(models_tests.rglob("test_*.py")):
        rel = path.relative_to(root).as_posix()
        source = path.read_text(encoding="utf-8")
        for issue in verify_integration_exception_catches(source):
            issues.append(f"{rel}: {issue}")
        for issue in verify_integration_test_markers(source):
            issues.append(f"{rel}: {issue}")
        for node in ast.walk(ast.parse(source)):
            if isinstance(node, ast.Try) and node.handlers:
                issues.append(f"{rel}: try/except handler at line {node.lineno} catches exceptions in an integration test (SKILL section 5)")
    return issues
```

In `verify_sync.py`, add the flag and the branch (after the existing `issues = verify_sync_artifacts(...)` block; note the extra `import argparse` addition `--scan-all-integration` action):

```python
    parser.add_argument(
        "--scan-all-integration",
        action="store_true",
        help="Report-only hygiene sweep over every model integration test file (disallowed raises, try/except, skip/xfail)",
    )
```

and in `main()` before the artifact verification:

```python
    if args.scan_all_integration:
        issues = scan_integration_hygiene(root)
        for issue in issues:
            print(f"HYGIENE: {issue}", file=sys.stderr)
        print(f"{len(issues)} integration hygiene finding(s)." if issues else "No integration hygiene findings.")
        return 1 if issues else 0
```

with `scan_integration_hygiene` added to the existing `from sync_tools import ...` import line.

- [ ] **Step 4: Run to verify green, then sweep the real repo**

Run: `python3 -m pytest -o addopts= .agents/skills/rhapsody-sync/tests -q`
Expected: all pass (34 + 1 = 35).

Run: `python3 .agents/skills/rhapsody-sync/scripts/verify_sync.py IRPClass --scan-all-integration 2>&1 | tail -3`
Expected: exit 1 with a per-file listing of the 65 known pins, 0 try/except handlers in model files, and 0 markers.

- [ ] **Step 5: Commit**

```bash
git add .agents/skills/rhapsody-sync/scripts/sync_tools.py .agents/skills/rhapsody-sync/scripts/verify_sync.py .agents/skills/rhapsody-sync/tests/test_sync_tools.py
git commit -m "feat(sync): add report-only all-integration hygiene sweep"
```

### Task 3: Fix the `IRPAssociationClass` stale docstring and record the blocker

The test docstring claims the test "is marked ``xfail``" — there is no marker; the test pins `AttributeError` on all four owned methods (certifying a broken binding). Phase 2 Task 10 converts it; until then the docs must tell the truth and the blocker must be recorded.

**Files:**
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_association_class.py:13-22` (docstring only)
- Modify: `docs/requirements/com/telelogic/rhapsody/core/irp_association_class.md`

- [ ] **Step 1: Replace the class docstring**

Replace the `Note:` paragraph of `TestRPAssociationClassIntegration` (keep the first line) with:

```python
    """Integration tests for IRPAssociationClass with real Rhapsody COM API.

    Blocker (open): in this Rhapsody build, ``addRelationTo`` with a non-empty
    ``linkName`` creates a plain association (metaclass ``AssociationEnd``), not
    an ``IRPAssociationClass``, so the four owned methods currently have no
    working live fixture. The test below pins ``AttributeError`` only as an
    interim record of that state — per SKILL §5 it must be replaced by an
    authentic live assertion (or an explicit documented blocker on the class's
    requirement doc) during the Windows conversion pass; the four methods keep
    full fake-COM unit coverage in the meantime.
    """
```

- [ ] **Step 2: Record the blocker in the requirement document**

In `docs/requirements/com/telelogic/rhapsody/core/irp_association_class.md`, add a row to the SWR entry table (keep `ID` stable — use the next free `SWR_…` id in that file; `Status: Blocked`; `Last Changed: 2026-11-23`) with Description:

```markdown
Live fixture: no in-build operation creates a true IRPAssociationClass
(`addRelationTo` yields a plain association), so the four owned methods
(get_end1/get_end2/get_is_class/set_is_class) have no live integration proof.
Blocked pending a Windows-side fixture investigation; unit-layer fake-COM
coverage is complete.
```

- [ ] **Step 3: Verify offline**

Run: `python3 -m pytest --collect-only -q tests/integration/models/com/telelogic/rhapsody/core/test_irp_association_class.py`
Expected: collection succeeds (1 test collected), no import errors.

- [ ] **Step 4: Commit**

```bash
git add tests/integration/models/com/telelogic/rhapsody/core/test_irp_association_class.py docs/requirements/com/telelogic/rhapsody/core/irp_association_class.md
git commit -m "docs(test): record IRPAssociationClass live-fixture blocker truthfully"
```

### Task 4: Remove the dead `test_stereotypes` fixture

The fixture has no consumer (grep confirms only conftest references it) and its failure path soft-skips dependent tests — forbidden by SKILL §4.

**Files:**
- Modify: `tests/integration/conftest.py:178-199` (delete the whole `test_stereotypes` fixture)

- [ ] **Step 1: Delete the fixture**

Remove the block from `@pytest.fixture(scope="session")\ndef test_stereotypes(...)` through its final `print(...)` line.

- [ ] **Step 2: Verify nothing referenced it and collection still works**

Run: `grep -rn "test_stereotypes" tests/ | grep -v conftest.py; python3 -m pytest --collect-only -q tests/integration 2>&1 | tail -1`
Expected: no matches outside conftest.py; collection reports no errors.

- [ ] **Step 3: Commit**

```bash
git add tests/integration/conftest.py
git commit -m "chore(test): remove dead test_stereotypes fixture"
```

### Task 5: Replace dummy literals with unique names

`add_extension_point("x")` / `add_argument("x")` create real elements with a colliding name in the shared session project. Keep behavior; make names unique. The remaining `"x"` uses inside raises-pin tests (use_case lines 142–195) are intentionally untouched — Phase 2 rewrites those tests entirely.

**Files:**
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_interface_item.py:65-77,93-95`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_use_case.py:99`

- [ ] **Step 1: `test_signature_methods` — unique argument name**

```python
        try:
            operation = test_class.add_operation(op_name)
            arg_name = self._unique("SigArg")
            operation.add_argument(arg_name)
            sig = operation.get_signature()
            assert arg_name in sig
            no_names = operation.get_signature_no_arg_names()
            assert arg_name not in no_names
            no_types = operation.get_signature_no_arg_types()
            assert arg_name in no_types
        finally:
            test_class.delete_from_project()
```

- [ ] **Step 2: `test_match_on_signature` — shared name for the matching pair, distinct for the non-match**

```python
        try:
            op1 = test_class.add_operation(op1_name)
            op2 = test_class.add_operation(op2_name)
            op3 = test_class.add_operation(op3_name)
            match_arg = self._unique("MatchArg")
            other_arg = self._unique("OtherArg")
            op1.add_argument(match_arg)
            op2.add_argument(match_arg)
            op3.add_argument(other_arg)
            assert isinstance(op1.match_on_signature(op2), bool)
            assert isinstance(op1.match_on_signature(op3), bool)
        finally:
            test_class.delete_from_project()
```

(The matching pair must share one name — `match_on_signature` compares names and types — hence one variable for op1/op2 and a different one for op3.)

- [ ] **Step 3: use_case — unique extension point**

```python
            assert use_case.add_extension_point(self._unique("ExtPt")) is None  # type: ignore[func-returns-value]
```

- [ ] **Step 4: Verify offline**

Run: `grep -rn 'add_[a-z_]*("x")\|add_[a-z_]*("y")' tests/integration/models/com/telelogic/rhapsody/core/test_irp_interface_item.py tests/integration/models/com/telelogic/rhapsody/core/test_irp_use_case.py; python3 -m pytest --collect-only -q tests/integration/models/com/telelogic/rhapsody/core/test_irp_interface_item.py tests/integration/models/com/telelogic/rhapsody/core/test_irp_use_case.py 2>&1 | tail -1`
Expected: no `add_*(...)"x"/"y")` matches in `test_signature_methods`/`test_match_on_signature`/`test_add_extension_point` (remaining `"x"` hits are inside raises-pin tests, converted in Phase 2); collection clean.

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/com/telelogic/rhapsody/core/test_irp_interface_item.py tests/integration/models/com/telelogic/rhapsody/core/test_irp_use_case.py
git commit -m "test(integration): replace dummy element names with unique names"
```

### Task 6: Worked pin conversion — `IRPProject.find_element_by_file_name` (wrapper fix + unit + integration)

This is the template for every Phase 2 conversion: the COM call is arity-wrong (report row: `SIGNATURE_ARITY_MISMATCH — declares 2 parameter(s) (2 required; params: theFolderName, theFileName; types: str, str)`), the integration test pins the resulting failure, and the fix touches wrapper → unit → integration in that order. Per SKILL §3, COM is authoritative for the call shape even where the JavaDoc documents one parameter.

**Files:**
- Modify: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py:439-452`
- Modify: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_project.py:828-833`
- Modify: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py` (replace the `find_element_by_file_name` pin test — `grep -n "find_element_by_file_name" tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py` to locate it)

- [ ] **Step 1: Write the failing unit test**

```python
def test_generated_find_element_by_file_name() -> None:
    fake = make_fake_element("Project")
    fake.findElementByFileName.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPProject(fake).find_element_by_file_name("demos/test_project", "TestProject.rpyx")
    assert result is not None
    fake.findElementByFileName.assert_called_once_with("demos/test_project", "TestProject.rpyx")
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/unit/models/com/telelogic/rhapsody/core/test_irp_project.py::test_generated_find_element_by_file_name -q -o addopts=`
Expected: FAIL (wrapper passes 1 positional arg, fake called with 2).

- [ ] **Step 3: Fix the wrapper**

```python
    def find_element_by_file_name(self, the_folder_name: str, the_file_name: str) -> IRPModelElement | None:
        """Finds an element in the project by file name.

        Args:
            the_folder_name: The folder that contains the file to search for.
            the_file_name: The file name to search for.

        Returns:
            The wrapped element if found, otherwise None.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::findElementByFileName — the
            registered type library declares two required string parameters
            (theFolderName, theFileName); COM is authoritative for the call shape
            even where the JavaDoc documents fewer parameters (SKILL §3).
        """
        return AbstractRPModelElement.wrap(
            AbstractRPModelElement.call_com(lambda: self._com.findElementByFileName(the_folder_name, the_file_name))
        )
```

- [ ] **Step 4: Run the unit test (and the full unit suite) to verify green**

Run: `.venv/bin/python -m pytest tests/unit/models/com/telelogic/rhapsody/core/test_irp_project.py -q -o addopts= && .venv/bin/python -m pytest tests/unit -q -o addopts= | tail -1`
Expected: focused file passes; full suite stays **1952 passed** (this task modifies an existing test, it does not add one).

- [ ] **Step 5: Rewrite the integration pin test into an authentic live assertion**

Replace the whole pin test with:

```python
    def test_find_element_by_file_name_finds_by_real_file(self, test_project: IRPProject) -> None:
        """Authentic data: search the live project folder for the project's own
        unit file. A found element or a real COM-returned None are both valid
        outcomes; what is forbidden is asserting the failure itself."""
        from tests.integration.conftest import TEST_PROJECT_DIR, TEST_PROJECT_NAME

        found = test_project.find_element_by_file_name(str(TEST_PROJECT_DIR), f"{TEST_PROJECT_NAME}.rpyx")
        assert found is None or isinstance(found, IRPModelElement)
```

(`IRPModelElement` is already imported in this test file; if the pin test carried local imports only it needed, drop them.)

- [ ] **Step 6: Verify offline (collection + validator + verify_sync expectation)**

Run: `python3 -m pytest --collect-only -q tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py 2>&1 | tail -1; .venv/bin/python scripts/validate_model_api.py IRPProject --source authority --path docs/reports >/dev/null 2>&1; echo "validator exit: $?"; grep -c "find_element_by_file_name" docs/reports/com/telelogic/rhapsody/core/IRPProject_api_report.md`
Expected: collection clean; validator exit 1 (other findings remain) but the `find_element_by_file_name` SIGNATURE_ARITY_MISMATCH row is gone (re-run the regen after committing to see it disappear from the report).

- [ ] **Step 7: Commit**

```bash
git add src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py tests/unit/models/com/telelogic/rhapsody/core/test_irp_project.py tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py docs/reports/com/telelogic/rhapsody/core/IRPProject_api_report.md
git commit -m "fix(project): find_element_by_file_name passes both COM parameters"
```

### Task 7: Phase 1 gate + verification battery

- [ ] **Step 1: Full gate**

Run: `.venv/bin/python -m ruff check src/ tests/ && .venv/bin/python -m black --check src/ tests/ && .venv/bin/python -m mypy src/ tests/ && .venv/bin/python -m pytest tests/unit -q -o addopts= | tail -1`
Expected: all green; unit count stays **1952 passed** (Tasks 1–2 add skill-tooling tests only; Task 6 modified an existing unit test).

- [ ] **Step 2: Skill suite**

Run: `python3 -m pytest -o addopts= .agents/skills/rhapsody-sync/tests -q`
Expected: 35 passed.

- [ ] **Step 3: verify_sync battery (expectations recorded honestly)**

Run: `for r in docs/reports/com/telelogic/rhapsody/core/*_api_report.md; do i=$(basename "$r" _api_report.md); python3 .agents/skills/rhapsody-sync/scripts/verify_sync.py "$i" >/dev/null 2>&1 && echo "$i: pass" || echo "$i: FAIL"; done`
Expected: the same 7 pass / 9 fail as before Phase 1 — the pins remain until Phase 2; IRPProject still fails (remaining pins). Record the output in the PR description.

- [ ] **Step 4: Push and open the PR**

```bash
git push -u origin fix/integration-review-offline
gh pr create --base fix/signature-validation-review --title "fix(test): offline integration-review fixes — hygiene enforcement, dead fixture, unique names, first pin conversion" --body "Closes the offline half of the 2026-11-23 integration review. See docs/superpowers/plans/2026-11-23-integration-test-fixes.md for the full plan; Phase 2 (Windows) follows separately."
```

---

## Phase 2 — Windows + live Rhapsody (gated; do NOT attempt offline)

**Environment baseline (Task 8):** launch a fresh Rhapsody instance (never attach to a stale process — SKILL §8), record baseline pass/fail for `python -m pytest tests/integration -q` and the `verify_sync` battery before any edit.

### Task 9: The repeatable pin-conversion recipe

For **each** method in the Task 10 worklist, in order:

1. **Read the evidence**: the method's JavaDoc section in `docs/java_api/com/telelogic/rhapsody/core/<INTERFACE>.html` (parameters, preconditions, return contract) and its row in `docs/reports/com/telelogic/rhapsody/core/<INTERFACE>_api_report.md` (if it carries `SIGNATURE_ARITY_MISMATCH`/`SIGNATURE_TYPE_MISMATCH`, the wrapper itself is wrong — fix the wrapper first, exactly as Task 6 did: wrapper → unit test → report regen).
2. **Build the authentic fixture**: create the real Rhapsody objects the method needs (class/package/port/element) with `_unique` names; pass their real identifiers/objects. Never fabricated placeholders; never a mocked binding; never an exception assertion (SKILL §5).
3. **Rewrite the test**: replace the pin with a real call asserting a real value, shape, or a COM-returned `None`. Keep the `try/finally` cleanup pattern the file already uses.
4. **If genuinely impossible live** (external file, license, remote server): do NOT keep the pin. Record the blocker on the interface's requirement-document SWR entry (Status: Blocked) and the sync ledger row, leave the TODO open, and delete the pin — the missing working-proof is then represented by the open blocker, exactly as the skill prescribes.
5. **Run focused**: `python -m pytest tests/integration/models/com/telelogic/rhapsody/core/test_<snake>.py -q` — must be green before moving on.
6. **Gate**: `python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE>` — one fewer (or zero) disallowed findings than before; when the interface's last pin is converted, `verify_sync` goes green.
7. **Commit per interface**: `fix(test): convert <INTERFACE> integration pins to live assertions`.

### Task 10: Conversion worklist (from the 2026-11-23 review; convert in this order — smallest first to build momentum)

| Interface | Shadowed methods (only exercised as pins today) |
| --- | --- |
| irp_port | get_contract, set_contract |
| irp_collection | add_graphical_item, to_list — plus add a first real test for `get_item` (never invoked anywhere) |
| irp_operation | set_flowchart, update_contained_diagrams_on_server |
| irp_use_case | add_event_reception_with_event, find_entry_point, find_extension_point, set_is_behavior_overriden, update_contained_diagrams_on_server |
| irp_unit | copy_to_another_project, get_unit_path, move_to_another_project_leave_a_reference, reference_to_another_project, set_unit_path |
| irp_class | add_event_reception_with_event, add_link, add_link_to_part_via_port, is_abstract, update_contained_diagrams_on_server |
| irp_package | add_activity_diagram, add_association, add_global_object, add_instance_specification, add_link, add_statechart_diagram, find_all_by_name, get_remote_requirements_populate_mode, get_root_instance_specifications, login_to_remote_artifact_server, update_contained_diagrams_on_server, update_contained_matrices_on_server, update_contained_tables_on_server |
| irp_model_element | add_association, add_link_to_element, add_property, add_redefines, add_remote_dependency_to, become_template_instantiation_of, create_oslc_link, delete_oslc_link, get_overridden_properties_by_pattern, get_property_value, get_property_value_conditional, get_property_value_conditional_explicit, get_property_value_explicit, get_rmm_url, remove_property, set_description_and_hyperlinks, set_description_html, set_main_diagram, set_property_value, set_tag_context_value, set_tag_element_value, set_tag_value, set_ti, synchronize_template_instantiation |
| irp_project | add_actor, add_class, add_node, add_spell_checker_result, apply_browser_custom_views_on_diagrams, apply_roundtrip_diff_merge, check_events_base_ids_solve_collisions, clean_unresolved_elements, close_csv_file, delete_node, enable_rhapsody_model_manager, find_element_by_binary_id, find_element_by_file_name (converted offline in Task 6 — verify live), find_elements_with_oslc_link, get_active_custom_views_on_diagram, get_default_directory_scheme, get_new_progress_bar, get_requirements_by_id, get_roundtrip_shadow_model, import_package_from_rose, import_project_from_rose, locate_in_ide, migrate_design_manager_links, reload_csv_file, save_as, save_as_prev_version, set_global_configuration |
| irp_association_class | get_end1, get_end2, get_is_class, set_is_class — see Task 11 first |

Known shortcuts where the signature report already names the defect: `find_element_by_file_name` (Task 6), `generate_report` (2 vs 6 params: modelscope, templatename, docType, filename, showDocument, silentMode), `gateway_export_to_xml` (filename, params), `find_element_by_binary_id` (type: pass the real `BinaryID` string obtained from a created element, per SKILL §5's example).

### Task 11: `IRPAssociationClass` live-fixture investigation

1. In the live session, try the documented creation paths and print what actually comes back:
   ```python
   pkg = test_project.add_package(_unique("AssocClsProbe"))
   cls = pkg.add_class(_unique("ProbeCls"))
   rel = cls.add_relation_to("Association", cls, cls, cls, cls, _unique("probeLink"))
   print(type(rel), rel.get_meta_class() if rel else None)
   ```
2. Search the demo/TestProject model for an existing association class: `test_project.find_element_by_binary_id(...)` is not usable here — instead enumerate `pkg.get_classes()`/relations via `get_relations`-style owned methods and check `get_meta_class() == "IRPAssociationClass"`.
3. If a genuine `IRPAssociationClass` can be produced: rewrite `test_owned_methods_via_wrapped_com_object` to build that fixture, call the four owned methods with real assertions, drop the `AttributeError` pins and the blocker docstring/requirement row.
4. If it cannot: keep the blocker recorded in Task 3, replace the pin test with a plain fixture-shaped test that constructs the wrapper from a real association (`IRPAssociationClass(assoc._com)` where `assoc` is the created plain association) and asserts the documented `NotImplementedError`-free real behavior that IS available — or, if none is exercisable, delete the pin test and leave the requirement-doc blocker as the representation (per SKILL §5; record the decision on the ledger row).
5. Gate: `python .agents/skills/rhapsody-sync/scripts/verify_sync.py IRPAssociationClass` green (pins gone), or red-with-documented-blocker acknowledged in the PR description.

### Task 12: Application facade breadth (20 untested methods)

For each of: `add_to_model`, `add_to_model_ex`, `check_model`, `create_new_collection`, `generate`, `generate_elements`, `generate_entire_project`, `get_code_gen_simplifiers_registry`, `get_diag_synth_api`, `get_external_checker_registry`, `get_external_ide_registry`, `get_external_roundtrip_invoker`, `get_ow_pane_mgr`, `get_search_manager`, `get_selection`, `open_project`, `regenerate`, `save_all`, `set_hidden_ui`, `set_log` — read the JavaDoc section in `IRPApplication.html`, add one authentic live test to `tests/integration/test_application.py` (reuse `rhapsody_app`; use the existing `test_project` for targets; assert value/shape/documented-None), or record a documented blocker in the class requirement doc if the method needs an environment feature that cannot be created in the test session. `quit`/`disconnect` stay excluded (documented). Gate: full `tests/integration/test_application.py` green live.

### Task 13: Explicitly out of scope

The 23 untested legacy `elements/` wrapper modules ride their future sync runs (each sync creates the mirrored integration file per SKILL §2/§5). Do not hand-write standalone tests for them here — it would duplicate the sync-run work and violate the own-methods ownership rules.

### Task 14: Phase 2 final gate

- [ ] Full live run: `python -m pytest tests/integration -q` green (CLI E2E included), zero pins remaining (`python .agents/skills/rhapsody-sync/scripts/verify_sync.py IRPClass --scan-all-integration` reports 0 disallowed findings), all 16 `verify_sync` runs green, both coverage figures re-measured and recorded per interface in the sync report (unit + integration independently 100%, SKILL §4/§8).
- [ ] PR to main with the per-interface conversion table filled in (method → fixture → assertion) and the verification transcript.
