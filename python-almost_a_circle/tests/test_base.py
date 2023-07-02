#!/usr/bin/python3
import unittest
from os import path, remove
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""Unittest for the class Base"""


class TestBase(unittest.TestCase):
    """Class Base Test"""
    def test_id(self):
        """Test for the correct id of instances"""
        shape = Base()
        self.assertEqual(shape.id, 1)
        shape1 = Base()
        self.assertEqual(shape1.id, 2)
        shape2 = Base(2)
        self.assertEqual(shape2.id, 2)
        shape3 = Base(-19)
        self.assertEqual(shape3.id, -19)
        shape4 = Base(None)
        self.assertEqual(shape4.id, 3)
        shape5 = Base("a string")
        self.assertEqual(shape5.id, "a string")
        shape6 = Base(1.2)
        self.assertEqual(shape6.id, 1.2)
        shape7 = Base(True)
        self.assertEqual(shape7.id, True)
        shape8 = Base(float("inf"))
        self.assertEqual(shape8.id is float("inf"), False)
        shape9 = Base(float("nan"))
        self.assertEqual(shape9.id is float("nan"), False)
        with self.assertRaises(NameError):
            shape = Base(x)

    def test_to_json_string(self):
        """Test for to_json_string() method"""
        self.assertEqual(Base.to_json_string([{"id": 9}]), '[{"id": 9}]')
        self.assertEqual(Base.to_json_string([None]), "[null]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([True]), "[true]")
        self.assertEqual(Base.to_json_string([False]), "[false]")

        dicty = Rectangle(9, 4, 1, 7).to_dictionary()
        dictyson = Base.to_json_string([dicty])
        self.assertTrue(type(dictyson), dict)
        self.assertTrue(type(dictyson) is str)

    def test_save_and_load(self):
        """Test for save to file"""
        square = Square(10, 0, 0, 2)
        square1 = Square(5, 2, 2, "an id")
        Square.save_to_file([square, square1])
        self.assertTrue(path.isfile("Square.json"))
        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertEqual(
                    f.read(),
                    '[{"id": 2, "x": 0, "y": 0, "size": 10},'
                    ' {"id": "an id", "x": 2, "y": 2, "size": 5}]')
        self.assertIsInstance(Square.load_from_file()[0], Square)
        remove("Square.json")

        Rectangle.save_to_file([])
        self.assertTrue(path.isfile("Rectangle.json"))
        self.assertEqual(Rectangle.load_from_file(), [])
        remove("Rectangle.json")

        Base.save_to_file(None)
        self.assertTrue(path.isfile("Base.json"))
        self.assertEqual(Base.load_from_file(), [])
        remove("Base.json")

    def test_from_json_string(self):
        """Test for from_json_string()"""
        self.assertEqual(Base.from_json_string(
            '[{"height": 27, "id": 9}]'),
            [{"height": 27, "id": 9}])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[]'), [])

        Shape = Base.load_from_file()
        self.assertEqual(Base.save_to_file(Shape), None)


if __name__ == "__main__":
    unittest.main()
