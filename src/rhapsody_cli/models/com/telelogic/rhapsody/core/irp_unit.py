"""Wrappers for ``com.telelogic.rhapsody.core.IRPUnit``.

Canonical module for :class:`IRPUnit`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_unit.md``.
"""

from __future__ import annotations

from enum import IntEnum
from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.core import AbstractRPModelElement


class AddToModelMode(IntEnum):
    """Constant values mirroring ``IRPApplication.AddToModel_Mode``.

    Returned by :meth:`IRPUnit.getAddToModelMode` to indicate how a unit was
    added to the model. ``IntEnum`` so callers may compare the raw ``int``
    returned by the COM call directly against these constants.
    """

    AS_REFERENCE = 0
    AS_UNIT_WITH_COPY = 1
    AS_UNIT_WITHOUT_COPY = 2


class IRPUnit(IRPModelElement):
    """Wraps ``IRPUnit``: model elements that can be saved as separate files."""

    # IRPUnit method parity checklist:
    # [x] copy_to_another_project                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_add_to_model_mode                   [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_cm_header                         [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_cm_state                          [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_current_directory                 [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_filename                         [x] impl  [x] docstring  [x] unit test  [x] integration test  (pre-existing)
    # [x] get_include_in_next_load                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_is_stub                           [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_language                         [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_last_modified_time                 [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_nested_save_units                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_nested_save_units_count             [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_structure_diagrams                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_unit_path                         [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] is_read_only                          [x] impl  [x] docstring  [x] unit test  [x] integration test  (pre-existing)
    # [x] is_reference_unit                     [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] is_separate_save_unit                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] load                                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] move_to_another_project_leave_a_reference [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] reference_to_another_project           [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] save                                [x] impl  [x] docstring  [x] unit test  [x] integration test  (pre-existing)
    # [x] set_cm_header                         [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_filename                         [x] impl  [x] docstring  [x] unit test  [x] integration test  (pre-existing)
    # [x] set_include_in_next_load                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_language                         [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_read_only                         [x] impl  [x] docstring  [x] unit test  [x] integration test  (pre-existing)
    # [x] set_separate_save_unit                 [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_unit_path                         [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] unload                              [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [inherited] get_nested_elements - provided by rp_model_element
    # No deprecated IRPUnit methods.

    def copy_to_another_project(self, parent_in_target: IRPModelElement) -> IRPModelElement:
        """Makes an editable copy of the unit in a different project.

        Args:
            parent_in_target: The model element that will be the parent of the
                new unit in the target project.

        Returns:
            The wrapped unit that was created in the target project.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::copyToAnotherProject(com.telelogic.rhapsody.core.IRPModelElement parentInTarget)
        """
        return cast(IRPModelElement, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.copyToAnotherProject(parent_in_target._com))))

    def get_add_to_model_mode(self) -> int:
        """Returns an indication of how the unit was added to the model.

        The returned value corresponds to one of the :class:`AddToModelMode`
        constants.

        Returns:
            A value indicating how the unit was added to the model (see
            :class:`AddToModelMode`).

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getAddToModelMode()
        """
        return int(AbstractRPModelElement.call_com(lambda: self._com.getAddToModelMode()))

    def get_cm_header(self) -> str:
        """Returns the header used by the Configuration Management tool for the unit.

        Returns:
            The Configuration Management tool header as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getCMHeader()
        """
        return str(AbstractRPModelElement.get_com_property(self._com, "CMHeader"))

    def get_cm_state(self) -> int:
        """Returns the configuration management state of the unit.

        Returns:
            The configuration management state of the unit.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getCMState()
        """
        return int(AbstractRPModelElement.call_com(lambda: self._com.getCMState()))

    def get_current_directory(self) -> str:
        """Gets the name of the directory that contains the file used to store the unit.

        The string returned consists of the full path except for the name of
        the file itself.

        Returns:
            The name of the directory that contains the file used to store the unit.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getCurrentDirectory()
        """
        return str(AbstractRPModelElement.get_com_property(self._com, "currentDirectory"))

    def get_filename(self) -> str:
        """Gets the name of the file used to store the unit.

        The string returned consists only of the filename, not the entire path.

        Returns:
            The name of the file used to store the unit.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getFilename()
        """
        return str(AbstractRPModelElement.get_com_property(self._com, "filename"))

    def get_include_in_next_load(self) -> int:
        """Checks whether the unit is going to be loaded the next time the model is loaded.

        Returns:
            ``1`` if the unit is going to be loaded the next time the model is
            loaded, ``0`` if it is not.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getIncludeInNextLoad()
        """
        return int(AbstractRPModelElement.get_com_property(self._com, "includeInNextLoad"))

    def get_is_stub(self) -> int:
        """Checks whether the unit is currently unloaded.

        Returns:
            ``1`` if the unit is not currently loaded, ``0`` if it is currently loaded.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getIsStub()
        """
        return int(AbstractRPModelElement.get_com_property(self._com, "isStub"))

    def get_language(self) -> str:
        """Gets the language of the unit.

        Returns:
            The language of the unit as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getLanguage()
        """
        return str(AbstractRPModelElement.call_com(lambda: self._com.getLanguage()))

    def get_last_modified_time(self) -> str:
        """Returns the time at which the file representing the unit was last modified.

        Returns:
            The last modified time as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getLastModifiedTime()
        """
        return str(AbstractRPModelElement.call_com(lambda: self._com.getLastModifiedTime()))

    def get_nested_save_units(self) -> IRPCollection:
        """Returns a collection of any sub-elements of the unit that were saved as individual files.

        Returns:
            An ``IRPCollection`` of sub-elements that were saved as individual files.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getNestedSaveUnits()
        """
        return IRPCollection(AbstractRPModelElement.call_com(lambda: self._com.getNestedSaveUnits()))

    def get_nested_save_units_count(self) -> int:
        """Returns the number of sub-elements of the unit that were saved as individual files.

        Returns:
            The number of sub-elements that were saved as individual files.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getNestedSaveUnitsCount()
        """
        return int(AbstractRPModelElement.call_com(lambda: self._com.getNestedSaveUnitsCount()))

    def get_structure_diagrams(self) -> IRPCollection:
        """Returns a collection of any structure diagrams that are sub-elements of the unit.

        Used primarily for structure diagrams that belong to individual classes.

        Returns:
            An ``IRPCollection`` of structure diagrams that are sub-elements of the unit.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getStructureDiagrams()
        """
        return IRPCollection(AbstractRPModelElement.get_com_property(self._com, "structureDiagrams"))

    def get_unit_path(self, b_full_path: int) -> str:
        """Returns the path of the unit, including the filename.

        Args:
            b_full_path: ``1`` to return the full path, ``0`` to return a
                relative path. For relative paths, the path returned is relative
                to the saved unit that owns this unit.

        Returns:
            The path of the unit, including the filename.

        Raises:
            RhapsodyRuntimeException: if the unit path cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::getUnitPath(int bFullPath)
        """
        return str(AbstractRPModelElement.call_com(lambda: self._com.getUnitPath(b_full_path)))

    def is_read_only(self) -> bool:
        """Checks whether the file used to store the unit is read-only.

        Returns:
            ``True`` if the file is read-only, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::isReadOnly()
        """
        return bool(AbstractRPModelElement.call_com(lambda: self._com.isReadOnly()))

    def is_reference_unit(self) -> int:
        """Checks whether the unit was added to the model as a reference.

        Returns:
            ``1`` if the unit was added to the model as a reference, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::isReferenceUnit()
        """
        return int(AbstractRPModelElement.call_com(lambda: self._com.isReferenceUnit()))

    def is_separate_save_unit(self) -> int:
        """Checks whether the current IRPUnit object is saved in its own file.

        ``IRPUnit`` objects represent any element that can in theory be saved
        as a separate file, even if this is not the case for a specific element
        in your model.

        Returns:
            ``1`` if the unit is saved in its own file, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::isSeparateSaveUnit()
        """
        return int(AbstractRPModelElement.call_com(lambda: self._com.isSeparateSaveUnit()))

    def load(self, with_subs: int) -> IRPModelElement:
        """Loads the unit.

        Args:
            with_subs: ``1`` to load the unit's subunits as well, ``0`` to load
                only the unit itself.

        Returns:
            The wrapped unit that was loaded.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::load(int withSubs)
        """
        return cast(IRPModelElement, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.load(with_subs))))

    def move_to_another_project_leave_a_reference(self, parent_in_target: IRPModelElement) -> IRPModelElement:
        """Moves the unit to a different project, and adds a reference to it in the original project.

        Args:
            parent_in_target: The model element that will be the parent of the
                new unit in the target project.

        Returns:
            The wrapped unit that was created in the target project.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::moveToAnotherProjectLeaveAReference(com.telelogic.rhapsody.core.IRPModelElement parentInTarget)
        """
        return cast(IRPModelElement, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.moveToAnotherProjectLeaveAReference(parent_in_target._com))))

    def reference_to_another_project(self, parent_in_target: IRPModelElement) -> IRPModelElement:
        """Creates a reference to the unit in a different project.

        Args:
            parent_in_target: The model element that will be the parent of the
                reference (read-only) unit created in the target project.

        Returns:
            The wrapped reference (read-only) unit that was created in the target project.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::referenceToAnotherProject(com.telelogic.rhapsody.core.IRPModelElement parentInTarget)
        """
        return cast(IRPModelElement, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.referenceToAnotherProject(parent_in_target._com))))

    def save(self, with_subs: int = 0) -> None:
        """Saves the unit.

        Args:
            with_subs: 1 to save the unit and its subunits, 0 to save only the unit itself (default: 0)

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::save(int)
        """
        AbstractRPModelElement.call_com(lambda: self._com.save(with_subs))

    def set_cm_header(self, cm_header: str) -> None:
        """Sets the Configuration Management tool header for the unit.

        Args:
            cm_header: The Configuration Management tool header to use for the unit.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::setCMHeader(java.lang.String cmHeader)
        """
        AbstractRPModelElement.set_com_property(self._com, "CMHeader", cm_header)

    def set_filename(self, filename: str) -> None:
        """Specifies the name that should be used for the file representing the unit.

        The string should only include the first part of the filename;
        Rhapsody handles the file extension. Note that if you change the
        filename, the old file remains on disk.

        Args:
            filename: The name that should be used for the file representing the unit.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::setFilename(java.lang.String filename)
        """
        AbstractRPModelElement.set_com_property(self._com, "filename", filename)

    def set_include_in_next_load(self, include_in_next_load: int) -> None:
        """Toggles whether the unit is going to be loaded the next time the model is loaded.

        Args:
            include_in_next_load: ``1`` to load the unit the next time the model
                is loaded, ``0`` to not load it.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::setIncludeInNextLoad(int)
        """
        AbstractRPModelElement.set_com_property(self._com, "includeInNextLoad", include_in_next_load)

    def set_language(self, new_language: str, recursive: int) -> None:
        """Specifies the programming language that should be used when code is generated for the unit.

        This method can be used for mixed-language models.

        Args:
            new_language: One of ``"C++"``/``"cpp"``, ``"C"``, ``"Java"``,
                ``"Ada"``, or ``"C#"``.
            recursive: ``1`` to set the language for all subunits of the
                element, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::setLanguage(java.lang.String newLanguage, int recursive)
        """
        AbstractRPModelElement.call_com(lambda: self._com.setLanguage(new_language, recursive))

    def set_read_only(self, read_only: bool) -> None:
        """Toggles the read-only status of the file used to store the unit.

        Args:
            read_only: ``True`` to change the file to read-only, ``False`` to
                change the file to read/write.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::setReadOnly(int)
        """
        AbstractRPModelElement.call_com(lambda: self._com.setReadOnly(1 if read_only else 0))

    def set_separate_save_unit(self, p_val: int) -> None:
        """Specifies whether the current IRPUnit object should be saved in its own file.

        Args:
            p_val: ``1`` to save the element in its own file, ``0`` to not save
                it in its own file.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::setSeparateSaveUnit(int)
        """
        AbstractRPModelElement.call_com(lambda: self._com.setSeparateSaveUnit(p_val))

    def set_unit_path(self, new_path: str) -> None:
        """Specifies the path that should be used to locate the unit when it is added to a model "By Reference".

        Args:
            new_path: The path that should be used to locate the unit when it is
                added to a model "By Reference".

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::setUnitPath(java.lang.String newPath)
        """
        AbstractRPModelElement.call_com(lambda: self._com.setUnitPath(new_path))

    def unload(self) -> None:
        """Unloads the unit.

        Reference:
            com.telelogic.rhapsody.core.IRPUnit::unload()
        """
        AbstractRPModelElement.call_com(lambda: self._com.unload())
