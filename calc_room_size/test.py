from functions import ask_yes_no
from functions import get_wall_size_normal
import unittest
from unittest import mock


class TestFunctions(unittest.TestCase):
    def test_yes(self):
        with mock.patch("builtins.input", return_value="yes"):
            actual_result = ask_yes_no("Yes?")
            assert actual_result

    def test_no(self):
        with mock.patch("builtins.input", return_value="no"):
            actual_result = ask_yes_no("No?")
            assert not actual_result

    def test_get_size(self):
        with mock.patch("builtins.input", return_value="10"):
            actual_result = get_wall_size_normal("length")
            assert actual_result == 10

    #def test_get_size(self):
    #    with mock.patch("builtins.input", return_value="number":
    #        assert get_wall_size_normal("length") is ValueError



if __name__ == '__main__':
    unittest.main()
