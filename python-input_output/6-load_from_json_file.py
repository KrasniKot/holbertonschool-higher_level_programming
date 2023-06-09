#!/usr/bin/python3
"""Contains load_from_json_file()"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
