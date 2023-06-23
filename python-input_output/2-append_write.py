#!/usr/bin/python3
"""Contains the fuunction append_write"""


def append_write(filename="", text=""):
    """Appends a string at the end of a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
