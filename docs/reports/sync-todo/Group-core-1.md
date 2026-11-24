# Sync todo: `core` — `Group-core-1.md`

Category: legacy module subpackage `core` · 7 classes · group 1 of 1 for this category.

Rows were regrouped from the former numbered batch files by legacy module subpackage (the domain folder in each row's path); classes without a legacy path were mapped from their legacy class names.

Steps = SKILL.md §1–§8, enumerated per row: ① §1 sync TODO · ② §2 resolve target · ③ §3 compare
evidence · ④ §4 unit tests (TDD) · ⑤ §5 integration tests · ⑥ §6 SWR update · ⑦ §7 RST update ·
⑧ §8 verify and report. Per-row binding rules: one pywin32-exposed COM member per call —
`call_com(lambda: self._com.Name(...))` for method-shaped members,
`get_com_property` / `set_com_property` for property-shaped members; catalog-absent sites are
blockers, never blind migrations.

Canonical package: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/` with mirrored
`tests/{unit,integration}/models/com/telelogic/rhapsody/core/test_<snake>.py`.

## Rows

- [ ] irp_model_element_remediation - IRPModelElement
  - Baseline before this remediation: getErrorMessage call arity 0 to 1; 22 disallowed integration exception assertions; 32 COM properties used method shape; Java getStereotype/setStereotype mapped to the missing read/write COM property stereotype. The invalid `set_ti` and `set_main_diagram` cases were already replaced with real relationship roundtrips.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, exports, and inherited-member scope verified.
  - [ ] Section 3 arity, property shape, stereotype member, and every owned member reconciled against JavaDoc/catalog.
  - [x] Section 4 fake-COM tests first; full unit suite green; irp_model_element.py at 100% statements/branches. Evidence: focused unit file 154 passed; coverage 307 statements/136 branches, 100.00%; full unit suite 2124 passed; mypy found no issues in 274 files.
  - [ ] Section 5 populated getter matrix and live assertions complete; final live result or blockers recorded. After the user-approved stubs, the full focused integration file completed **103 passed, 0 failed, exit 0** using `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH=src python -m pytest tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py -q -o addopts= --rhapsody-hidden-ui`; the two explicit NotImplementedError tests passed. The regular plugin-autoload run previously emitted fatal reporter-teardown traces after reporting 103 passed, while the disabled-autoload run exited cleanly. The getter follow-up matrix is:

    | Getter / Python member | Parent and real related data | JavaDoc setup / relationship | Retrieval assertion | Integration test | Cleanup / status |
    | --- | --- | --- | --- | --- | --- |
    | `getConstraints()` / `constraints` | Class + created Constraint | `addNewAggr("Constraint", name)` creates a child model element; `IRPConstraint` identifies constraint elements | Created constraint name is present in `constraints` | `test_irp_model_element.py::TestRPModelElementRedefinesConstraintsIntegration::test_get_constraints_returns_constraint_created_on_element` | Delete package; **passed live** |
    | `getLocalTags()` / `local_tags` | Package + created Tag | `addNewAggr("Tag", name)` creates the local model element; `setTagValue` applies the tag | Created tag name is present in `local_tags` | `test_irp_model_element.py::TestRPModelElementStereotypesTagsIntegration::test_get_local_tags_returns_tag_created_on_element` | Delete package; **passed live** |
    | `getConstraintsByHim()` / `constraints_by_him` | Class; direct and anchored Constraint fixtures were probed | Created with `addNewAggr("Constraint", name)` and anchored with JavaDoc `IRPAnnotation.addAnchor`; both returned no result and JavaDoc says “For internal use only” | By explicit user decision on 2026-11-24, the getter now raises `NotImplementedError` before COM dispatch; this is not populated retrieval evidence | `test_irp_model_element.py::TestRPModelElementRedefinesConstraintsIntegration::test_get_constraints_by_him_is_not_implemented` | Delete package; user-approved runtime stub despite pywin32 property exposure |
    | `getHyperLinks()` / `hyper_links` | Class + target model element was probed | JavaDoc creation API `setDescriptionAndHyperlinks(rtfText, targets)` faulted `E_INVALIDARG`; `addNewAggr("HyperLink", name)` did not expose documented `IRPHyperLink.setTarget` through COM | By explicit user decision on 2026-11-24, the getter now raises `NotImplementedError` before COM dispatch; this is not populated retrieval evidence | `test_irp_model_element.py::TestRPModelElementOslcRemoteIntegration::test_get_hyper_links_is_not_implemented` | Delete package; user-approved runtime stub despite pywin32 property exposure |

    Other live blockers remain: `add_remote_dependency_to` needs an external Design Manager remote-requirements fixture; the GUID property put silently resets the GUID to a placeholder (destructive, unsupported live), so its write roundtrip remains removed; `add_link_to_element` faults E_FAIL with null ports despite the JavaDoc contract, and `addRedefines` only works at feature level, so the live test uses an attribute redefined against its inherited base after generalization. `high_light_element` / `open_features_dialog` remain mock-based due to modal UI. The user explicitly approved disabling `constraints_by_him` and `hyper_links` with `NotImplementedError` even though their COM properties are cataloged. This is a deliberate exception to the usual pywin32-forwarding rule and does not count as populated getter retrieval; Section 5 remains open for the interface's other unresolved live cases.
  - [x] Section 6 irp_model_element.md checked/updated. Evidence: requirement page records the property surface, get_error_message MIDL buffer, add_link_to_element None-ports contract, documented-unavailable get_rmm_url, and the user-approved runtime stubs for constraints_by_him / hyper_links.
  - [x] Section 7 irp_model_element.rst checked/updated for every public member. Evidence: RST regenerated with 33 autoattribute and 70 automethod directives; verify_sync.py exits 0.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded. Evidence: report regenerated; `validate_interface.py IRPModelElement --source authority` exits 1 with two actionable findings because the user-approved stubs intentionally have no static COM binding; `verify_sync.py` exits 0; skill harness 31 passed; full unit suite 2124 passed; full focused live file 103 passed / 0 failed; ruff, black, and mypy clean. The two report findings are explicitly documented as intentional in this ledger and the per-class requirement page; the validator output is not hand-edited. Section 5 remains open for other unresolved live cases.
- [ ] irp_collection_remediation - IRPCollection
  - Baseline: COM Count property is exposed as get_count; integration test asserts forbidden IndexError for a negative index.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 COM property/method shape and collection index contract reconciled.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_collection.py at 100% statements/branches.
  - [ ] Section 5 populated collection getter test asserts the created item/count; negative-index behavior stays unit-tested.
  - [ ] Section 6 irp_collection.md checked/updated.
  - [ ] Section 7 irp_collection.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
- [ ] irp_unit_remediation - IRPUnit
  - Baseline: 6 property-shape conversions; 4 integration tests assert RhapsodyRuntimeException.
  - [ ] Section 1 member checklist and getter matrix published.
  - [ ] Section 2 canonical wrapper, tests, and exports verified.
  - [ ] Section 3 all 6 properties and four failing cases reconciled against the report/catalog.
  - [ ] Section 4 fake-COM tests first; full unit suite green; irp_unit.py at 100% statements/branches.
  - [ ] Section 5 replace the four exception assertions with authentic live outcomes or evidence-backed blockers.
  - [ ] Section 6 irp_unit.md checked/updated.
  - [ ] Section 7 irp_unit.rst checked/updated for every public member.
  - [ ] Section 8 generated report, verify_sync, gates, live counts, and blockers recorded.
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
- [x] irp_unit_api_report (IRPUnit · canonical `models/com/telelogic/rhapsody/core/irp_unit.py`) — 8/8, archived in commit `1c81084`
  - Note: unit-family members — catalog kinds: methods `getAddToModelMode`/`getCMState`/`getLanguage`/`getLastModifiedTime`/`getNestedSaveUnits`/`getNestedSaveUnitsCount`/`isReadOnly`/`isReferenceUnit`/`isSeparateSaveUnit`/`setReadOnly`/`setSeparateSaveUnit`/`setUnitPath`; properties `CMHeader`/`currentDirectory`/`filename`/`includeInNextLoad`/`isStub`/`structureDiagrams`; landing this row resolves IRPModelElement's cross-catalog blockers.
  - [x] Step 1 — §1 sync TODO published: 7 shared step tasks + 29-member inventory (all owned; inherited `IRPModelElement` members kept separate)
  - [x] Step 2 — §2 target resolved and canonical move completed: report Java package `com.telelogic.rhapsody.core` agrees with `IRPUnit.html`; `RPUnit` → `IRPUnit` renamed, then wrapper + `AddToModelMode` moved to `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_unit.py`; mirrored tests at `tests/{unit,integration}/models/com/telelogic/rhapsody/core/test_irp_unit.py`; canonical `__init__.py` lazy exports; all internal imports updated; `core.py:get_save_unit()` imports locally before `cast()` (no cycle; quoted types unnecessary under `from __future__ import annotations`); no compatibility shim. Doubled-prefix artifacts from the bulk rename were fixed repo-wide.
  - [x] Step 3 — §3 evidence compared offline (regenerated report: 0 deviations, 29 owned members; 21 legacy dual-binding sites mapped one-to-one to pywin32 members; catalog-absent `getUnitPath` left unchanged as expected informational difference; no python-only members)
  - [x] Step 4 — §4 unit tests (TDD): 10 tests red → green; structural guard (21 offenders → 0) + future-annotations guard added; full unit suite 1714 green; canonical `irp_unit.py` coverage 100% (68/68 statements, 40/40 branches)
  - [x] Step 5 — §5 integration tests: mirrored canonical path, 22 tests collected; Windows live run 15 passed / 3 skipped (pre-existing `second_test_project` TODO fixture) / 4 xfailed (pre-existing getUnitPath COM gaps), no failures
  - [x] Step 6 — §6 SWR update: `docs/requirements/com/telelogic/rhapsody/core/irp_unit.md` (SWR_CORE_00002 moved out of `swr_core_requirements.md`, no duplicate; canonical implementation path)
  - [x] Step 7 — §7 RST update: `docs/api/com/telelogic/rhapsody/core/irp_unit.rst` (anchor + 7-row deviation list-table covering getUnitPath/setUnitPath and method-vs-property shapes; canonical import; toctree wired in `docs/api/elements.rst`)
  - [x] Step 8 — §8 verify and report: `validate_interface.py` ✓ (0 deviations), `verify_sync.py` ✓ (artifacts verified), skill self-tests 15 ✓, full unit suite 1714 ✓, ruff/black/mypy ✓, Windows live integration ✓
- [x] irp_model_element_api_report (IRPModelElement · models/core.py · 1 blocker site left)
  - Note: re-run completed 2026-11-21 under the updated skill (shape-follows-COM, future annotations, own-members report + Correct Items, Java-package declaration). Class renamed `RPModelElement` → `IRPModelElement`; python-only `get_oslc_links` removed (stale premise — `getOSLCLinks` is exposed by pywin32); `core.py` converted to `from __future__ import annotations` with unquoted type references and local runtime imports for `cast()` (25 casts + 84 annotations); `wrap()` reads the `metaClass` property; RPCollection migrated; IRPUnit's 21 sites remain for its own row.
  - [x] Step 1 — §1 sync TODO published (per-run checklist rendered live)
  - [x] Step 2 — §2 target resolved; report Java-package declaration verified (`com.telelogic.rhapsody.core`, agrees with JavaDoc); canonical move complete: `IRPModelElement` → `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py`, `AbstractRPModelElement` stays in `models/core.py` with a local import in `wrap()`; 78 import sites updated; mirrored unit/integration test files moved; canonical `__init__.py` and RST import path updated.
  - [x] Step 3 — §3 evidence compared offline (committed own-members report + catalog: 1 actionable blocker `get_rmm_url` left unchanged, 96 correct items, 5 backlog rows; python-only `get_oslc_links` removed per §4 — report row disappears at closeout regeneration)
  - [x] Step 4 — §4 unit tests (structural guard green; future-annotations guard green: no quoted casts/annotations, `from __future__ import annotations` present; full unit suite 1711 green)
  - [x] Step 5 — §5 integration tests (mirror unit/integration files verified exercising `IRPModelElement` via `test_core.py`; behavior-preserving; Windows live run tracked in Step 8)
  - [x] Step 6 — §6 SWR update (`docs/requirements/com/telelogic/rhapsody/core/irp_model_element.md` — binding rules, `get_rmm_url` blocker, deferred-move note, future-annotations fact)
  - [x] Step 7 — §7 RST update (`docs/api/com/telelogic/rhapsody/core/irp_model_element.rst` — 6 deviation rows + 96 Correct-Items rows, coverage complete; get_oslc_links row removed per §7; toctree wired)
  - [x] Step 8 — §8 verify and report (all eight steps green: report regenerated with canonical target line, `validate_interface.py` ✓, `verify_sync.py` ✓, 0 skip/xfail markers, 100% statement/branch coverage at both unit and integration layers, 105 live integration tests ✓, full unit suite ✓, ruff/black/mypy ✓; commits `6cbebc3` + `1778607` + `5175b93`)
