.. _rhapsody-java-interface-IRPCollection:

IRPCollection
============

The IRPCollection interface is Rhapsody's generic collection of model elements.

- **Java interface:** IRPCollection
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** A generic collection of model elements with 1-based indexed access.
- **Python wrapper:** IRPCollection
- **Python import:** ``from rhapsody_cli.models.core import IRPCollection``
- **Canonical module:** pending — the §2 package move is deferred until the IRPUnit and
  IRPModelElement rows leave ``models/core.py`` (see ``docs/reports/sync-todo``).


`add_graphical_item` and `to_list` are documented blockers: their Java members
(`addGraphicalItem`, `toList`) are absent from the committed pywin32 catalog, so the call
sites stay unchanged until Windows typelib evidence lands. Every other member calls exactly
one pywin32-exposed COM member: `Count` is read as a property via ``get_com_property``, `Item`
and the mutators are invoked as methods via ``call_com``. The Python-implementation column
reflects the post-migration single-member labels.


.. list-table:: Verified IRPCollection deviations and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - addGraphicalItem (method)
     - —
     - add_graphical_item() -> addGraphicalItem
     - PYWIN32_MEMBER_MISSING; Use a member exposed by the registered type library or verify the Rhapsody version.
   * - toList (method)
     - —
     - to_list() (no static COM member)
     - PYWIN32_MEMBER_MISSING; Use a member exposed by the registered type library or verify the Rhapsody version.

.. list-table:: Correct items (verified direct bindings)
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - addItem (method)
     - addItem (method)
     - add_item() -> addItem
     - MATCH; —
   * - empty (method)
     - empty (method)
     - empty() -> empty
     - MATCH; —
   * - getCount (method)
     - Count (property)
     - get_count() -> Count
     - MATCH; —
   * - getItem (method)
     - Item (method)
     - get_item() -> Item
     - MATCH; —
   * - remove (method)
     - remove (method)
     - remove() -> remove
     - MATCH; —
   * - setInteger (method)
     - setInteger (method)
     - set_integer() -> setInteger
     - MATCH; —
   * - setModelElement (method)
     - setModelElement (method)
     - set_model_element() -> setModelElement
     - MATCH; —
   * - setSize (method)
     - setSize (method)
     - set_size() -> setSize
     - MATCH; —
   * - setString (method)
     - setString (method)
     - set_string() -> setString
     - MATCH; —
