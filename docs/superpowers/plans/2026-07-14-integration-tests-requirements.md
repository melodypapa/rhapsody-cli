# Requirements Subpackage Integration Tests Completion Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add integration tests for all remaining untested methods of `RPRequirement` (anchors, body, specification, requirement ID) and `RPAnnotation`. Flip in-source `[ ] integration test` markers to `[x]` as work completes.

**Architecture:** Extends `tests/integration/models/elements/requirements/test_model_requirements.py`.

**Tech Stack:** pytest, pywin32 (win32com), live Rhapsody COM API, `uuid.uuid4().hex[:8]`.

## Global Constraints

- Windows-only runtime (requires Windows + a running Rhapsody instance)
- All test classes use `@pytest.mark.integration`
- All tests consume the `test_project: RPProject` fixture
- Use `_unique(prefix)` with `uuid.uuid4().hex[:8]`
- Always `try/finally` cleanup via `element.delete_from_project()`
- Assert both `isinstance()` and read-back values
- Flip `[ ] integration test` to `[x]` per task in `model_requirements.py`
- Quality gate after each task: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
- Import via subpackage `__init__.py` re-exports

---

## Scope Summary

`src/rhapsody_cli/models/elements/requirements/model_requirements.py` — 12 checklist rows total, all currently `[ ] integration test`:

**`RPAnnotation`** (10 methods):
`add_anchor`, `get_anchored_by_me`, `get_body`, `get_specification`, `get_specification_rtf`, `is_specification_rtf`, `remove_anchor`, `set_body`, `set_specification`, `set_specification_rtf`

**`RPRequirement`** (2 methods):
`get_requirement_id`, `set_requirement_id`

Existing coverage in `tests/integration/models/elements/requirements/test_model_requirements.py`: only `test_create_requirement_in_package` (creation, `get_name`, `get_meta_class` — these are inherited `RPModelElement`/`RPUnit` methods already covered elsewhere and are not part of this subpackage's checklist).

---

### Task 1: Anchor management

**Files:**
- Modify: `tests/integration/models/elements/requirements/test_model_requirements.py`
- Modify: `src/rhapsody_cli/models/elements/requirements/model_requirements.py` (flip checklist boxes only)

**Methods covered:** `add_anchor`, `remove_anchor`, `get_anchored_by_me`

- [ ] **Step 1: Write the new integration test**

```python
def test_anchor_management(self, test_project: RPProject) -> None:
    pkg_name = self._unique("AnchorPkg")
    annotation_name = self._unique("Anno")
    target_class_name = self._unique("AnchorTarget")
    pkg = self._create_package(test_project, pkg_name)
    annotation = pkg.add_new_aggr("Annotation", annotation_name)
    target = pkg.add_class(target_class_name)
    try:
        assert annotation is not None
        assert isinstance(annotation, RPAnnotation)

        annotation.add_anchor(target)
        anchored = list(annotation.get_anchored_by_me())
        assert target in anchored

        annotation.remove_anchor(target)
        anchored_after = list(annotation.get_anchored_by_me())
        assert target not in anchored_after
    finally:
        annotation.delete_from_project()
        target.delete_from_project()
```

Add the corresponding import at the top of the test file: `from rhapsody_cli.models.elements.requirements import RPAnnotation, RPRequirement`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/requirements/test_model_requirements.py -m integration -v -k test_anchor_management`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/requirements/model_requirements.py`, flip `add_anchor`, `remove_anchor`, `get_anchored_by_me` rows to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/requirements/test_model_requirements.py src/rhapsody_cli/models/elements/requirements/model_requirements.py
git commit -m "test: add integration tests for RPAnnotation anchor management"
```

---

### Task 2: Specification & body content

**Files:**
- Modify: `tests/integration/models/elements/requirements/test_model_requirements.py`
- Modify: `src/rhapsody_cli/models/elements/requirements/model_requirements.py` (flip checklist boxes only)

**Methods covered:** `get_body`, `set_body`, `get_specification`, `set_specification`, `get_specification_rtf`, `set_specification_rtf`, `is_specification_rtf`

- [ ] **Step 1: Write the new integration test**

```python
def test_body_and_specification_roundtrip(self, test_project: RPProject) -> None:
    pkg_name = self._unique("SpecPkg")
    annotation_name = self._unique("Anno")
    pkg = self._create_package(test_project, pkg_name)
    annotation = pkg.add_new_aggr("Annotation", annotation_name)
    try:
        assert annotation is not None
        assert isinstance(annotation, RPAnnotation)

        body_text = "This is the annotation body."
        annotation.set_body(body_text)
        assert annotation.get_body() == body_text

        spec_text = "This is the specification text."
        annotation.set_specification(spec_text)
        assert annotation.get_specification() == spec_text

        # RTF flag reflects whichever format was last written; just confirm it's a bool
        assert annotation.is_specification_rtf() in (True, False)

        rtf_text = r"{\rtf1\ansi This is RTF specification.}"
        annotation.set_specification_rtf(rtf_text)
        assert "RTF specification" in annotation.get_specification_rtf()
        assert annotation.is_specification_rtf() is True
    finally:
        annotation.delete_from_project()
```

If Rhapsody's COM layer does not persist `is_specification_rtf()` as expected after `set_specification_rtf`, mark the assertion with `@pytest.mark.xfail(reason="...", strict=False)` on the whole test rather than silently dropping the assertion — do not skip the method from the checklist.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/requirements/test_model_requirements.py -m integration -v -k test_body_and_specification_roundtrip`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/requirements/model_requirements.py`, flip `get_body`, `set_body`, `get_specification`, `set_specification`, `get_specification_rtf`, `set_specification_rtf`, `is_specification_rtf` rows to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/requirements/test_model_requirements.py src/rhapsody_cli/models/elements/requirements/model_requirements.py
git commit -m "test: add integration tests for RPAnnotation body and specification"
```

---

### Task 3: Requirement ID

**Files:**
- Modify: `tests/integration/models/elements/requirements/test_model_requirements.py`
- Modify: `src/rhapsody_cli/models/elements/requirements/model_requirements.py` (flip checklist boxes only)

**Methods covered:** `get_requirement_id`, `set_requirement_id`

- [ ] **Step 1: Write the new integration test**

```python
def test_requirement_id_roundtrip(self, test_project: RPProject) -> None:
    pkg_name = self._unique("ReqIdPkg")
    req_name = self._unique("ReqWithId")
    pkg = self._create_package(test_project, pkg_name)
    req = pkg.add_new_aggr("Requirement", req_name)
    try:
        assert req is not None
        assert isinstance(req, RPRequirement)

        req_id = self._unique("REQ")
        req.set_requirement_id(req_id)
        assert req.get_requirement_id() == req_id
    finally:
        req.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/requirements/test_model_requirements.py -m integration -v -k test_requirement_id_roundtrip`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/requirements/model_requirements.py`, flip `get_requirement_id`, `set_requirement_id` rows to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/requirements/test_model_requirements.py src/rhapsody_cli/models/elements/requirements/model_requirements.py
git commit -m "test: add integration tests for RPRequirement requirement ID"
```

---

### Task 4: Full Subpackage Verification

**Files:**
- Read-only verification: `src/rhapsody_cli/models/elements/requirements/model_requirements.py`
- Read-only verification: `tests/integration/models/elements/requirements/test_model_requirements.py`

- [ ] **Step 1: Confirm all 12 checklist rows are flipped**

```bash
grep -c "\[ \] integration test" src/rhapsody_cli/models/elements/requirements/model_requirements.py
```

Expected output: `0`.

- [ ] **Step 2: Run the complete integration test file**

Run: `pytest tests/integration/models/elements/requirements/test_model_requirements.py -m integration -v`

All tests (creation test + the 3 new tests from Tasks 1–3) must pass or be explicitly `xfail`-marked with a documented reason.

- [ ] **Step 3: Run the full quality gate one final time**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 4: Commit final verification (if any cleanup was needed)**

```bash
git add -A
git commit -m "test: complete requirements subpackage integration test coverage"
```
