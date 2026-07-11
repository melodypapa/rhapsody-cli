# Software Requirements - Port Command

**Category:** Port Command
**Prefix:** SWR_PORT
**Source:** Extracted from spec 2026-07-10-element-commands-design.md
**Last Validated:** 2026-07-10

---

## SWR_PORT_00001: Port Create Command

**ID:** SWR_PORT_00001
**Title:** port create command creates one or multiple ports
**Status:** Planned
**Priority:** High
**Description:**
The port CLI
- SHALL provide a `port create` command to create one or multiple ports.
- SHALL accept `--path <class-path>` argument (required) - parent classifier path
- SHALL accept `--input <json-file>` argument (optional)
- SHALL accept positional `attributes` argument (inline JSON or file path)
- SHALL support bulk creation via JSON array
- SHALL validate parent path resolves to Classifier element
- SHALL create ports via `classifier.addPort(name)`
- SHALL set validated attributes: name, isBehavioral, isReversed, portContract, description
- SHALL apply name via `addPort()`, isBehavioral via `setIsBehavioral(0/1)`, isReversed via `setIsReversed(0/1)`, description via `setDescription()`
- SHALL resolve portContract by name via `findNestedClassifierRecursive()` on parent's package
- SHALL set portContract via `setPortContract(classifier)`
- SHALL skip unknown attributes with warning log
- SHALL detect inline JSON (starts with `{` or `[`) vs file path automatically
- SHALL parse JSON file with UTF-8 encoding
**Implementation:** src/rhapsody_cli/actions/port_action.py:PortCreateAction
**Last Changed:** 2026-07-10

---

## SWR_PORT_00002: Port Delete Command

**ID:** SWR_PORT_00002
**Title:** port delete command deletes a port
**Status:** Planned
**Priority:** High
**Description:**
The port CLI
- SHALL provide a `port delete` command to delete a port.
- SHALL accept `--path <class-path>` argument (optional) - parent classifier path
- SHALL accept `--guid <guid>` argument (optional) - port GUID
- SHALL accept `--name <port-name>` argument (optional) - port name within class
- SHALL require exactly one of `--path` + `--name` OR `--guid`
- SHALL validate type when using --guid (metaClass == "Port", raise CliExecutionError if mismatch)
- SHALL resolve port by iterating `getPorts()` and matching by name
- SHALL delete port via `deleteFromProject()`
- SHALL log deletion to stderr
**Implementation:** src/rhapsody_cli/actions/port_action.py:PortDeleteAction
**Last Changed:** 2026-07-10

---

## SWR_PORT_00003: Port View Command

**ID:** SWR_PORT_00003
**Title:** port view command displays port details
**Status:** Planned
**Priority:** High
**Description:**
The port CLI
- SHALL provide a `port view` command to view port details.
- SHALL accept `--path <class-path>` argument (optional)
- SHALL accept `--guid <guid>` argument (optional)
- SHALL accept `--name <port-name>` argument (optional)
- SHALL require exactly one of `--path` + `--name` OR `--guid`
- SHALL validate type when using --guid (metaClass == "Port")
- SHALL accept `--format <format>` argument (table/json/csv, default: table)
- SHALL accept `--output <file>` argument (optional)
- SHALL display fields: Name, GUID, Description, IsBehavioral, IsReversed, PortContract, MetaClass, FullPath
- SHALL support table (Property|Value layout), JSON (8-key object), CSV (horizontal 8-column) output formats
- SHALL write to file if `--output` specified, else stdout
**Implementation:** src/rhapsody_cli/actions/port_action.py:PortViewAction
**Last Changed:** 2026-07-10

---

## SWR_PORT_00004: Port List Command

**ID:** SWR_PORT_00004
**Title:** port list command lists ports on a classifier
**Status:** Planned
**Priority:** High
**Description:**
The port CLI
- SHALL provide a `port list` command to list ports on a classifier.
- SHALL accept `--path <class-path>` argument (required)
- SHALL accept `--format <format>` argument (table/json/csv, default: table)
- SHALL accept `--output <file>` argument (optional)
- SHALL list ports via `getPorts()` and collect names via `getName()`
- SHALL support table (single Name column), JSON (array of strings), CSV (1-column horizontal) output formats
- SHALL write to file if `--output` specified, else stdout
**Implementation:** src/rhapsody_cli/actions/port_action.py:PortListAction
**Last Changed:** 2026-07-10

---

## SWR_PORT_00005: Port Update Command

**ID:** SWR_PORT_00005
**Title:** port update command modifies port attributes
**Status:** Planned
**Priority:** High
**Description:**
The port CLI
- SHALL provide a `port update` command to modify attributes of an existing port.
- SHALL accept `--path <class-path>` argument (optional)
- SHALL accept `--guid <guid>` argument (optional)
- SHALL accept `--name <port-name>` argument (optional)
- SHALL require exactly one of `--path` + `--name` OR `--guid`
- SHALL validate type when using --guid (metaClass == "Port", raise CliExecutionError if mismatch)
- SHALL accept `--input <json-file>` argument (optional)
- SHALL accept positional `attributes` argument (inline JSON with fields to update)
- SHALL perform partial update - only specified fields are modified
- SHALL support validated attributes: name, isBehavioral, isReversed, portContract, description
- SHALL skip unknown attributes with warning log
- SHALL log INFO for successful updates
**Implementation:** src/rhapsody_cli/actions/port_action.py:PortUpdateAction
**Last Changed:** 2026-07-10

---

## SWR_PORT_00006: Path and Name Validation

**ID:** SWR_PORT_00006
**Title:** All port commands validate path and name before execution
**Status:** Planned
**Priority:** High
**Description:**
All port commands
- SHALL validate path before execution.
- SHALL resolve classifier path using PathResolver
- SHALL resolve port by iterating `getPorts()` and matching by name
- SHALL raise CliExecutionError if path not found
- SHALL raise CliExecutionError if port name not found in classifier
**Implementation:** src/rhapsody_cli/actions/port_action.py:AbstractPortAction._resolve_classifier, _resolve_port
**Last Changed:** 2026-07-10

---

## SWR_PORT_00007: External JSON File Support

**ID:** SWR_PORT_00007
**Title:** Port create/update supports external JSON files
**Status:** Planned
**Priority:** Medium
**Description:**
Port create and update commands
- SHALL support external JSON files.
- SHALL accept `--input <file>` argument
- SHALL detect inline JSON vs file path automatically
- SHALL parse JSON file with UTF-8 encoding
- SHALL raise CliExecutionError if file not found
- SHALL raise CliExecutionError if JSON invalid
**Implementation:** src/rhapsody_cli/actions/port_action.py:PortCreateAction._load_json_data
**Last Changed:** 2026-07-10

---

## SWR_PORT_00008: Multi-Format Output

**ID:** SWR_PORT_00008
**Title:** Port view and list support multiple output formats
**Status:** Planned
**Priority:** Medium
**Description:**
Port view and list commands
- SHALL support multiple output formats.
- SHALL support table format (default)
- SHALL support JSON format
- SHALL support CSV format
- SHALL use horizontal layout for CSV
**Implementation:** src/rhapsody_cli/actions/port_action.py:PortViewAction._format_output, PortListAction._format_output
**Last Changed:** 2026-07-10

---

## SWR_PORT_00009: Error Handling and Logging

**ID:** SWR_PORT_00009
**Title:** All port actions follow consistent error handling patterns
**Status:** Planned
**Priority:** High
**Description:**
All port actions
- SHALL follow consistent error handling patterns.
- SHALL use `_handle_execution_error()` for COM errors
- SHALL raise CliExecutionError for validation failures
- SHALL log INFO for successful operations
- SHALL log WARNING for skipped attributes
- SHALL log ERROR for failures
**Implementation:** src/rhapsody_cli/actions/port_action.py:AbstractPortAction
**Last Changed:** 2026-07-10

---

## SWR_PORT_00010: GUID Lookup Support

**ID:** SWR_PORT_00010
**Title:** Port view/delete/update support --guid as alternative to --path + --name
**Status:** Planned
**Priority:** Medium
**Description:**
Port view, delete, and update commands
- SHALL support `--guid` as alternative to `--path` + `--name`.
- SHALL accept `--guid <guid>` argument
- SHALL locate port by GUID via `findElementByGUID(guid)`
- SHALL validate located element is Port (metaClass == "Port")
- SHALL raise CliExecutionError if GUID not found
- SHALL raise CliExecutionError if GUID resolves to wrong type
**Implementation:** src/rhapsody_cli/actions/port_action.py:AbstractPortAction._resolve_port_by_guid
**Last Changed:** 2026-07-10

---

## SWR_PORT_00011: PortContract Resolution

**ID:** SWR_PORT_00011
**Title:** Port create/update resolves portContract by name
**Status:** Planned
**Priority:** Medium
**Description:**
Port create and update commands
- SHALL resolve portContract by name.
- SHALL accept `portContract` field as class name string
- SHALL resolve class via `findNestedClassifierRecursive(class_name)` on parent's package
- SHALL raise CliExecutionError if class name not found
- SHALL set resolved class via `setPortContract(classifier)`
**Implementation:** src/rhapsody_cli/actions/port_action.py:PortCreateAction._resolve_port_contract
**Last Changed:** 2026-07-10

---

## SWR_PORT_00012: IsBehavioral and IsReversed Support

**ID:** SWR_PORT_00012
**Title:** Port create/update supports isBehavioral and isReversed flags
**Status:** Planned
**Priority:** Medium
**Description:**
Port create and update commands
- SHALL support isBehavioral and isReversed flags.
- SHALL accept `isBehavioral` int (0/1) in JSON, set via `setIsBehavioral(val)`
- SHALL accept `isReversed` int (0/1) in JSON, set via `setIsReversed(val)`
**Implementation:** src/rhapsody_cli/actions/port_action.py:PortCreateAction._set_flags
**Last Changed:** 2026-07-10

---

## SWR_PORT_00013: Bulk Creation Support

**ID:** SWR_PORT_00013
**Title:** Port create supports bulk creation via JSON array
**Status:** Planned
**Priority:** Medium
**Description:**
Port create command
- SHALL support bulk creation.
- SHALL accept JSON array of port definitions
- SHALL create each port in sequence
- SHALL log INFO with count of created ports
**Implementation:** src/rhapsody_cli/actions/port_action.py:PortCreateAction.execute
**Last Changed:** 2026-07-10