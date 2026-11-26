# Sync todo — `core` (group 1 of 1)

**7 classes** · ✅ 7 archived · ⬜ 0 open

One row per sync run. A step is ticked only when its evidence lands; a row is archived only after all eight steps pass. Binding rule: one pywin32-exposed COM member per call — `call_com(lambda: self._com.Name(...))` for methods, `get_com_property` / `set_com_property` for properties; catalog-absent sites are blockers, never blind migrations. Canonical package: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/`, mirrored tests under `tests/{unit,integration}/models/com/telelogic/rhapsody/core/`.

## Step legend

| Step | Meaning |
| --- | --- |
| ① §1 | publish the per-run checklist with a subtask per target-owned JavaDoc member |
| ② §2 | resolve the wrapper, inheritance, exports, and tests; move to the canonical package |
| ③ §3 | reconcile every owned member against JavaDoc, pywin32, and the Python wrapper |
| ④ §4 | failing fake-COM unit tests first, then migrate the legacy sites |
| ⑤ §5 | integration coverage on the mirrored path; live run on Windows |
| ⑥ §6 | update the per-class requirement document |
| ⑦ §7 | update the per-class RST page and its toctree entry |
| ⑧ §8 | run the validator, `verify_sync.py`, skill tests, both suites, and the quality gate |

`[x] §2` on every row records the 2026-11-24 bulk package move; other steps show their evidence inline when it differs from the legend.

## At a glance

| # | Class | Interface | Legacy source | Sites | Owned | Steps | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `irp_model_element_remediation` | IRPModelElement | — | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 2 | `irp_collection_remediation` | IRPCollection | — | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 3 | `irp_unit_remediation` | IRPUnit | — | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 4 | `irp_class_api_report` | IRPClass | `models/com/telelogic/rhapsody/core/irp_class.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 5 | `irp_collection_api_report` | IRPCollection | `models/core.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 6 | `irp_unit_api_report` | IRPUnit | `models/com/telelogic/rhapsody/core/irp_unit.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 7 | `irp_model_element_api_report` | IRPModelElement | `models/core.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |

## Row details

<details>
<summary><code>irp_model_element_remediation</code> · IRPModelElement · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- Baseline before this remediation: getErrorMessage call arity 0 to 1; 22 disallowed integration exception assertions; 32 COM properties used method shape; Java getStereotype/setStereotype mapped to the missing read/write COM property stereotype. The invalid `set_ti` and `set_main_diagram` cases were already replaced with real relationship roundtrips.
- [x] ① §1 — owned-member checklist in `irp_model_element.py` now includes the restored `get_oslc_links`; the regenerated report counts 104 Python members (the checklist has 113 rows, including legacy `get_*` alias entries, so the two numbers are not the same); getter matrix below covers `constraints`, `local_tags`, the two approved stubs, and the new OSLC-link getter row.
- [x] ② §2
- [x] ③ §3 — regenerated report shows Python `104` / Java `119` / pywin32 `104` with 96 verified MATCH rows; `get_error_message` uses the 1-arg MIDL buffer; all 32 properties are Python `@property` backed by `get_com_property`/`set_com_property`; `stereotype` maps to the exposed `stereotype` property. The 3 prior `MISSING_PYTHON_WRAPPER` findings were resolved: `get_oslc_links()` implemented and unit-tested; `lockOnDesignManager`/`unlockOnDesignManager` recorded under `documented_intentionally_unsupported` on live pywin32 evidence (2026-11-25 fresh hidden-UI instance: both zero-arg COM calls raised `com_error` HRESULT `0x80040010`, `isRemote`/`getRemoteURI` unchanged at `0`/`''`, recorded in SWR_ELEM_00035) — decision no longer rests on the JavaDoc deprecation note. Only the two user-approved runtime stubs remain actionable in the validator, exactly as documented.
- [x] ④ §4 — focused unit file 155 passed; coverage 311 statements/142 branches, 100.00%; full unit suite 2166 passed; mypy found no issues in 230 files.
- [x] ⑤ §5
- [x] ⑥ §6 — requirement page records the property surface, get_error_message MIDL buffer, add_link_to_element None-ports contract, documented-unavailable get_rmm_url, the user-approved runtime stubs for constraints_by_him / hyper_links, the OSLC link methods (SWR_ELEM_00033), and the live COM-fault evidence for the Design Manager members (SWR_ELEM_00035).
- [x] ⑦ §7 — RST regenerated with 33 autoattribute and 71 automethod directives; verify_sync.py exits 0.
- [x] ⑧ §8 — report regenerated (Python `104`, 96 MATCH, 2 backlog, 2 actionable); `validate_interface.py IRPModelElement --source authority` exits 1 with exactly two actionable findings because the user-approved `constraints_by_him`/`hyper_links` stubs intentionally have no static COM binding; `verify_sync.py` exits 0; skill harness 49 passed; focused unit file 155 passed at 100.00% statement/branch coverage (311 statements / 142 branches); full unit suite 2166 passed; full focused live file 100 passed / 0 failed; full integration suite 443 passed / 0 failed; ruff, black, and mypy clean. The two report findings are explicitly documented as intentional in this ledger and the per-class requirement page; the validator output is not hand-edited.

| Getter / Python member | Parent and real related data | JavaDoc setup / relationship | Retrieval assertion | Integration test | Cleanup / status |
| --- | --- | --- | --- | --- | --- |
| `getConstraints()` / `constraints` | Class + created Constraint | `addNewAggr("Constraint", name)` creates a child model element; `IRPConstraint` identifies constraint elements | Created constraint name is present in `constraints` | `test_irp_model_element.py::TestRPModelElementRedefinesConstraintsIntegration::test_get_constraints_returns_constraint_created_on_element` | Delete package; **passed live** |
| `getLocalTags()` / `local_tags` | Package + created Tag | `addNewAggr("Tag", name)` creates the local model element; `setTagValue` applies the tag | Created tag name is present in `local_tags` | `test_irp_model_element.py::TestRPModelElementStereotypesTagsIntegration::test_get_local_tags_returns_tag_created_on_element` | Delete package; **passed live** |
| `getConstraintsByHim()` / `constraints_by_him` | Class; direct and anchored Constraint fixtures were probed | Created with `addNewAggr("Constraint", name)` and anchored with JavaDoc `IRPAnnotation.addAnchor`; both returned no result and JavaDoc says “For internal use only” | By explicit user decision on 2026-11-24, the getter now raises `NotImplementedError` before COM dispatch; this is not populated retrieval evidence | `test_irp_model_element.py::TestRPModelElementRedefinesConstraintsIntegration::test_get_constraints_by_him_is_not_implemented` | Delete package; user-approved runtime stub despite pywin32 property exposure |
| `getHyperLinks()` / `hyper_links` | Class + target model element was probed | JavaDoc creation API `setDescriptionAndHyperlinks(rtfText, targets)` faulted `E_INVALIDARG`; `addNewAggr("HyperLink", name)` did not expose documented `IRPHyperLink.setTarget` through COM | By explicit user decision on 2026-11-24, the getter now raises `NotImplementedError` before COM dispatch; this is not populated retrieval evidence | `test_irp_model_element.py::TestRPModelElementOslcRemoteIntegration::test_get_hyper_links_is_not_implemented` | Delete package; user-approved runtime stub despite pywin32 property exposure |
| `getOSLCLinks()` / `get_oslc_links()` | Plain class with no OSLC links; creating a link needs an OSLC-enabled remote server | JavaDoc `createOSLCLink(type, purl)` requires `IRPPackage.loginToRemoteArtifactServer` and faults `E_FAIL` in this build (SWR_ELEM_00033) | Live empty-state result asserted (`IRPCollection`, length 0); a populated link fixture cannot be built locally | `test_irp_model_element.py::TestRPModelElementOslcRemoteIntegration::test_get_oslc_links_returns_empty_collection_for_plain_class` | Delete package; **passed live**; populated-retrieval row remains open on the OSLC-server blocker |
Other live blockers remain: `add_remote_dependency_to` needs an external Design Manager remote-requirements fixture; the GUID property put silently resets the GUID to a placeholder (destructive, unsupported live), so its write roundtrip remains removed; `add_link_to_element` faults E_FAIL with null ports despite the JavaDoc contract, and `addRedefines` only works at feature level, so the live test uses an attribute redefined against its inherited base after generalization. `high_light_element` / `open_features_dialog` remain mock-based due to modal UI. The user explicitly approved disabling `constraints_by_him` and `hyper_links` with `NotImplementedError` even though their COM properties are cataloged. This is a deliberate exception to the usual pywin32-forwarding rule and does not count as populated getter retrieval. The remaining unresolved live cases (populated OSLC links, modal GUI dialogs, remote Design Manager, destructive GUID write) are recorded as blockers in `irp_model_element.md` (SWR_ELEM_00023, SWR_ELEM_00033); the getters tracked in the matrix above are covered by populated, stub, or documented-negative live assertions, while the remaining owned getters keep their existing smoke/empty-state integration cases.

</details>

<details>
<summary><code>irp_collection_remediation</code> · IRPCollection · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Baseline:** COM Count property is exposed as get_count; integration test asserts forbidden IndexError for a negative index.
- [x] ① §1 — wrapper checklist covers all 11 owned JavaDoc members; `count` is a Python `@property` over the catalog's `Count` property (not `get_count`), and the negative-index `IndexError` assertion is unit-only. Getter matrix:
- [x] ② §2
- [x] ③ §3 — regenerated report shows Python `11` / Java `11` / pywin32 `10` with 0 actionable findings. `set_string`'s `value` annotation changed from `str` to `object` to match the catalog's VT_BYREF|VT_BSTR declaration (TDD test added). `add_graphical_item` migrated to the catalog-exposed `addGraphicalElementItem` alias after a live probe confirmed it succeeds with a real `IRPGraphElement` (count 0->1) and faults `Type mismatch` for non-graph elements; recorded in `documented_aliases` and SWR_ELEM_00036, with a one-pair normalization in `scripts/validate_model_api.py` so the report shows MATCH instead of stacked JAVA_DOC_MISSING / JAVA_ONLY_MEMBER rows. `to_list` remains the documented-unavailable stub.
- [x] ④ §4 — focused unit file 8 passed; coverage 40 statements/26 branches, 100.00%; full unit suite 2168 passed; skill harness 49 passed; mypy found no issues in 230 files.
- [x] ⑤ §5 — `test_nested_elements_are_wrapped_collections` asserts the created package is present in a live `IRPCollection`; `test_collection_mutators_and_accessors` asserts real string/integer/element values and count; `test_add_graphical_item_adds_real_graph_element` asserts count 0->1 with a real graph element; the only integration exception assertion is the documented-unavailable `to_list` stub; negative index stays a fake-COM unit test. Focused live file 5 passed / 0 failed; full live suite 443 passed / 0 failed.
- [x] ⑥ §6 — SWR_ELEM_00015 records the catalog-aligned `set_string` annotation, the working graphical alias, and the `to_list` blocker; SWR_ELEM_00036 records the live alias evidence.
- [x] ⑦ §7 — all 11 public members remain documented via autodoc directives; no deviation tables; verify_sync.py exits 0.
- [x] ⑧ §8 — report regenerated (Python `11`, Java `11`, pywin32 `10`, 0 actionable, 1 expected difference `to_list`); `validate_interface.py IRPCollection --source authority` exits 0; `verify_sync.py` exits 0; skill harness 49 passed; focused unit coverage 100.00% (40 statements / 26 branches), full unit suite 2168 passed; focused live 5 passed / 0 failed; full live integration 443 passed / 0 failed; ruff, black, and mypy clean.

| Getter / Python member | Parent and real related data | JavaDoc setup / relationship | Retrieval assertion | Integration test | Cleanup |
| --- | --- | --- | --- | --- | --- |
| `getCount()` / `count` | fresh live collection; then a collection sized by `set_size(3)` | `rhapsody_app.create_new_collection()` | `count == 0` then `len == 3` after mutators | `TestIRPCollectionIntegration::test_create_new_collection_is_empty`, `::test_collection_mutators_and_accessors` | no project objects created |
| `getItem()` / `get_item` | live project + package created for the case | `test_project.add_package(...)` then `test_project.get_nested_elements()` | created package is present in the returned `IRPCollection` | `TestIRPCollectionIntegration::test_nested_elements_are_wrapped_collections` | `created.delete_from_project()` |

</details>

<details>
<summary><code>irp_unit_remediation</code> · IRPUnit · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Baseline:** 6 property-shape conversions; 4 integration tests assert RhapsodyRuntimeException.
- [x] ① §1 — wrapper checklist covers all 26 owned members (23 MATCH + `get_unit_path`/`set_unit_path` family + inherited `get_nested_elements`); no `RhapsodyRuntimeException` assertions and no skip/xfail markers remain in either mirrored test file. Getter matrix:
- [x] ② §2
- [x] ③ §3 — regenerated report shows Python `26` / Java `29` / pywin32 `25`, 0 actionable findings, 23 MATCH rows; `CMHeader`, `currentDirectory`, `filename`, `includeInNextLoad`, `isStub`, `structureDiagrams` are `@property` backed by `get_com_property`/`set_com_property`. The four former `RhapsodyRuntimeException` assertions were already replaced with real roundtrips. `get_unit_path` remains a documented-unavailable stub; a live COM probe on 2026-11-25 confirmed no getter member exists (only `setUnitPath`), recorded in SWR_CORE_00012.
- [x] ④ §4 — focused unit file 33 passed; coverage 76 statements/38 branches, 100.00%; full unit suite 2168 passed; skill harness 49 passed; mypy found no issues in 230 files.
- [x] ⑤ §5 — no `RhapsodyRuntimeException` assertions, `try`/`except`, skip or xfail markers remain; the only exception assertion is the documented-unavailable `get_unit_path` `NotImplementedError` stub. Populated getter assertions added for `structure_diagrams` (diagram created via `add_new_aggr`) and `get_nested_save_units` (nested package saved as own unit, asserted by containment). Focused live file 18 passed / 0 failed; full live suite 444 passed / 0 failed.
- [x] ⑥ §6 — SWR_CORE_00002 records the binding rules and live-confirmed `get_unit_path` absence; new SWR_CORE_00012 records the live path-member probe and populated getter fixtures; no duplicate monolith entry.
- [x] ⑦ §7 — 6 autoproperty and 20 automethod directives cover all 26 public members; the malformed `Canonical module` line was repaired; verify_sync.py exits 0.
- [x] ⑧ §8 — report regenerated from authority (Python `26`, Java `29`, pywin32 `25`, 0 actionable, 1 expected difference `getUnitPath`/`setUnitPath` family); `validate_interface.py IRPUnit --source authority` exits 0; `verify_sync.py` exits 0; skill harness 49 passed; focused unit coverage 100.00% (76 statements / 38 branches), full unit suite 2168 passed; focused live 18 passed / 0 failed; full live integration 444 passed / 0 failed; ruff, black, and mypy clean.

| Getter / Python member | Parent and real related data | JavaDoc setup / relationship | Retrieval assertion | Integration test | Cleanup |
| --- | --- | --- | --- | --- | --- |
| `getCMHeader()` / `cm_header` | package created for the case | `pkg.save()` then unique `cm_header` | read-back equals set value | `::test_set_and_get_cm_header_roundtrip` | `pkg.delete_from_project()` |
| `getCurrentDirectory()` / `current_directory` | live test project | `test_project.add_package(...)` | resolved path contains `TEST_PROJECT_DIR` | `::test_get_current_directory_matches_project` | delete package |
| `getFilename()` / `filename` | package created for the case | unique `pkg.filename` | set name present in read-back | `::test_set_and_get_filename_roundtrip` | delete package |
| `getIncludeInNextLoad()` / `include_in_next_load` | saved package | set to 1 then 0 | read-back equals each value | `::test_set_and_get_include_in_next_load_roundtrip` | delete package |
| `getIsStub()` / `is_stub` | package created for the case | `load(0)` then `unload()` | value in `(0, 1)` | `::test_load_and_unload_roundtrip` | delete package |
| `getStructureDiagrams()` / `structure_diagrams` | class + diagram created on it | `cls.add_new_aggr("StructureDiagram", unique)` | created diagram present by identity and name | `::test_get_structure_diagrams_returns_diagram_created_on_class` | delete package |
| `getAddToModelMode()` / `get_add_to_model_mode()` | saved package | `pkg.save()` | value in `AddToModelMode` | `::test_get_add_to_model_mode_returns_int` | delete package |
| `getCMState()` / `get_cm_state()` | saved package | `pkg.save()` | int result | `::test_get_cm_state_returns_int` | delete package |
| `getLanguage()` / `get_language()` | package created for the case | `pkg.set_language("C++", 0)` | read-back equals `C++`, then restored | `::test_set_and_get_language_roundtrip` | delete package |
| `getLastModifiedTime()` / `get_last_modified_time()` | renamed + saved package | `pkg.name = unique; pkg.save()` | non-empty string | `::test_get_last_modified_time_after_save` | delete package |
| `getNestedSaveUnits()` / `get_nested_save_units()` | package + nested package saved as own unit | `add_nested_package`, `set_separate_save_unit(1)`, `save()` | created nested package present in returned collection | `::test_get_nested_save_units_count_matches_collection` | delete package |
| `getNestedSaveUnitsCount()` / `get_nested_save_units_count()` | same fixture | same | count equals `len(units)` and is at least 1 | same test | delete package |
| `getUnitPath()` / `get_unit_path()` | package created for the case | live COM probe found no `getUnitPath`-like member (SWR_CORE_00012) | stub raises `NotImplementedError` before dispatch | `::test_get_unit_path_raises_not_implemented` | delete package |
| `isReadOnly()` / `is_read_only()` | saved package | `set_read_only(True/False)` | read-back `True`/`False` | `::test_set_and_get_read_only_roundtrip` | delete package |
| `isReferenceUnit()` / `is_reference_unit()` | saved local package | `pkg.save()` | `0` | `::test_is_reference_unit_false_for_local_unit` | delete package |
| `isSeparateSaveUnit()` / `is_separate_save_unit()` | saved package | `set_separate_save_unit(1/0)` | read-back `1`/`0` | `::test_set_and_get_separate_save_unit_roundtrip` | delete package |

</details>

<details>
<summary><code>irp_class_api_report</code> · IRPClass · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived. Duplicate row for IRPClass also in Group-classifiers-1.md.
- **Note:** pilot run 2026-11-21, commits `7163149` + `b27a8bb`; 7 property-shaped flag sites migrated to `get_com_property`/`set_com_property` (`is_final` was already direct); six flag rows rewritten in `elements.rst`, SWR_ELEM_00004 updated.
- [x] ① §1 — sync TODO published (per-run checklist rendered live in the run report)
- [x] ② §2 — target resolved (wrapper canonical; JavaDoc evidence from committed report — live `docs/java_api` absent on macOS)
- [x] ③ §3 — six flag families ALIAS_DOCUMENTED/informational, 78+5 matching committed summary)
- [x] ④ §4 — unit tests (2 setter tests + structural guard red → 34/34 green in `test_irp_class.py`)
- [x] ⑤ §5 — integration tests (behavior-preserving change; existing mirrored integration file collected 17 tests ✓ — no new coverage required)
- [x] ⑥ §6 — SWR update (`docs/requirements/com/telelogic/rhapsody/core/irp_class.md` — SWR_ELEM_00004 moved from the legacy monolith; property mention + pywin32-direct binding statement)
- [x] ⑦ §7
- [x] ⑧ §8 — `validate_interface.py IRPClass --source authority` exit 0 / 0 deviations; `verify_sync.py IRPClass` exit 0; skill self-tests 9 ✓; unit suite 1708 ✓ with `PYTHONPATH=src`; ruff/black/mypy ✓; live integration 17/17 ✓ on a fresh Rhapsody instance — first attempt crashed against the pre-existing user session instance, rerun with a clean instance passed)

</details>

<details>
<summary><code>irp_collection_api_report</code> · IRPCollection · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** run 2026-11-21 — `get_count` migrated to the `Count` property and `get_item` migrated to the direct `Item` method (the legacy `getItem` name-probe removed); `make_fake_collection` exposes both forms (`Count` attribute + `Item` side_effect) keeping the ~163 dependent call sites green; `add_graphical_item` and `to_list` are documented blockers (Java members absent from pywin32).
- [x] ① §1 — sync TODO published (per-run checklist with 11 owned-member subtasks rendered live at run start)
- [x] ② §2 — target resolved (report Java package `com.telelogic.rhapsody.core` agrees with JavaDoc; wrapper class body moved to canonical `models/com/telelogic/rhapsody/core/irp_collection.py`, re-exported from `rhapsody_cli.models` / `core.py`; 64 importers rewritten; lazy canonical `__init__` breaks the import cycle; report regenerated, `verify_sync.py IRPCollection` exit 0)
- [x] ③ §3 — evidence compared (validator baseline exit 1 with only the 2 known `PYWIN32_MEMBER_MISSING` deviations; 11 owned members reconciled — 9 MATCH, `add_graphical_item`/`to_list` catalog-absent blockers; RST table coverage confirmed by `verify_sync.py`)
- [x] ④ §4 — unit tests (prior guard-red → migration retained; canonical module has its own fake-COM tests plus the no-legacy-helper structural guard); full unit suite 1711 ✓
- [x] ⑤ §5 — 11 passed + 1 xfailed over 3 owned classes ✓)
- [x] ⑥ §6 — SWR update (`docs/requirements/com/telelogic/rhapsody/core/irp_collection.md` — SWR_ELEM_00015; implementation path updated to the canonical module)
- [x] ⑦ §7
- [x] ⑧ §8 — `validate_interface.py IRPCollection --source authority` exit 1 with only the 2 known blockers; `verify_sync.py IRPCollection` exit 0; 13 skill tests ✓; 1711 unit tests ✓; ruff/black/mypy ✓; live integration 11 passed + 1 xfailed ✓; archived)

</details>

<details>
<summary><code>irp_unit_api_report</code> · IRPUnit · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** unit-family members — catalog kinds: methods `getAddToModelMode`/`getCMState`/`getLanguage`/`getLastModifiedTime`/`getNestedSaveUnits`/`getNestedSaveUnitsCount`/`isReadOnly`/`isReferenceUnit`/`isSeparateSaveUnit`/`setReadOnly`/`setSeparateSaveUnit`/`setUnitPath`; properties `CMHeader`/`currentDirectory`/`filename`/`includeInNextLoad`/`isStub`/`structureDiagrams`; landing this row resolves IRPModelElement's cross-catalog blockers.
- [x] ① §1 — 7 shared step tasks + 29-member inventory (all owned; inherited `IRPModelElement` members kept separate)
- [x] ② §2 — report Java package `com.telelogic.rhapsody.core` agrees with `IRPUnit.html`; `RPUnit` → `IRPUnit` renamed, then wrapper + `AddToModelMode` moved to `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_unit.py`; mirrored tests at `tests/{unit,integration}/models/com/telelogic/rhapsody/core/test_irp_unit.py`; canonical `__init__.py` lazy exports; all internal imports updated; `core.py:get_save_unit()` imports locally before `cast()` (no cycle; quoted types unnecessary under `from __future__ import annotations`); no compatibility shim. Doubled-prefix artifacts from the bulk rename were fixed repo-wide.
- [x] ③ §3 — 0 deviations, 29 owned members; 21 legacy dual-binding sites mapped one-to-one to pywin32 members; catalog-absent `getUnitPath` left unchanged as expected informational difference; no python-only members)
- [x] ④ §4 — 10 tests red → green; structural guard (21 offenders → 0) + future-annotations guard added; full unit suite 1714 green; canonical `irp_unit.py` coverage 100% (68/68 statements, 40/40 branches)
- [x] ⑤ §5 — mirrored canonical path, 22 tests collected; Windows live run 15 passed / 3 skipped (pre-existing `second_test_project` TODO fixture) / 4 xfailed (pre-existing getUnitPath COM gaps), no failures
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_unit.md` (SWR_CORE_00002 moved out of `swr_core_requirements.md`, no duplicate; canonical implementation path)
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_unit.rst` (anchor + 7-row deviation list-table covering getUnitPath/setUnitPath and method-vs-property shapes; canonical import; toctree wired in `docs/api/elements.rst`)
- [x] ⑧ §8 — `validate_interface.py` ✓ (0 deviations), `verify_sync.py` ✓ (artifacts verified), skill self-tests 15 ✓, full unit suite 1714 ✓, ruff/black/mypy ✓, Windows live integration ✓

</details>

<details>
<summary><code>irp_model_element_api_report</code> · IRPModelElement · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** re-run completed 2026-11-21 under the updated skill (shape-follows-COM, future annotations, own-members report + Correct Items, Java-package declaration). Class renamed `RPModelElement` → `IRPModelElement`; python-only `get_oslc_links` removed (stale premise — `getOSLCLinks` is exposed by pywin32); `core.py` converted to `from __future__ import annotations` with unquoted type references and local runtime imports for `cast()` (25 casts + 84 annotations); `wrap()` reads the `metaClass` property; RPCollection migrated; IRPUnit's 21 sites remain for its own row.
- [x] ① §1 — sync TODO published (per-run checklist rendered live)
- [x] ② §2 — `IRPModelElement` → `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py`, `AbstractRPModelElement` stays in `models/core.py` with a local import in `wrap()`; 78 import sites updated; mirrored unit/integration test files moved; canonical `__init__.py` and RST import path updated.
- [x] ③ §3 — 1 actionable blocker `get_rmm_url` left unchanged, 96 correct items, 5 backlog rows; python-only `get_oslc_links` removed per §4 — report row disappears at closeout regeneration)
- [x] ④ §4 — no quoted casts/annotations, `from __future__ import annotations` present; full unit suite 1711 green)
- [x] ⑤ §5 — integration tests (mirror unit/integration files verified exercising `IRPModelElement` via `test_core.py`; behavior-preserving; Windows live run tracked in Step 8)
- [x] ⑥ §6 — SWR update (`docs/requirements/com/telelogic/rhapsody/core/irp_model_element.md` — binding rules, `get_rmm_url` blocker, deferred-move note, future-annotations fact)
- [x] ⑦ §7
- [x] ⑧ §8 — report regenerated with canonical target line, `validate_interface.py` ✓, `verify_sync.py` ✓, 0 skip/xfail markers, 100% statement/branch coverage at both unit and integration layers, 105 live integration tests ✓, full unit suite ✓, ruff/black/mypy ✓; commits `6cbebc3` + `1778607` + `5175b93`)

</details>
