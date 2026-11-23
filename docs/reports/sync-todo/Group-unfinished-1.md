# Sync todo: `docs/reports` — `Group-unfinished-1` (IRPApplication closeout)

Baseline: 16 committed reports under `docs/reports/com/telelogic/rhapsody/core/` · 1 open row
(Resume = the first row still `[ ]`; a row archives to Group-finished.md only when all 8 steps are `[x]` and its commit exists)
Steps = SKILL.md §1–§8, enumerated per row: ① §1 sync TODO · ② §2 resolve target · ③ §3 compare evidence ·
④ §4 unit tests (TDD) · ⑤ §5 integration tests · ⑥ §6 SWR update · ⑦ §7 RST update · ⑧ §8 verify and report
Per-row binding rules: one pywin32-exposed COM member per call — `call_com(lambda: self._com.Name(...))` for
method-shaped members, `get_com_property`/`set_com_property` for property-shaped members, names confirmed in
`docs/reports/pywin32_authority.json`; catalog-absent sites are blockers, never blind migrations.

- [x] irp_application_api_report (IRPApplication · RhapsodyApplication · application.py · 3 sites)
  - Note: `getProjects`→`projects` property, `getIsHiddenUI`→`isHiddenUI` property, `setHiddenUI` method (catalog); application.py calls `com_utils.*` directly (no AbstractRPModelElement inheritance) — Step 2's package move is N/A (application layer, not a model element wrapper).
  - [x] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [x] Step 2 — §2 resolve target: locate wrapper/exports/tests (package move N/A — application layer, stays at `src/rhapsody_cli/application.py`)
  - [x] Step 3 — §3 compare evidence: baseline `validate_interface.py IRPApplication --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [x] Step 4 — §4 unit tests (TDD): failing fake-COM tests first (`tests/unit/test_application.py`), then migrate the 3 sites; full unit suite green
  - [x] Step 5 — §5 integration tests: add/update integration coverage for owned behavior; Windows = live run, macOS = collection-only noted
  - [x] Step 6 — §6 SWR update: class requirement document `docs/requirements/com/telelogic/rhapsody/core/<snake_case>.md` (moved out of the legacy monolith)
  - [x] Step 7 — §7 RST update: class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPApplication:` + deviation list-table)
  - [ ] Step 8 — §8 verify and report (deviations now 0/0/0 after implementing all 156 backlog members plus the `getPlugInWindow`/`GetPlugInWindow` case-insensitive alias; 13 COM-property-backed members exposed as `@property` with `documented_aliases` entries; unit 100%/100% on 409 statements/358 branches, report regenerated, `validate_interface.py` ✓, `verify_sync.py` ✓, 2118 unit tests ✓, ruff/black/mypy ✓, 38 integration tests collect; OPEN blocker: no live Rhapsody available on this machine, so live execution and the integration-layer-only 100% coverage measurement cannot be performed here)
