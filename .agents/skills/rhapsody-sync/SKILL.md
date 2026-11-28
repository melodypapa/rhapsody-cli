---
name: rhapsody-sync
description: "Use when bringing an IRP* Python wrapper to parity with its JavaDoc — JavaDoc/pywin32/Python method parity, pywin32 or COM binding mismatches, moving a wrapper or its tests to the Java-derived package path, or writing the per-class API report, requirement page, or RST API reference — even when the user says 'bring IRPClass up to date' rather than 'sync'. Do not use for read-only API questions, CLI usage, user-guide edits, or unrelated code."
license: MIT
author: rhapsody-cli maintainers
repository: https://github.com/melodypapa/rhapsody-cli
version: 0.1.0
product-version: 0.1.0
spec-version: 1.0.0
keywords: [rhapsody, javadoc, com, api-sync, python]
agents: [pi]
---

# Rhapsody API sync

Sync one requested Java API interface with its Python wrapper in this project. The input is the JavaDoc interface name (such as `IRPClass`), not a hard-coded Python class. The Python class keeps the same name as the Java interface, so treat `IRPClass` as the example pattern, never as the default target.

## When to use, and when not to

Use this skill whenever the request is, in any phrasing, about bringing one IRP* interface's Python wrapper in line with its JavaDoc: "sync IRPClass", "bring IRPActor up to date", "audit IRPPort for parity", a wrapper missing JavaDoc methods or calling COM members pywin32 does not expose, a wrapper whose tests must move to the Java-derived package path, or a per-class report/requirement/RST page that must be refreshed as part of such a sync.

Do not use it for read-only API questions, CLI command work, user-guide edits, JavaDoc HTML fixes, package-architecture proposals, generated tables that never inspect the wrapper, COM connection troubleshooting, or one-off fixes that do not touch a wrapper's COM bindings or public surface. When the request names several interfaces, pick one (ask which, if ambiguous), run it end to end, and leave the others for their own runs.

## 1. Create the sync TODO list

Before any analysis or edit, publish the TODO list: use an available task-list tool, otherwise show the Markdown checklist in the response. Keep the shared steps concise, then add a subtask for every target-owned JavaDoc member so no method is silently skipped:

```markdown
## Sync TODO — IRPClass (`com.telelogic.rhapsody.core`)
- [ ] §2 Resolve JavaDoc package, class description, and member inventory; move wrapper + tests to the canonical package.
- [ ] §3 Compare every owned member across JavaDoc, COM exposure, and Python implementation.
- [ ] §4 Write/upgrade the fake-COM unit tests first (red), then migrate the binding call sites (green) — each Python member's shape (method vs `@property`) follows the COM shape, and synced wrappers use `from __future__ import annotations` with unquoted type references.
- [ ] §5 Add/update integration tests in the mirrored test package.
- [ ] §6 Update the class requirement document (per-class, package path).
- [ ] §7 Write the class RST API reference (per-class, package path) documenting every public wrapper member.
- [ ] §8 Run validation (unit suite, gate, validate_interface, verify_sync); summarize unresolved items.
- [ ] Render this checklist as the final sync report.
- [ ] Member: addExample() — [ ] JavaDoc [ ] COM [ ] wrapper [ ] disposition
- [ ] Getter: getClasses() — [ ] JavaDoc [ ] COM [ ] wrapper [ ] create class [ ] relate class to package [ ] assert returned collection contains that class [ ] cleanup
```

For every getter member, render the Getter fixture matrix row from §1 and keep it open until the setup, relation, positive retrieval assertion, test path, and cleanup are evidenced. A generic fixture-builder task or an empty-state assertion does not complete the getter row.

This checklist is the run's live report. Tick a checkbox in the same response where its evidence lands — a command result, a test count, a documented disposition — and never batch-tick at the end. A box ends the run either ticked or open with the blocker and reason stated next to it. Only mark a task done after checking its evidence. Keep inherited-member notes separate from owned-member tasks.

Use these class-level completion statuses consistently: `✅ archived` means every live integration case passed; `⚠️ complete with deviation` means every target integration case either passed or is an explicitly user-approved, evidence-backed skip, and every unit/API/documentation/quality gate passed. `Complete with deviation` completes the class's API-sync work, not live verification: keep each member-level blocker and linked issue open, report live pass/skip counts, and never describe skipped behavior as live-green or the full suite/PR as green. Any unapproved skip, missing approval/reason/ledger entry, or unskipped target failure keeps the class open.

## 2. Resolve the target and move to the canonical package

If the interface name is missing or ambiguous, ask for it before editing. Find its JavaDoc in `docs/java_api/`, read the declared package, then resolve the matching wrapper, base class, tests, and current exports. Do not infer the Java package or wrapper mapping from the existing Python folder alone.

The canonical Python package mirrors every Java package segment beneath `rhapsody_cli.models`, and the Python class name matches the Java interface name — never the legacy `RP*` facade name. Every derived name uses the Java interface's snake_case too: the module file (`IRPClass` → `irp_class.py`), the mirrored test modules (`test_irp_class.py`), and the per-class requirement/RST documents (`irp_class.md` / `irp_class.rst`). For example:

- Java: `com.telelogic.rhapsody.core.IRPClass`
- Python import: `from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass`
- Directory: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_class.py`

Every canonical `docs/reports/<java.package.path>/<INTERFACE>_api_report.md` carries a `- Java package: <package>` line in its Summary; the authority snapshot remains at `docs/reports/pywin32_authority.json`. Use the report's package — cross-checked against the JavaDoc directory — when deriving the canonical model class package `rhapsody_cli.models.<java.package.path>` and the mirrored `docs/requirements/<java.package.path>/` and `docs/api/<java.package.path>/` paths. If the line is missing or disagrees with the JavaDoc, stop and record it as a blocker; regenerate the report first with `python scripts/validate_model_api.py <INTERFACE> --source authority --path docs/reports` (or `--source typelib` on Windows with Rhapsody); the report is written under its package path before moving any wrapper or tests.

Move the wrapper only if it is not already in the canonical package. Add package `__init__.py` exports, preserve registration/import side effects, and update every internal reference to the canonical import. Keep the existing module naming convention where practical. Do not leave a compatibility shim at the old path for the migrated interface. Migrate only the requested interface; avoid unrelated package moves and refactors. If moving it safely requires broad changes or would break public imports, stop and ask before expanding scope.

Both unit and integration tests move with it, mirroring the canonical package segment by segment — the same report-declared Java package as the wrapper. Use snake_case for the test module name derived from the Java interface (`IRPClass` → `test_irp_class.py`), and add `__init__.py` at every mirrored directory level. For example:

- Unit test: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_class.py`
- Integration test: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_class.py`

Do not leave the class's tests under an old domain folder such as `tests/unit/models/elements/classifiers/`.

## 3. Compare evidence efficiently, without skipping coverage

Run the skill-local wrapper once for a baseline and use its report as the member-by-member index:

```bash
python .agents/skills/rhapsody-sync/scripts/validate_interface.py <INTERFACE> --source authority
```

The helper locates the project root and delegates to the canonical `scripts/validate_model_api.py`; it does not duplicate that logic. A nonzero exit of `1` means actionable deviations were found, not that validation crashed. A nonzero exit of `2` is a setup failure: missing JavaDoc, or offline validation without COM evidence. On Windows with Rhapsody available, use `--source typelib` to inspect the registered binding. Without Rhapsody, the COM evidence is the committed report pair `docs/reports/<java.package.path>/<INTERFACE>_api_report.md` plus `docs/reports/pywin32_authority.json`, and the helper exits with a blocker when that evidence is missing. If the committed report exists but the catalog lacks the interface, rebuild the catalog recursively from the package-organized reports with `python scripts/pywin32_authority.py --source reports` (on Windows you may instead regenerate from the live binding with `--source typelib`) and commit the refreshed JSON. If the committed report does not exist, exit the sync: with neither Rhapsody nor a committed report there is no COM evidence to compare against — record the missing package-path report as the blocker on the corresponding TODO and stop; do not edit wrapper code, tests, or docs on unverifiable evidence. The validator resolves the Java package from the selected JavaDoc and writes the report under `docs/reports/<java.package.path>/`; use a fully qualified interface name when a simple name is ambiguous.

Use these sources for different questions:

| Source | Trust it for | Do not infer |
| --- | --- | --- |
| JavaDoc HTML | Declared package, Java API, signatures, descriptions | That COM exposes a callable member |
| pywin32 catalog/type library | COM member presence and method/property shape | The complete Java contract or wrapper behavior |
| Python wrapper | Actual facade, COM calls, conversions, and return wrapping | That an absent wrapper is intentionally unsupported |

Reconcile every member declared by the target interface against the validator inventory. To save time, inspect implementation bodies and secondary references deeply for deviations, missing coverage, unsupported members, and code you will change; do not reread unrelated wrappers or inherited implementations. Check JavaDoc descriptions for the class and each method being added or changed. If evidence conflicts, record the sources and ask rather than guessing.

**Deviation buckets are strict: a finding is demoted only by evidence, never by label.** `apply_pywin32_authority()` in `scripts/validate_model_api.py` is the bucket authority — actionable rows land in `Comparison details`; only a documented `documented_unavailable` decision for a JavaDoc member absent from pywin32, a verified correct binding, a verified inherited implementation, or a documented alias referencing the row's own Java member moves a row into `Expected Binding Differences`. `documented_intentionally_unsupported` is a legacy catalog field and must not be added or used to waive a pywin32-exposed member in a new sync. `MISSING_PYTHON_WRAPPER`, `PYWIN32_ONLY_MEMBER`, `ACCESSOR_ALIAS_MISMATCH`, and `METHOD_PROPERTY_MISMATCH` are actionable findings — implement the member or verify that the target's Python MRO already supplies the exact catalog binding. `documented_unavailable` entries that the catalog actually exposes are ignored with a warning instead of hiding wrappable work.

For each target-owned JavaDoc member, track: Java name/signature and description; inherited vs owned; COM method/property/alias/unavailable status; Python method and actual COM call; result type/wrapping; and a disposition. Use concise dispositions such as matched, inherited, binding mismatch, JavaDoc-only, COM-only, missing wrapper, or unresolved. A missing static COM member is not by itself a removal decision. Compare JavaDoc presence, pywin32 presence, and whether the Python body forwards to that COM member. Section 4 defines the treatment: JavaDoc-only methods become documented `NotImplementedError` stubs; COM-forwarding methods absent from both contracts are removed; local Python lifecycle/orchestration APIs such as `RhapsodyApplication.connect()` are retained.

**Pywin32-exposed members must be implemented in the target wrapper or inherited from a base wrapper.** Before adding a target-class method for a catalog member, inspect the Java superinterfaces and the Python base-class MRO. If the member is inherited and a base wrapper already forwards to the exact pywin32 member with the catalog's shape and signature, mark it `inherited` and use that implementation; do not create a duplicate child override. For example, `IRPPackage.add_association` is inherited from `IRPModelElement` and its parent implementation satisfies the package API. If no inherited binding exists, implement the catalog member even when it is absent from the target interface's direct JavaDoc, and document it as a COM-only extension. Never use `documented_intentionally_unsupported` to close a catalog-exposed gap.

For every getter or collection-valued property, add one row to the sync TODO's **Getter fixture matrix**. This is a required output field, not an optional note:

| Java getter / Python member | Real parent and expected child/value | JavaDoc-verified setup and relationship | Expected returned identity/value | Integration test | Cleanup |
| --- | --- | --- | --- | --- | --- |
| `getClasses()` / `classes` | the test package and the class created for this case | create the class with the package's documented add method | returned collection contains that exact class | mirrored test path + test name | delete the test package |

Complete a row for every target-owned getter, including getters owned by `IRPApplication`; its application-layer location is not an exclusion. For a model relationship or collection, name the concrete child and how it is attached; for an application/environment scalar, name the real source and expected value. A generic "fixture builder" entry does not complete these rows.

The authoritative machine-readable copy lives in `docs/reports/sync-todo/getter-matrix.md`, one `## <INTERFACE>` section per wrapper. Seed or refresh a section with `python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE> --write-getter-matrix` (it derives the property list from the wrapper and the test references from the mirrored integration file), then replace `MISSING`/`WEAK` rows with the real test when the name convention does not find it. `verify_sync.py` fails Step 8 when the file, the interface section, or a row for an owned getter is absent, when a row's assertion/status pair disagrees, or when a referenced test no longer exists.

**Verify the full COM signature, not just the member name.** When comparing evidence, check that the wrapper's COM call matches the pywin32 member's parameter count and types, not only that the member name exists. `pywin32_authority.json` stores a `signatures` section captured from the type library (parameter `count`, `required`, `names`, and `types`; `required` excludes trailing parameters that makepy gives Python defaults for). The validator emits `SIGNATURE_ARITY_MISMATCH` / `SIGNATURE_TYPE_MISMATCH` as actionable rows in `Comparison details` — counted in the Summary and failing the run — when a `call_com(lambda: self._com.Name(...))` passes a count outside the `required`..`count` band or a non-convertible parameter type (numeric/bool variants convert at the COM boundary). Treat these as actionable deviations that must be fixed before archiving — a correct member name with wrong arguments still fails at runtime. JavaDoc may document fewer parameters than the type library; pywin32/COM is authoritative for the call shape.

Never add a direct COM call for a member absent from the binding. Keep exact camelCase COM identifiers and snake_case Python names. Follow `AGENTS.md` for `call_com`, property helpers, argument unwrapping, result wrapping, collection handling, annotations, and exception handling. In particular, do not add `Any`. Synced wrappers use `from __future__ import annotations` and write type references unquoted (e.g. `-> IRPClass`, not `-> "IRPClass"`); a name used only in `cast()` must be imported at runtime (a local import inside the method avoids circular imports).

Bindings are pywin32-authoritative: every wrapper member depends on exactly one pywin32-exposed COM member, with no runtime name probing or Java-name fallback. Method-shaped members are called with `call_com(lambda: self._com.Name(...))`; property-shaped members are read/written with `get_com_property` / `set_com_property` (name confirmed against `docs/reports/pywin32_authority.json`). Legacy dual-binding call sites (`_get_method_or_property` / `_set_method_or_property`) are migrated as part of the sync — see section 4.

**The Python-facing shape follows the COM shape recorded in `docs/reports/<java.package.path>/<INTERFACE>_api_report.md`.** The report's pywin32 column is the authority for whether a member is a method or a property: a member listed as `method` is exposed as a snake_case Python method that calls `call_com(lambda: self._com.Name(...))`; a member listed as `property` is exposed as a Python `@property` (a setter only when the member is writable) backed by `get_com_property` / `set_com_property`. Do not turn a COM method into a Python `@property` (or a COM property into a method) for style reasons — the Python surface mirrors the COM definition in the report. This is machine-enforced, not advisory: `verify_sync.py` compares each binding's enclosing Python member (decorators included) with the catalog shape, so a property-shaped binding in a plain `def` — or a method-shaped binding under `@property` — fails Step 8. A documented deviation (for example a Java-name alias resolved as `ALIAS_DOCUMENTED`) may keep the Python member name, but it cannot waive this shape rule; record the COM shape and the reason in the report and fix the member shape.

## 4. Write the unit tests first (TDD)

Follow TDD: write or update a focused fake-COM unit test before changing behavior or import wiring. Unit tests must not use real COM. For each wrapper method added or changed, use JavaDoc for its description, arguments, and return contract while retaining project-specific usage notes and known runtime limitations.

**No xfailed or unapproved skipped model-class tests.** Unit tests must all run and pass; unit skips and all xfails are forbidden. An integration test may use `@pytest.mark.skip(reason="...")` only when (a) the user has explicitly approved that exact method in the current session, (b) the reason records the observed live result or unmet precondition, and (c) the exact interface/member is listed in the central P0 blocker report and linked issue. Never use `pytest.skip(...)` in a test body or an unconditional early return. A skip is a deviation, not a pass. When all non-skipped target integration tests pass, all skips meet these conditions, and every other sync/quality gate passes, the class may be marked `⚠️ complete with deviation` under §1; leave the blocker rows and issues open and do not describe the class as live-verified. Any unapproved skip or unskipped target failure keeps the class open. This rule applies to every model class, not only the one being synced. Step 8 machine-checks the mirrored unit and integration test files: `pytest.mark.xfail`, `pytest.skip(...)`, `pytest.xfail(...)`, and any skip marker in a unit test fail; an integration `@pytest.mark.skip` must carry a non-empty `reason=`, while exact user approval and matching ledger/issue entries are checked manually.

**100% coverage from the unit layer.** The unit tests alone must give 100% statement and branch coverage of the synced wrapper module, measured with `PYTHONPATH=src python -m pytest <unit test file> --cov=<canonical module> --cov-report=term-missing`. Integration tests exercise the wrapper against live Rhapsody with authentic data, but there is **no coverage percentage gate on the integration layer**; integration tests only need to pass and assert real outcomes. Do not combine unit and integration coverage to reach the unit gate, and do not count a line covered only by integration. Add unit tests rather than lowering the threshold, excluding lines, or adding `# pragma: no cover`. State the measured unit figure and the integration pass/fail counts in the sync report.

**Migrate legacy binding call sites for this class.** For every `_get_method_or_property` / `_set_method_or_property` call in the class's **own** methods: look up the pywin32 member for that operation in `docs/reports/pywin32_authority.json`, then rewrite the site to a direct call — method-shaped → `call_com(lambda: self._com.Name(...))`, property-shaped → `get_com_property` / `set_com_property` — and expose the member with the shape the catalog declares (`@property` for property-shaped, a plain method for method-shaped); `verify_sync.py` fails any remaining legacy helper, direct `self._com.<Name>` access, or mismatched Python member shape. Update the class's unit tests to configure and assert on that single member (fakes use the `properties=` channel of `make_fake_element` for property-shaped members). Inherited members keep base-class behavior until the base class's own sync run. If a call site's member is absent from the catalog for this interface, record it as a blocker and leave the site unchanged — do not migrate on unverifiable evidence.

Run the full unit suite after the change and fix any failure before continuing; never advance to the next step with a failing unit test (verification rules in section 8).

**Treat unavailable and Python-only members by evidence, not status label alone.** For every member compare its JavaDoc declaration, pywin32 catalog entry, and Python implementation:

| JavaDoc | pywin32 | Python behavior | Required treatment |
| --- | --- | --- | --- |
| Present | Absent | Any | Keep the Java-signature Python method as a stub that raises `NotImplementedError`; do not attempt a COM call or runtime name probe. List the Java member in `documented_unavailable`, test it in both the fake-COM unit layer and the live integration layer, and document the limitation in the generated report's deviation table (never in the RST — section 7). The unit test must verify no COM dispatch occurs; the integration test must invoke the stub through the normal concrete-wrapper fixture and assert the same exception. |
| Present | Present, call proven ineffective | Wrapper forwards to the exact catalog member; live result is ineffective | Keep the exact COM binding. Do not replace it with a `NotImplementedError` stub or assert the COM failure; record the unmet live behavior as a blocker and retain the JavaDoc/catalog evidence in the sync report. |
| Present | Present, JavaDoc itself declares the member unimplemented | Wrapper forwards to the exact catalog member and preserves the JavaDoc warning | Pywin32 exposure still requires the wrapper binding. Quote the JavaDoc warning in the wrapper docstring; if a live call cannot be exercised safely or returns an unusable result, leave an integration blocker rather than replacing the binding with a `NotImplementedError` stub. |
| Absent | Absent | Directly forwards to a COM member | Remove the unsupported Python wrapper method and its tests/docs/RST row (e.g. `RhapsodyApplication.close_all_projects()` forwarding to `closeAllProjects`). Search callers with `grep -rn "<python_name>" src/rhapsody_cli` and migrate them to a supported API. If callers cannot be migrated safely, leave the sync blocked; do not claim the removal complete. |
| Absent | Absent | Pure Python lifecycle/orchestration, not a wrapper for a missing COM member | Retain the Python API (e.g. `RhapsodyApplication.connect()`, which selects attach/launch behavior). Do not remove it solely because the validator labels it `PYTHON_ONLY_MEMBER`; keep its report/RST treatment explicit as a Python-only helper. |
| Present | Present | Wrapper calls a different/unexposed name | Migrate to the exact catalog member and its method/property shape, following section 3. |
| Present in a Java superinterface; absent from target's direct declarations | Present | Base wrapper calls the exact catalog member | Use the inherited implementation and mark the member `inherited`; do not add a duplicate child override. |
| Absent from all JavaDoc | Present | No direct or inherited Python binding | Implement the catalog member as a COM-only extension with the catalog's method/property shape; do not mark it intentionally unsupported. |

A method-shaped Java API member missing from pywin32 is intentionally unavailable, not Python-only. Its stub must preserve the Java method signature and raise `NotImplementedError` immediately. A COM-forwarding method absent from both JavaDoc and pywin32 is unsupported and must be removed once callers are migrated. Never use a blanket rule that deletes every `PYTHON_ONLY_MEMBER`: first determine whether it is an unsupported COM forwarding method or a supported pure-Python application helper.

**Wrappable gaps must be implemented.** `MISSING_PYTHON_WRAPPER` (JavaDoc and pywin32 expose the member, but no direct or inherited Python binding exists) and `PYWIN32_ONLY_MEMBER` (COM-only member with no inherited binding) require a wrapper in this sync. A correct inherited binding satisfies the requirement; `documented_intentionally_unsupported` does not. An accessor family flagged `ACCESSOR_ALIAS_MISMATCH` / `METHOD_PROPERTY_MISMATCH` is likewise actionable unless the wrapper demonstrably calls exactly the exposed member with the catalog's shape; a derived status or decision label never justifies skipping wrappable work.

## 5. Update the integration tests

Add or update integration coverage only for supported behavior owned by this wrapper; inherited methods may set up fixtures but are not child assertions. Respect the integration-test ownership rules in `AGENTS.md`, including child overrides with different return contracts. Integration tests live in the mirrored test path from section 2 — do not leave them under an old domain folder. These rules target the mirrored model-wrapper tests under `tests/integration/models/**`; CLI-level integration tests under `tests/integration/cli/` follow their own conventions and are outside this section and the Step 8 scan.

**No exception catching in integration tests, with one exception.** An integration test must never assert that a call raises `AttributeError`, `RhapsodyRuntimeException`, `TypeError`, `ValueError`, or any other COM failure. Such assertions bless a wrong or unverified binding. The only permitted `pytest.raises(NotImplementedError)` assertion is for a JavaDoc-defined member absent from the pywin32 catalog, whose wrapper stub raises before dispatch and whose evidence is recorded as `documented_unavailable` (section 4). A catalog-exposed member must use its direct or inherited COM binding; do not replace it with a runtime or JavaDoc-unimplemented stub, even when a live call is ineffective or JavaDoc warns against use. In that case, keep the exact binding and record the missing live precondition or ineffective result as an open blocker; do not assert the COM failure. Do not use `try`/`except` at all in test bodies, no broad `except` / helper that accepts a documented exception or a completed call, and no `except <Exception>: pass` cleanup guards that mask a stale-session cascade; fix the session instead. Record the permitted `NotImplementedError` assertions (JavaDoc-defined, pywin32-absent only) in the sync report (section 8).

**Design integration cases from JavaDoc with authentic data — never dummy inputs.** Before writing an integration test for a wrapper method, read its JavaDoc signature (`docs/java_api/<java.package.path>/<INTERFACE>.html`) to learn each parameter's real meaning, return contract, and preconditions, then build a test that supplies **authentic data**: create the required real Rhapsody objects first (a package, class, element, diagram, etc.) and pass their real identifiers/objects — e.g. for `find_element_by_binary_id(binary_id)`, actually create an element, read its real `BinaryID`, and assert the element is found; for `find_element_by_file_name(name)`, use a real file name from the live project. Do not pass fabricated strings such as `"arg"` / `"x"` / generated UUIDs as placeholders and do not give up with a mocked COM binding or an exception assertion when a real setup is possible — a mocked binding proves only the call shape, not that the method works against Rhapsody. A test that passes only because a fake or dummy value is used does not validate the method. If a genuine precondition cannot be satisfied live (e.g. an external file or license is unavailable), record it as a real blocker on the TODO and leave the row open rather than substituting mock data. Delete or clean up any objects the test creates so the session-shared project is left intact.

**Negative lookups are the one exception to "authentic inputs".** When the method's contract is to report absence (`find_*` returning `None`, an empty collection, or `0`), pass a key that is generated per run, guaranteed not to exist in the live project, and checked absent before the call — for example `missing = f"missing_{uuid.uuid4().hex}"`. That key is a verified negative fixture, not a dummy value: it must not replace a positive-path lookup of a real object, and the assertion must be the documented empty result (`None` / empty collection / `0`), never an exception.

### Getter tests must prove retrieval from live data

**A getter integration task is complete only when its populated-state assertion passes or the member remains an open blocker.** Time pressure, an already-green smoke test, a generic fixture-builder, shared-project concerns, or a request to keep scope small do not turn an empty-state, type-only, count-only, or non-`None` assertion into getter coverage.

For each JavaDoc getter or collection-valued property, build the positive fixture that its contract needs, invoke the getter on the object that owns the relationship, and assert that it returns the object or value created by the test. For a collection getter, assert the created child is present (prefer object identity or a stable model identifier); a non-`None` result, type check, or count by itself does not prove the getter retrieves the right member. Every getter's matrix row must point to this populated-state assertion and its test; an empty-state assertion cannot close the getter's integration task. Step 8 machine-checks getter tests grouped by property (`test_<property>`, `test_get_<property>`, and their `_empty`/`_empty_state` variants): if every assertion in the group is non-`None`, `isinstance`, `len`, truthiness, an empty-collection literal, or `assert True`, Step 8 fails and points at the group's tests.

```python
import uuid

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


def test_get_classes_returns_class_attached_to_package(test_project: IRPProject) -> None:
    package = test_project.add_package(f"GetterPkg_{uuid.uuid4().hex}")
    created_class = package.add_class(f"GetterClass_{uuid.uuid4().hex}")
    try:
        classes = list(package.classes)
        assert created_class in classes
    finally:
        package.delete_from_project()
```

Apply the same setup → relation → retrieval → identity/value assertion to application-level getters. For example, `IRPApplication.get_list_of_selected_elements()` needs a real model element placed in an `IRPCollection`, passed to the documented `select_model_elements()` API, then verified in the returned collection. Restore the prior application selection through a documented API during cleanup; deleting the selected object alone does not prove that shared application state was restored. Read JavaDoc and the pywin32 catalog before choosing setup or cleanup calls; do not infer or invent APIs such as `select()`, `deselect()`, or `setSelected()` from a getter's name. Getters whose contract reads application, filesystem, or environment state use a real value from that source and assert against it instead of creating an unrelated model object.

An empty-state test is an additional case: establish that the parent has no related child and assert the documented empty result. It does not replace the populated-state getter test. Do not defer a missing populated getter test to a follow-up ticket or exclude it as "out of scope" while claiming the interface synced. If the required relationship or state cannot be created through a verified live API, record the unmet precondition as an open blocker; do not substitute a dummy value, a fake COM object, a type/count-only check, or a non-`None` smoke assertion.

The no-xfail/no-unapproved-skip rule in section 4 applies here too. A user-approved integration skip must identify the exact owned method and observed live blocker, and be entered in the central blocker report and linked issue. It does not count as an executed or passing test. If every non-skipped test for the target class passes and the approved skips are the only remaining integration cases, §5 may be marked `complete with deviation`; record live pass/skip counts, keep the blocker issue open, and preserve the distinction from fully live-verified coverage. Any remaining unskipped failure keeps §5 open. Documented-unavailable Java-member stubs still require a live integration assertion that the method raises `NotImplementedError`; the test does not need the absent COM member because the stub must raise before dispatch. Collection-only evidence never substitutes for a pass or an approved, evidence-backed skip.

## 6. Update the class requirement document

Create or update the class's own requirement file at
`docs/requirements/<java.package.path>/<snake_case>.md` — `<java.package.path>` is the Java
package declared in the report's Summary (section 2), mirrored beneath `docs/requirements/`
regardless of where the wrapper currently lives (for example
`docs/requirements/com/telelogic/rhapsody/core/irp_class.md` for
`IRPClass`). Use the JavaDoc class description for the summary, but retain project-specific
requirements and implementation facts that JavaDoc cannot express. Keep the existing SWR
entry format (`ID`, `Title`, `Status`, `Priority`, `Description`, `Implementation`,
`Last Changed`); the `ID` stays stable when the entry moves. When migrating a class out of
the legacy monolith `docs/requirements/swr_elem_requirements.md`, move its entry into the
per-class file — do not duplicate it; leave unrelated and not-yet-migrated entries in the
monolith until their own sync run moves them.

## 7. Write the class RST API reference

Create or update the class's API page at `docs/api/<java.package.path>/<snake_case>.rst` —
`<java.package.path>` is the same report-declared Java package as in section 6, mirrored
beneath `docs/api/` regardless of where the wrapper currently lives (for example
`docs/api/com/telelogic/rhapsody/core/irp_class.rst` for `IRPClass`). Start the
page with the verifier-recognized anchor `.. _rhapsody-java-interface-<INTERFACE>:` and
include the Java interface, Java package, JavaDoc-derived description, Python wrapper, and
canonical import path. Promote the class heading to the page title.

**The page is a JavaDoc-style API reference of the Python wrapper — not a deviation
report.** After the identity block, add an `API reference` section that introduces the
class (description borrowed from the JavaDoc) and documents **every public member** of the
wrapper: its Python signature and a description borrowed from the JavaDoc, translated to
the wrapper's contract. Prefer `.. autofunction::` / `.. autoattribute::` directives per
member so descriptions flow from the wrapper docstrings (which mirror the JavaDoc) instead
of duplicating them; explicit member sections are acceptable when a member needs extra
narrative. `verify_sync.py` fails the page when any public wrapper member's name does not
appear in it.

Keep deviations out of the RST: they are the generated report's content (section 3's
`<INTERFACE>_api_report.md`, regenerated and committed every sync per section 8), not the
API reference's. Do not reproduce deviation or backlog tables here. Keep the page reachable
by listing it in `docs/api/elements.rst`'s toctree under
the Java package heading (one entry per synced class). When migrating a class out of
the legacy `elements.rst` sections, move its section — do not duplicate it; leave unrelated and
not-yet-migrated classes unchanged. Keep RST navigation valid.

## 8. Verify and report

After edits, run final validation and artifact checks:

```bash
python .agents/skills/rhapsody-sync/scripts/validate_interface.py <INTERFACE> --source authority
python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE>
python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE> --strict-getters
python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE> --write-getter-matrix
python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE> --write-getter-diff
python -m pytest -o addopts= .agents/skills/rhapsody-sync/tests -q
PYTHONPATH=src python -m pytest tests/unit -q -o addopts=
PYTHONPATH=src python -m pytest tests/integration -q -o addopts=
```

`verify_sync.py` checks that the report declares `- Java package: <package>` in its Summary and that the value agrees with the JavaDoc, then verifies Java-package-derived wrapper placement, the class requirement entry, and the RST anchor plus API-reference coverage: the RST page must document every public member of the wrapper class (names compared against the wrapper source). It also parses the wrapper body and checks every COM binding (`call_com(lambda: self._com.Name(...))`, `get_com_property`/`set_com_property(..., "Name", ...)`) against `docs/reports/pywin32_authority.json`: each member must exist for the interface and match the catalog's method/property shape (names compared case-insensitively, since COM identifiers are case-insensitive). The enclosing Python member must follow that shape too — a property-shaped binding in a plain `def` or a method-shaped binding under `@property` fails — and any direct `self._com.<Name>` access or remaining `_get_method_or_property` / `_set_method_or_property` helper fails as well. A Java-named member absent from pywin32, or a member bound with the wrong shape, fails Step 8 — this catches syncs that document a `COM_MEMBER_NOT_EXPOSED` blocker but leave the wrapper calling the unexposed name. It also scans the mirrored integration test file and fails Step 8 on any `pytest.raises` other than `NotImplementedError` or on any `try`/`except` handler (section 5) — a wrong binding cannot be kept green by asserting its failure, and a caught failure cannot masquerade as a pass; `try`/`finally` cleanup without an `except` clause stays allowed. The same scan applies to both mirrored unit and integration test files: `pytest.mark.xfail`, `pytest.skip(...)`, `pytest.xfail(...)`, and any skip marker in a unit test fail (section 4); an integration `@pytest.mark.skip(reason="...")` remains the documented approved-skip case, with its approval and ledger entry checked manually. The mirrored integration file must also contain no `finally` block whose only statement is `pass` — an empty cleanup shell that leaves created objects in the session-shared project (section 5). For each owned property, getter tests are grouped by the property name they target: `test_<property>`, `test_get_<property>`, and the `_empty` / `_empty_state` variants of either all count toward the same property. A property fails Step 8 when every test in its group is weak — all assertions are non-`None`, `isinstance`, `len`, truthiness (`assert not x`, `assert x`), `== []`/`{}`/`()`/`set()`, `is not None`, or `assert True`. At least one group member must create the related object and assert identity/value (section 5); an empty-state test is allowed only when a populated sibling covers the same property. It also validates `docs/reports/sync-todo/getter-matrix.md`: the interface section must exist, contain one row per owned property, use a known `identity/value`/`weak`/`none` assertion with its matching `OK`/`WEAK`/`MISSING` status, and reference an integration test that still exists; missing sections, missing rows, stale rows for removed properties, and dangling test references fail Step 8. It also validates the `## NotImplementedError stubs` table in `docs/reports/sync-todo/index.md`: for a new sync, only a `not-exposed` stub is permitted; legacy `java-doc-unimplemented` and `runtime-stub` rows may still be recognized for historical classes, but must be replaced with exact catalog bindings when those classes are synced. A not-exposed stub must have one ledger row and `pytest.raises(NotImplementedError)` assertions in both unit and integration layers; missing or stale rows fail Step 8. It also compares every wrapper `call_com` call arity against the pywin32 signature captured in the authority catalog (parameter band `required`..`count`), so a correct member name called with the wrong number of arguments fails Step 8; parameter-type comparison remains the validator's job (section 3). `verify_sync.py <INTERFACE> --write-getter-diff` regenerates the `## <INTERFACE>` section of `docs/reports/sync-todo/getter-catalog-diff.md`, a per-getter record of the Python binding, the COM member, both shapes, and a status (`match`, `catalog-missing`, `shape-mismatch`, `no-binding`, `stub`) plus catalog properties with no Python property of the derived snake_case name in the wrapper MRO (`catalog-only`, a review candidate). It is a review artifact, not a gate: binding correctness remains enforced by the binding scan above, and `catalog-only` rows need a human decision rather than an automatic failure. An advisory inherited-member scan reports integration assertions that reference only parent-class members (the AGENTS.md own-method scope); pass `--strict-inherited` to promote those notes to failures. An exit code of `1` lists incomplete or mismatched artifacts. Also run import/registration checks, relevant lint/type checks, and RST/Sphinx validation when available.

Verification rules (each row cites the section that fully specifies it — this table is the pre-finish checklist):

| Rule | Requirement | From |
| --- | --- | --- |
| Report package line | The report Summary declares `- Java package: <package>` and the value equals the JavaDoc's declared package (`IRPClass` is the reference case); regenerate the report before claiming success. | §2 |
| Report regenerated every sync | Regenerate `docs/reports/<java.package.path>/<INTERFACE>_api_report.md` from current evidence (`python scripts/validate_model_api.py <INTERFACE> --source authority`, or `--source typelib` on Windows with Rhapsody) and commit it with the sync; never hand-edit it or leave it stale after a binding change — it is the artifact Step 8 is validated against. | §3 |
| Report contents | State the measured unit-layer coverage figure (statements and branches, 100%) with the exact `pytest --cov=<module>` command and its result line, plus integration pass/fail/skip counts, exact approved-skip members with reasons and issue links, and the section 5 exception-catch list; a row is not complete until they appear. | §1, §4, §5 |
| Python member shape matches COM | Every binding's enclosing Python member follows the catalog shape — `@property` (setter only when writable) for property-shaped members, a plain method otherwise; no direct `self._com.<Name>` access and no `_get_method_or_property` / `_set_method_or_property` helpers. `verify_sync.py` fails Step 8 when this is violated. | §3, §4 |
| Unit suite green at every step | Fix any failure before continuing; never advance to the next step or finish with a failing unit test. | §4 |
| No regressions | Record baseline pass/fail counts for the full unit and integration suites before editing; re-run both afterwards and confirm every previously passing test still passes. A moved/renamed wrapper must not break another class's tests, and a mirrored test file must not be deleted simply to make a suite green. On Windows, run the full integration suite against a freshly launched Rhapsody instance (never a stale process); if a single live COM call faults the automation server, isolate that call with a mocked COM binding in its test rather than letting the suite cascade. Any new unskipped target failure is a blocker. Approved skips may support only the `complete with deviation` status in §1; unrelated/pre-existing class failures remain separately tracked and never count as passes. | — |
| Mirrored tests exercise the class | `verify_sync.py` requires `tests/{unit,integration}/models/.../test_<snake>.py` (mirroring the wrapper's package) to exist and exercise the wrapper class; run the focused unit test with coverage on the wrapper module and state the measured coverage in the report. | §2 |
| Approved skips only; unit 100% | `verify_sync.py` fails Step 8 on `pytest.mark.xfail`, `pytest.skip(...)`, `pytest.xfail(...)`, or any skip marker in a mirrored unit test; in the mirrored integration test an `@pytest.mark.skip(reason="...")` must carry a non-empty reason, and exact user approval plus the central blocker/issue entries are checked manually. It also fails on any `finally` block containing only `pass`. Keep `grep -rnE "skip\|xfail" <test files>` to confirm every approved skip carries a reason and matching report/issue entries. Measure coverage on the canonical wrapper module from the unit test file alone — 100% statements and branches. Integration tests have no coverage gate; combined figures do not satisfy the unit gate. A class may be `complete with deviation` only when every non-skipped target integration test passes and the approved skips are the sole remaining target cases; keep each live issue open and do not claim live-green or archive as fully verified. | §1, §4, §5 |
| Windows integration disposition | On Windows, run the migrated class's focused integration tests against live Rhapsody. Every unskipped target case must pass; a remaining case may be skipped only with explicit user approval, a non-empty evidence-based reason, and central report/issue entries. Report pass/skip counts. Collection-only is not a live test, and a `complete with deviation` status is not live-green. | §4, §5 |
| Getter fixture matrix complete | Every owned getter has a matrix row naming the real parent, related child/value, JavaDoc-verified setup, getter assertion by identity/value, test path, and cleanup. Populated live retrieval passes; an empty/type/count/non-`None` check alone is not evidence. `verify_sync.py` groups `test_<property>`, `test_get_<property>`, and their `_empty`/`_empty_state` variants per property and fails Step 8 unless at least one test in the group asserts identity/value; a weak empty-state test is accepted only alongside a populated sibling. The same run validates `docs/reports/sync-todo/getter-matrix.md` (section + one row per owned getter + resolvable test reference). `--strict-getters` additionally fails any `WEAK`/`MISSING` row whose member is not recorded in the P0 blocker table of `docs/reports/sync-todo/index.md`. A blocked getter remains an open member-level deviation even if the class is `complete with deviation`; use identity/value only for passing populated retrievals, never for a skipped case. | §1, §5 |
| Stub evidence ledger | For a new sync, `NotImplementedError` is allowed only when JavaDoc declares a member and pywin32 lacks it (`not-exposed`); catalog-exposed members require a direct or inherited COM binding. Legacy `java-doc-unimplemented`/`runtime-stub` ledger entries are migration debt, not acceptable new dispositions. | §4, §5 |
| Getter-catalog diff report | Regenerate the interface section of `docs/reports/sync-todo/getter-catalog-diff.md` with `verify_sync.py <INTERFACE> --write-getter-diff` after any getter change, and review the `catalog-only` candidates it lists. The report is a review artifact, not a gate; binding correctness stays with the Step 8 binding scan. | §8 |
| Non-Windows integration | Collection-only is acceptable **as import/collection evidence only**. It executes no Rhapsody call, so it does not satisfy §5 or close any Getter fixture matrix row; state which integration assertions and getter rows remain unverified in the report. Never report collection-only as "integration green". | §5, §8 |

Leave TODO items open when blocked, with the reason.

Finish by rendering the TODO checklist as the sync report: every shared step ticked with its key evidence (command result, integration pass/skip counts, files changed) or left open with the blocker and reason next to it, and every member line showing its final disposition. A class completed with approved skips is labeled `⚠️ complete with deviation`, not `✅ archived`; keep its issue and P0 blocker rows open. Lead the report with the Java interface/package, the old and canonical Python paths, and the files changed, followed by the checklist. Sync one interface per run; complete and review it before starting another.

## Red flags — stop and re-read the cited rule

Violating the letter of these rules is violating their spirit. Each row is a rationalization seen under pressure; the cited section is the counter.

| Rationalization | Reality |
| --- | --- |
| "I'll tick every checkbox at the end" | Tick each box in the response where its evidence lands; never batch-tick (§1). |
| "The generated report is nearly right; I'll adjust it by hand" | Reports are generated evidence — regenerate them, never hand-edit (§3, §8). |
| "Just this once, xfail or skip the flaky COM test" | No xfail or unapproved skip. An explicitly approved, evidence-backed skip must be recorded with the exact member in the P0 report and issue; it may count only toward `complete with deviation`, never as live-green or clean archive (§1, §4). |
| "Integration coverage must reach 100%" | There is no integration-layer coverage gate; only the unit layer must reach 100% statements and branches (§4). |
| "The test asserts the documented failure, so it is fine" | Exception assertions bless wrong bindings; only `NotImplementedError` stubs may be asserted (§5). |
| "Keep a shim so old imports keep working" | No compatibility shims — update every reference to the canonical import (§2). |
| "Deleting the stale mirrored test file makes the suite green" | That is a forbidden regression and a blocker, not a fix (§8). |
| "Two interfaces in one run is more efficient" | One interface per run; complete and review it before starting another (§8). |
| "pywin32 lacks the member, so drop the Java API too" | JavaDoc-present members become documented `NotImplementedError` stubs, never removals (§4). |
| "The COM name is close enough to the catalog entry" | Bind exactly one catalog member with its recorded method/property shape — no probing, no fallback (§3). |
| "The report lists it as expected difference or backlog, so there is nothing to do" | A pywin32-exposed member must be implemented directly or inherited; `documented_intentionally_unsupported` cannot waive it (§3, §4). |
| "A getter method is fine even though COM exposes a property" | Property-shaped catalog members must be exposed as `@property` (setter only when writable); a property-shaped binding in a plain `def` fails Step 8 (§3, §8). |
| "`self._com.Name(...)` or the legacy helper is shorter" | Direct COM access and `_get_method_or_property` / `_set_method_or_property` probes fail Step 8; use `call_com` or the property helpers (§3, §4). |
| "The getter returned a non-`None` collection, so it is covered" | Create a real related object, attach/select it through a documented API, then assert the getter returns that object (§5). |
| "An empty collection or type/count check is enough" | Empty state is an additional case; the Getter fixture matrix still needs a populated fixture and an identity/value assertion (§1, §5). |
| "The selection method is probably `select()`" | Verify setup APIs in JavaDoc and the pywin32 catalog; never invent a setup call to make a getter test pass (§5). |
| "Any invented string is fine for an absent-value lookup" | Negative lookups need a per-run key verified absent and must assert the documented empty result, never an exception (§5). |
| "Collection-only ran clean, so integration is green" | Collection-only proves import/collection only; report it as unverified and keep getter rows open (§5, §8). |
| "A generic fixture-builder task covers the getters" | Complete one Getter fixture matrix row per getter with its real parent, related data, assertion, and cleanup (§1). |
| "Application-level getters are outside the model-class audit" | Include every getter owned by the requested interface, including `IRPApplication`; use real app state or related model data according to its contract (§1, §5). |
| "We'll add populated getter cases after the release" | The interface stays open until every supported getter has its populated live assertion or a documented blocker (§5, §8). |
