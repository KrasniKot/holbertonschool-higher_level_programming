#!/usr/bin/python3
"""Contains the class Base"""
import json


class Base:
    """
    Defines a Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Returns the JSON representation of an instance"""
        inlistdict = []

        if list_objs is not None:
            for instance in list_objs:
                inlistdict.append(instance.to_dictionary())

        with open(str(cls.__name__) + ".json", "w", encoding="utf8") as f:
            f.write(cls.to_json_string(inlistdict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the string representation of JSON data"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)
