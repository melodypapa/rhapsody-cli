"""Integration tests for IRPContextSpecification with live Rhapsody COM API."""

import uuid
from typing import cast

import pytest

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_context_specification import IRPContextSpecification
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_variables import IRPTag


@pytest.mark.integration
class TestIRPContextSpecificationIntegration:
    """Integration tests for IRPContextSpecification with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _context_specification(pkg: IRPPackage, rhapsody_app: RhapsodyApplication) -> tuple[IRPContextSpecification, IRPClass]:
        owner = pkg.add_class(f"ContextOwner_{uuid.uuid4().hex[:8]}")
        target = pkg.add_class(f"ContextTarget_{uuid.uuid4().hex[:8]}")
        tag = owner.add_new_aggr("Tag", f"ContextTag_{uuid.uuid4().hex[:8]}")
        assert isinstance(tag, IRPTag)

        elements = rhapsody_app.create_new_collection()
        elements.add_item(target)
        multiplicities = rhapsody_app.create_new_collection()
        multiplicities.set_size(1)
        multiplicities.set_string(1, "1")
        applied_tag = owner.set_tag_context_value(tag, elements, multiplicities)
        value_specifications = applied_tag.get_value_specifications()
        assert value_specifications.count == 1
        return cast(IRPContextSpecification, value_specifications.get_item(1)), target

    @staticmethod
    def _string_collection(rhapsody_app: RhapsodyApplication, values: tuple[str, ...]) -> IRPCollection:
        collection = rhapsody_app.create_new_collection()
        collection.set_size(len(values))
        for index, value in enumerate(values, start=1):
            collection.set_string(index, value)
        return collection

    def test_multiplicities(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = test_project.add_package(self._unique("MultiplicitiesPkg"))
        try:
            context, _ = self._context_specification(pkg, rhapsody_app)
            values = tuple(str(value) for value in context.multiplicities)
            context.multiplicities = self._string_collection(rhapsody_app, values)
            assert list(context.multiplicities) == list(values)
        finally:
            pkg.delete_from_project()

    def test_value_returns_populated_context_path(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = test_project.add_package(self._unique("ValuePkg"))
        try:
            context, target = self._context_specification(pkg, rhapsody_app)
            values = tuple(str(value) for value in context.value)
            assert any(target.name in value for value in values)
        finally:
            pkg.delete_from_project()
