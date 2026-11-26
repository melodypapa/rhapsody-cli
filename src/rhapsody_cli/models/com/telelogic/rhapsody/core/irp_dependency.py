"""Wraps ``com.telelogic.rhapsody.core.IRPDependency``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPDependency(IRPModelElement):
    """Wraps ``IRPDependency``: a dependency relationship."""

    # IRPDependency parity checklist (typelib authority 2026-11-26):
    # [x] dependent                          property (read/write)                 [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] depends_on                         property (read/write)                 [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_need_to_migrate                 JavaDoc-only, documented unavailable  [x] stub  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_link_type                      JavaDoc-only, documented unavailable  [x] stub  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_owner_without_changing_dependent  method                             [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by IRPModelElement checklists)
    # No deprecated IRPDependency methods.

    @property
    def dependent(self) -> IRPModelElement | None:
        """The model element that is dependent.

        Returns:
            The wrapped dependent model element, or ``None`` if not set.

        Raises:
            RhapsodyRuntimeException: if the dependent cannot be retrieved or set.

        Reference:
            com.telelogic.rhapsody.core.IRPDependency::getDependent()
        """
        return self.wrap(self.get_com_property(self._com, "dependent"))

    @dependent.setter
    def dependent(self, dependent: IRPModelElement) -> None:
        """Sets the model element that is dependent.

        Args:
            dependent: The wrapped model element to set as dependent.

        Reference:
            com.telelogic.rhapsody.core.IRPDependency::setDependent(com.telelogic.rhapsody.core.IRPModelElement dependent)
        """
        self.set_com_property(self._com, "dependent", dependent._com)

    @property
    def depends_on(self) -> IRPModelElement | None:
        """The model element that is depended upon.

        Returns:
            The wrapped model element that is depended upon, or ``None`` if not set.

        Raises:
            RhapsodyRuntimeException: if the supplier cannot be retrieved or set.

        Reference:
            com.telelogic.rhapsody.core.IRPDependency::getDependsOn()
        """
        return self.wrap(self.get_com_property(self._com, "dependsOn"))

    @depends_on.setter
    def depends_on(self, depends_on: IRPModelElement) -> None:
        """Sets the model element that is depended upon.

        Args:
            depends_on: The wrapped model element to set as the dependency target.

        Reference:
            com.telelogic.rhapsody.core.IRPDependency::setDependsOn(com.telelogic.rhapsody.core.IRPModelElement dependsOn)
        """
        self.set_com_property(self._com, "dependsOn", depends_on._com)

    def is_need_to_migrate(self) -> int:
        """Checks whether the dependency needs to be migrated.

        Raises:
            NotImplementedError: The Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPDependency::isNeedToMigrate()
        """
        raise NotImplementedError("isNeedToMigrate is not exposed in the Rhapsody COM automation type library.")

    def set_link_type(self, link_type: str) -> None:
        """Sets the link type of the dependency.

        Args:
            link_type: The link type string to set.

        Raises:
            NotImplementedError: The Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPDependency::setLinkType(java.lang.String linkType)
        """
        raise NotImplementedError("setLinkType is not exposed in the Rhapsody COM automation type library.")

    def set_owner_without_changing_dependent(self, owner: IRPModelElement) -> None:
        """Sets the owner of the dependency without changing the dependent.

        Args:
            owner: The wrapped model element to set as the owner.

        Raises:
            RhapsodyRuntimeException: if the owner cannot be set.

        Reference:
            com.telelogic.rhapsody.core.IRPDependency::setOwnerWithoutChangingDependent(IRPModelElement owner)
        """
        self.call_com(lambda: self._com.setOwnerWithoutChangingDependent(owner._com))


IRPModelElement.register_wrapper("Dependency", IRPDependency)
