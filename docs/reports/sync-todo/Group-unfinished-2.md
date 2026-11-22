# Sync todo: `docs/reports` — `Group-unfinished-2` (IRPState → IRPCollaboration)

Baseline: 2026-11-22 survey of all wrapper classes not covered by Group-finished (15 rows) or
Group-unfinished-1 (IRPApplication). 10 open rows · one group · ordered by **importance** (how
central the element is to Rhapsody models) and **use frequency** (references in `src/` then
`tests/`), with base classes ahead of their subclasses where a base is in scope.

(Resume = the first row still `[ ]`; a row archives to [Group-finished.md](Group-finished.md)
only when all eight steps are `[x]` and its commit exists.)

## Why these 10 (survey evidence)

| # | Interface (legacy facade) | src refs | test refs | owned methods | legacy sites | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | IRPState (RPState) | 234 | 99 | 48 | 28 | Highest-use unsynced class; state-machine behaviour is central to Rhapsody models. |
| 2 | IRPComponent (RPComponent) | 118 | 29 | 43 | 17 | Core structural element; blocks clean component/package navigation. |
| 3 | IRPInstance (RPInstance) | 118 | 69 | 13 | 6 | Base of parts/ports; inherits `RPRelation` (row 4) — sync that first. |
| 4 | IRPRelation (RPRelation) | 108 | 47 | 31 | 27 | Base relation type; 27 legacy sites removed by this row's move. |
| 5 | IRPFlow (RPFlow) | 107 | 59 | 17 | 4 | Activity-flow element used across diagrams and operations. |
| 6 | IRPStatechart (RPStatechart) | 97 | 14 | 31 | 10 | Behavioural container; already extends the synced `IRPClass`. |
| 7 | IRPDiagram (RPDiagram) | 84 | 14 | 33 | 2 | Base diagram type; most diagram-specific wrappers derive from it. |
| 8 | IRPMessage (RPMessage) | 44 | 48 | 36 | 32 | Interaction core; 32 legacy sites make the cleanup high-value. |
| 9 | IRPTableLayout (RPTableLayout) | 122 | 14 | 50 | 5 | High-frequency graphics helper despite narrow domain; 50 owned members. |
| 10 | IRPCollaboration (RPCollaboration) | 77 | 11 | 39 | 1 | Common containment wrapper; completes the high-use set. |

Excluded deliberately: stale legacy copies of already-synced interfaces (`IRPType`,
`IRPUseCase`, `IRPAttribute`, `IRPArgument` still present in old modules); support-layer
utilities with no model semantics (`RPSearchQuery`, `RPowPaneMgr`, …); and diagram leaf
classes with zero owned methods (`RPComponentDiagram`, `RPPanelDiagram`, …).

## Prerequisites (blocking for every row)

None of these 10 interfaces is present in `docs/reports/pywin32_authority.json` and none has a
committed `*_api_report.md`. Per SKILL §3, Step 3 cannot begin with offline evidence until each
report exists. On a machine with Rhapsody:

```bash
python scripts/pywin32_authority.py --source typelib          # extend the catalog
python scripts/validate_model_api.py <IFACE> --source typelib --path docs/reports
```

JavaDoc is available locally at `docs/java_api/com/telelogic/rhapsody/core/<IFACE>.html` for all
10 (gitignored; absent on other machines). If the catalog/report cannot be regenerated, record
the blocker on the row and stop — never migrate a member absent from the catalog.

Steps = SKILL.md §1–§8, enumerated per row: ① §1 sync TODO · ② §2 resolve target · ③ §3 compare
evidence · ④ §4 unit tests (TDD) · ⑤ §5 integration tests · ⑥ §6 SWR update · ⑦ §7 RST update ·
⑧ §8 verify and report. Each row's Step 1 must publish a subtask for every target-owned JavaDoc
member before any edit.

Per-row binding rules: one pywin32-exposed COM member per call —
`call_com(lambda: self._com.Name(...))` for method-shaped members,
`get_com_property`/`set_com_property` for property-shaped members, names confirmed in
`docs/reports/pywin32_authority.json`; catalog-absent sites are blockers, never blind
migrations. Canonical package: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/` with mirrored
`tests/{unit,integration}/models/com/telelogic/rhapsody/core/test_<snake>.py`; class and module
names follow the Java interface (`IRPState` → `irp_state.py`), no compatibility shim.

- [ ] irp_state_api_report (IRPState · RPState · elements/statemachine/model_statemachine.py · 28 legacy sites)
  - Note: highest-use unsynced wrapper (234 src / 99 test references, 48 owned methods). Depends on `RPStateVertex` (stays in the legacy module); inherited members wait for a future base row. Sync after the catalog/report prerequisite above.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate the committed report + catalog entry; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy helper sites in own methods; full unit suite green
  - [ ] Step 5 — §5 integration tests: add/update integration coverage for owned behavior in the mirrored test path; Windows = live run
  - [ ] Step 6 — §6 SWR update: per-class requirement document `docs/requirements/com/telelogic/rhapsody/core/irp_state.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `docs/api/com/telelogic/rhapsody/core/irp_state.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit and integration suites (new no-regression rule) + ruff/black/mypy; render the sync-report checklist

- [ ] irp_component_api_report (IRPComponent · RPComponent · elements/containment/model_component.py · 17 legacy sites)
  - Note: core structural element (118 src / 29 test, 43 owned methods). Extends the synced `IRPUnit`, so this is a leaf-style migration with no base-class dependency.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_component.md`
  - [ ] Step 7 — §7 RST update: `irp_component.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate

- [ ] irp_instance_api_report (IRPInstance · RPInstance · elements/relations/model_instance.py · 6 legacy sites)
  - Note: base of parts/ports (118 src / 69 test). Inherits `RPRelation` — finish row 4 first, then treat inherited members as setup only per the integration ownership rule.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_instance.md`
  - [ ] Step 7 — §7 RST update: `irp_instance.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate

- [ ] irp_relation_api_report (IRPRelation · RPRelation · elements/relations/model_relation.py · 27 legacy sites)
  - Note: foundational relation type (108 src / 47 test, 31 owned methods). Do this before IRPInstance; 27 legacy sites make it the highest cleanup value in this group.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_relation.md`
  - [ ] Step 7 — §7 RST update: `irp_relation.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate

- [ ] irp_flow_api_report (IRPFlow · RPFlow · elements/activity/model_activity.py · 4 legacy sites)
  - Note: activity-flow element (107 src / 59 test) shared by operations, diagrams and statecharts. Module also defines `RPFlowchart`/`RPFlowItem`/`RPObjectNode` — migrate only the row's class; siblings stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_flow.md`
  - [ ] Step 7 — §7 RST update: `irp_flow.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate

- [ ] irp_statechart_api_report (IRPStatechart · RPStatechart · elements/classifiers/model_statechart.py · 10 legacy sites)
  - Note: behavioural container (97 src / 14 test, 31 owned methods). Already extends the synced `IRPClass`; a direct leaf migration once its report exists.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_statechart.md`
  - [ ] Step 7 — §7 RST update: `irp_statechart.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate

- [ ] irp_diagram_api_report (IRPDiagram · RPDiagram · elements/diagrams/model_diagrams.py · 2 legacy sites)
  - Note: base diagram type (84 src / 14 test, 33 owned methods). Module defines many diagram leaves with zero owned methods — migrate only `RPDiagram` and leave the leaves for a later group.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_diagram.md`
  - [ ] Step 7 — §7 RST update: `irp_diagram.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate

- [ ] irp_message_api_report (IRPMessage · RPMessage · elements/interactions/model_interactions.py · 32 legacy sites)
  - Note: interaction core (44 src / 48 test, 36 owned methods) with the largest legacy-site count here. Module also holds `RPEvent`/`RPTransition` etc. — only this class migrates in this row.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_message.md`
  - [ ] Step 7 — §7 RST update: `irp_message.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate

- [ ] irp_table_layout_api_report (IRPTableLayout · RPTableLayout · elements/graphics/model_graphics.py · 5 legacy sites)
  - Note: high-frequency graphics helper (122 src / 14 test, 50 owned methods — the largest surface in this group). Extends the synced `IRPUnit`; migrate only this class out of the shared graphics module.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_table_layout.md`
  - [ ] Step 7 — §7 RST update: `irp_table_layout.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate

- [ ] irp_collaboration_api_report (IRPCollaboration · RPCollaboration · elements/containment/model_collaboration.py · 1 legacy site)
  - Note: common containment wrapper (77 src / 11 test, 39 owned methods). Extends the synced `IRPUnit`; low legacy-site count but high structural use closes the group.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_collaboration.md`
  - [ ] Step 7 — §7 RST update: `irp_collaboration.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + gate
