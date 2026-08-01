# Integration Test Plans — Java API Cross-Review

**Reviewed:** all 15 per-domain plans in `docs/superpowers/plans/2026-07-14-integration-tests-*.md`
plus `2026-07-13-integration-tests.md`, against `docs/java_api` (authoritative per `AGENTS.md`).
**Date:** 2026-07-26.
**Method:** automated parse of all 1301 wrapper methods (snake_case → camelCase COM call + IRP
class from docstring) verified against `docs/java_api/.../IRP*.html`; plus every method call inside
each plan's `python` code blocks cross-checked against source `def`s; suspects re-verified against
the Java API HTML.

## Bottom line

The plans are **largely sound**. The wrapper layer is **99.6 % faithful** to the Java API (1296/1301
COM calls resolve to a real method on their referenced IRP interface). 12 of the 15 domain plans are
correct as written and will pass (with their documented `xfail`s). **Two plans had real defects that
would have caused test failures when executed**, concentrated entirely in the **containment** plan
(with one ripple into the **activity** plan). The **existing** integration tests (59 `xfail`s, 3687
lines) do **not** reference any of the broken methods — every defect below is plan-only (future work).

> **✅ Status (2026-07-26): PATCHED.** All three 🔴 defects and the checklist typo have been fixed
> in the plan files and `model_project.py` (see "Remediation applied" under each defect). Re-verified:
> zero invented-method calls remain in any plan; all 31 patched Python code blocks parse cleanly;
> `ruff`/`black`/`mypy` pass on the changed source. The 🟡 five `RPPackage` wrappers remain open
> (they need **live** Rhapsody confirmation — cannot be resolved statically).

---

## ✅ Plans verified correct (no action needed)

| Plan | Verdict |
|------|---------|
| `integration-tests-core` | Sound. |
| `integration-tests-classifiers` | Sound. |
| `integration-tests-variables` | Sound. |
| `integration-tests-common` | Sound. |
| `integration-tests-relations` | Sound. |
| `integration-tests-requirements` | **Fully verified** in detail — all 12 methods match source + Java API. |
| `integration-tests-diagrams` | Sound. `add_structure_diagram` correctly handled via generic `add_new_aggr("StructureDiagram", …)` + `xfail` (`getStructureDiagrams` exists on `IRPPackage`; `addStructureDiagram` does not). |
| `integration-tests-statemachine` | Sound. |
| `integration-tests-interactions` | Sound. |
| `integration-tests-values` | Sound. |
| `integration-tests-templates` | Sound. Correctly states no `add_template_*` exists; uses `add_new_aggr("TemplateParameter", …)` + `become_template_instantiation_of(…)` (both backed by real `IRPClass` methods). |
| `integration-tests-graphics` | Sound. |
| `integration-tests-support` | Sound. All 8 `RhapsodyApplication` getters it depends on (`get_search_manager`, `get_selection`, `get_code_gen_simplifiers_registry`, `get_diag_synth_api`, `get_external_checker_registry`, `get_external_ide_registry`, `get_external_roundtrip_invoker`, `get_ow_pane_mgr`) **exist** in `application.py`. |
| `2026-07-13-integration-tests.md` | Sound (conftest design only). |
| `2026-07-21-fix-xfailed-integration-tests.md` | Sound (categorization/cleanup only). |
| `2026-07-14-integration-tests-index.md` | Accurate; its documented `xfail` list matches reality. |

---

## 🔴 Defects that will break tests when executed

### Defect 1 — Containment plan: `RPProject` collaboration task invents methods that don't exist
**Plan:** `2026-07-14-integration-tests-containment.md`, task at line ~434 (`test_collaboration_lifecycle`).
**Calls:** `test_project.add_collaboration(...)`, `get_collaborations()`, `find_collaboration(...)`, `delete_collaboration(...)`.

| Wrapper call | Wrapper exists? | Java API method (`IRPProject`) | Verdict |
|---|---|---|---|
| `add_collaboration` | ❌ no | `addCollaboration` ✅ exists | **Wrapper must be added** before the test can run. |
| `delete_collaboration` | ❌ no | `deleteCollaboration` ✅ exists | **Wrapper must be added.** |
| `get_collaborations` | ❌ no | **none** | Fabricated. Use `getNestedElementsByMetaClass("Collaboration")` (real). |
| `find_collaboration` | ❌ no | **none** | Fabricated. Use `findElementsByFullName(...)` or `findAllByName(...)` (both real on `IRPProject`). |

Only `get_new_collaboration()` (`→ getNewCollaboration`) exists on `RPProject` today.

**Fix:** either (a) add the two missing wrappers (`add_collaboration`, `delete_collaboration`) and
rewrite the get/find parts to use `get_nested_elements_by_meta_class("Collaboration")` /
`find_elements_by_full_name(...)`, or (b) drop the dedicated collaboration lifecycle test and create
via `test_project.add_new_aggr("Collaboration", name)` then iterate `get_nested_elements_by_meta_class`.

> **✅ Remediation applied (option b):** Task `RPProject-B` and all three `RPCollaboration-*` tasks
> in the containment plan now create via `add_new_aggr("Collaboration", name)`, verify membership
> via `get_nested_elements_by_meta_class("Collaboration", 0)`, and clean up via `collab.delete_from_project()`.
> The invented `add_collaboration`/`get_collaborations`/`find_collaboration`/`delete_collaboration`
> were removed from "Methods covered" (now 3 real `RPProject` methods). No new wrapper rows added.

### Defect 2 — Containment plan: `RPProject` find/dirty task invents methods with no Java API basis
**Plan:** `2026-07-14-integration-tests-containment.md`, tasks at line ~483 and ~534.
Both tasks say "*add rows for* …" and propose new wrappers:

| Proposed wrapper | Proposed COM name | Real `IRPProject` method? | Fix |
|---|---|---|---|
| `find_by_name` | `findByName` | ❌ none | `findElementsByFullName` / `findAllByName` |
| `find_by_meta_class` | `findByMetaClass` | ❌ none | `getNestedElementsByMetaClass` |
| `get_is_dirty` / `set_dirty` | `getIsDirty`/`setDirty` | ❌ none — **zero** "dirty" symbols on `IRPProject` | **Remove entirely** — no backing API. Use `isModifiedRecursive` (real) if "modified"-semantics are what's wanted. |

> **✅ Remediation applied:** Task `RPProject-C` dropped the invented `find_by_name`/`find_by_meta_class`
> ("Methods covered" now 6) and rewrote `test_find_by_name_and_guid` → `test_find_element_by_guid_roundtrip`
> using the inherited `get_nested_elements_by_meta_class("Class", 1)`. Task `RPProject-D` dropped
> `get_is_dirty`/`set_dirty` ("Methods covered" now 8) and replaced `test_dirty_flag_roundtrip` with
> `test_is_modified_recursive_returns_bool`. The `pytest -k` filter no longer references "Dirty".

### Defect 3 — Activity plan: stale line reference to a nonexistent method
**Plan:** `2026-07-14-integration-tests-activity.md`, line 56 (creation chain) and line 836 (test body).
States: *"`RPProject.add_collaboration(name)` (… defined in `model_project.py:423`)"* and calls
`test_project.add_collaboration(...)`. **That method does not exist** — `model_project.py:423` is
`find_element_by_file_name`. (See Defect 1.)

**Fix:** replace with `test_project.get_new_collaboration()` (exists → `getNewCollaboration`) or
`test_project.add_new_aggr("Collaboration", name)`.

> **✅ Remediation applied:** both the creation-chain note (line 56) and the `RPActionBlock` test
> body (line 836) now use `test_project.add_new_aggr("Collaboration", name)` (returns `RPCollaboration`
> via the `"Collaboration"` meta-class registration).

---

## 🟡 Wrappers that claim a Java API reference which doesn't exist (MEDIUM)

> **✅ Status (2026-07-26): RESOLVED by removal.** All five wrapper methods (`get_activity_diagrams`,
> `delete_activity_diagram`, `find_nested_package`, `get_associations`, `delete_association`) were
> **deleted** from `model_package.py` along with their unit tests and the corresponding containment-plan
> tasks, applying the same "no Java API backing → remove" rule used for Defects 1–2. Re-verified: the
> cited COM methods remain absent from `IRPPackage.html`; every retained sibling (`addAssociation`,
> `addActivityDiagram`, `addNestedPackage`, `deletePackage`, `getPackages`, `getBehavioralDiagrams`)
> **is** present. `RPCollaboration.get_associations` is unrelated and retained (`getAssociations`
> exists on `IRPCollaboration`).

Five `RPPackage` wrappers reference `IRPPackage` methods that are **absent** from the Java API doc,
while their sibling add/get methods **are** present — so the absence is not a doc artifact:

| Wrapper (`model_package.py`) | COM call | In `IRPPackage` Java API? | Sibling that IS present |
|---|---|---|---|
| `get_activity_diagrams` | `getActivityDiagrams` | ❌ | `addActivityDiagram` ✅ |
| `delete_activity_diagram` | `deleteActivityDiagram` | ❌ | `addActivityDiagram` ✅ |
| `find_nested_package` | `findNestedPackage` | ❌ | `findClass`, `getNestedElements` ✅ |
| `get_associations` | `getAssociations` | ❌ | — |
| `delete_association` | `deleteAssociation` | ❌ | — |

The containment plan tests all five. Per `AGENTS.md` the Java API is authoritative for "does this
method exist on this `IRP*` interface", so these are suspect. They *may* still work against live
Rhapsody (the COM surface is sometimes broader than the Java doc) — they need a live confirmation,
and if they fail should become documented `xfail`s, not silent test failures.

**Secondary issue:** these five methods have **no** in-source `# [x] method … integration test`
checklist rows at all, so they aren't tracked by the parity-checklist system the index relies on.

---

## 🟢 Minor / informational

- **`get_new_collaboration`** (`model_project.py:357`) is implemented (calls `getNewCollaboration`)
  but its checklist row read `[ ] impl` — stale. Flip to `[x] impl`.

> **✅ Fixed:** checklist row in `model_project.py` flipped from `[ ] get_new_collaboration` to
> `[x] get_new_collaboration`.

---

## Verification evidence (reproducible)

```bash
# 1. Wrapper faithfulness: every COM call vs its docstring-referenced IRP class
#    → 1296/1301 resolve; 5 mismatches, all on RPPackage (see 🟡 above)

# 2. Confirm the 5 absent IRPPackage methods (vs present siblings)
python -c "
import re
t=open('docs/java_api/com/telelogic/rhapsody/core/IRPPackage.html',encoding='utf-8').read()
p=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',t))
for m in ['getActivityDiagrams','deleteActivityDiagram','findNestedPackage',
          'getAssociations','deleteAssociation','addActivityDiagram','findClass']:
    print(f'{m:24} {\"FOUND\" if m in p else \"ABSENT\"}')
"

# 3. Confirm IRPProject has NO dirty / findByName / findByMetaClass
python -c "
import re
t=open('docs/java_api/com/telelogic/rhapsody/core/IRPProject.html',encoding='utf-8').read()
p=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',t))
for m in ['isDirty','setDirty','findByName','findByMetaClass',
          'findElementsByFullName','findAllByName','getNestedElementsByMetaClass',
          'addCollaboration','deleteCollaboration','getNewCollaboration']:
    print(f'{m:30} {\"YES\" if m in p else \"no\"}')
"

# 4. Existing tests don't touch any broken method (defects are plan-only)
grep -rnE 'get_activity_diagrams|find_nested_package|get_associations|add_collaboration|get_collaborations|find_collaboration|get_is_dirty|set_dirty|find_by_name\b' tests/integration/
# → no matches
```

## Recommended remediation order

1. ✅ **Defect 3** (activity plan) — swapped `add_collaboration` → `add_new_aggr("Collaboration", …)` in the creation-chain note and the `RPActionBlock` test body.
2. ✅ **Defects 1 & 2** (containment plan) — rewrote the collaboration task (`RPProject-B` + 3 `RPCollaboration-*` tasks) and the find/dirty tasks (`RPProject-C`, `RPProject-D`); removed the fabricated `get_is_dirty`/`set_dirty` and invented `find_by_name`/`find_by_meta_class`/`get_collaborations`/`find_collaboration` entirely.
3. ✅ **🟡 five `RPPackage` wrappers** — **RESOLVED by removal** (see status note under the 🟡 heading above): all five methods, their unit tests, and the containment-plan tasks referencing them were deleted, since the cited `IRPPackage` methods are absent from the Java API doc.
4. ✅ **Minor** — fixed the stale `get_new_collaboration` checklist row.
