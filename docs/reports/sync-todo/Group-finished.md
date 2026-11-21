# Sync todo: `docs/reports` — `Group-finished` (archive)

Rows move here from `Group-unfinished-*.md` once all eight steps (SKILL.md §1–§8) are `[x]` and
the run's commit exists. Keep the row's original text and ticks; do not rewrite history.

- [x] irp_class_api_report (IRPClass · IRPClass · models/com/telelogic/rhapsody/core/irp_class.py · 0 sites left)
  - Note: pilot run 2026-11-21, commits `7163149` + `b27a8bb`; 7 property-shaped flag sites migrated to `get_com_property`/`set_com_property` (`is_final` was already direct); six flag rows rewritten in `elements.rst`, SWR_ELEM_00004 updated.
  - [x] Step 1 — §1 sync TODO published (per-run checklist rendered live in the run report)
  - [x] Step 2 — §2 target resolved (wrapper canonical; JavaDoc evidence from committed report — live `docs/java_api` absent on macOS)
  - [x] Step 3 — §3 evidence compared (7 legacy sites identified, all property-shaped per catalog; offline proof: six flag families ALIAS_DOCUMENTED/informational, 78+5 matching committed summary)
  - [x] Step 4 — §4 unit tests (2 setter tests + structural guard red → 34/34 green in `test_irp_class.py`)
  - [x] Step 5 — §5 integration tests (behavior-preserving change; existing mirrored integration file collected 17 tests ✓ — no new coverage required)
  - [x] Step 6 — §6 SWR update (`docs/requirements/com/telelogic/rhapsody/core/irp_class.md` — SWR_ELEM_00004 moved from the legacy monolith; property mention + pywin32-direct binding statement)
  - [x] Step 7 — §7 RST update (`docs/api/com/telelogic/rhapsody/core/irp_class.rst` — section moved from `elements.rst`, six flag rows rewritten, two malformations fixed; toctree entry added)
  - [x] Step 8 — §8 verify and report (Windows closeout 2026-11-21: `validate_interface.py IRPClass --source authority` exit 0 / 0 deviations; `verify_sync.py IRPClass` exit 0; skill self-tests 9 ✓; unit suite 1708 ✓ with `PYTHONPATH=src`; ruff/black/mypy ✓; live integration 17/17 ✓ on a fresh Rhapsody instance — first attempt crashed against the pre-existing user session instance, rerun with a clean instance passed)

- [x] irp_collection_api_report (IRPCollection · IRPCollection · models/core.py · 2 blocker sites left)
  - Note: run 2026-11-21 — `get_count` migrated to the `Count` property and `get_item` migrated to the direct `Item` method (the legacy `getItem` name-probe removed); `make_fake_collection` exposes both forms (`Count` attribute + `Item` side_effect) keeping the ~163 dependent call sites green; `add_graphical_item` and `to_list` are documented blockers (Java members absent from pywin32).
  - [x] Step 1 — §1 sync TODO published (per-run checklist with 11 owned-member subtasks rendered live at run start)
  - [x] Step 2 — §2 target resolved (report Java package `com.telelogic.rhapsody.core` agrees with JavaDoc; wrapper class body moved to canonical `models/com/telelogic/rhapsody/core/irp_collection.py`, re-exported from `rhapsody_cli.models` / `core.py`; 64 importers rewritten; lazy canonical `__init__` breaks the import cycle; report regenerated, `verify_sync.py IRPCollection` exit 0)
  - [x] Step 3 — §3 evidence compared (validator baseline exit 1 with only the 2 known `PYWIN32_MEMBER_MISSING` deviations; 11 owned members reconciled — 9 MATCH, `add_graphical_item`/`to_list` catalog-absent blockers; RST table coverage confirmed by `verify_sync.py`)
  - [x] Step 4 — §4 unit tests (prior guard-red → migration retained; canonical module has its own fake-COM tests plus the no-legacy-helper structural guard); full unit suite 1711 ✓
  - [x] Step 5 — §5 integration tests (behavior-preserving; live Windows run of `tests/integration/models/test_core.py -k IRPCollection`: 11 passed + 1 xfailed over 3 owned classes ✓)
  - [x] Step 6 — §6 SWR update (`docs/requirements/com/telelogic/rhapsody/core/irp_collection.md` — SWR_ELEM_00015; implementation path updated to the canonical module)
  - [x] Step 7 — §7 RST update (`docs/api/com/telelogic/rhapsody/core/irp_collection.rst` — canonical Python import added, deferred-move note removed; deviation table unchanged and verified)
  - [x] Step 8 — §8 verify and report (2026-11-21: `validate_interface.py IRPCollection --source authority` exit 1 with only the 2 known blockers; `verify_sync.py IRPCollection` exit 0; 13 skill tests ✓; 1711 unit tests ✓; ruff/black/mypy ✓; live integration 11 passed + 1 xfailed ✓; archived)
