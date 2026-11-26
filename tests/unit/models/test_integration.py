"""Cross-wrapper integration tests: factory methods return correct subclasses."""

import subprocess
import sys

from rhapsody_cli.models.com.telelogic.rhapsody.core import (
    IRPAssociationRole,
    IRPClass,
    IRPComponent,
    IRPConfiguration,
    IRPDependency,
    IRPGeneralization,
    IRPInstance,
    IRPPackage,
    IRPProfile,
    IRPStereotype,
)
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_comment import IRPComment
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_constraint import IRPConstraint
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_enumeration_literal import IRPEnumerationLiteral
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_fresh_import_registers_all_core_wrappers() -> None:
    """A standalone CLI process must resolve Class/Attribute/Operation/Port.

    Unit tests import the wrapper modules at collection time, hiding the fact
    that a bare ``import rhapsody_cli`` registers only three wrappers.
    """
    code = (
        "import rhapsody_cli\n"
        "from rhapsody_cli.models.core import ComHelper\n"
        "required = {'Class', 'Attribute', 'Operation', 'Port', 'Package', 'Project'}\n"
        "missing = required - set(ComHelper._WRAPPER_REGISTRY)\n"
        "assert not missing, missing\n"
    )
    result = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=30)

    assert result.returncode == 0, result.stderr


def test_wrap_dispatches_profile_to_rpprofile() -> None:
    fake = make_fake_element("Profile", properties={"name": "SysML"})

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPProfile)
    assert isinstance(result, IRPPackage)


def test_wrap_dispatches_component_to_rpcomponent() -> None:
    fake = make_fake_element("Component", properties={"name": "Comp1"})

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPComponent)


def test_wrap_dispatches_configuration_to_rpconfiguration() -> None:
    fake = make_fake_element("Configuration", properties={"name": "Config1"})

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPConfiguration)


def test_wrap_dispatches_module_to_rpmodule() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPModule

    fake = make_fake_element("Module", properties={"name": "Module1"})

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPModule)
    assert isinstance(result, IRPInstance)


def test_wrap_dispatches_generalization_to_rpgeneralization() -> None:
    fake = make_fake_element("Generalization")

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPGeneralization)
    assert isinstance(result, IRPModelElement)


def test_wrap_dispatches_dependency_to_rpdependency() -> None:
    fake = make_fake_element("Dependency")

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPDependency)
    assert isinstance(result, IRPModelElement)


def test_wrap_dispatches_hyperlink_to_rphyperlink() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPHyperLink

    fake = make_fake_element("HyperLink")

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPHyperLink)
    assert isinstance(result, IRPDependency)


def test_wrap_dispatches_association_role_to_rpassociation_role() -> None:
    fake = make_fake_element("AssociationRole")

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPAssociationRole)
    assert isinstance(result, IRPInstance)


def test_wrap_dispatches_comment_to_rpcomment() -> None:
    fake = make_fake_element("Comment", properties={"name": "Comment1"})

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPComment)
    assert isinstance(result, IRPModelElement)


def test_wrap_dispatches_constraint_to_rpconstraint() -> None:
    fake = make_fake_element("Constraint", properties={"name": "Constraint1"})

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPConstraint)
    assert isinstance(result, IRPModelElement)


def test_wrap_dispatches_enumeration_literal_to_rpenumeration_literal() -> None:
    fake = make_fake_element("EnumerationLiteral", properties={"name": "LITERAL1"})

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPEnumerationLiteral)
    assert isinstance(result, IRPModelElement)


def test_wrap_dispatches_stereotype_to_rpstereotype() -> None:
    fake = make_fake_element("Stereotype", properties={"name": "MyStereo"})

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPStereotype)
    assert isinstance(result, IRPClassifier)


def test_wrap_dispatches_association_class_to_rpassociation_class() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_class import IRPAssociationClass

    fake = make_fake_element("AssociationClass", properties={"name": "MyAssoc"})

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPAssociationClass)
    assert isinstance(result, IRPClass)


def test_wrap_dispatches_tag_to_rptag() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag

    fake = make_fake_element("Tag", properties={"name": "MyTag"})

    result = IRPModelElement.wrap(fake)

    assert isinstance(result, IRPTag)


def test_collection_contains_mixed_element_types() -> None:
    class1 = make_fake_element("Class", properties={"name": "Class1"})
    actor1 = make_fake_element("Actor", properties={"name": "Actor1"})
    coll = make_fake_collection([class1, actor1])

    result = IRPCollection(coll)

    assert len(result) == 2
    assert isinstance(result[0], IRPClass)
    assert isinstance(result[1], IRPClassifier)


def test_all_new_wrappers_exist() -> None:
    """Verify all new wrappers can be imported."""
    from rhapsody_cli.models.com.telelogic.rhapsody.core import (
        IRPAssociationClass,
        IRPAssociationRole,
        IRPCollaboration,
        IRPComponentInstance,
        IRPDependency,
        IRPGeneralization,
        IRPHyperLink,
        IRPModule,
        IRPNode,
        IRPStereotype,
        IRPTag,
    )
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_comment import IRPComment
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_constraint import IRPConstraint
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_enumeration_literal import IRPEnumerationLiteral

    # All imports should succeed
    assert IRPAssociationClass is not None
    assert IRPStereotype is not None
    assert IRPModule is not None
    assert IRPNode is not None
    assert IRPCollaboration is not None
    assert IRPComponentInstance is not None
    assert IRPGeneralization is not None
    assert IRPDependency is not None
    assert IRPHyperLink is not None
    assert IRPAssociationRole is not None
    assert IRPComment is not None
    assert IRPConstraint is not None
    assert IRPEnumerationLiteral is not None
    assert IRPTag is not None
