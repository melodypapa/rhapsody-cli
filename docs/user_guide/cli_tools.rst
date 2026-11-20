CLI Tools
=========

Overview
--------

rhapsody-cli provides a command-line interface for common Rhapsody operations. The CLI is built using Python's standard-library argparse and supports multiple output formats.

Command Structure
-----------------

The CLI has two types of commands:

* **Single-Level Commands**: Direct actions (connect, disconnect, status, version, export, import)
* **Two-Level Commands**: Action groups with subcommands (project, package, class)

Command groups ``attribute``, ``operation``, and ``port`` are temporarily
suspended: running them prints a notice and exits with code 2 (their
implementations remain in the codebase).

Session Management Commands
----------------------------

``connect`` - Connect to Rhapsody
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli connect [OPTIONS]

Connects to Rhapsody. If an instance is already running, attaches to it.
Otherwise, launches a new instance.

**Options:**

* ``--attach-only`` - Only attach to an existing instance (don't launch if none running)
* ``--timeout MINUTES`` - Set session timeout (default: 30 minutes)
* ``--no-gui`` - Keep Rhapsody GUI hidden
* ``-v, --verbose`` - Enable debug logging

**Example:**

.. code-block:: bash

   rhapsody-cli connect
   rhapsody-cli connect --attach-only
   rhapsody-cli connect --timeout 60 --no-gui
   rhapsody-cli connect --verbose

``disconnect`` - Disconnect from Rhapsody
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli disconnect [OPTIONS]

Disconnects from the current Rhapsody session.

**Options:**

* ``-v, --verbose`` - Enable debug logging

**Example:**

.. code-block:: bash

   rhapsody-cli disconnect
   rhapsody-cli disconnect --verbose

``status`` - Show Connection Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli status [OPTIONS]

Shows the current connection status and open projects.

**Options:**

* ``-v, --verbose`` - Enable debug logging

**Example:**

.. code-block:: bash

   rhapsody-cli status
   rhapsody-cli status --verbose

``version`` - Show CLI Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli version [OPTIONS]

Displays the installed rhapsody-cli version.

**Options:**

* ``-v, --verbose`` - Enable debug logging

**Example:**

.. code-block:: bash

   rhapsody-cli version



Getting Started
---------------

View Help
~~~~~~~~~

.. code-block:: bash

   rhapsody-cli --help

View Subcommand Help
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli project --help
   rhapsody-cli package --help
   rhapsody-cli class --help

Output Formats
--------------

The ``--format`` option (for two-level commands) controls the output format:

* ``table`` (default) - Human-readable table
* ``json`` - JSON format
* ``csv`` - Comma-separated values

Examples
~~~~~~~~

.. code-block:: bash

   # Table format (default)
   rhapsody-cli project list

   # JSON format
   rhapsody-cli package view --path Sensors --format json

   # CSV format
   rhapsody-cli class list --path Sensors --format csv

Global Options
---------------

* ``--format {table,json,csv}`` - Output format for two-level commands (default: table)
* ``-v, --verbose`` - Enable debug logging for any command
* ``-h, --help`` - Show help message


Project Commands
----------------

``project new`` - Create a New Empty Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli project new <PROJECT_LOCATION> <PROJECT_NAME>

Creates a new empty Rhapsody project in ``PROJECT_LOCATION`` and names it
``PROJECT_NAME``. The new project becomes the active project.

**Example:**

.. code-block:: bash

   rhapsody-cli project new "C:\MyModels" MyNewProject

``project open`` - Open a Rhapsody Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli project open <PROJECT_PATH>

Opens the specified Rhapsody project file (.rpy).

**Example:**

.. code-block:: bash

   rhapsody-cli project open "C:\MyModels\myproject.rpy"

``project list`` - List Open Projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli project list

Lists all currently open Rhapsody projects.

**Example:**

.. code-block:: bash

   rhapsody-cli project list
   rhapsody-cli --format json project list

``project close`` - Close Active Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli project close

Closes the currently active project.

**Example:**

.. code-block:: bash

   rhapsody-cli project close

Class Commands
--------------

Classes are managed through the ``class`` command group with the
subcommands ``create``, ``view``, ``list``, ``link``, ``update``, and
``delete``. All subcommands except ``create`` require ``--path`` (or
``--guid``) to identify the class. Paths use "/" or "\\"-separated
segments to navigate nested packages, e.g. ``parent-pkg/pkg/child-pkg``;
when ``--path`` is omitted on ``create``, the class is created at the
project root.

``class create`` - Create a Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli class create --path PARENT_PATH ATTRIBUTES

Create one or more classes under the package/classifier at
``PARENT_PATH``. ``ATTRIBUTES``/``--input`` accepts inline JSON or a
JSON file; ``name`` is required.

**Example:**

.. code-block:: bash

   rhapsody-cli class create --path pkg '{"name": "TemperatureSensor"}'

``class view`` / ``class list``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli class view --path pkg/TemperatureSensor [--format table|json|csv]
   rhapsody-cli class list --path pkg [--format table|json|csv]

``class link`` - Link a Generalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli class link --path pkg/Child --add BaseName

``class update`` / ``class delete``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli class update --path pkg/TemperatureSensor '{"description": "Updated"}'
   rhapsody-cli class delete --path pkg/TemperatureSensor

.. note::

   The ``isAbstract`` flag cannot be persisted on property-style Rhapsody
   Prog IDs (the COM property accepts writes but never persists them);
   ``class update`` reports this explicitly instead of silently ignoring it.

Package Commands
-----------------

Packages have their own dedicated command group (``package``). All
``package`` subcommands except ``create`` require ``--path``, which must
resolve to an *existing* Package. The ``package create`` command has
an optional ``--path``: when omitted, packages are created directly at
the project root.

``package create`` - Create a Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli package create ATTRIBUTES
   rhapsody-cli package create --path PARENT_PATH ATTRIBUTES
   rhapsody-cli package create --input FILE
   rhapsody-cli package create --path PARENT_PATH --input FILE

Create one or more packages. When ``--path`` is omitted, packages are
created at the **project root**. When ``--path`` is given, packages are
created nested under the package at ``PARENT_PATH``.

``ATTRIBUTES``/``--input`` accepts either inline JSON (an object for a
single package, or an array for several) or the path to a JSON file.
Recognized attribute keys: ``name`` (required), ``description``,
``description_html``, ``description_rtf``, ``display_name``,
``display_name_rtf``, ``properties``, ``stereotypes``, ``tags``.

**Examples:**

.. code-block:: bash

   # Create at project root (no --path)
   rhapsody-cli package create '{"name": "TopLevel"}'

   # Create at project root with description
   rhapsody-cli package create '{"name": "TopLevel", "description": "Top-level package"}'

   # Create nested under an existing package
   rhapsody-cli package create --path pkg '{"name": "Sensors"}'

   # Create nested with extra attributes
   rhapsody-cli package create --path pkg '{"name": "Sensors", "description": "Sensor models"}'

   # Multiple packages from an inline JSON array (at project root)
   rhapsody-cli package create '[{"name": "Sensors"}, {"name": "Actuators"}]'

   # Multiple packages nested under existing package
   rhapsody-cli package create --path pkg '[{"name": "Sensors"}, {"name": "Actuators"}]'

   # From an external JSON file (at project root)
   rhapsody-cli package create --input packages.json

   # From an external JSON file (nested under existing package)
   rhapsody-cli package create --path pkg --input packages.json

``package delete`` - Delete a Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli package delete --path PATH

Delete the package at ``PATH`` (and everything nested within it).

**Example:**

.. code-block:: bash

   rhapsody-cli package delete --path pkg/Sensors

``package view`` - View Package Details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli package view --path PATH [--format table|json|csv] [--output FILE]

Display a package's name, GUID, description, metaclass, and full path.
``--format`` selects the rendering (independent of the global
``--output`` flag); ``--output FILE`` writes the result to a file
instead of stdout.

**Example:**

.. code-block:: bash

   rhapsody-cli package view --path pkg/Sensors
   rhapsody-cli package view --path pkg/Sensors --format json

``package list`` - List Nested Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli package list --path PATH [--format table|json|csv] [--output FILE]

List the names of packages directly nested under ``PATH``.

**Example:**

.. code-block:: bash

   rhapsody-cli package list --path pkg
   rhapsody-cli package list --path pkg --format json --output nested.json

Model Import/Export
-------------------

``export`` and ``import`` are single-level commands for YAML-based model
exchange, operating at package granularity. ``--path`` is optional and
defaults to the project root, so exporting the root covers the whole
model.

.. code-block:: bash

   # Export the whole model (root package) to YAML
   rhapsody-cli export --file model.yaml

   # Export one package
   rhapsody-cli export --path pkg/Sensors --file sensors.yaml

   # Import a YAML file into the root package
   rhapsody-cli import --file model.yaml

   # Import a YAML file into a package
   rhapsody-cli import --path pkg/Sensors --file model.yaml

Suspended Commands
------------------

The ``attribute``, ``operation``, and ``port`` command groups are
temporarily suspended. Running them prints a notice on stderr and exits
with code 2. Their implementations remain in
``src/rhapsody_cli/actions/`` and can be re-enabled by removing them
from ``SUSPENDED_COMMANDS`` in ``src/rhapsody_cli/cli/cli.py``.

Common Use Cases
----------------

Create a New Project with Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Open project
   rhapsody-cli project open myproject.rpy

   # Add a package nested inside an existing top-level package
   rhapsody-cli package create --path ExistingPackage '{"name": "MyPackage"}'

   # Add a class inside the new package
   rhapsody-cli class create --path ExistingPackage/MyPackage '{"name": "MyClass"}'

   # View what we created
   rhapsody-cli class view --path ExistingPackage/MyPackage/MyClass

   # Close project
   rhapsody-cli project close

Query and Export
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Open project
   rhapsody-cli project open myproject.rpy

   # Export the whole model to YAML
   rhapsody-cli export --file elements.yaml

   # Close project
   rhapsody-cli project close

Script Integration
------------------

Using CLI in Scripts
~~~~~~~~~~~~~~~~~~~~

Example bash script (Windows):

.. code-block:: bash

   @echo off
   REM Open project
   rhapsody-cli project open "C:\MyModels\myproject.rpy"

   REM Export the model to a YAML file
   rhapsody-cli export --file model.yaml

   REM Close project
   rhapsody-cli project close

   echo Done!

Example Python integration:

.. code-block:: python

   import subprocess

   # Export the model via CLI
   result = subprocess.run(
       ["rhapsody-cli", "export", "--file", "model.yaml"],
       capture_output=True,
       text=True
   )

   if result.returncode == 0:
       print("Model exported successfully")
   else:
       print(f"Error: {result.stderr}")

Advanced Tips
-------------

Using Redirection
~~~~~~~~~~~~~~~~~~

Save CLI output to file:

.. code-block:: bash

   rhapsody-cli project list > projects.txt
   rhapsody-cli class list --path pkg --format json > classes.json

Piping Output
~~~~~~~~~~~~~

Process output with other tools:

.. code-block:: bash

   rhapsody-cli class list --path pkg --format json | python -m json.tool

Output Format Flag
~~~~~~~~~~~~~~~~~~

Pass ``--format`` after the command group:

.. code-block:: bash

   rhapsody-cli class list --path pkg --format json

Troubleshooting
---------------

Command Not Found
~~~~~~~~~~~~~~~~~~

**Problem**: ``rhapsody-cli: command not found``

**Solution**: Ensure package is installed:

.. code-block:: bash

   pip install rhapsody-cli

Project Not Found
~~~~~~~~~~~~~~~~~

**Problem**: ``Error: Project file not found``

**Solution**: Use full path to project:

.. code-block:: bash

   rhapsody-cli project open "C:\full\path\to\project.rpy"

See Also
--------

* :doc:`quickstart` - Quick start guide
* :doc:`connecting_to_rhapsody` - Connection information
