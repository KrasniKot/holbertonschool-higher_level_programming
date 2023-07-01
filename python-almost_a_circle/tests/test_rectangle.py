#!/usr/bin/python3
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
"""Contains test for the class Rectangle"""


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle"""

    def setUp(self):
        """Set rectangles for later use"""
        self.rectangle = Rectangle(3, 5, 6, 1, "id")
        self.rectangle1 = Rectangle(4, 1)

    def test_area(self):
        """Tests #area()"""
        self.assertEqual(self.rectangle.area(), 15)
        self.assertEqual(self.rectangle1.area(), 4)

    def test_display(self):
        """Tests display()"""
        outt = StringIO()
        sys.stdout = outt
        self.rectangle1.display()
        outt = outt.getvalue()
        self.assertEqual(outt, "####\n")

        outt = StringIO()
        sys.stdout = outt
        self.rectangle.display()
        outt = outt.getvalue()
        self.assertEqual(
                outt,
                "\n      ###\n      ###\n      ###\n      ###\n      ###\n")

    def test_update_print(self):
        """Test update() and __str__()"""
        self.rectangle1.update(1, 1, 1, 1, id="another id")
        outt = StringIO()
        sys.stdout = outt
        print(self.rectangle1)
        outt = outt.getvalue()
        self.assertEqual(
                outt,
                "[Rectangle] (1) 1/0 - 1/1\n")


if __name__ == "__main__":
    unittest.main()
