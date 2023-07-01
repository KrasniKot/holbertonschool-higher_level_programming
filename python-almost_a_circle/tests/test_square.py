#!/usr/bin/python3
import unittest
from models.square import Square
"""Contains tests for the class Square"""


class TestSquare(unittest.TestCase):
    """Square tests"""

    def test_print(self):
        """tests __str__()"""
        square = Square(2, 3, 1, 4)
        self.assertEqual(str(square), "[Square] (4) 3/1 - 2")

    def test_update(self):
        """Tests update()"""
        square = Square(1, 1, 2, 3)
        self.assertEqual(str(square), "[Square] (3) 1/2 - 1")
        square.update(1, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (1) 3/4 - 2")
        square.update(0)
        self.assertEqual(str(square), "[Square] (0) 3/4 - 2")
        square.update(0, 40)
        self.assertEqual(str(square), "[Square] (0) 3/4 - 40")
        square.update(0, 30, 40)
        self.assertEqual(str(square), "[Square] (0) 40/4 - 30")
        square.update(0, 40, 50, 0)
        self.assertEqual(str(square), "[Square] (0) 50/0 - 40")
