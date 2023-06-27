#!/usr/bin/python3
"""Contains write"""


def write_file(filename="", text=""):
    """Write text to a fie"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
