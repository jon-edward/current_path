import os
from pathlib import Path
from unittest import TestCase
from current_path import *


CURRENT_PATH_TRUTH = Path(__file__).absolute()
TEST_DIR = Path("test_dir/").absolute()


class TestCurrentPath(TestCase):
    def setUp(self) -> None:
        os.mkdir(TEST_DIR)

    def tearDown(self) -> None:
        os.rmdir(TEST_DIR)

    def test_current_file(self):
        self.assertEqual(current_file(), CURRENT_PATH_TRUTH, "current_file must return the same "
                                                             "path as __file__")

    def test_current_dir(self):
        self.assertEqual(current_dir(),
                         Path(CURRENT_PATH_TRUTH).parent.absolute(), "current_dir must return the "
                                                                     "same path as parent "
                                                                     "of __file__")

    def test_current_dir_as_cwd(self):
        os.chdir(TEST_DIR)
        with current_dir_as_cwd():
            self.assertEqual(Path(os.getcwd()).absolute(), CURRENT_PATH_TRUTH.parent.absolute(),
                             "using current_dir_as_cwd as a context manager should change the "
                             "current working directory within the code block under the CM")

    def test_current_dir_as_cwd_resetting_cwd(self):
        os.chdir(TEST_DIR)
        with current_dir_as_cwd():
            pass
        self.assertEqual(Path(os.getcwd()).absolute(), TEST_DIR, "using current_dir_as_cwd as a "
                                                                 "context manager should reset "
                                                                 "the cwd after code block under "
                                                                 "CM has been exited")


