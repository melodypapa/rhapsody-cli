# Sync todo — `classifiers` (group 2 of 2)

**6 classes** · ✅ 6 archived · ⬜ 0 open

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
| 1 | `irp_interface_item_remediation` | IRPInterfaceItem | — | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 2 | `irp_classifier_api_report` | IRPClassifier | `models/elements/classifiers/model_classifier.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 3 | `irp_operation_api_report` | IRPOperation | `models/elements/classifiers/model_operation.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 4 | `irp_association_class_api_report` | IRPAssociationClass | `models/elements/classifiers/model_association_class.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 5 | `irp_interface_item_api_report` | IRPInterfaceItem | `models/elements/classifiers/model_interface_item.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 6 | `irp_usecase_api_report` | IRPUseCase | `models/elements/classifiers/model_usecase.py` | — | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |

## Row details

<details>
<summary><code>irp_interface_item_remediation</code> · IRPInterfaceItem · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Baseline:** JavaDoc and report declare `com.telelogic.rhapsody.core`; seven owned members, zero validator deviations. Existing canonical wrapper/tests/exports verified.
- [x] ① §1 — member checklist published; both getter matrix rows include fixture, relationship, identity/value assertion, test, and package cleanup.
- [x] ② §2 — canonical wrapper, mirrored tests, imports/exports, and registration verified; report package agrees with JavaDoc.
- [x] ③ §3 — all seven owned members reconciled and matched. Live COM showed `addArgumentBeforePosition` expects zero-based position although JavaDoc specifies 1-based; wrapper converts `pos - 1`. Report regenerated; no actionable deviations.
- [x] ④ §4 — unit test first failed on the position conversion, then passed after the minimal wrapper fix. Focused unit coverage: 100% statements and branches (25 statements, 10 branches); full unit suite: 2,172 passed.
- [x] ⑤ §5 — four live integration tests pass, including populated `arguments` identity, exact operation/signature values, insertion order, and positive/negative signature matching. Fixtures delete their test packages; no exception assertions, skips, or xfails. Full integration suite: 449 passed.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_interface_item.md` updated with JavaDoc class description and verified COM position conversion.
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_interface_item.rst` corrected to JavaDoc description and complete canonical identity; all seven public members documented; page already present in `docs/api/elements.rst` toctree.
- [x] ⑧ §8 — report regenerated; `validate_interface.py`, `verify_sync.py`, and `--strict-getters` pass; sync self-tests 83 passed; `ruff`, `black`, and `mypy` clean; baseline → final counts: unit 2,171 → 2,172 passed, integration 449 → 449 passed. Integration exception-catch list: none. Commit is recorded by the commit that archives this row.
- Members: `addArgument(String)` matched; `addArgumentBeforePosition(String, int)` matched with documented 1-based → COM 0-based conversion; `getArguments()` → `arguments` matched/property; `getSignature()` → `signature` matched/property; `getSignatureNoArgNames()` matched; `getSignatureNoArgTypes()` matched; `matchOnSignature(IRPInterfaceItem)` matched.

</details>

<details>
<summary><code>irp_classifier_api_report</code> · IRPClassifier · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived. Duplicate row for IRPClassifier also in Group-classifiers-1.md.
- **Note:** 3 method-shaped (`getAttributesIncludingBases`, `getInterfaceItemsIncludingBases`, `getRelationsIncludingBases`), rest property-shaped.
- [x] ① §1
- [x] ② §2
- [x] ③ §3 — baseline `validate_interface.py IRPClassifier --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
- [x] ④ §4
- [x] ⑤ §5 — add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
- [x] ⑥ §6
- [x] ⑦ §7 — class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPClassifier:` + deviation list-table)
- [x] ⑧ §8 — `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

</details>

<details>
<summary><code>irp_operation_api_report</code> · IRPOperation · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived. Duplicate row for IRPOperation also in Group-classifiers-1.md.
- **Note:** 3 method-shaped (`setReturnTypeDeclaration`, `getReturnTypeDeclaration`, `getImplementationSignature`); `isAbstract`/`isStatic`/`isVirtual` are IRPOperation **properties** (arg2 wins — unlike IRPClass's method-exposed `getIsFinal`); `operation_action.py` facade stays untouched.
- [x] ① §1
- [x] ② §2
- [x] ③ §3 — baseline `validate_interface.py IRPOperation --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
- [x] ④ §4
- [x] ⑤ §5 — add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
- [x] ⑥ §6
- [x] ⑦ §7 — class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPOperation:` + deviation list-table)
- [x] ⑧ §8 — `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

</details>

<details>
<summary><code>irp_association_class_api_report</code> · IRPAssociationClass · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived. Duplicate row for IRPAssociationClass also in Group-classifiers-1.md.
- **Note:** integration-test ownership rules apply — assert only `get_end1`/`get_end2`/`get_is_class`/`set_is_class`.
- [x] ① §1
- [x] ② §2
- [x] ③ §3 — baseline `validate_interface.py IRPAssociationClass --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
- [x] ④ §4
- [x] ⑤ §5 — add/update integration coverage for owned behavior only (own-method assertions; mirrored test path); Windows = live run, macOS = collection-only noted
- [x] ⑥ §6
- [x] ⑦ §7 — class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPAssociationClass:` + deviation list-table)
- [x] ⑧ §8 — `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

</details>

<details>
<summary><code>irp_interface_item_api_report</code> · IRPInterfaceItem · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** 2 method-shaped (`getSignatureNoArgNames`, `getSignatureNoArgTypes`).
- [x] ① §1
- [x] ② §2
- [x] ③ §3 — baseline `validate_interface.py IRPInterfaceItem --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
- [x] ④ §4
- [x] ⑤ §5 — add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
- [x] ⑥ §6
- [x] ⑦ §7 — class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPInterfaceItem:` + deviation list-table)
- [x] ⑧ §8 — `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

</details>

<details>
<summary><code>irp_usecase_api_report</code> · IRPUseCase · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived. Duplicate row for IRPUseCase also in Group-classifiers-1.md.
- **Note:** RPExtensionPoint lives in the same module with 0 legacy sites.
- [x] ① §1
- [x] ② §2
- [x] ③ §3 — baseline `validate_interface.py IRPUseCase --source authority`; reconcile every owned member; one pywin32 member per call; catalog-absent sites = blockers
- [x] ④ §4
- [x] ⑤ §5 — add/update integration coverage for owned behavior (mirrored test path); Windows = live run, macOS = collection-only noted
- [x] ⑥ §6
- [x] ⑦ §7 — class RST page `docs/api/com/telelogic/rhapsody/core/<snake_case>.rst` (anchor `.. _rhapsody-java-interface-IRPUseCase:` + deviation list-table)
- [x] ⑧ §8 — `validate_interface.py` + `verify_sync.py` + skill self-tests + full unit suite + ruff/black/mypy (Windows: live integration); render the sync-report checklist

</details>
