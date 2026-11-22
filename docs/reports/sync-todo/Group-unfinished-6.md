# Sync todo: `docs/reports` — `Group-unfinished-6` (IRPInternalOEMPlugin → IRPPin)

Baseline: 2026-11-22 inventory of unsynced wrapper classes. 10 open rows · ordered by
importance (usage in `src/` then `tests/`, legacy cleanup value and owned surface). All
higher-importance classes are already queued in Group-unfinished-1/2 or archived in
Group-finished.md.

(Resume = first row still `[ ]`; archive to [Group-finished.md](Group-finished.md) only when all
eight steps are `[x]` and its commit exists.)

## Prerequisites

None of these interfaces has a committed API report or a catalog entry yet. Regenerate both on
Windows with Rhapsody before Step 3 (see Group-unfinished-2.md). JavaDoc is available locally at
`docs/java_api/com/telelogic/rhapsody/core/<IFACE>.html`. Never migrate a catalog-absent member.

Steps = SKILL.md §1–§8; canonical package and mirrored test paths as in Group-unfinished-2.md.

Prerequisite for every row: regenerate API report + catalog entry before §3.

- [ ] irp_internal_oem_plugin_api_report (IRPInternalOEMPlugin · RPInternalOEMPlugin · rhapsody_cli/models/support/model_ide.py · 0 legacy sites)
  - Note: usage 18 src / 16 test refs, 14 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_internal_oem_plugin.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_internal_oem_plugin.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_flow_item_api_report (IRPFlowItem · RPFlowItem · rhapsody_cli/models/elements/activity/model_activity.py · 0 legacy sites)
  - Note: usage 24 src / 12 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_flow_item.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_flow_item.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_graph_edge_api_report (IRPGraphEdge · RPGraphEdge · rhapsody_cli/models/elements/graphics/model_graphics.py · 0 legacy sites)
  - Note: usage 23 src / 10 test refs, 5 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_graph_edge.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_graph_edge.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_selection_api_report (IRPSelection · RPSelection · rhapsody_cli/models/support/model_ide.py · 0 legacy sites)
  - Note: usage 19 src / 12 test refs, 8 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_selection.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_selection.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_enumeration_literal_api_report (IRPEnumerationLiteral · RPEnumerationLiteral · rhapsody_cli/models/elements/common/model_misc.py · 1 legacy sites)
  - Note: usage 21 src / 11 test refs, 2 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_enumeration_literal.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_enumeration_literal.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_object_node_api_report (IRPObjectNode · RPObjectNode · rhapsody_cli/models/elements/activity/model_activity.py · 3 legacy sites)
  - Note: usage 17 src / 12 test refs, 7 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_object_node.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_object_node.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_component_instance_api_report (IRPComponentInstance · RPComponentInstance · rhapsody_cli/models/elements/containment/model_component_instance.py · 0 legacy sites)
  - Note: usage 21 src / 11 test refs, 3 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_component_instance.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_component_instance.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_image_map_api_report (IRPImageMap · RPImageMap · rhapsody_cli/models/elements/graphics/model_graphics.py · 5 legacy sites)
  - Note: usage 18 src / 6 test refs, 7 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_image_map.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_image_map.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_diag_synth_api_api_report (IRPDiagSynthAPI · RPDiagSynthAPI · rhapsody_cli/models/support/model_codegen.py · 0 legacy sites)
  - Note: usage 18 src / 11 test refs, 7 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_diag_synth_api.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_diag_synth_api.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

- [ ] irp_pin_api_report (IRPPin · RPPin · rhapsody_cli/models/elements/graphics/model_graphics.py · 4 legacy sites)
  - Note: usage 17 src / 7 test refs, 6 owned methods. Confirm canonical-package applicability for support-layer wrappers during §2; siblings in the same module stay for their own rows.
  - [ ] Step 1 — §1 sync TODO: publish the per-run checklist with a subtask per target-owned JavaDoc member before any edit
  - [ ] Step 2 — §2 resolve target: locate wrapper/inheritance/exports/tests; move wrapper + tests to canonical `models/com/telelogic/rhapsody/core/`
  - [ ] Step 3 — §3 compare evidence: regenerate report + catalog entry; reconcile owned members; one pywin32 member per call; catalog-absent sites = blockers
  - [ ] Step 4 — §4 unit tests (TDD): failing fake-COM tests first, then migrate legacy sites; full unit suite green
  - [ ] Step 5 — §5 integration tests: mirrored path, assert only owned methods; live run on Windows
  - [ ] Step 6 — §6 SWR update: per-class requirement document `irp_pin.md` (move entry out of the legacy monolith)
  - [ ] Step 7 — §7 RST update: `irp_pin.rst` (anchor + deviation list-table) and toctree entry
  - [ ] Step 8 — §8 verify and report: validator + `verify_sync.py` + skill tests + both full suites + ruff/black/mypy

