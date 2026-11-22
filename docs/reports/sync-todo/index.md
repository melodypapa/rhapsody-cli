# Sync todo index — `docs/reports` interface sync (pywin32-direct bindings)

Execution ledger for the 16 committed interface reports under `docs/reports/<java.package.path>/`
(`*_api_report.md`; the authority catalog remains at `docs/reports/pywin32_authority.json`) and their wrappers. One row = one report = one rhapsody-sync run; every row's steps enumerate
the rules and steps of [`.agents/skills/rhapsody-sync/SKILL.md`](../../.agents/skills/rhapsody-sync/SKILL.md)
(§1–§8). Runs tick a step the moment it passes; rows archive to `Group-finished.md` only when
all eight steps pass and the run's commit exists.

## Layout (2026-11-22)

API reports are grouped by their declared Java package; the current core reports live in
`docs/reports/com/telelogic/rhapsody/core/`. One open row (IRPApplication Step 8) lives in [Group-unfinished-1.md](Group-unfinished-1.md), and the
10 highest-importance unsynced classes are queued in [Group-unfinished-2.md](Group-unfinished-2.md),
the remaining 103 in [Groups 3–13](Group-unfinished-3.md) (10 per group, importance-ordered);
completed rows
archive to [Group-finished.md](Group-finished.md) (a batch file is deleted when its last row
archives). Queue order: core.py base classes first (their migration removes the inherited
dual-binding fallback for every subclass), then leaves.

| Batch file | Rows | Legacy sites | Interface span | Status |
| --- | --- | --- | --- | --- |
| [Group-unfinished-1.md](Group-unfinished-1.md) | 1 | 3 | IRPApplication closeout | ⬜ 1 open (Step 8 only) |
| [Group-finished.md](Group-finished.md) | 15 | ~219 | IRPClass → IRPModelElement | ✅ 15 archived |
| [Group-unfinished-2.md](Group-unfinished-2.md) | 10 | ~133 | IRPState → IRPCollaboration | ⬜ 10 open (new) |
| [Group-unfinished-3.md](Group-unfinished-3.md) | 10 | ~104 | IRPSearchQuery → IRPFile | ⬜ 10 open |
| [Group-unfinished-4.md](Group-unfinished-4.md) | 10 | ~36 | IRPVariable → IRPEventReception | ⬜ 10 open |
| [Group-unfinished-5.md](Group-unfinished-5.md) | 10 | ~27 | IRPActor → IRPSendAction | ⬜ 10 open |
| [Group-unfinished-6.md](Group-unfinished-6.md) | 10 | ~13 | IRPInternalOEMPlugin → IRPPin | ⬜ 10 open |
| [Group-unfinished-7.md](Group-unfinished-7.md) | 10 | ~25 | IRPPlugInWindow → IRPInstanceSpecification | ⬜ 10 open |
| [Group-unfinished-8.md](Group-unfinished-8.md) | 10 | ~14 | IRPInstanceSlot → IRPGraphicalProperty | ⬜ 10 open |
| [Group-unfinished-9.md](Group-unfinished-9.md) | 10 | ~13 | IRPExternalIDERegistry → IRPTimingDiagram | ⬜ 10 open |
| [Group-unfinished-10.md](Group-unfinished-10.md) | 10 | ~7 | IRPCodeGenSimplifiersRegistry → IRPDeploymentDiagram | ⬜ 10 open |
| [Group-unfinished-11.md](Group-unfinished-11.md) | 10 | ~4 | IRPComponentDiagram → IRPExternalRoundtripInvoker | ⬜ 10 open |
| [Group-unfinished-12.md](Group-unfinished-12.md) | 10 | ~0 | IRPASCIIFile → IRPStructureDiagram | ⬜ 10 open |
| [Group-unfinished-13.md](Group-unfinished-13.md) | 3 | ~0 | IRPExtensionPoint → IRPIntegrator | ⬜ 3 open |

Progress: **15/129 rows tracked as archived** (128 wrapper classes + 1 application layer;
10 queued in Group-unfinished-2, 103 in Groups 3–13). All 13 rows from
Group-unfinished-1 reached 8/8 except
IRPApplication, whose Step 8 stays open on integration layer-only coverage (44.68%). Commits
`6cbebc3` (sync), `1778607` (test-rule compliance), `5175b93` (COM hardening), `2a6334c`…`3479937`
(Windows closeout: real-COM outcome enforcement, report regeneration) and the review-fix commit
(this one) carry the batch.

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

## Resume rule

Take the first row still `[ ]` in queue order: the open IRPApplication Step 8 row in
[Group-unfinished-1.md](Group-unfinished-1.md), then the queued rows in
[Group-unfinished-2.md](Group-unfinished-2.md) through [Group-unfinished-13.md](Group-unfinished-13.md)
(once their Windows-side Step 1/3 report regeneration unblocks them). Execute one rhapsody-sync
run for that
interface following SKILL.md §1–§8 exactly as enumerated in the row's steps; tick a step when
its evidence lands (never batch-tick at the end); move the row to
[Group-finished.md](Group-finished.md) only after its commit exists and no step is open. Do
not re-derive scope or decisions already recorded in the row's Notes.

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
- **core.py base rows (revised user decision 2026-11-21):** the earlier deferral is lifted —
  the only cycle risk was a module-level import of a moved class back into `models/core.py`.
  With `from __future__ import annotations` already in `core.py`, annotations never evaluate at
  runtime (quoted types are therefore unnecessary); a runtime `cast()` target imports locally
  inside the method, the pattern already used at `core.py:314` for `IRPAssociationClass`. A
  moved class imports its bases from `core.py` one-way, so each base row does the full §2 move
  in its own run and `verify_sync.py` can go green.
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
- **core.py split (complete):** `models/core.py` now holds only `AbstractRPModelElement`; the
  forwarder definitions are gone and every sync row has moved its class to the canonical core
  package. `IRPModelElement.get_rmm_url` is a documented-unavailable `NotImplementedError` stub
  (its `getRmmUrl` member is absent from the catalog), not a probe site.
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
- **Group-unfinished-2 (2026-11-22):** the 10 highest-importance / most-used unsynced model
  classes are queued in one batch. None has a committed API report or a catalog entry yet, so
  every row's Step 1/3 starts with regenerating the catalog and report on Windows with Rhapsody;
  JavaDoc HTML for all 10 exists under `docs/java_api/com/telelogic/rhapsody/core/` locally.
- **Full queue coverage (2026-11-22):** every wrapper class in `src/rhapsody_cli/models/` and the
  application layer now has a row in a Group file. Groups 3–13 hold the lower-importance
  remainder in descending usage order. Support-layer wrappers (codegen, files, IDE) are queued
  too; §2 must confirm whether their canonical home is the core package or their current
  `models/support/` location before any move.
- **Termination (pending):** only IRPApplication's Step 8 is open. After it archives, delete
  `_get_method_or_property` / `_set_method_or_property` from `com_utils.py` / `core.py` (all
  wrapper call sites are gone as of the 2026-11-22 review fix — only the definitions remain), drop the legacy notes from
  `AGENTS.md`, `docs/CODE_GUIDELINES.md`, and the sync skill, and confirm
  `grep -rn "_method_or_property" src/ --include='*.py'` finds only the deleted definitions.
