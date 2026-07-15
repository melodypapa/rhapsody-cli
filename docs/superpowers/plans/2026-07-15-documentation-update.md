# Documentation Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update README.md and docs/index.rst to reflect v0.2.0 changes including snake_case API, new CLI command structure, and current test count.

**Architecture:** Documentation-only changes across two files. README.md needs test count update. docs/index.rst needs version, test count, API examples, CLI examples, and architecture diagram updates.

**Tech Stack:** Markdown, reStructuredText, Sphinx documentation.

## Global Constraints

- All method names use snake_case (e.g., `get_name`, `add_class`, `get_packages`)
- CLI command groups: `project`, `package`, `class`, `attribute`, `operation`, `port`
- No `element` or `io` command groups (removed in v0.2.0)
- Current test count: 1519 unit tests
- Current version: 0.2.0
- Changelog already updated in README.md

---

## File Structure

| File | Changes |
|------|---------|
| `README.md` | Update test count from 936 to 1519 |
| `docs/index.rst` | Update version, test count, API examples, CLI examples, architecture diagram |

---

## Task 1: Update README.md test count

**Files:**
- Modify: `README.md:175-177` (test count in Development section)
- Modify: `README.md:204-207` (test count in Test Coverage section)

- [ ] **Step 1: Update test count in Development section**

In `README.md`, find line 176:
```markdown
# Run all unit tests (936 tests, no Rhapsody installation required)
```

Replace with:
```markdown
# Run all unit tests (1519 tests, no Rhapsody installation required)
```

- [ ] **Step 2: Update test count in Test Coverage section**

In `README.md`, find line 204:
```markdown
- **936 unit tests** covering all wrapped methods and edge cases
```

Replace with:
```markdown
- **1519 unit tests** covering all wrapped methods and edge cases
```

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "docs: update test count from 936 to 1519"
```

---

## Task 2: Update docs/index.rst version and test count

**Files:**
- Modify: `docs/index.rst:8` (version)
- Modify: `docs/index.rst:49` (test count)

- [ ] **Step 1: Update version**

In `docs/index.rst`, find line 8:
```rst
**Current Version**: 0.1.0
```

Replace with:
```rst
**Current Version**: 0.2.0
```

- [ ] **Step 2: Update test count**

In `docs/index.rst`, find line 49:
```rst
* **Test-Driven**: Comprehensive test suite with 161+ tests
```

Replace with:
```rst
* **Test-Driven**: Comprehensive test suite with 1519 tests
```

- [ ] **Step 3: Commit**

```bash
git add docs/index.rst
git commit -m "docs: update version to 0.2.0 and test count to 1519"
```

---

## Task 3: Update docs/index.rst API examples to snake_case

**Files:**
- Modify: `docs/index.rst:95-127` (Basic Usage section)

- [ ] **Step 1: Update Basic Usage API examples**

In `docs/index.rst`, find lines 95-127. Replace the entire Basic Usage section with:

```rst
Basic Usage
~~~~~~~~~~~

Connect to Rhapsody and open a project:

.. code-block:: python

   from rhapsody_cli.application import RhapsodyApplication

   app = RhapsodyApplication()
   app.connect()  # Try to attach to existing instance, then launch if needed

   project = app.open_project("C:\\path\\to\\project.rpy")

Access model elements:

.. code-block:: python

   # Get all packages
   packages = project.get_packages()

   # Find a specific package
   package = project.find_nested_package_by_name("MyPackage")

   # Get all classes in a package
   classes = package.get_classes()

   # Create a new class
   new_class = package.add_class("NewClass")

   # Add attributes and operations
   attribute = new_class.add_attribute("myAttribute")
   operation = new_class.add_operation("myOperation")

Close the project:

.. code-block:: python

   project.close()
   app.disconnect()
```

Key changes:
- `openProject` → `open_project`
- `getPackages` → `get_packages`
- `findNestedPackageByName` → `find_nested_package_by_name`
- `getClasses` → `get_classes`
- `createClassElement` → `add_class`
- `createAttribute` → `add_attribute`
- `createOperation` → `add_operation`

- [ ] **Step 2: Commit**

```bash
git add docs/index.rst
git commit -m "docs: update API examples to snake_case naming"
```

---

## Task 4: Update docs/index.rst CLI examples to new command structure

**Files:**
- Modify: `docs/index.rst:129-161` (Command-Line Usage section)

- [ ] **Step 1: Update Command-Line Usage section**

In `docs/index.rst`, find lines 129-161. Replace the entire Command-Line Usage section with:

```rst
Command-Line Usage
~~~~~~~~~~~~~~~~~~~

View available commands:

.. code-block:: bash

   rhapsody-cli --help

Project management:

.. code-block:: bash

   rhapsody-cli project new "C:\Models" NewProject
   rhapsody-cli project open "C:\path\to\project.rpy"
   rhapsody-cli project list
   rhapsody-cli project close

Package management:

.. code-block:: bash

   rhapsody-cli package create --path Sensors '{"name":"Actuators"}'
   rhapsody-cli package view --path Sensors/Actuators --format json
   rhapsody-cli package list --path Sensors --format table
   rhapsody-cli package update --path Sensors/Actuators '{"description":"Updated"}'
   rhapsody-cli package delete --path Sensors/Actuators

Class management:

.. code-block:: bash

   rhapsody-cli class create --path Sensors '{"name":"TemperatureSensor"}'
   rhapsody-cli class view --path Sensors/TemperatureSensor --format json
   rhapsody-cli class list --path Sensors
   rhapsody-cli class link --path Sensors/TemperatureSensor --add BaseSensor
   rhapsody-cli class update --path Sensors/TemperatureSensor '{"isAbstract":true}'
   rhapsody-cli class delete --path Sensors/TemperatureSensor

Attribute, Operation, and Port management:

.. code-block:: bash

   rhapsody-cli attribute create --path Sensors/TemperatureSensor '{"name":"threshold","type":"int"}'
   rhapsody-cli operation create --path Sensors/TemperatureSensor '{"name":"readValue"}'
   rhapsody-cli port create --path Sensors/TemperatureSensor '{"name":"clientPort"}'

   rhapsody-cli attribute list --path Sensors/TemperatureSensor
   rhapsody-cli attribute update --path Sensors/TemperatureSensor --name threshold '{"isStatic":true}'
   rhapsody-cli attribute delete --path Sensors/TemperatureSensor --name threshold
```

Key changes:
- Removed `element query`, `element view` examples (deprecated)
- Added `package`, `class`, `attribute`, `operation`, `port` command examples
- Updated to match current CLI structure

- [ ] **Step 2: Commit**

```bash
git add docs/index.rst
git commit -m "docs: update CLI examples to new command structure"
```

---

## Task 5: Update docs/index.rst architecture diagram

**Files:**
- Modify: `docs/index.rst:246-283` (Project Structure section)

- [ ] **Step 1: Update Project Structure diagram**

In `docs/index.rst`, find lines 246-283. Replace the Project Structure section with:

```rst
Project Structure
-----------------

.. code-block:: text

   src/rhapsody_cli/
   ├── __init__.py                    # Public API exports
   ├── application.py                 # RhapsodyApplication entry point
   ├── exceptions/                    # Exception types
   │   ├── __init__.py
   │   └── core.py                   # RhapsodyConnectionError, RhapsodyRuntimeException
   ├── models/                        # Element wrappers
   │   ├── __init__.py
   │   ├── core.py                   # RPModelElement, RPCollection, wrap(), call_com()
   │   ├── application.py            # RhapsodyApplication COM wrapper
   │   └── elements/                 # Specific element types
   │       ├── __init__.py
   │       ├── classifiers/          # RPClass, RPActor, RPOperation, RPAttribute, etc.
   │       ├── containment/          # RPPackage, RPProject, RPComponent, etc.
   │       ├── relations/            # RPRelation, RPGeneralization, RPPort, etc.
   │       ├── diagrams/             # RPDiagram and subclasses
   │       ├── activity/             # RPFlowchart, RPFlow, RPFlowItem
   │       ├── statemachine/         # RPStatechart, RPState, RPTransition
   │       ├── interactions/         # RPCollaboration, RPMessage
   │       ├── graphics/             # RPGraphElement, RPGraphNode
   │       ├── common/               # RPType, RPConstraint, etc.
   │       ├── values/               # RPEnumerationLiteral
   │       ├── templates/            # RPTemplateParameter, RPTemplateInstantiation
   │       ├── requirements/         # RPRequirement, RPAnnotation
   │       └── variables/            # RPVariable, RPArgument
   ├── commands/                      # CLI command groups
   │   ├── __init__.py
   │   ├── abstract_command.py       # AbstractCommand base class
   │   ├── project_command.py        # ProjectCommand
   │   ├── package_command.py        # PackageCommand
   │   ├── class_command.py          # ClassCommand
   │   ├── attribute_command.py      # AttributeCommand
   │   ├── operation_command.py      # OperationCommand
   │   └── port_command.py           # PortCommand
   ├── actions/                       # CLI subcommand actions
   │   ├── __init__.py
   │   ├── abstract_action.py        # AbstractAction, RhapsodyContextAction
   │   ├── project_action.py         # Project subcommand actions
   │   ├── package_action.py         # Package subcommand actions
   │   ├── class_action.py           # Class subcommand actions
   │   ├── attribute_action.py       # Attribute subcommand actions
   │   ├── operation_action.py       # Operation subcommand actions
   │   └── port_action.py            # Port subcommand actions
   └── cli/                           # CLI entry point and support
       ├── main.py                   # Entry point (re-exports cli.main)
       ├── cli.py                    # main() dispatcher
       ├── context.py                # RhapsodyContext (state management)
       ├── formatters.py             # OutputFormatter (table/JSON/CSV)
       └── logging_config.py         # CliLoggingConfigurator
```

Key changes:
- `_core.py` → `core.py`
- Added `application.py` in models/
- Reorganized `elements/` subpackages to match current structure
- Updated `commands/` to list new command files
- Updated `actions/` to list new action files
- Removed deprecated `element_command.py`, `element_action.py`

- [ ] **Step 2: Commit**

```bash
git add docs/index.rst
git commit -m "docs: update architecture diagram to reflect v0.2.0 structure"
```

---

## Task 6: Update docs/index.rst Supported Element Types section

**Files:**
- Modify: `docs/index.rst:284-313` (Supported Element Types section)

- [ ] **Step 1: Update Supported Element Types section**

In `docs/index.rst`, find lines 284-313. Replace the Supported Element Types section with:

```rst
Supported Element Types
-----------------------

The package currently wraps **50+ element types** including:

**Containment Elements**: Project, Package, Profile, Module, Configuration, Node, Component, ComponentInstance, Collaboration

**Classifier Elements**: Class, Actor, UseCase, Interface, InterfaceItem, Stereotype, Statechart, Operation, AssociationClass, Signal, Exception, Enumeration

**Relation Elements**: Relation, Instance, Dependency, Generalization, Hyperlink, AssociationRole

**Activity Elements**: Flowchart, Flow, FlowItem, DecisionNode, MergeNode, ForkNode, JoinNode

**Statechart Elements**: State, Transition, Trigger

**Interaction Elements**: Message, ClassifierRole, DiagramObject

**Leaf Elements**: Attribute, Tag, Requirement, Variable, Annotation, Constraint, EnumerationLiteral, Diagram, Comment

**Support Elements**: CodeGenerator, SearchManager, Selection, ProgressBar, File, ControlledFile

Plus **hundreds of generic methods** from `RPModelElement` available on all element types.
```

Key changes:
- Added Activity Elements category
- Added Statechart Elements category
- Added Interaction Elements category
- Added Support Elements category
- Updated Classifier Elements to include Signal, Exception, Enumeration

- [ ] **Step 2: Commit**

```bash
git add docs/index.rst
git commit -m "docs: update supported element types list"
```

---

## Task 7: Verify Sphinx build

- [ ] **Step 1: Build Sphinx documentation**

Run:
```bash
cd docs
.\make.bat html
```

Expected: Build succeeds with no warnings

- [ ] **Step 2: Check for warnings**

If any warnings appear, fix them and rebuild.

- [ ] **Step 3: Final commit (if any fixes needed)**

```bash
git add docs/
git commit -m "docs: fix Sphinx build warnings"
```

---

## Task 8: Final verification and push

- [ ] **Step 1: Verify all changes are committed**

Run:
```bash
git status
git log --oneline -5
```

Expected: Working tree clean, 7-8 commits visible

- [ ] **Step 2: Push to remote**

```bash
git push origin HEAD
```

Or create a PR if on a feature branch.

---

## Self-Review Checklist

**Spec coverage:**
- [x] README.md test count (936 → 1519) — Task 1
- [x] docs/index.rst version (0.1.0 → 0.2.0) — Task 2
- [x] docs/index.rst test count (161+ → 1519) — Task 2
- [x] docs/index.rst API examples (camelCase → snake_case) — Task 3
- [x] docs/index.rst CLI examples (element → package/class/etc.) — Task 4
- [x] docs/index.rst architecture diagram (_core.py → core.py, new structure) — Task 5
- [x] docs/index.rst supported elements list — Task 6
- [x] Sphinx build verification — Task 7

**Placeholder scan:** No placeholders found — all sections contain actual content.

**Type consistency:**
- All method names use snake_case throughout ✓
- All CLI commands match current implementation ✓