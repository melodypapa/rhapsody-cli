# Class Command Design

**Date:** 2026-07-09
**Status:** Revised 2026-07-10 (COM signature corrections, scope reduced to generalization-only in `link`, requirement ID padding fix)
**Author:** User + Assistant

## Overview

Implement a `class` command group for managing Rhapsody RPClass elements via CLI. The design mirrors the existing `package` command structure, with 5 subcommands: create, delete, view, list, and link.

## Architecture

Follows the package command pattern exactly:

### AbstractClassAction (Base Class)

Base class with two path validation methods:

- `_resolve_and_validate_package(path)` - Validates path resolves to Package (metaClass == "Package"). Used by create and list.
- `_resolve_and_validate_class(path)` - Validates path resolves to Class (metaClass == "Class"). Used by delete, view, and link.

Inherits from `ElementManagementAction`.

### 5 Action Classes

1. **ClassCreateAction** - Create classes with bulk JSON support, validated attributes
2. **ClassDeleteAction** - Delete a class via `deleteFromProject()`
3. **ClassViewAction** - View class details in table/JSON/CSV formats
4. **ClassListAction** - List classes in a package via `getClasses()`
5. **ClassLinkAction** - Add/remove generalization relationships between classes (v1 — association/unidirectional deferred to future iteration due to COM signature complexity)

## Subcommands

### create

Create one or multiple classes under a parent package.

**Arguments:**
- `--path <parent-package-path>` (required) - Parent package path
- `--input <json-file>` (optional) - External JSON file
- `attributes` (positional, optional) - Inline JSON or JSON file path

**Validated Attributes:**

| Attribute | Type | COM Method |
|-----------|------|------------|
| `name` | string (required) | `package.addClass(name)` |
| `description` | string | `setDescription()` |
| `isAbstract` | bool | `setIsAbstract(1/0)` |
| `isFinal` | bool | `setIsFinal(1/0)` |
| `isActive` | bool | `setIsActive(1/0)` |
| `stereotypes` | array of strings | `addStereotype(name, "Class")` |
| `tags` | dict (key-value) | `setPropertyValue(key, val)` |
| `operations` | array of strings | `addOperation(name)` |
| `attributes` | array of strings | `addAttribute(name)` |
| `superclasses` | array of strings | `addGeneralization(classifier)` — each name resolved via `findNestedClassifierRecursive(name)` on parent package, then `addGeneralization(target_classifier)` on the new class (`model_classifier.py:100`) |

**Bulk creation:** Supports JSON array for creating multiple classes at once.

**Unknown attributes:** Skipped with warning log.

**External JSON file support:** Detects inline JSON (starts with `{` or `[`) vs file path automatically. Reads with UTF-8 encoding.

**Example JSON:**
```json
{
  "name": "TemperatureSensor",
  "description": "Temperature sensor class",
  "isAbstract": false,
  "isFinal": false,
  "isActive": false,
  "stereotypes": ["active"],
  "tags": {"status": "active"},
  "operations": ["readValue", "setThreshold"],
  "attributes": ["threshold", "unit"],
  "superclasses": ["BaseSensor"]
}
```

**Attribute setting methods (following single responsibility principle):**

- `_set_attributes()` - Orchestrates all attribute setting
- `_set_basic_attributes()` - Sets description
- `_set_boolean_flags()` - Sets isAbstract, isFinal, isActive
- `_set_properties()` - Sets custom properties (tags)
- `_set_stereotypes()` - Applies stereotypes
- `_set_operations()` - Adds operations
- `_set_attributes_list()` - Adds attributes
- `_set_superclasses()` - Adds generalization relationships

### delete

Delete a class.

**Arguments:**
- `--path <class-path>` (optional) - Class path to delete
- `--guid <guid>` (optional) - Class GUID to delete (format: `12345678-1234-1234-1234-123456789abc`)

**Behavior:**
- Exactly one of `--path` or `--guid` must be specified
- If `--path`: Resolves class via PathResolver, validates `metaClass == "Class"`
- If `--guid`: Locates class by GUID via `findElementByGUID()` on the project (`model_project.py:110`). Validates `metaClass == "Class"`.
- Calls `deleteFromProject()` on the resolved class. Logs deletion to stderr.

### view

View class details.

**Arguments:**
- `--path <class-path>` (optional) - Class path to view
- `--guid <guid>` (optional) - Class GUID to view (format: `12345678-1234-1234-1234-123456789abc`)
- `--format <table|json|csv>` (optional, default: table) - Output format
- `--output <file>` (optional) - Write to file instead of stdout

**Lookup behavior:**
- Exactly one of `--path` or `--guid` must be specified
- If `--path`: Resolves class via PathResolver, validates `metaClass == "Class"`
- If `--guid`: Locates class by GUID via `findElementByGUID()` on the project (`model_project.py:110`). Validates `metaClass == "Class"`.

**View Fields:**

| Field | Source Method |
|-------|---------------|
| Name | `getName()` |
| GUID | `getGUID()` |
| Description | `getDescription()` |
| IsAbstract | `getIsAbstract()` |
| IsActive | `getIsActive()` |
| IsFinal | `getIsFinal()` |
| IsComposite | `getIsComposite()` |
| IsReactive | `getIsReactive()` |
| MetaClass | `getMetaClass()` |
| FullPath | `getFullPathName()` |
| Operations | `getOperations()` — returns list of operation names (collected via `op.getName()`) |
| Attributes | `getAttributes()` — returns list of attribute names (collected via `attr.getName()`) |

**Note:** `getIsAbstract()` returns `bool`, while `getIsActive/Final/Composite/Reactive()` return `int` (0/1). The formatter normalizes to `int` in JSON output (matching the majority and ensuring clean round-trip with `create`'s `isAbstract: bool` input — accepts either type on input).

**Output Formats:**

**Table format:**
```
Property     | Value
-------------|---------------------
Name         | TemperatureSensor
GUID         | 12345678-1234-1234-1234-123456789abc
Description  | Temperature sensor
IsAbstract   | 0
IsActive     | 1
IsFinal      | 0
IsComposite  | 0
IsReactive   | 0
MetaClass    | Class
FullPath     | Sensors/TemperatureSensor
Operations   | readValue, setThreshold
Attributes   | threshold, unit
```

**JSON format:**
```json
{
  "name": "TemperatureSensor",
  "guid": "12345678-1234-1234-1234-123456789abc",
  "description": "Temperature sensor",
  "isAbstract": 0,
  "isActive": 1,
  "isFinal": 0,
  "isComposite": 0,
  "isReactive": 0,
  "metaClass": "Class",
  "fullPath": "Sensors/TemperatureSensor",
  "operations": ["readValue", "setThreshold"],
  "attributes": ["threshold", "unit"]
}
```

**CSV format (horizontal):**
```
Name,GUID,Description,IsAbstract,IsActive,IsFinal,IsComposite,IsReactive,MetaClass,FullPath,Operations,Attributes
TemperatureSensor,12345678-1234-1234-1234-123456789abc,Temperature sensor,0,1,0,0,0,Class,Sensors/TemperatureSensor,"readValue,setThreshold","threshold,unit"
```

**View-to-Create Workflow:** The JSON output from `view` can be used as input to `create`. Unknown fields (`guid`, `isComposite`, `isReactive`, `metaClass`, `fullPath`) are skipped during `create` with a warning. All other fields (`name`, `description`, `isAbstract`, `isActive`, `isFinal`, `stereotypes`, `tags`, `operations`, `attributes`, `superclasses`) round-trip cleanly.

### list

List classes in a package.

**Arguments:**
- `--path <package-path>` (required) - Package path
- `--format <table|json|csv>` (optional, default: table) - Output format
- `--output <file>` (optional) - Write to file instead of stdout

**Output Formats:**

**Table format:**
```
Name
--------------------
TemperatureSensor
PressureSensor
HumiditySensor
```

**JSON format:**
```json
["TemperatureSensor", "PressureSensor", "HumiditySensor"]
```

**CSV format (horizontal):**
```
Name
TemperatureSensor
PressureSensor
HumiditySensor
```

### link

Manage relationships between classes on an existing class.

**Arguments:**
- `--path <class-path>` (optional) - Class path to modify
- `--guid <guid>` (optional) - Class GUID to modify (format: `12345678-1234-1234-1234-123456789abc`)
- `--add <class-name>` (optional) - Add a generalization to target class by name
- `--remove <class-name>` (optional) - Remove a generalization to target class by name
- `--type <generalization>` (optional, default: generalization) - Relationship type (v1 supports only generalization; `--type` flag reserved for future expansion)

**Lookup behavior (source class):**
- Exactly one of `--path` or `--guid` must be specified
- If `--path`: Resolves class via PathResolver, validates `metaClass == "Class"`
- If `--guid`: Locates class by GUID via `findElementByGUID()` on the project (`model_project.py:110`). Validates `metaClass == "Class"`.

**Relationship Types (v1):**

| Type | COM Method (add) | COM Method (remove) |
|------|-------------------|---------------------|
| `generalization` | `addGeneralization(target_classifier)` — target resolved via `findNestedClassifierRecursive(name)` → `RPClassifier` object, then `addGeneralization(target)` (`model_classifier.py:100`) | `deleteGeneralization(target_classifier)` — same resolution, then `deleteGeneralization(target)` (`model_classifier.py:362`) |

**Behavior:**
- `--add`: Resolves the target class by name via `findNestedClassifierRecursive(name)` in the same package, calls `addGeneralization(target_classifier)`
- `--remove`: Resolves the target class by name via `findNestedClassifierRecursive(name)`, calls `deleteGeneralization(target_classifier)`
- Exactly one of `--add` or `--remove` must be specified
- If target name is not found, raises `CliExecutionError` with descriptive message

**Example:**
```
# Using path
rhapsody-cli class link --path Sensors/TemperatureSensor --add BaseSensor
rhapsody-cli class link --path Sensors/TemperatureSensor --remove BaseSensor

# Using GUID
rhapsody-cli class link --guid 12345678-1234-1234-1234-123456789abc --add BaseSensor
```

**Future work — association and unidirectional:** These relationship types are deferred to a future iteration. Their COM signatures require richer CLI surfaces:
- `addRelation` takes 9 string parameters (`model_classifier.py:146`) — class name, package name, two role names, two link types, two multiplicities, link name.
- `addUnidirectionalRelation` takes 6 string parameters (`model_classifier.py:260`).
- `deleteRelation` takes an `IRPRelation` object (`model_classifier.py:379`), requiring a `findRelation(name)` lookup (`model_classifier.py:479`) to obtain the handle.

Adding these would require exposing the extra parameters as CLI flags (e.g., `--role-from`, `--role-to`, `--mult-from`, `--mult-to`, `--link-name`) or defining sensible defaults.

## Path Validation

All commands validate path before execution (SWR_CLS_0005):

- **create, list**: Path must resolve to Package (metaClass == "Package" **or "Project"** to accept the project root, since `RPProject` inherits `addClass`/`getClasses` from `RPPackage`)
- **delete, view, link**: Path must resolve to Class (metaClass == "Class")
- Path resolution uses PathResolver for multi-level navigation
- Errors raised via CliExecutionError with descriptive message

## Error Handling and Logging

All class actions follow consistent error handling patterns (SWR_CLS_0010):

- Use `_handle_execution_error()` for COM errors
- Raise `CliExecutionError` for validation failures
- Log INFO for successful operations
- Log WARNING for skipped attributes
- Log ERROR for failures

## File Structure

**New files:**
- `src/rhapsody_cli/actions/class_action.py` - 6 Action classes (AbstractClassAction + 5 concrete)
- `src/rhapsody_cli/commands/class_command.py` - Command dispatcher
- `tests/unit/commands/test_class_commands.py` - Action and command tests (follows `test_package_commands.py` convention)
- `docs/requirements/swr_cls_requirements.md` - SW requirements
- `docs/tests/unit/uts_cls_test-specs.md` - Unit test specs
- `docs/user_guide/working_with_classes.rst` - User documentation

**Modified files:**
- `src/rhapsody_cli/cli/cli.py` - Register `class` command

## SW Requirements IDs

- SWR_CLS_00001: Class Create Command
- SWR_CLS_00002: Class Delete Command
- SWR_CLS_00003: Class View Command
- SWR_CLS_00004: Class List Command
- SWR_CLS_00005: Path Validation
- SWR_CLS_00006: External JSON File Support
- SWR_CLS_00007: Stereotype and Tag Support
- SWR_CLS_00008: Multi-Format Output
- SWR_CLS_00009: View-to-Create Workflow
- SWR_CLS_00010: Error Handling and Logging
- SWR_CLS_00011: Class Link Command (generalization only — association/unidirectional deferred)
- SWR_CLS_00012: Boolean Flag Support
- SWR_CLS_00013: GUID Lookup Support (view/delete/link support `--guid` as alternative to `--path`)

## Test Case IDs

- UTS_CLS_00001 - UTS_CLS_00025 (estimated — reduced from original 30 due to dropping association/unidirectional from `link` subcommand)
