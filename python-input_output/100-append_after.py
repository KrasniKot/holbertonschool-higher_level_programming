#!/usr/bin/python3
"""Contains append_after()"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line into a text file"""
    new_cntt = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.readlines():
            new_cntt += line
            if search_string in line:
                new_cntt += new_string

    with open(filename, "w", encoding="utf-8") as f:
        f = f.write(new_cntt)
