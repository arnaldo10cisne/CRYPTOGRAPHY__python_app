import unittest
from functions_module import *


class testFunctionsModule(unittest.TestCase):

    #Tests for the GET_PATTERN function
    def test_get_pattern(self):
        self.assertEqual(get_pattern("moon"), "0112")
        self.assertEqual(get_pattern("arnaldo"), "0120345")
        self.assertEqual(get_pattern(""), "")
        self.assertEqual(get_pattern("ababab"), "010101")
        self.assertEqual(get_pattern("ok"), "01")
        self.assertEqual(get_pattern("uncopyrightables"), "0123456789ABCDEF")


if __name__ == '__main__':
    unittest.main()