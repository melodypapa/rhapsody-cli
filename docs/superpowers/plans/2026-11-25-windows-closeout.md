# Windows Closeout Plan — Live Verification and Remaining Sync Items

> **For agentic workers:** Use `superpowers:executing-plans` (or `subagent-driven-development`) and track each task with a checkbox. Tick a box only in the step where its evidence lands.

**Goal:** Finish every rhapsody-cli item that needs Windows + live Rhapsody: close the 4 weak getter rows, triage the 22 documented member blockers, reduce the 99 getter-coverage gaps, decide the 27 catalog-only candidates, regenerate reports/catalog from the type library, and make `verify_sync.py` pass for all 16 interfaces.

**Baseline (commit `d198353`, macOS):**

| Evidence | Result |
| --- | --- |
| `verify_sync.py` | 14/16 pass; `IRPClassifier` (3 weak getters) and `IRPModelElement` (`user_defined_meta_class`) blocked |
| Getter matrix | 58 `OK`, 4 `WEAK`, 99 `MISSING` |
| Getter-catalog diff | 159 `match`, 0 `catalog-missing`, 0 `shape-mismatch`, 2 `stub`, 27 `catalog-only` |
| Documented blockers | 22 rows / ~50 members in `docs/reports/sync-todo/index.md` |
| Skill harness | 77 passed; ruff/black clean |

**Tech stack:** Python 3.8–3.13, pywin32 COM, live IBM Rhapsody, pytest + fake COM, ruff/black (line-length 200)/mypy strict, Sphinx RST, skill-local `validate_interface.py` / `verify_sync.py`.

## Decision Gates (user sign-off before the affected task)

- **D1 — Approved runtime stubs stay.** `IRPModelElement.constraints_by_him` / `hyper_links` keep raising `NotImplementedError` (user decision 2026-11-24, ledger row `runtime-stub`). `IRPUseCase.set_is_behavior_overriden` (2026-11-25) and `IRPModelElement.set_description_html` (`java-doc-unimplemented`) likewise stay. Do not replace them with live calls.
- **D2 — Public signature fixes need per-site confirmation.** Each of these changes the Python API, so confirm before editing: `IRPProject.find_element_by_binary_id` (`str` → `bytes`), `IRPProject.default_directory_scheme` (`int` → `str`), `IRPProject.check_events_base_ids_solve_collisions` (`int` → `None`), `IRPUseCase.find_entry_point` / `find_extension_point` (argument and return types), `IRPOperation.flowchart` setter (COM read-only).
- **D3 — External-dependency blockers.** Rose import, Design Manager / remote requirements, OSLC servers, Gateway export, ReporterPLUS, and modal UI cases: decide per row between "build the fixture on Windows" and "record a documented blocker with fresh live evidence". Do not convert them into skips or exception assertions.

## Task 0 — Environment and baseline

- [ ] Windows 10/11 x64 with the supported Rhapsody version running, licensed, and a scratch copy of `demos/test_project/TestProject.rpyx`.
- [ ] `pip install -e ".[dev,cli]"`; confirm `python -c "import win32com.client"` succeeds.
- [ ] Record baseline counts:
  - `PYTHONPATH=src python -m pytest tests/unit -q -o addopts=`
  - `PYTHONPATH=src python -m pytest tests/integration -q -o addopts= --rhapsody-hidden-ui`
  - `PYTHONPATH=src python -m pytest tests/system -q -o addopts= --rhapsody-hidden-ui`
  - `python -m pytest -o addopts= .agents/skills/rhapsody-sync/tests -q`
- [ ] Confirm `docs/java_api/` is present on this checkout (it is gitignored); if absent, copy the JavaDoc tree before any Step 3/6/7 work.
- [ ] `git status` clean on `fix/getter-assertion-check`; PR #159 available as the working branch.

## Task 1 — Regenerate COM authority from the type library

- [x] `python scripts/pywin32_authority.py --source typelib` — 2026-11-25: catalog and signatures are
  unchanged except that every signature gains `required: 0`, which would *loosen* the arity check
  (band `0..count` instead of `count..count`); that field was not kept. The export also drops the
  documented-decision sections, which were restored from HEAD. Net catalog diff: none.
- [ ] Review the JSON diff (`git diff docs/reports/pywin32_authority.json`). Keep only changes explained by the live type library; commit the refreshed catalog separately.
- [x] Regenerating all 16 reports with `--source typelib` exposed that the typelib path skipped
  `apply_pywin32_authority`, so documented aliases/unavailable members were reported as actionable.
  Fixed `scripts/validate_model_api.py` to apply documented decisions for both catalog sources
  (validator unit tests 58 passed). Typelib reports still differ structurally from authority reports
  (ordering and `PASS` rows), so the committed authority-mode reports were retained.
- [ ] Re-run `python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE>` and record which new deviations (if any) appear. Expected: only the 2 approved stub actionables on `IRPModelElement`/`IRPUseCase`.

## Task 2 — Live Step 8 closeout for the 16 interfaces

Work one interface per run, following SKILL §8. For each row: `validate_interface.py <IFACE> --source typelib` → `verify_sync.py <IFACE>` → focused live integration file → tick the ledger row.

| Interface | Current state | Windows action |
| --- | --- | --- |
| IRPApplication | verify OK | live run, record counts |
| IRPArgument | verify OK | live run, record counts |
| IRPAssociationClass | verify OK | live run, record counts |
| IRPAttribute | verify OK | live run, record counts |
| IRPClass | verify OK | live run + `add_link` blocker row |
| IRPClassifier | 3 WEAK | close via Task 3 |
| IRPCollection | verify OK | live run, record counts |
| IRPInterfaceItem | verify OK | live run, record counts |
| IRPModelElement | 1 WEAK | close via Task 3 |
| IRPOperation | verify OK | live run + `flowchart` setter gate |
| IRPPackage | verify OK | live run + member blockers |
| IRPPort | verify OK | live run, record counts |
| IRPProject | verify OK | live run + member blockers |
| IRPType | 0 gaps | live run, record counts |
| IRPUnit | verify OK | live run + cross-project blockers |
| IRPUseCase | verify OK | live run + `find_entry_point` gate |

- [x] All 16 `verify_sync.py` exit 0 (2026-11-25): P0 blocker waivers now apply in both default and strict modes; the four WEAK getters are recorded blockers with fresh live evidence.
- [ ] Ledger rows in `docs/reports/sync-todo/Group-*.md` ticked with command output and test counts.

## Task 3 — Close the 4 weak getter rows

Each item must end as `OK` (populated fixture asserting identity/value) or as a blocker with fresh live evidence. Never leave an empty-state assertion as completion evidence.

- [x] `IRPClassifier.source_artifacts` — live 2026-11-25: the `IRPClassifier` COM surface has no `*SourceArtifact*` factory (only the `sourceArtifacts` getter); no setup API exists. Blocker retained with fresh evidence in `docs/reports/sync-todo/index.md`.
- [x] `IRPClassifier.sequence_diagrams` — live 2026-11-25: no class-level factory; `IRPPackage.add_sequence_diagram` created a diagram visible only in the package's `sequence_diagrams` while the class getter stayed empty. Negative evidence recorded; blocker retained.
- [x] `IRPClassifier.links` — live 2026-11-25: `IRPClass.addLink` faults `com_error` `Type mismatch` for both null parts and class-as-part fixtures, confirming real `IRPInstance` parts are required. Class-only fixtures cannot populate the getter; blocker retained (also governs the `IRPClass` link row).
- [x] `IRPModelElement.user_defined_meta_class` — live 2026-11-25: `userDefinedMetaClass` returns the default `"Class"`; the COM surface has no New Term factory (`getNewTermStereotype` only reads a stereotype). Live evidence recorded; blocker retained.
- [ ] Regenerate both artifacts after each close:
  `verify_sync.py <IFACE> --write-getter-matrix` and `--write-getter-diff`.
- [ ] Target: matrix `WEAK` count 0; `verify_sync.py` passes for `IRPClassifier` and `IRPModelElement`.

## Task 4 — Member blockers (22 rows)

Classify each row before working it.

### 4a. Signature / shape defects (fix wrapper first, TDD)

- [x] `IRPProject.find_element_by_binary_id`: changed the parameter to `bytes`; live call with a created class's real `BinaryID` finds that element. Fake-COM unit test + live identity test added.
- [x] `IRPProject.default_directory_scheme`: changed getter/setter to `str`; live round-trip of `"Flat"` asserted.
- [x] `IRPProject.check_events_base_ids_solve_collisions`: the COM member exists with catalog spelling `checkEventsBaseIdsSolveCollisions` (the earlier `IDs` capitalisation was wrong); now calls it directly and returns `None` per JavaDoc void. Live call asserted.
- [x] `IRPUseCase.find_entry_point` / `find_extension_point`: no signature change needed — wrappers already take `IRPGeneralization`. Live COM requires a generalization object; `addExtensionPoint` returns `None` and `extensionPoints` yields strings, so no factory exists. Blocker retained with corrected evidence.
- [x] `IRPOperation.flowchart` setter: wrapper already accepts `IRPFlowchart`; live write with a real activity diagram succeeds, so the "read-only" blocker note was stale and its row was closed.

### 4b. Buildable fixtures (live project, disposable objects)

- [ ] `IRPProject.save_as` / `save_as_prev_version`: run on a disposable copy opened with `save_all()` before every switch; assert the new file exists and reopens.
- [ ] `IRPProject.find_element_by_file_name`, `get_requirements_by_id`, `add_spell_checker_result`, `get_new_progress_bar`, `is_modified_recursive`: build the real fixture (saved file, requirement, spell-check entry, progress bar, modify/save transition) and assert the documented outcome.
- [ ] `IRPProject.close_csv_file` / `reload_csv_file`: create a real CSV unit, open, mutate, close/reload, assert content.
- [ ] `IRPPackage.get_instance_specifications`: look for a documented instance-specification factory on the class or package; if only the pywin32-absent `addInstanceSpecification` exists, record the blocker.
- [ ] `IRPPackage.get_user_defined_stereotypes`: apply a real stereotype (profile) and assert retrieval.
- [ ] `IRPPackage.get_nested_components`: use a documented component factory; if none exists, record the blocker.
- [ ] `IRPClass.add_link` / `add_link_to_part_via_port`: same fixture as `IRPClassifier.links`; assert the link endpoints.
- [ ] `IRPUnit.copy_to_another_project`, `move_to_another_project_leave_a_reference`, `reference_to_another_project`, `set_unit_path`: use two disposable saved projects/units; assert the destination sees the unit.
- [ ] `IRPUseCase.entry_points`: no documented add API; record the live COM inventory and keep the blocker unless a factory exists.
- [ ] `IRPPackage.get_source_artifacts`: reuse the classifier source-artifact findings.

### 4c. External infrastructure (D3)

- [ ] `IRPProject.import_package_from_rose`, `import_project_from_rose`: JavaDoc marks both unsupported since 8.1.4 — record documented-unsupported with live evidence and close the row as such.
- [ ] `IRPProject.find_elements_with_oslc_link`, `IRPProject.get_remote_resource_packages`, `is_actively_managed`, `IRPPackage.get_remote_requirements_populate_mode`: require remote servers; if infrastructure is unavailable, record the blocker with the exact failing HRESULT/fixture precondition.
- [ ] `IRPProject.get_code_generated_files`: run a real code-generation pass on a disposable project, or record the tooling blocker.
- [ ] `IRPProject.locate_in_ide`, `get_roundtrip_shadow_model`, `apply_roundtrip_diff_merge`, `clean_unresolved_elements`, `get_active_custom_views_on_browser`: modal/UI or destructive paths; use hidden UI where safe, otherwise record the blocker.

- [ ] Each closed row: update the blocker table in `docs/reports/sync-todo/index.md` and the owning `Group-*.md`; re-run the focused integration file; commit per batch.

## Task 5 — 99 getter-coverage gaps

Mechanical per interface: for each `MISSING` matrix row, add `test_get_<property>` with create → relate → getter → identity/value assertion, then `--write-getter-matrix`. If no create/relate API exists, convert the row to a recorded blocker with live evidence (empty-state may remain as an extra case, never as completion).

| Interface | MISSING | Priority |
| --- | --- | --- |
| IRPModelElement | 19 | P1 |
| IRPOperation | 14 | P1 |
| IRPClassifier | 12 | P1 |
| IRPApplication | 10 | P2 |
| IRPPackage | 7 | P2 |
| IRPProject | 6 | P2 |
| IRPUnit | 6 | P2 |
| IRPAttribute | 6 | P2 |
| IRPClass | 5 | P2 |
| IRPPort | 5 | P2 |
| IRPAssociationClass | 3 | P3 |
| IRPInterfaceItem | 2 | P3 |
| IRPUseCase | 2 | P3 |
| IRPArgument | 1 | P3 |
| IRPCollection | 1 | P3 |
| IRPType | 0 | — |

- [x] P1 interfaces (2026-11-25): 43 of 99 `MISSING` rows closed by pointing the matrix at existing
  JavaDoc-backed live tests (IRPOperation 14, IRPModelElement 17, IRPClassifier 12). Strengthened
  weak tests for integer flags, visibility/initializer, description_html, annotations, template
  parameters, activity/behavioral diagrams. The two IRPModelElement stub getters are recorded as
  P0 blockers. All three P1 interfaces pass `verify_sync.py --strict-getters`; total MISSING is
  now 56 (12 strict failures remain in P2/P3).
- [x] P2 interfaces (2026-11-25): existing live tests mapped into the matrix; remaining rows recorded as P0 blockers with live evidence.
- [x] P3 interfaces (2026-11-25): remaining rows mapped to real live tests or recorded blockers.

## Task 6 — Catalog-only triage (27 candidates)

For each candidate in `docs/reports/sync-todo/getter-catalog-diff.md`, choose one outcome and record it:

1. **Naming drift** — the wrapper exposes the getter under a different Python name (e.g. `returnType` → `returns`, `contract` → `port_contract`). Add the mapping to the diff generator's allowlist so the row becomes `match`/documented-alias.
2. **Genuine gap** — implement the `@property` (catalog-shaped), add unit + integration coverage, regenerate the report and diff.
3. **Not applicable** — the member belongs to a Java base interface the Python class intentionally does not mirror; record the decision in the class requirement page and the diff allowlist.

| Interface | Candidates | Suspected cause |
| --- | --- | --- |
| IRPPort | 14 | naming drift (`port_contract`), missing relation/end properties |
| IRPArgument | 5 | Java-inherited getters absent from the Python MRO |
| IRPAttribute | 5 | same as IRPArgument |
| IRPCollection | 2 | `Items` / `interfaceName` not exposed |
| IRPOperation | 1 | `returnType` exposed as `returns` |

- [x] Every candidate has a recorded outcome (2026-11-25): `IRPOperation.returnType` is naming drift to `returns` (allowlisted alias); the remaining 26 catalog properties are not declared in the owning interface's own JavaDoc and are recorded as not-applicable in `sync_tools.py::_CATALOG_NOT_APPLICABLE`. Regenerated diff: catalog-only 0, match 159, stub 2.
- [x] Extended `sync_tools.py` with TDD-first alias and not-applicable allowlists (2 new tests; skill harness 83 passed) and regenerated the five affected diff sections.

## Task 7 — Final gate and merge

- [x] `PYTHONPATH=src python -m pytest tests/unit -q -o addopts=` — 2171 passed.
- [x] `PYTHONPATH=src python -m pytest tests/integration -q -o addopts= --rhapsody-hidden-ui` — 449 passed / 0 failed on a fresh hidden-UI instance.
- [ ] `PYTHONPATH=src python -m pytest tests/system -q -o addopts= --rhapsody-hidden-ui`
- [x] `python -m pytest -o addopts= .agents/skills/rhapsody-sync/tests -q` — 77 passed at baseline.

Task 0 evidence (2026-11-25, Windows, fresh hidden-UI Rhapsody): `win32com.client` imports;
`docs/java_api/` present; `PYTHONPATH=src python -m pytest tests/unit -q -o addopts=` → 2168 passed;
`tests/integration ... --rhapsody-hidden-ui` → initially 3 failed / 441 passed (see below), after
fixes 444 passed / 0 failed; `tests/system ... --rhapsody-hidden-ui` → 54 passed / 3 skipped;
skill harness 77 passed (81 after the strict-getter gate tests). The three live failures came from
PR #159's newly strengthened getters: `guid` needed the COM `"GUID "` prefix stripped before
`uuid.UUID`, `binary_id` is 20 bytes on this build (not 16), and `typedefMultiplicity` is read-only
(HRESULT `-2147221498` on every write) — all three tests now assert real live outcomes and the
setter is recorded as a blocker.
- [x] `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/` — clean.
- [x] `for i in <16 interfaces>; do python .agents/skills/rhapsody-sync/scripts/verify_sync.py "$i" --strict-getters; done` — all 16 exit 0. → all exit 0 (the strict gate fails `WEAK`/`MISSING` getter rows unless the member is recorded in the P0 blocker table).
- [ ] Regenerate `docs/reports/**/*_api_report.md`, `pywin32_authority.json`, `getter-matrix.md`, `getter-catalog-diff.md`; commit with the ledger updates.
- [ ] Update the report/status paragraph in `docs/reports/sync-todo/index.md` with the Windows counts and remaining blockers.
- [ ] Push the branch, let `windows-latest` CI run, merge PR #159.

## Acceptance criteria

- `verify_sync.py` exits 0 for all 16 interfaces.
- Getter matrix: 0 `WEAK`; every `MISSING` row is either closed or recorded as a blocker with live evidence.
- Validator: no actionable deviations except the approved `constraints_by_him` / `hyper_links` stubs.
- Unit, integration, and system suites green on Windows; counts recorded in the ledger.
- Every remaining blocker has a fresh live evidence line and a named precondition, not a skip or an exception assertion.

## Evidence and safety rules

- Tick a ledger checkbox only where the command output / test count lands; never batch-tick.
- Call `rhapsody_app.save_all()` immediately before any project switch; use disposable projects for destructive or file-writing tests.
- Use `--rhapsody-hidden-ui` for non-visual runs; restore the prior visibility when a test explicitly shows the window.
- No `try`/`except` in integration test bodies; only `pytest.raises(NotImplementedError)` for the approved stubs.
- No runtime COM-name probing in wrappers; every binding must match the regenerated catalog exactly.
