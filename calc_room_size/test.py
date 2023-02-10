"""The unit test for our calculator"""
import unittest
from unittest import mock
from functions import ask_yes_no
from functions import get_wall_size_normal


class TestFunctions(unittest.TestCase):
    """Here we are going to test our functions"""

    def test_yes(self):
        """This function tests the answer yes"""
        with mock.patch("builtins.input", return_value="yes"):
            actual_result = ask_yes_no("Yes?")
            assert actual_result

    def test_no(self):
        """This function tests the answer no"""
        with mock.patch("builtins.input", return_value="no"):
            actual_result = ask_yes_no("No?")
            assert not actual_result

    def test_get_size(self):
        """This tests whether the normal room calculations work"""
        with mock.patch("builtins.input", return_value="10"):
            actual_result = get_wall_size_normal("length")
            assert actual_result == 10


if __name__ == '__main__':
    unittest.main()
