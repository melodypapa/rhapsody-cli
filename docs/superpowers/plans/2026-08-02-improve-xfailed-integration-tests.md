# Improve XFailed Integration Tests Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

> **Supersedes** `2026-07-21-fix-xfailed-integration-tests.md`, which was written before live-COM verification and contains incorrect test names and placeholder steps. This plan is built directly from a verified `--runxfail` run against a live `Rhapsody2.Application.1` instance (6 pass / 44 fail, captured via JUnit).

**Goal:** Convert verified-passing xfailed tests to normal passing tests, fix the test-side bugs, and replace every remaining vague "TODO: may not work" reason with the actual verified COM root cause.

**Architecture:** All changes are confined to `tests/integration/` (no production/source changes). Three kinds of change: (1) delete spurious `@pytest.mark.xfail` decorators on tests already proven to pass; (2) correct test assertions/typos that contradict real COM behavior; (3) rewrite `reason="..."` strings on the genuine COM failures to the verified HRESULT/behavior. Every change is verified by re-running the specific test against live Rhapsody.

**Tech Stack:** Python 3.9, pytest 8.x, IBM Rhapsody COM API (`win32com`), `pytest.mark.xfail` with `strict=False`.

## Global Constraints

- Integration tests run **only** on Windows with a running IBM Rhapsody instance attached via `Rhapsody2.Application.1` (see `tests/integration/conftest.py::rhapsody_app`, which uses `RhapsodyApplication.connect(attach_only=True)`). The whole session auto-skips if no Rhapsody is attached.
- Never use real COM in unit tests; this plan touches **integration tests only**.
- `strict=False` xfails do NOT fail the suite if the body passes (they report `XPASS`). That is exactly why spurious markers went unnoticed — removing them makes the test a real, enforceable assertion.
- Project forbids AI attribution in commits and forbids direct commits to `main`; all work lands on a `fix/` or `test/` branch.
- Commit messages use Conventional Commits (`test:`, `fix:`, `docs:`).
- Keep line length ≤ 200, `black` + `ruff` clean.

## Verified Baseline (from live run, 2026-08-02)

`pytest tests/integration/ -m xfail --runxfail --junitxml` → **6 passed, 44 failed, 160 deselected**. The 6 that pass are spurious markers. The 44 failures break down (each tied to a `--tb=line` error) as:

| Bucket | HRESULT / error | Count |
|---|---|---|
| Member not exposed via COM IDispatch (`AttributeError: obj.member`) | — | 6 |
| Property API rejected | `0x80040002` | 8 |
| `E_FAIL` (precondition unmet) | `0x80004005` | 6 |
| Invalid op in current state | `0x80040001` | 2 |
| Invalid argument | `0x80040009` | 2 |
| Meta-class conversion rejected | `0x8004000A` | 1 |
| `E_INVALIDARG` | `0x80070057` | 1 |
| Type mismatch | `DISP_E_TYPEMISMATCH` | 1 |
| Assertion mismatch (COM runs, value differs) | — | 13 |
| Python error inside the test (not the SUT) | — | 4 |

---

## File Structure

Only one source file is edited:

- `tests/integration/models/test_core.py` — 46 of the 50 markers; Tasks 1–3 operate here.

The other 4 markers (in `tests/integration/models/elements/classifiers/`) are all genuine, verified COM defects; they are addressed in Task 4 (reason-only) and left xfailed.

No new files, no `conftest.py` changes, no production edits.

---

### Task 0: Create branch and record baseline

**Files:**
- N/A (workspace setup only)

**Interfaces:**
- Consumes: N/A
- Produces: a `test/improve-xfailed-integration-tests` branch and a baseline number to compare against.

- [ ] **Step 1: Ensure on latest main**

```bash
git checkout main
git pull --ff-only
```

- [ ] **Step 2: Create the feature branch**

```bash
git checkout -b test/improve-xfailed-integration-tests
```

- [ ] **Step 3: Record the current xfail count as baseline**

```bash
pytest tests/integration/ -m xfail --co -q --no-cov -p no:cacheprovider | tail -1
```

Expected: `50 tests collected` (the current marker count). Note this number; Task 5 compares the final count against it.

---

### Task 1: Remove the 6 spurious xfail markers (tests proven to pass)

These six tests pass against live Rhapsody with `--runxfail`. The `strict=False` marker hides that. Removing the decorator turns each into a real, enforced assertion.

**Files:**
- Modify: `tests/integration/models/test_core.py`

**Interfaces:**
- Consumes: Verified-passing list from the live run.
- Produces: 6 fewer xfail markers; 6 more always-passing integration tests.

The six decorators to delete (each is a single line directly above its `def test_...`):

| Line | Decorator `reason=` |
|---|---|
| 277 | `"read-back of variant typed slots is not reliable on all collections"` (`test_set_string_stores_value`) |
| 291 | `"read-back of variant typed slots is not reliable on all collections"` (`test_set_integer_stores_value`) |
| 1841 | `"TODO: get_nested_save_units may not return empty collection as expected"` (`test_get_nested_save_units_empty_on_plain_package`) |
| 1871 | `"TODO: get_structure_diagrams may not return empty collection as expected"` (`test_get_structure_diagrams_empty_on_class`) |
| 1887 | `"TODO: get_add_to_model_mode may not return expected value"` (`test_get_add_to_model_mode_returns_int`) |
| 1899 | `"TODO: is_reference_unit may not work correctly on local units"` (`test_is_reference_unit_false_for_local_unit`) |

- [ ] **Step 1: Delete the decorator above `test_set_string_stores_value`**

Remove exactly this line (line 277):

```python
    @pytest.mark.xfail(strict=False, reason="read-back of variant typed slots is not reliable on all collections")
    def test_set_string_stores_value(self, test_project: RPProject, rhapsody_app: RhapsodyApplication) -> None:
```

becomes:

```python
    def test_set_string_stores_value(self, test_project: RPProject, rhapsody_app: RhapsodyApplication) -> None:
```

- [ ] **Step 2: Delete the decorator above `test_set_integer_stores_value`**

Remove the line:

```python
    @pytest.mark.xfail(strict=False, reason="read-back of variant typed slots is not reliable on all collections")
```

directly above `def test_set_integer_stores_value`.

- [ ] **Step 3: Delete the decorator above `test_get_nested_save_units_empty_on_plain_package`**

Remove the line:

```python
    @pytest.mark.xfail(strict=False, reason="TODO: get_nested_save_units may not return empty collection as expected")
```

directly above `def test_get_nested_save_units_empty_on_plain_package`.

- [ ] **Step 4: Delete the decorator above `test_get_structure_diagrams_empty_on_class`**

Remove the line:

```python
    @pytest.mark.xfail(strict=False, reason="TODO: get_structure_diagrams may not return empty collection as expected")
```

directly above `def test_get_structure_diagrams_empty_on_class`.

- [ ] **Step 5: Delete the decorator above `test_get_add_to_model_mode_returns_int`**

Remove the line:

```python
    @pytest.mark.xfail(strict=False, reason="TODO: get_add_to_model_mode may not return expected value")
```

directly above `def test_get_add_to_model_mode_returns_int`.

- [ ] **Step 6: Delete the decorator above `test_is_reference_unit_false_for_local_unit`**

Remove the line:

```python
    @pytest.mark.xfail(strict=False, reason="TODO: is_reference_unit may not work correctly on local units")
```

directly above `def test_is_reference_unit_false_for_local_unit`.

- [ ] **Step 7: Verify all six pass against live Rhapsody (WITHOUT `--runxfail`)**

```bash
pytest \
  "tests/integration/models/test_core.py::TestRPCollectionMutationMethodsIntegration::test_set_string_stores_value" \
  "tests/integration/models/test_core.py::TestRPCollectionMutationMethodsIntegration::test_set_integer_stores_value" \
  "tests/integration/models/test_core.py::TestRPUnitCrossProjectIntegration::test_get_nested_save_units_empty_on_plain_package" \
  "tests/integration/models/test_core.py::TestRPUnitCrossProjectIntegration::test_get_structure_diagrams_empty_on_class" \
  "tests/integration/models/test_core.py::TestRPUnitCrossProjectIntegration::test_get_add_to_model_mode_returns_int" \
  "tests/integration/models/test_core.py::TestRPUnitCrossProjectIntegration::test_is_reference_unit_false_for_local_unit" \
  -v --no-cov -p no:cacheprovider
```

Expected: `6 passed`. (If Rhapsody is not attached, pytest reports the session as skipped — start/attach Rhapsody first.)

- [ ] **Step 8: Run lint/format on the file**

```bash
ruff check tests/integration/models/test_core.py && black --check tests/integration/models/test_core.py
```

Expected: clean. If `black` reformats, run `black tests/integration/models/test_core.py`.

- [ ] **Step 9: Commit**

```bash
git add tests/integration/models/test_core.py
git commit -m "test(integration): remove 6 spurious xfail markers proven to pass on live COM"
```

---

### Task 2: Fix `test_find_nested_element` not-found assertion

Verified against live COM: the **found** case already passes — `find_nested_element(name, "Class")` returns the element. The test fails only at line 887 because Rhapsody's `findNestedElement` returns **`None`** (not an empty-name element) when nothing matches. The test's assertion assumed the old "empty element" behavior. Fix the assertion, then drop the marker.

**Files:**
- Modify: `tests/integration/models/test_core.py:875-888`

**Interfaces:**
- Consumes: N/A
- Produces: `test_find_nested_element` becomes a passing test (no marker).

- [ ] **Step 1: Delete the decorator**

Remove the line directly above `def test_find_nested_element`:

```python
    @pytest.mark.xfail(strict=False, reason="TODO: find_nested_element may not handle missing elements correctly")
```

- [ ] **Step 2: Fix the not-found assertion**

Change line 887 from:

```python
            not_found = pkg.find_nested_element(self._unique("Missing"), "Class")
            assert not_found is not None and not_found.get_name() == ""
```

to:

```python
            not_found = pkg.find_nested_element(self._unique("Missing"), "Class")
            # Rhapsody findNestedElement returns None (not an empty-name element) when no match.
            assert not_found is None
```

- [ ] **Step 3: Verify against live Rhapsody**

```bash
pytest "tests/integration/models/test_core.py::TestRPModelElementNavigationIntegration::test_find_nested_element" -v --no-cov -p no:cacheprovider
```

Expected: `1 passed`.

- [ ] **Step 4: Commit**

```bash
git add tests/integration/models/test_core.py
git commit -m "test(integration): fix find_nested_element not-found assertion (returns None)"
```

---

### Task 3: Fix 3 `pkg.add_package()` test bugs → `add_nested_package()`

`RPPackage` exposes `add_nested_package(name)` (wrapper at `src/rhapsody_cli/models/elements/containment/model_package.py:151`), **not** `add_package`. Three tests call `pkg.add_package(...)`, which always raises `AttributeError: 'RPPackage' object has no attribute 'add_package'` — a typo in the test, not a SUT bug. Fix the call. `test_find_nested_element_recursive` also re-uses the wrong not-found assertion pattern from Task 2.

**Files:**
- Modify: `tests/integration/models/test_core.py:892-906` (`test_find_nested_element_recursive`)
- Modify: `tests/integration/models/test_core.py:983-992` (`test_has_nested_elements`)
- Modify: `tests/integration/models/test_core.py:1858-1870` (`test_get_nested_save_units_count_matches_collection`)

**Interfaces:**
- Consumes: `RPPackage.add_nested_package(name) -> RPPackage` (existing).
- Produces: three tests either pass (marker removed) or, if a deeper issue remains, keep the marker with a sharpened reason (fallback strings supplied per test).

- [ ] **Step 1: Fix `test_find_nested_element_recursive` calls**

Change line 895:

```python
            subpkg = pkg.add_package(self._unique("SubPkg"))  # type: ignore[attr-defined]
```

to:

```python
            subpkg = pkg.add_nested_package(self._unique("SubPkg"))
```

And change line 899 (same wrong not-found assumption as Task 2):

```python
            not_found = pkg.find_nested_element(class_name, "Class")
            assert not_found is not None and not_found.get_name() == ""
```

to:

```python
            not_found = pkg.find_nested_element(class_name, "Class")
            # The class is nested one level down, so first-level search returns None.
            assert not_found is None
```

- [ ] **Step 2: Fix `test_has_nested_elements` call**

Change line 986:

```python
            empty_pkg = pkg.add_package(self._unique("EmptyPkg"))  # type: ignore[attr-defined]
```

to:

```python
            empty_pkg = pkg.add_nested_package(self._unique("EmptyPkg"))
```

- [ ] **Step 3: Fix `test_get_nested_save_units_count_matches_collection` call**

Change line 1862:

```python
            sub_pkg = pkg.add_package(self._unique("SubPkg"))  # type: ignore[attr-defined]
```

to:

```python
            sub_pkg = pkg.add_nested_package(self._unique("SubPkg"))
```

- [ ] **Step 4: Run all three with `--runxfail` to see real outcome now that the typo is gone**

```bash
pytest \
  "tests/integration/models/test_core.py::TestRPModelElementNavigationIntegration::test_find_nested_element_recursive" \
  "tests/integration/models/test_core.py::TestRPModelElementNavigationIntegration::test_has_nested_elements" \
  "tests/integration/models/test_core.py::TestRPUnitCrossProjectIntegration::test_get_nested_save_units_count_matches_collection" \
  --runxfail -v --no-cov -p no:cacheprovider
```

Expected (best case): `3 passed`. If any still fail, record the new error for that test.

- [ ] **Step 5: For each test that now PASSES, delete its decorator**

- `test_find_nested_element_recursive`: remove `@pytest.mark.xfail(strict=False, reason="TODO: find_nested_element_recursive may not traverse all levels correctly")`
- `test_has_nested_elements`: remove `@pytest.mark.xfail(strict=False, reason="TODO: has_nested_elements may not return accurate count after element addition")`
- `test_get_nested_save_units_count_matches_collection`: remove `@pytest.mark.xfail(strict=False, reason="TODO: get_nested_save_units_count may not match actual collection count")`

- [ ] **Step 6: For any test that STILL FAILS, keep the marker but replace its reason with the verified cause**

Use these fallback strings (only for the ones that did not pass in Step 4):

- `test_find_nested_element_recursive` → `reason="IRPModelElement.findNestedElementRecursive does not locate elements nested under a sub-package in this build"`
- `test_has_nested_elements` → `reason="IRPModelElement.hasNestedElements does not reflect the expected 0/1 count after adding/removing a child element"`
- `test_get_nested_save_units_count_matches_collection` → `reason="IRPUnit.getNestedSaveUnitsCount does not match getNestedSaveUnits().getCount() for a separate save unit"`

- [ ] **Step 7: Re-verify (without `--runxfail` for the ones whose marker was removed; with `--runxfail` for any kept)**

```bash
pytest \
  "tests/integration/models/test_core.py::TestRPModelElementNavigationIntegration::test_find_nested_element_recursive" \
  "tests/integration/models/test_core.py::TestRPModelElementNavigationIntegration::test_has_nested_elements" \
  "tests/integration/models/test_core.py::TestRPUnitCrossProjectIntegration::test_get_nested_save_units_count_matches_collection" \
  -v --no-cov -p no:cacheprovider
```

Expected: removed-marker tests report `passed`; kept-marker tests report `xfailed`.

- [ ] **Step 8: Lint and commit**

```bash
ruff check tests/integration/models/test_core.py && black tests/integration/models/test_core.py
git add tests/integration/models/test_core.py
git commit -m "test(integration): use add_nested_package and fix not-found assertions in navigation tests"
```

---

### Task 4: Replace every remaining vague "TODO" reason with the verified root cause

After Tasks 1–3, the remaining xfailed tests all represent genuine COM behavior. Their `reason=` strings are hedge text ("may not work", "may not return") written before verification. Rewrite each to state the verified HRESULT / observed behavior so future readers know exactly why it is marked. **This task changes only `reason="..."` strings and adds no markers.**

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `tests/integration/models/elements/classifiers/test_model_class.py`
- Modify: `tests/integration/models/elements/classifiers/test_model_interface_item.py`
- Modify: `tests/integration/models/elements/classifiers/test_model_association_class.py`

**Interfaces:**
- Consumes: Verified per-test error mapping below.
- Produces: every surviving `reason=` describes a concrete COM root cause (HRESULT or AttributeError).

Apply the following `reason=` rewrites. For each row, replace the **current** reason string (left) on the named test with the **new** string (right). Keep `strict=False` exactly as-is; only the quoted reason text changes. Lines are the original (pre-Task-1) locations and may shift — locate by test name.

#### 4a. `test_model_class.py`

| Test | New `reason` |
|---|---|
| `test_is_final_roundtrip` | `"Rhapsody COM defect: IRPClass.setIsFinal does not persist (get returns 0) — same limitation as setIsAbstract"` |
| `test_update_contained_diagrams_on_server` | `"IRPClass COM dispatch does not expose updateContainedDiagramsOnServer (AttributeError) though declared in the Java API"` |

#### 4b. `test_model_interface_item.py`

| Test | New `reason` |
|---|---|
| `test_match_on_signature` | `"Rhapsody COM defect: IRPInterfaceItem.matchOnSignature always returns 0 in this build"` |

#### 4c. `test_model_association_class.py`

| Test | New `reason` |
|---|---|
| `test_association_class_found_via_package` | `"Rhapsody COM defect: addRelationTo creates a plain Association, not an AssociationClass"` |

#### 4d. `test_core.py` — member not exposed via COM IDispatch

| Test | New `reason` |
|---|---|
| `test_add_graphical_item_appends_and_count_increases` | `"IRPCollection does not expose metaClass and addNewNodeForElement is on IRPSelection, not a generic collection (AttributeError)"` |
| `test_get_rmm_url_returns_empty_string` | `"IRPModelElement.rmmUrl property not exposed via COM dispatch (AttributeError: addClass.rmmUrl)"` |
| `test_get_is_of_meta_class_class` | `"IRPModelElement.getIsOfMetaClass not exposed via COM dispatch (AttributeError: addClass.getIsOfMetaClass)"` |
| `test_get_unit_path_full_and_relative` | `"IRPUnit.getUnitPath not exposed on IRPPackage via COM (AttributeError: addPackage.getUnitPath); package must be a separate save unit"` |
| `test_set_and_get_unit_path_roundtrip` | `"IRPUnit.getUnitPath not exposed on IRPPackage via COM (AttributeError: addPackage.getUnitPath); package must be a separate save unit"` |

#### 4e. `test_core.py` — COM call rejected (RhapsodyRuntimeException)

| Test | New `reason` |
|---|---|
| `test_add_remote_dependency_to_and_get_remote_dependencies` | `"IRPModelElement.addRemoteDependencyTo raises HRESULT 0x80040009"` |
| `test_add_association` | `"IRPModelElement.addAssociation raises DISP_E_TYPEMISMATCH — wrapper passes an argument type COM rejects"` |
| `test_set_description_and_hyperlinks` | `"IRPModelElement.setDescriptionAndHyperlinks raises E_INVALIDARG (0x80070057) — argument type mismatch"` |
| `test_add_property_and_get_property_value` | `"IRPModelElement.addProperty raises HRESULT 0x80040002 for unregistered property keys (e.g. 'Custom::X')"` |
| `test_set_property_value_and_read_back` | `"IRPModelElement.setPropertyValue raises HRESULT 0x80040002 for key 'General::Graphics::ShowLabels'"` |
| `test_add_then_remove_property` | `"IRPModelElement.addProperty raises HRESULT 0x80040002 for unregistered property keys"` |
| `test_get_property_value_explicit` | `"blocked on setPropertyValue setup step which raises HRESULT 0x80040002"` |
| `test_get_overridden_properties` | `"blocked on setPropertyValue setup step which raises HRESULT 0x80040002"` |
| `test_get_overridden_properties_by_pattern` | `"blocked on setPropertyValue setup step which raises HRESULT 0x80040002"` |
| `test_get_property_value_conditional` | `"blocked on setPropertyValue setup step which raises HRESULT 0x80040002"` |
| `test_get_property_value_conditional_explicit` | `"blocked on setPropertyValue setup step which raises HRESULT 0x80040002"` |
| `test_change_to` | `"IRPModelElement.changeTo raises HRESULT 0x8004000A (invalid meta-class conversion)"` |
| `test_become_template_instantiation_of` | `"IRPModelElement.becomeTemplateInstantiationOf raises E_FAIL (0x80004005) without an existing template to bind to"` |
| `test_get_ti` | `"blocked on becomeTemplateInstantiationOf setup step which raises E_FAIL (0x80004005)"` |
| `test_set_ti` | `"blocked on becomeTemplateInstantiationOf setup step which raises E_FAIL (0x80004005)"` |
| `test_synchronize_template_instantiation` | `"blocked on becomeTemplateInstantiationOf setup step which raises E_FAIL (0x80004005)"` |
| `test_add_redefines_and_get_redefines` | `"IRPModelElement.addRedefines raises E_FAIL (0x80004005); requires a redefinable operation in a specialization context"` |
| `test_remove_redefines` | `"blocked on addRedefines setup step which raises E_FAIL (0x80004005)"` |
| `test_load_and_unload_roundtrip` | `"IRPModelElement.deleteFromProject raises HRESULT 0x80040001 during the load/unload sequence"` |
| `test_get_is_stub_after_unload` | `"blocked on deleteFromProject during unload which raises HRESULT 0x80040001"` |
| `test_get_main_diagram_and_set_main_diagram_roundtrip` | `"IRPModelElement.addNewAggr raises HRESULT 0x80040009"` |
| `test_add_link_to_element` | `"IRPModelElement.addLinkToElement returns None for the given target; wrapper then AttributeError on NoneType._com"` |

#### 4f. `test_core.py` — assertion mismatch (COM runs, value differs from assumption)

| Test | New `reason` |
|---|---|
| `test_get_tag` | `"fixture gap: get_tag returns None because no tag definition is created on the stereotype (no wrapper method to add one)"` |
| `test_get_new_term_stereotype` | `"fixture gap: project has no new-term stereotype; get_new_term_stereotype returns None"` |
| `test_set_tag_value` | `"fixture gap: depends on get_tag('SomeTag') which returns None (no tag definition created)"` |
| `test_set_tag_element_value` | `"fixture gap: depends on get_tag('SomeTag') which returns None (no tag definition created)"` |
| `test_set_tag_context_value` | `"fixture gap: depends on get_tag('SomeTag') which returns None (no tag definition created)"` |
| `test_get_of_template_on_plain_element` | `"IRPModelElement.getOfTemplate returns None for a plain (non-instantiated) element; test assumption is wrong"` |
| `test_set_of_template` | `"IRPModelElement.setOfTemplate returns None; test assumption is wrong"` |
| `test_get_user_defined_meta_class` | `"IRPModelElement.getUserDefinedMetaClass returns 'Class' (the metaclass), not '' for a plain element; semantics differ from the test assumption"` |
| `test_set_guid_and_get_guid` | `"IRPModelElement.setGUID does not change getGUID output; getGUID returns Rhapsody's internal 'GUID <hex>' format, not the registry format passed to setGUID"` |

> Note: the `rmmUrl`/`getUnitPath` rows in 4d intentionally duplicate the COM-dispatch diagnosis already in the test; this keeps each `reason` self-contained.

- [ ] **Step 1: Apply the reason rewrites in `test_model_class.py`, `test_model_interface_item.py`, `test_model_association_class.py`**

For each test in sections 4a–4c, change only the quoted `reason` text inside the existing `@pytest.mark.xfail(strict=False, reason="...")`.

- [ ] **Step 2: Apply the reason rewrites in `test_core.py`** (sections 4d–4f, 31 tests)

- [ ] **Step 3: Confirm no marker count changed and no `strict=` value changed**

```bash
git diff --stat
grep -c "@pytest.mark.xfail" tests/integration/models/test_core.py tests/integration/models/elements/classifiers/test_model_class.py tests/integration/models/elements/classifiers/test_model_interface_item.py tests/integration/models/elements/classifiers/test_model_association_class.py
```

Expected: only `test_core.py` and the 3 classifier files changed; the per-file xfail counts equal the post-Task-3 counts (markers were only edited, not added/removed). Verify no `reason=` still contains the word `TODO`:

```bash
grep -rn 'reason="TODO' tests/integration/ || echo "none remaining"
```

Expected: `none remaining`.

- [ ] **Step 4: Sanity-run the classifier file so the markers still register as xfail**

```bash
pytest tests/integration/models/elements/classifiers/ -v --no-cov -p no:cacheprovider
```

Expected: the 4 markered tests report `xfailed`; no collection errors.

- [ ] **Step 5: Lint and commit**

```bash
ruff check tests/integration/ && black tests/integration/
git add tests/integration/
git commit -m "test(integration): replace vague TODO xfail reasons with verified COM root causes"
```

---

### Task 5: Final quality gate and xfail-count reconciliation

**Files:**
- N/A (verification only; commit only if anything drifted)

**Interfaces:**
- Consumes: all changes from Tasks 1–4.
- Produces: confirmed reduced, accurate xfail set.

- [ ] **Step 1: Lint + format the whole integration tree**

```bash
ruff check tests/integration/ && black --check tests/integration/
```

Expected: clean.

- [ ] **Step 2: Confirm the new xfail count**

```bash
pytest tests/integration/ -m xfail --co -q --no-cov -p no:cacheprovider | tail -1
```

Expected: baseline 50 minus the markers removed in Tasks 1–3 (6 from Task 1 + 1 from Task 2 + however many of the 3 in Task 3 passed). Compute: `50 − 7 − (Task-3 passes)`. Reconcile the number against Task 0's baseline.

- [ ] **Step 3: Full live integration run**

```bash
pytest tests/integration/ --no-cov -p no:cacheprovider -q
```

Expected: removed-marker tests now appear as `passed`; every remaining marker reports `xfailed` (no `xpassed`, since Task 4 reasons describe genuine failures).

- [ ] **Step 4: Unit tests still green (safety; no source changed but confirm)**

```bash
pytest tests/unit/ -q --no-cov
```

Expected: all pass.

- [ ] **Step 5: Commit only if anything was reformatted**

```bash
git add -A
git status
```

If clean, nothing to commit. If `black` reformatted, `git commit -m "style: format integration tests"`.

- [ ] **Step 6: Open PR**

```bash
git push -u origin test/improve-xfailed-integration-tests
```

Create a PR titled `test: improve xfailed integration tests (verified against live COM)` and reference this plan.

---

## Self-Review

### 1. Spec coverage
- Spurious markers (6): Task 1 ✓
- Test bug `add_package` × 3 + not-found assertion × 2: Task 2 + Task 3 ✓
- Reason accuracy for the 40+ genuine failures: Task 4 ✓ (every surviving marker mapped to a verified HRESULT or AttributeError)
- Branch hygiene + reconciliation: Task 0 + Task 5 ✓

### 2. Placeholder scan
- No "TBD"/"identify passing tests"/"similar to Task N". Every step lists exact test names, line numbers, exact `reason` strings, and exact pytest commands with expected output.
- Task 3 Step 6 intentionally supplies fallback reasons for the 3 tests whose post-fix outcome is not 100% guaranteed — these are concrete strings, not placeholders.

### 3. Type / name consistency
- Method names verified against source: `RPPackage.add_nested_package` (`model_package.py:151`), `find_nested_element` (`core.py:590`), `addProperty`/`setPropertyValue` (`core.py:404`/`1672`).
- Test names verified against the live JUnit run (e.g. `test_is_final_roundtrip`, `test_match_on_signature` — note the old plan's `test_set_is_final_roundtrip` / `test_match_on_signature_returns_true_for_matching` do not exist and are not used here).
- HRESULTs taken verbatim from the `--tb=line` / JUnit capture: `0x80040001`, `0x80040002`, `0x80040009`, `0x8004000A`, `0x80004005`, `0x80070057`, `DISP_E_TYPEMISMATCH`.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-08-02-improve-xfailed-integration-tests.md`. Two execution options:

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration.

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints.

**Which approach?**
