#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing max_integer()"""

    def test_Result(self):
        """Checks for the return value to be correct"""
        self.assertEqual(max_integer([1, 4, 19, 0]), 19)
        self.assertEqual(max_integer([-30, -1, -3]), -1)
        self.assertEqual(max_integer([4.5, 1, 9.2, 9.1]), 9.2)
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([20, float("Inf")]), float("inf"))
        self.assertEqual(max_integer([1]), 1)

    def test_CorrectType(self):
        """Checks for a TypeError to be raised"""
        with self.assertRaises(TypeError):
            max_integer(["five", 9, 17, 14])
        with self.assertRaises(TypeError):
            max_integer([4, None, 19, 1])

    def test_EmptyList(self):
        """Checks for the return value to be correct (None)"""
        self.assertEqual(max_integer([]), None)

if __name__ == "__main_":
    unittest.main()
