from Mainframe3270 import Mainframe3270
from Mainframe3270.librarycomponent import LibraryComponent


def test__init__():
    library = Mainframe3270()
    under_test = LibraryComponent(library)

    assert under_test.library == library


def test_librarycomponent_returns_common_attributes():
    library = Mainframe3270()
    under_test = LibraryComponent(library)

    assert library.visible == under_test.visible
    assert library.timeout == under_test.timeout
    assert library.wait_time == under_test.wait_time
    assert library.wait_time_after_write == under_test.wait_time_after_write
    assert library.img_folder == under_test.img_folder
    assert library.cache == under_test.cache
    assert library.mf == under_test.mf
    assert library.output_folder == under_test.output_folder
    assert library.model == under_test.model


def test_can_set_visible():
    library = Mainframe3270(visible=True)
    under_test = LibraryComponent(library)

    assert library.visible == under_test.visible is True

    under_test.visible = False

    assert library.visible == under_test.visible is False


def test_can_set_timeout():
    library = Mainframe3270(timeout="1 minute")
    under_test = LibraryComponent(library)

    assert library.timeout == under_test.timeout == 60.0

    under_test.timeout = 10.0

    assert library.timeout == under_test.timeout == 10.0


def test_can_set_wait_time():
    library = Mainframe3270(wait_time="5 seconds")
    under_test = LibraryComponent(library)

    assert library.wait_time == under_test.wait_time == 5.0

    under_test.wait_time = 1.0

    assert library.wait_time == under_test.wait_time == 1.0


def test_can_set_wait_time_after_write():
    library = Mainframe3270(wait_time_after_write="5 seconds")
    under_test = LibraryComponent(library)

    assert library.wait_time_after_write == under_test.wait_time_after_write == 5.0

    under_test.wait_time_after_write = 0.5

    assert library.wait_time_after_write == under_test.wait_time_after_write == 0.5


def test_can_set_img_folder():
    library = Mainframe3270(img_folder="/home/myfolder")
    under_test = LibraryComponent(library)

    assert library.img_folder == under_test.img_folder == "/home/myfolder"

    under_test.img_folder = "/another_folder"

    assert library.img_folder == under_test.img_folder == "/another_folder"
