"""The unit test for our calculator"""
import sys
import unittest
from io import StringIO
from unittest import mock

from functions import ask_yes_no
from functions import calc_room_size
from functions import get_room_type
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

    def test_get_type(self):
        """This tests whether determination of room type works"""
        with mock.patch("builtins.input", return_value="1"):
            actual_result = get_room_type()
            assert actual_result == "normal"

    def test_calc_room_size(self):
        """This tests whether determination of room type works"""

        def mock_input(prompt):
            if "name of" in prompt:
                return "Test"
            if "type" in prompt:
                return "1"
            if "length" in prompt:
                return 10
            if "width" in prompt:
                return 10
            return False

        output = StringIO()  # Create StringIO object
        sys.stdout = output  # and redirect stdout.
        with mock.patch("builtins.input", mock_input):
            calc_room_size()
        sys.stdout = sys.__stdout__  # Reset redirect.
        assert "This room is 100.0 m²" in output.getvalue()


if __name__ == "__main__":
    unittest.main()
