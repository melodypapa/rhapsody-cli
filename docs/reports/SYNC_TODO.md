# Sync TODO — `docs/reports` Interface Queue

Tracking list for bringing every interface report in `docs/reports/` (and its wrapper) to the
pywin32-direct binding rule. **One interface per sync run** — follow
[`.agents/skills/rhapsody-sync/SKILL.md`](../.agents/skills/rhapsody-sync/SKILL.md) and render
that run's live checklist before starting the next. Reference pilot: `IRPClass`
(commit `7163149`, migrated 2026-11-21).

## Standing rules for every run

- Binding rule: every wrapper member calls exactly **one** pywin32-exposed COM member from
  `pywin32_authority.json` — method-shaped via `call_com(lambda: self._com.Name(...))`,
  property-shaped via `get_com_property` / `set_com_property`. No runtime name probing.
- A call site whose member is absent from the catalog for that interface is a **blocker**:
  leave it unchanged, record it, do not migrate on unverifiable evidence.
- Inherited members keep base-class behavior until the base class's own run.
- Machine split (as of 2026-11-21): macOS can run the TDD migration, unit suite, and quality
  gate; the JavaDoc tree (`docs/java_api/`) is gitignored and absent, so **report regeneration,
  `validate_interface.py`, and `verify_sync.py` must run on the Windows machine** as the run's
  closeout step. Record the blocker in the run's sync report until then.

## Shared per-run checklist

- [ ] Baseline evidence: committed report + catalog entry present (`validate_interface.py <IFACE> --source authority` where possible; otherwise record blocker).
- [ ] Move wrapper to the canonical package `src/rhapsody_cli/models/com/telelogic/rhapsody/core/<snake_case>.py`, update imports/exports/registration, and move its unit + integration tests to the mirrored test package (`tests/{unit,integration}/models/com/telelogic/rhapsody/core/test_<snake_case>.py`).
- [ ] TDD: update the class's unit tests first (red), then migrate every legacy `_get_method_or_property` / `_set_method_or_property` site in the class's **own** methods (green). Fakes use `make_fake_element(properties={...})` for property-shaped members.
- [ ] Update the class checklist comment and any docstrings referencing the legacy helper.
- [ ] Update the class's deviation list-table in `docs/api/elements.rst` and its entry in `docs/requirements/swr_elem_requirements.md`.
- [ ] Verify: full unit suite, `ruff`/`black`/`mypy`, `pytest -o addopts= .agents/skills/rhapsody-sync/tests -q`, integration collection-only (macOS).
- [ ] Windows closeout: regenerate the report (`validate_interface.py <IFACE> --source authority`), run `verify_sync.py <IFACE>`, commit report artifacts.
- [ ] Render the run's sync-report checklist (every box ticked or blocker stated).

## Queue — catalog-covered interfaces (16 reports)

Order: core.py bases first (removes inherited fallback for every subclass), then leaves.
Legacy-site counts from the 2026-11-21 survey — re-survey at run start (`grep -c` per wrapper).

| # | Interface | Wrapper | Current location | Legacy sites | Status |
|---|-----------|---------|------------------|-------------:|--------|
| 0 | IRPClass | `IRPClass` | `models/com/telelogic/rhapsody/core/irp_class.py` | 0 | ✅ done (pilot, `7163149`) |
| 1 | IRPModelElement | `RPModelElement` | `models/core.py` | ~86 | ☐ not started |
| 2 | IRPCollection | `RPCollection` | `models/core.py` | ~2 (core.py total 92 incl. 2 forwarders) | ☐ not started |
| 3 | IRPUnit | `RPUnit` | `models/core.py` | (within core.py 92) | ☐ not started |
| 4 | IRPClassifier | `RPClassifier` | `models/elements/classifiers/model_classifier.py` | 20 | ☐ not started |
| 5 | IRPOperation | `RPOperation` | `models/elements/classifiers/model_operation.py` | 25 | ☐ not started |
| 6 | IRPAttribute | `RPAttribute` | `models/elements/variables/model_variables.py` | (within 14 w/ IRPArgument) | ☐ not started |
| 7 | IRPPort | `RPPort` | `models/elements/relations/model_port.py` | 10 | ☐ not started |
| 8 | IRPPackage | `RPPackage` | `models/elements/containment/model_package.py` | 36 | ☐ not started |
| 9 | IRPProject | `RPProject` | `models/elements/containment/model_project.py` | 24 | ☐ not started |
| 10 | IRPType | `RPType` | `models/elements/common/model_other_model.py` | 9 | ☐ not started |
| 11 | IRPArgument | `RPArgument` | `models/elements/variables/model_variables.py` | (within 14 w/ IRPAttribute) | ☐ not started |
| 12 | IRPApplication | `RhapsodyApplication` | `application.py` | 3 | ☐ not started |
| 13 | IRPAssociationClass | `RPAssociationClass` | `models/elements/classifiers/model_association_class.py` | 3 | ☐ not started |
| 14 | IRPInterfaceItem | `RPInterfaceItem` | `models/elements/classifiers/model_interface_item.py` | 4 | ☐ not started |
| 15 | IRPUseCase | `RPUseCase` | `models/elements/classifiers/model_usecase.py` | 4 | ☐ not started |

Note on runs 1–3: `core.py` holds `AbstractRPModelElement` (2 forwarder definitions),
`RPModelElement`, `RPCollection`, and `RPUnit` — 92 legacy sites total. Survey and split them
per class at each run's start; `AbstractRPModelElement.wrap()` (`getMetaClass`/`metaClass`)
migrates with IRPModelElement. IRPModelElement also has 22 sites whose names live only in
**other** interfaces' catalogs (unit-family members such as `CMHeader`, `filename`,
`isReadOnly`) — resolve those against `IRPUnit`'s catalog entry, or record a blocker.

## Backlog — uncovered interfaces (blocked on catalog evidence)

380 legacy sites across wrappers whose interfaces have **no** catalog entry. Every run here is
blocked until the catalog is regenerated on Windows (`python scripts/pywin32_authority.py
--source typelib`) and the new interface reports are committed. Do not migrate blind.

Interactions (66), Graphics (51), Codegen/support (35), StateVertex/State (31), Relation (27),
Configuration (23), Activity actions (19), Component (17), RPVariable/RPTag (16),
Files (12), Annotation/Requirement (10), Statechart (10), Activity flows (10), Templates (9),
IDE support (8), Instance (6), Generalization (5), AssociationRole (3), Stereotype (3),
ClassifierRole (1), SysMLPort (3), Values (2), HyperLink (2), Dependency (2), Diagram (2),
Node (2), EnumerationLiteral/Comment/Constraint (2), Actor (2), Collaboration (1).

## Termination

- [ ] After the last covered-interface run and the unblocked backlog runs: delete
      `_get_method_or_property` / `_set_method_or_property` from `com_utils.py` / `core.py`,
      drop the legacy notes from `AGENTS.md` / `CODE_GUIDELINES.md` / the sync skill, and
      confirm `grep -r "_method_or_property" src/` is empty.
