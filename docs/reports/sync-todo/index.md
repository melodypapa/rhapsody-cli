# Sync todo index — `docs/reports` interface sync (pywin32-direct bindings)

Execution ledger for the 19 committed interface reports under `docs/reports/<java.package.path>/` (`*_api_report.md`; the authority catalog lives at `docs/reports/pywin32_authority.json`) and their wrappers. One row = one report = one rhapsody-sync run, enumerating the steps of [`.agents/skills/rhapsody-sync/SKILL.md`](../../.agents/skills/rhapsody-sync/SKILL.md) (§1–§8).

## At a glance

| Metric | Value |
| --- | --- |
| Interfaces with a committed API report | 19 |
| Group files | 24 |
| Rows tracked | 146 |
| Rows archived | 21 (19 unique + 2 preserved duplicate remediation rows) |
| Rows open | 125 |
| Step checks ticked | 337 / 1168 |
| NotImplementedError evidence rows | 30 |
| P0 blocker rows | 22 (10 interfaces) |
| `verify_sync.py` sweep | 19 / 19 interfaces pass |

## Contents

1. [Layout and group files](#layout-and-group-files)
2. [Resume rule](#resume-rule)
3. [Standing decisions](#standing-decisions)
4. [History](#history)
5. [NotImplementedError stubs](#notimplementederror-stubs) — machine-read by `verify_sync.py`
6. [P0 integration-test blockers](#p0-integration-test-blockers-2026-11-24) — machine-read by `verify_sync.py`
7. [Evidence notes](#evidence-notes)

## Layout and group files

Group files are organized **by category**, where the category is the legacy module subpackage in
each row's path (`elements/<subpackage>/`, `models/support/`, `models/core.py`, `application.py`).
Each group file holds **at most 10 classes**; a category larger than 10 is split into `-1`, `-2`, …
files. Classes whose rows point at canonical post-sync paths (or carry only a remediation label)
were mapped to their legacy category by class name. All 146 tracked rows are preserved.

| Group file | Category | Classes | Status |
| --- | --- | --- | --- |
| [Group-activity-1.md](Group-activity-1.md) | `activity` | 10 | ⬜ 10 open |
| [Group-activity-2.md](Group-activity-2.md) | `activity` | 2 | ⬜ 2 open |
| [Group-application-1.md](Group-application-1.md) | `application` | 1 | ✅ all archived |
| [Group-classifiers-1.md](Group-classifiers-1.md) | `classifiers` | 10 | ⬜ 9 open · ✅ 1 archived |
| [Group-classifiers-2.md](Group-classifiers-2.md) | `classifiers` | 6 | ✅ all archived |
| [Group-common-1.md](Group-common-1.md) | `common` | 7 | ⬜ 6 open · ✅ 1 archived |
| [Group-containment-1.md](Group-containment-1.md) | `containment` | 10 | ⬜ 9 open · ✅ 1 archived |
| [Group-containment-2.md](Group-containment-2.md) | `containment` | 1 | ✅ all archived |
| [Group-core-1.md](Group-core-1.md) | `core` | 7 | ✅ all archived |
| [Group-diagrams-1.md](Group-diagrams-1.md) | `diagrams` | 10 | ⬜ 10 open |
| [Group-diagrams-2.md](Group-diagrams-2.md) | `diagrams` | 2 | ⬜ 2 open |
| [Group-graphics-1.md](Group-graphics-1.md) | `graphics` | 10 | ⬜ 10 open |
| [Group-graphics-2.md](Group-graphics-2.md) | `graphics` | 4 | ⬜ 4 open |
| [Group-interactions-1.md](Group-interactions-1.md) | `interactions` | 10 | ⬜ 10 open |
| [Group-interactions-2.md](Group-interactions-2.md) | `interactions` | 1 | ⬜ 1 open |
| [Group-relations-1.md](Group-relations-1.md) | `relations` | 8 | ⬜ 7 open · ✅ 1 archived |
| [Group-requirements-1.md](Group-requirements-1.md) | `requirements` | 2 | ⬜ 2 open |
| [Group-statemachine-1.md](Group-statemachine-1.md) | `statemachine` | 2 | ⬜ 2 open |
| [Group-support-1.md](Group-support-1.md) | `support` | 10 | ⬜ 10 open |
| [Group-support-2.md](Group-support-2.md) | `support` | 10 | ⬜ 10 open |
| [Group-support-3.md](Group-support-3.md) | `support` | 7 | ⬜ 7 open |
| [Group-templates-1.md](Group-templates-1.md) | `templates` | 3 | ⬜ 3 open |
| [Group-values-1.md](Group-values-1.md) | `values` | 5 | ⬜ 5 open |
| [Group-variables-1.md](Group-variables-1.md) | `variables` | 8 | ⬜ 6 open · ✅ 2 archived |

### Progress

- Progress: **19 unique rows archived / 146** (21 including the two preserved duplicate remediation rows).
- As of 2026-11-25 the `application` row in [Group-application-1.md](Group-application-1.md) and all seven `core` rows in [Group-core-1.md](Group-core-1.md) are archived.
- The queued unsynced classes sit in the remaining files, ordered by importance within each category.
- Commits `6cbebc3` (sync), `1778607` (test-rule compliance), `5175b93` (COM hardening), `2a6334c`…`3479937` (Windows closeout: real-COM outcome enforcement, report regeneration) and the review-fix commit carry the batch.

## Resume rule

1. The `IRPApplication` Step 8 row and the `core` remediation rows are complete.
2. Next take the remaining current-rule remediation rows in their category files (`containment`, `classifiers`, `relations`, `common`, `variables`).
3. Then take the queued rows in the category files once their Windows-side Step 1/3 report regeneration unblocks them.
4. Execute one rhapsody-sync run for that interface following SKILL.md §1–§8 exactly as enumerated in the row's steps.
5. Tick a step when its evidence lands — never batch-tick at the end.
6. Mark the row archived in place only after its commit exists and no step is open.
7. Do not re-derive scope or decisions already recorded in the row's Notes.

## Standing decisions

- **Binding rule (SKILL §3):** every wrapper member calls exactly one pywin32-exposed COM
  member from `pywin32_authority.json` — method-shaped via
  `call_com(lambda: self._com.Name(...))`, property-shaped via `get_com_property` /
  `set_com_property`. No runtime name probing or Java-name fallback; COM names are string
  arguments only. A call site whose member is absent from the catalog for that interface is a
  blocker: leave the site unchanged, record it, never migrate blind.
- **Machine split (2026-11-21):** `docs/java_api/` is gitignored and absent on macOS. There,
  Steps 1–7 are executable (Steps 3/8 use the committed report + catalog as COM evidence, with
  an offline proof substituting for regeneration checks); Step 8's Windows closeout —
  `validate_interface.py <IFACE> --source authority`, `verify_sync.py <IFACE>`, live
  integration run — stays open with the blocker recorded on the row.
- **Canonical package (SKILL §4):** all 15 synced wrappers now live in
  `src/rhapsody_cli/models/com/telelogic/rhapsody/core/` (the application layer stays at
  `src/rhapsody_cli/application.py`); completed rows performed the
  package move (wrapper, imports/exports/registration, unit + integration tests to the
  mirrored `tests/{unit,integration}/models/com/telelogic/rhapsody/core/` paths, snake_case
  test module names, `__init__.py` at every level, no compatibility shim). The canonical
  `__init__.py` uses lazy `__getattr__` exports to keep package import acyclic.
- **Python-only members are removed (SKILL §3/§4, added 2026-11-21):** a wrapper member with
  no static COM member (`PYTHON_ONLY_MEMBER` — facade helpers, unbacked conveniences) is
  deleted from the class during its sync: method, unit tests, integration references,
  checklist row, RST row. Sole exception: documented-unavailable `NotImplementedError` stubs
  for Java members the COM cannot serve (they stay, listed in `documented_unavailable`).
  In-repo callers must be migrated (or the removal blocked) before deletion. Classes synced
  before this rule (IRPClass, IRPModelElement) still carry python-only rows; their removal
  folds into the Step 8 closeout pass before those rows archive.
- **Per-class documents (SKILL §6/§7):** requirement and RST artifacts live at the class's
  package path — `docs/requirements/<java.package.path>/<snake_case>.md` and
  `docs/api/<java.package.path>/<snake_case>.rst` — not in the legacy monoliths
  (`swr_elem_requirements.md`, `elements.rst`). Each run moves its class's entries out of the
  monoliths into the per-class files (no duplicates); `elements.rst` lists per-class pages in
  its toctree. `verify_sync.py` checks the per-class paths strictly (no legacy fallback).
- **COM helper split (merged 2026-11-23):** `models/core.py` now defines the `ComHelper` mixin; `IRPModelElement` inherits it and the canonical wrappers inherit the direct COM helpers from that base. `IRPModelElement.get_rmm_url` remains a documented-unavailable `NotImplementedError` stub (its `getRmmUrl` member is absent from the catalog), not a probe site.
- **Deviation semantics (2026-11-22, review fix):** deviations count **items**, not kinds, and
  Wrapper Backlog rows are deviations. API reports now report
  `- Deviation items: N (actionable a, expected binding differences b, wrapper backlog c)` in
  one line, and `verify_sync.py` includes Wrapper Backlog members in the deviation-member
  coverage it demands from the RST page — an unwrapped-but-COM-supported member is a deviation
  from Java-API parity whose RST row records the "intentionally unsupported" disposition.
  Consequence at closeout: `irp_application.rst` enumerates all 139 IRPApplication backlog
  members (report regenerated offline in authority mode; verify_sync 13/13).
- **Per-class SWR IDs (2026-11-22, review fix):** the 12 per-class requirement documents carry
  unique IDs — the six entries moved out of `swr_elem_requirements.md` kept their original IDs
  (`SWR_ELEM_00001/2/3/6/7/12` → project/package/classifier/operation/attribute/use_case); the
  six new documents took the next free IDs (`SWR_ELEM_00016..00020` → argument/association_class/
  interface_item/port/type, `SWR_CORE_00011` → application, which stays a non-element wrapper in
  the CORE series like `irp_unit`). `traceability_matrix.md` implementation rows point at the
  real current paths; rows mapping `SWR_ELEM_00016..00020` / `SWR_CORE_00011` into the UTS/ITS
  inventory are still to be added when those suites are documented.
- **Category-based groups (2026-11-24):** files are `Group-<category>-N.md`; a category
  larger than 10 classes is split into `-1`, `-2`, … files. Category = legacy module subpackage. None has a committed API report or a catalog entry yet, so
  every row's Step 1/3 starts with regenerating the catalog and report on Windows with Rhapsody;
  JavaDoc HTML for all 10 exists under `docs/java_api/com/telelogic/rhapsody/core/` locally.
- **Full queue coverage (2026-11-22):** every wrapper class in `src/rhapsody_cli/models/` and the
  application layer now has a row in a Group file. Rows are distributed across category
  files, in descending importance within each category. Support-layer wrappers (codegen, files, IDE) are queued
  too; §2 must confirm whether their canonical home is the core package or their current
  `models/support/` location before any move.
- **Termination (pending):** IRPApplication Step 8 and the `core` remediation rows are archived; the remaining remediation rows in other category files are still open. After all of them archive, remove the deprecated `_get_method_or_property` / `_set_method_or_property` definitions from `ComHelper` in `src/rhapsody_cli/models/core.py`, drop legacy notes from `AGENTS.md`, `docs/CODE_GUIDELINES.md`, and the sync skill, and confirm `grep -rn "_method_or_property" src/ --include='*.py'` finds no definitions or call sites.

## History

### 2026-11-24 — Bulk Java-package move

All 113 legacy `RP*` wrapper classes in `models/elements/<domain>/` and `models/support/` were
moved to the canonical Java package path `src/rhapsody_cli/models/com/telelogic/rhapsody/core/` as
`irp_<x>.py` modules, renamed to their Java interface names (`RPState` → `IRPState`), with unit and
integration tests mirrored under `tests/{unit,integration}/models/com/telelogic/rhapsody/core/`,
all imports rewritten, canonical lazy exports rebuilt, and no compatibility shim left behind.
§2 (package move) is therefore ticked on the migrated rows below. §3–§8 remain open where no
committed API report / catalog entry exists (the Windows regeneration blocker); 2157 unit tests
pass, ruff and black are clean, and all 479 integration tests collect.

### 2026-11-24 — Integration-test compliance pass

All mirrored model-wrapper integration tests under `tests/integration/models/**` were audited
against SKILL §5/§8: no non-`NotImplementedError` exception assertions, no `except` handlers or
skip/xfail markers in test bodies, no `assert True`, no literal dummy inputs, and no empty
`finally` cleanup. Fixes: `test_delete_type` now asserts the deleted type is absent instead of
`assert True`; six `IRPType` setter cases now assert real round-trips with authentic values
(`"Enumeration"`, `"int x"`, `"0..1"`, flag `1`); literal `"x"` lookups in `IRPUseCase`/`IRPInterfaceItem`
cases use per-run unique keys; `IRPProject` file-based cases use real on-disk paths (`__file__`,
`tmp_path`) instead of fabricated `"arg"` strings; the project-switch case calls `save_all()`
before `open_project()` and deletes its created package. `verify_sync.py` passes for all 16
interfaces; 472 integration tests collect (live Rhapsody unavailable on macOS). Open blockers:
`cg_simplified_model_package` has no live populated fixture, and Gateway export / ReporterPLUS
generation require external tools — recorded on the respective rows.

### 2026-11-22 — Report/status refresh and review-fix pass

Figures below are as of that date and are kept for the decision record.

Report/status refresh (2026-11-22, after the second review-fix pass on top of the Windows
closeout): unit suite **1947 passed**, integration + system suites **504 collected** (live
re-run pending on Windows), skill self-tests **22 passed**; ruff/black/mypy clean; an AST
cross-check proves zero catalog-absent COM members and zero legacy probe call sites across the
16 canonical wrappers, and `verify_sync.py` passes for **all 13 interfaces**. All 15
synced wrappers reach 100% statement/branch coverage independently at both unit and integration
layers, with zero skip/xfail markers.

`close_all_projects()` and `get_rhapsody_dir()` were removed from `RhapsodyApplication` in the
review-fix pass: both were `PYTHON_ONLY_MEMBER` conveniences whose COM members do not exist
(the Windows-authored integration tests had pinned their `AttributeError` as the live outcome,
and the teardown call only "succeeded" because it swallowed that error with a printed warning).
The integration teardown now closes each open project through the catalog-exposed
`IRPProject.close()` member; `connect`/`disconnect` remain as documented python-only facade
helpers (live callers throughout the codebase, so their removal stays blocked per the standing
decision).

### 2026-11-25 — Getter-assertion checker tightening

`verify_sync.py` now groups `test_<property>`, `test_get_<property>`, and their `_empty`/`_empty_state`
variants under the same property and fails Step 8 unless at least one test in the group asserts
identity/value (a weak empty-state test is accepted only beside a populated sibling). This makes the
previously unscanned `test_get_*` tests visible. `IRPType`'s four getters and `IRPModelElement`'s
`association_classes`, `references`, `guid`, and `binary_id` were fixed with JavaDoc-backed populated
fixtures. IRPClassifier's populated fixtures for `source_artifacts`, `sequence_diagrams`, and `links`
were verified live on 2026-11-26 via the documented inherited `add_new_aggr` factory, closing its three
getter blockers. `IRPModelElement.user_defined_meta_class` remains an open getter blocker until a
Windows + Rhapsody run settles its fixture.

The same pass replaced 21 `assert pkg.add_* (...) is not None` factory checks in `test_irp_package.py`
and the `add_package`/`add_component`/`add_profile` checks in `test_irp_project.py` with name-identity
assertions, and removed the remaining literal `"arg"` fixture prefixes from the integration tests.

Step 8 now also validates the machine-readable Getter fixture matrix at
`docs/reports/sync-todo/getter-matrix.md`: every interface section must exist, hold one row per owned
wrapper property, use a known assertion/status pair, and reference an integration test that still
exists. Regenerate a section with `verify_sync.py <INTERFACE> --write-getter-matrix`. The seed run
records 58 `OK`, 4 `WEAK`, and 99 `MISSING` rows; `MISSING` marks getters whose test is not
discoverable by the `test_<property>`/`test_get_<property>` convention (for example `ports` is covered
by `test_add_port_and_get_ports`) and must be pointed at the real test by hand.

### 2026-11-26 — Getter matrix and stub evidence completed

- Added the Getter fixture matrix sections for `IRPActor` (1 row, OK), `IRPStatechart` (5 rows, OK), and `IRPStereotype` (2 OK, `icon` MISSING) with `verify_sync.py <INTERFACE> --write-getter-matrix`.
- Added four `not-exposed` stub evidence rows (`IRPActor.addEventReceptionWithEvent`, `updateContainedDiagramsOnServer`; `IRPStatechart.addNewAcceptEventAction`, `addNewAcceptTimeEvent`) after confirming each member is absent from the catalog, listed in `documented_unavailable`, and asserted in both mirrored test layers.
- Recorded `IRPStereotype.icon` as a P0 blocker: no documented API attaches or edits a stereotype icon.
- Result: all 19 interfaces pass the default sweep, and `IRPActor`, `IRPStatechart`, `IRPStereotype` also pass `--strict-getters`.

## NotImplementedError stubs

Added 2026-11-25. `verify_sync.py` reads this table for every interface wrapper and fails Step 8 unless every
`NotImplementedError` stub has one row whose basis matches the committed COM evidence:

- `not-exposed` — the Java member is absent from `docs/reports/pywin32_authority.json` and listed
  in `documented_unavailable`; the stub raises before any COM dispatch (SKILL §4).
- `java-doc-unimplemented` — JavaDoc itself declares the member "Not implemented"; the catalog may
  expose a property, but the Java API forbids its use.
- `runtime-stub` — pywin32 exposes the member, the documented call is proven ineffective, and the
  user approved the deviation on the recorded date; the wrapper and test docstrings cite the
  JavaDoc member, the catalog entry, and the live evidence (SKILL §4/§5).

Each stub must also be asserted as `pytest.raises(NotImplementedError)` in both mirrored test
layers. A row whose member no longer raises is stale and fails Step 8.

| Interface | Python member | COM member | Basis | Evidence | Approved |
| --- | --- | --- | --- | --- | --- |
| IRPActor | `add_event_reception_with_event` | `addEventReceptionWithEvent` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPActor | `update_contained_diagrams_on_server` | `updateContainedDiagramsOnServer` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPComponent | `get_path` | `getPath` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPComponent | `set_path` | `setPath` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPComponent | `update_contained_diagrams_on_server` | `updateContainedDiagramsOnServer` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPConfiguration | `get_path` | `getPath` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPConfiguration | `set_path` | `setPath` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPClass | `is_abstract` | `isAbstract` | not-exposed | The setter's `setIsAbstract` is absent from the catalog and listed in `documented_unavailable`; the `isAbstract` property accepts the write but never persists it (observed live). | — |
| IRPClass | `add_event_reception_with_event` | `addEventReceptionWithEvent` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPClass | `update_contained_diagrams_on_server` | `updateContainedDiagramsOnServer` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPCollection | `to_list` | `toList` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPModelElement | `constraints_by_him` | `constraintsByHim` | runtime-stub | Java API documents it as internal-only; the user's explicit decision on 2026-11-24 keeps the stub before COM dispatch. | 2026-11-24 |
| IRPModelElement | `hyper_links` | `hyperLinks` | runtime-stub | Live retrieval could not be established through the documented APIs; the user's explicit decision on 2026-11-24 keeps the stub before COM dispatch. | 2026-11-24 |
| IRPModelElement | `get_rmm_url` | `getRmmUrl` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPModelElement | `set_description_html` | `descriptionHTML` | java-doc-unimplemented | JavaDoc: "Not implemented - should not be used." | — |
| IRPOperation | `update_contained_diagrams_on_server` | `updateContainedDiagramsOnServer` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPPackage | `add_instance_specification` | `addInstanceSpecification` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPPackage | `get_root_instance_specifications` | `getRootInstanceSpecifications` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPPackage | `login_to_remote_artifact_server` | `loginToRemoteArtifactServer` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPPackage | `update_contained_diagrams_on_server` | `updateContainedDiagramsOnServer` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPPackage | `update_contained_matrices_on_server` | `updateContainedMatricesOnServer` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPPackage | `update_contained_tables_on_server` | `updateContainedTablesOnServer` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPPort | `get_contract` | `getContract` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPPort | `set_contract` | `setContract` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPProject | `enable_rhapsody_model_manager` | `enableRhapsodyModelManager` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPProject | `migrate_design_manager_links` | `migrateDesignManagerLinks` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPProject | `is_resolve_on_demand` | `isResolveOnDemand` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPProject | `set_global_configuration` | `setGlobalConfiguration` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPProject | `set_resolve_on_demand` | `setResolveOnDemand` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPStatechart | `add_new_accept_event_action` | `addNewAcceptEventAction` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPStatechart | `add_new_accept_time_event` | `addNewAcceptTimeEvent` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPUnit | `get_unit_path` | `getUnitPath` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPUseCase | `add_event_reception_with_event` | `addEventReceptionWithEvent` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPUseCase | `set_is_behavior_overriden` | `isBehaviorOverriden` | runtime-stub | `setIsBehaviorOverriden` is absent from the catalog; the `isBehaviorOverriden` property is readable, but writes do not work for use cases (the IRPActor/IRPClass setters do); observed live; user approved on 2026-11-25. | 2026-11-25 |
| IRPUseCase | `update_contained_diagrams_on_server` | `updateContainedDiagramsOnServer` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPInstance | `get_all_nested_elements` | `getAllNestedElements` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPInstance | `update_contained_diagrams_on_server` | `updateContainedDiagramsOnServer` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPDependency | `is_need_to_migrate` | `isNeedToMigrate` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |
| IRPDependency | `set_link_type` | `setLinkType` | not-exposed | Absent from the catalog; listed in `documented_unavailable`. | — |

`IRPCollection.add_graphical_item` had a `not-exposed` row here until 2026-11-25, when a live
probe proved the pywin32 `addGraphicalElementItem` alias works with a real `IRPGraphElement`
(SWR_ELEM_00036). The wrapper now forwards to that member, so the stub row was removed; a row
for a member that no longer raises `NotImplementedError` fails Step 8 as stale.

## P0 integration-test blockers (2026-11-24)

The following integration tests were removed rather than converted into exception assertions or skips
(SKILL §5: a genuine blocker keeps the row open). Each item needs a Windows + Rhapsody run or a
wrapper-signature fix before its getter/member row can close.

| Interface | Member(s) | Blocker |
| --- | --- | --- |
| IRPProject | `save_as`, `save_as_prev_version` | Writes/switches the session-shared project file; cannot be exercised safely in the shared live project. |
| IRPProject | `find_element_by_file_name`, `locate_in_ide`, `apply_roundtrip_diff_merge`, `get_roundtrip_shadow_model`, `clean_unresolved_elements` | Binding now matches COM, but no safe live fixture (known file name, UI focus, shadow model, or destructive cleanup). |
| IRPProject | `close_csv_file`, `reload_csv_file`, `find_elements_with_oslc_link`, `add_spell_checker_result`, `get_requirements_by_id`, `get_new_progress_bar` | Binding now matches COM; still needs a CSV/OSLC/requirement/progress fixture or a meaningful assertion for a void result. |
| IRPProject | `import_package_from_rose`, `import_project_from_rose` | External Rose fixture required; JavaDoc marks both unsupported since Rhapsody 8.1.4. |
| IRPPackage | `get_remote_requirements_populate_mode` | A local live probe set the documented mode to `"None"` but the getter returned `""`; a valid populated value requires a Design Manager/remote requirements server. |
| IRPClass | `add_link`, `add_link_to_part_via_port` | Needs a real `IRPInstance` part and structure-diagram endpoints; class-as-part fixtures only produced exceptions. |
| IRPModelElement | `user_defined_meta_class` (`getUserDefinedMetaClass`) | JavaDoc defines the result as the New Term name, but the COM surface exposes no API to define a New Term, so only the default value's type is observable; evidence: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_user_defined_meta_class`. |
| IRPModelElement | `constraints_by_him`, `hyper_links` | User-approved runtime stubs (2026-11-24, `runtime-stub` rows in the NotImplementedError evidence ledger); retrieval fixtures could not be built live. |
| IRPUnit | `copy_to_another_project`, `move_to_another_project_leave_a_reference`, `reference_to_another_project`, `set_unit_path` | Requires a second saved project/unit file and mutates the shared project. |
| IRPType | `typedef_multiplicity` setter | Live 2026-11-25: the catalog exposes `typedefMultiplicity` as a property and reads return `"1"` on a new type, but every write (`"0..1"`, `"1"`, `"0..*"`, `"*"`, `"[0..1]"`, `"1..1"`) faults with COM HRESULT `-2147221498`; no live setter success, so the getter asserts the observed default and the setter stays a blocker. |
| IRPUseCase | `entry_points` | No documented add API in the COM surface; only an empty-state result is observable. |
| IRPStereotype | `icon` | No documented API attaches or edits a stereotype icon; the getter returns the image path declared by the stereotype definition file, so no populated live fixture exists. |
| IRPProject | `get_code_generated_files` | Requires a real code-generation run; no safe fixture in the shared project. |
| IRPProject | `get_remote_resource_packages`, `is_actively_managed` | Require a remote resource/management server. |
| IRPProject | `active_component`, `active_configuration`, `set_active_component`, `set_active_configuration` | The wrapper now follows pywin32's string setter signatures. This Rhapsody build still faults on getter/setter calls (HRESULT `0x80040005`/`0x80040006`) even with valid names; no successful live value or safe round-trip is available. |
| IRPProject | `cg_simplified_model_package` | The live project returns `None`; JavaDoc and COM expose no setter/factory to establish a populated simplified-model package. Keep the empty-state case weak and the getter row open. |
| IRPApplication | `add_profile_to_model` | Needs a real installed profile name on Windows; `"0"` is an unverified profile index and the model-level addition has no cleanup API. Evidence: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_add_profile_to_model`. |
| IRPProject | `is_modified_recursive` | Needs a controlled modify/save transition on the session-shared project. |
| IRPProject | `move_to_design_manager`, `move_to_design_manager_after_login` | Both JavaDoc methods are deprecated because Design Manager support was removed in Rhapsody 8.4; no supported Design Manager server is available for authentic live execution. Keep the exact catalog bindings and leave live verification open. |
| IRPClass | `is_abstract`, `is_active`, `is_behavior_overriden` | Documented pywin32 aliases; getters are readable but no populated live fixture exists (setters are read-only or JavaDoc-unimplemented). |
| IRPPort | `is_behavioral`, `is_reversed`, `port_contract`, `provided_interfaces`, `required_interfaces` | Port relation/end properties have no live factory; recovered via catalog-only triage but no populated fixture. |
| IRPComponent | `panel_diagrams` | No documented API attaches a panel diagram to a component; only the empty collection is observable. |
| IRPComponent | `variation_points` | No documented API creates a variation point on a component; only the empty collection is observable. |
| IRPCollaboration | `activation_condition` | No documented API populates this read-only property on a fresh collaboration; only the documented empty/default state is observable. |
| IRPCollaboration | `activation_mode` | No documented API populates this read-only property on a fresh collaboration; only the documented empty/default state is observable. |
| IRPCollaboration | `associations` | No documented API populates this read-only property on a fresh collaboration; only the documented empty/default state is observable. |
| IRPCollaboration | `classifier` | No documented API populates this read-only property on a fresh collaboration; only the documented empty/default state is observable. |
| IRPCollaboration | `execution_occurrences` | No documented API populates this read-only property on a fresh collaboration; only the documented empty/default state is observable. |
| IRPCollaboration | `interaction_occurrences` | No documented API populates this read-only property on a fresh collaboration; only the documented empty/default state is observable. |
| IRPCollaboration | `interaction_operators` | No documented API populates this read-only property on a fresh collaboration; only the documented empty/default state is observable. |
| IRPCollaboration | `message_points` | No documented API populates this read-only property on a fresh collaboration; only the documented empty/default state is observable. |
| IRPCollaboration | `mode` | No documented API populates this read-only property on a fresh collaboration; only the documented empty/default state is observable. |
| IRPConfiguration | `additional_sources` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `all_elements_in_instrumentation_scope` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `build_set` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `compiler_switches` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `generate_code_for_actors` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `include_path` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `initial_instances` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `initialization_code` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `instrumentation_scope` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `instrumentation_type` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `libraries` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `link_switches` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `scope_type` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `standard_headers` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `statechart_implementation` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPConfiguration | `time_model` | No documented API populates this read-only configuration property on a fresh configuration; only the documented empty/default state is observable. |
| IRPProject | `nodes` | `nodes` is inherited from `IRPPackage`; the project root rejects both `addNode(name)` and `addNewAggr("Node", name)`, and a nested-package node is not returned by `project.nodes`. No populated project-root fixture is available. |
| IRPUseCase | `is_behavior_overriden` | Runtime stub (user approved 2026-11-25): setter faults live; see the NotImplementedError evidence ledger. |

## Evidence notes

**Fresh live evidence (2026-11-25, hidden-UI Rhapsody):** three of the original four WEAK getter
rows were closed by attaching children with the documented generic factory
`IRPModelElement.add_new_aggr` directly on the classifier — `add_new_aggr("File")`,
`add_new_aggr("SequenceDiagram")` and `add_new_aggr("Link")` each produce a child that the
corresponding `source_artifacts` / `sequence_diagrams` / `links` getter returns by identity
(`test_source_artifacts`,
`test_sequence_diagrams`,
`test_links`). Earlier probes of the specialized factories
(`addLink`, `add_sequence_diagram`) failed, but the generic factory is sufficient. The remaining
`IRPModelElement.userDefinedMetaClass` row stays a blocker: it returns the default `"Class"` and the
surface has no New Term factory (`getNewTermStereotype` only reads a stereotype); its empty-state
test is an additional case, not completion evidence.

**D2 signature cases (2026-11-25, approved case-by-case):** `IRPProject.find_element_by_binary_id`
now takes `bytes` (live COM requires a VT_UI1 SAFEARRAY and finds the real element);
`default_directory_scheme` now reads/writes `str` (live values `"Flat"`/`"Nested"`);
`check_events_base_ids_solve_collisions` now calls the exact catalog spelling
`checkEventsBaseIdsSolveCollisions` and returns `None` (the earlier probe used the wrong
capitalisation, `IDs` instead of `Ids`). All three have fake-COM unit tests and live identity/value
assertions, so their blocker rows are closed. `IRPUseCase.find_entry_point` /
`find_extension_point` already take `IRPGeneralization` (the old note was stale); no live factory
returns a generalization, so the rows stay blockers with corrected evidence. `IRPOperation.flowchart`
already has an `IRPFlowchart` setter and writing a real flowchart object succeeds live, so that
blocker row is closed.
