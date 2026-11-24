from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_files import (
    IRPASCIIFile,
    IRPControlledFile,
    IRPFile,
    IRPFileFragment,
)
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from tests.unit.models.fakes import make_fake_collection, make_fake_element


class TestRPASCIIFile:
    def test_close_delegates_to_com(self) -> None:
        fake = make_fake_element("ASCIIFile")
        obj = IRPASCIIFile(fake)
        obj.close()
        fake.close.assert_called_once_with()

    def test_open_delegates_to_com(self) -> None:
        fake = make_fake_element("ASCIIFile")
        obj = IRPASCIIFile(fake)
        obj.open("x")
        fake.open.assert_called_once_with("x")

    def test_write_delegates_to_com(self) -> None:
        fake = make_fake_element("ASCIIFile")
        obj = IRPASCIIFile(fake)
        obj.write("x")
        fake.write.assert_called_once_with("x")


class TestRPControlledFile:
    def test_get_full_path_file_name_delegates_to_com(self) -> None:
        fake = make_fake_element("ControlledFile")
        fake.getFullPathFileName.return_value = "value"
        obj = IRPControlledFile(fake)
        assert obj.get_full_path_file_name() == "value"

    def test_open_delegates_to_com(self) -> None:
        fake = make_fake_element("ControlledFile")
        obj = IRPControlledFile(fake)
        obj.open()
        fake.open.assert_called_once_with()

    def test_set_target_delegates_to_com(self) -> None:
        fake = make_fake_element("ControlledFile")
        obj = IRPControlledFile(fake)
        obj.set_target("file.txt")
        fake.setTarget.assert_called_once_with("file.txt")


class TestRPFile:
    def test_add_element_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        target = make_fake_element("X")
        obj = IRPFile(fake)
        obj.add_element(cast(IRPClassifier, IRPModelElement.wrap(target)), "x")
        fake.addElement.assert_called_once_with(target, "x")

    def test_add_model_element_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        target = make_fake_element("X")
        obj = IRPFile(fake)
        obj.add_model_element(cast(IRPModelElement, IRPModelElement.wrap(target)), "x")
        fake.addModelElement.assert_called_once_with(target, "x")

    def test_add_package_to_scope_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        target = make_fake_element("X")
        obj = IRPFile(fake)
        obj.add_package_to_scope(cast(IRPPackage, IRPModelElement.wrap(target)))
        fake.addPackageToScope.assert_called_once_with(target)

    def test_add_text_element_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        obj = IRPFile(fake)
        obj.add_text_element("x")
        fake.addTextElement.assert_called_once_with("x")

    def test_add_to_scope_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        target = make_fake_element("X")
        obj = IRPFile(fake)
        obj.add_to_scope(cast(IRPClassifier, IRPModelElement.wrap(target)))
        fake.addToScope.assert_called_once_with(target)

    def test_get_elements_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        inner = make_fake_element("X", properties={"name": "y"})
        fake.getElements.return_value = make_fake_collection([inner])
        obj = IRPFile(fake)
        result = obj.get_elements()
        assert isinstance(result, IRPCollection)
        assert len(result) == 1

    def test_get_file_fragments_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        inner = make_fake_element("X", properties={"name": "y"})
        fake.getFileFragments.return_value = make_fake_collection([inner])
        obj = IRPFile(fake)
        result = obj.get_file_fragments()
        assert isinstance(result, IRPCollection)
        assert len(result) == 1

    def test_get_file_type_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        fake.getFileType.return_value = "value"
        obj = IRPFile(fake)
        assert obj.get_file_type() == "value"

    def test_get_files_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        inner = make_fake_element("X", properties={"name": "y"})
        fake.getFiles.return_value = make_fake_collection([inner])
        obj = IRPFile(fake)
        result = obj.get_files()
        assert isinstance(result, IRPCollection)
        assert len(result) == 1

    def test_get_imp_name_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        fake.getImpName.return_value = "value"
        obj = IRPFile(fake)
        assert obj.get_imp_name(1) == "value"

    def test_get_path_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        fake.getPath.return_value = "value"
        obj = IRPFile(fake)
        assert obj.get_path(1) == "value"

    def test_get_spec_name_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        fake.getSpecName.return_value = "value"
        obj = IRPFile(fake)
        assert obj.get_spec_name(1) == "value"

    def test_is_empty_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        fake.isEmpty.return_value = 1
        obj = IRPFile(fake)
        result = obj.is_empty()
        fake.isEmpty.assert_called_once_with()
        assert result == 1

    def test_set_file_type_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        obj = IRPFile(fake)
        obj.set_file_type("file.txt")
        fake.setFileType.assert_called_once_with("file.txt")

    def test_set_path_delegates_to_com(self) -> None:
        fake = make_fake_element("File")
        obj = IRPFile(fake)
        obj.set_path("file.txt")
        fake.setPath.assert_called_once_with("file.txt")


class TestRPFileFragment:
    def test_get_fragment_element_delegates_to_com(self) -> None:
        fake = make_fake_element("FileFragment")
        inner = make_fake_element("X", properties={"name": "y"})
        fake.getFragmentElement.return_value = inner
        obj = IRPFileFragment(fake)
        result = obj.get_fragment_element()
        assert result is not None and result.name == "y"

    def test_get_fragment_text_delegates_to_com(self) -> None:
        fake = make_fake_element("FileFragment")
        fake.getFragmentText.return_value = "value"
        obj = IRPFileFragment(fake)
        assert obj.get_fragment_text() == "value"

    def test_get_fragment_type_delegates_to_com(self) -> None:
        fake = make_fake_element("FileFragment")
        fake.getFragmentType.return_value = "value"
        obj = IRPFileFragment(fake)
        assert obj.get_fragment_type() == "value"

    def test_move_fragment_in_owner_delegates_to_com(self) -> None:
        fake = make_fake_element("FileFragment")
        obj = IRPFileFragment(fake)
        obj.move_fragment_in_owner(1)
        fake.moveFragmentInOwner.assert_called_once_with(1)

    def test_set_fragment_text_delegates_to_com(self) -> None:
        fake = make_fake_element("FileFragment")
        obj = IRPFileFragment(fake)
        obj.set_fragment_text("file.txt")
        fake.setFragmentText.assert_called_once_with("file.txt")
