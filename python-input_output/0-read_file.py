#!/usr/bin/python3
"""Contains read_file()"""


def read_file(filename=""):
    """Reads a file and prints it to the stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(f"{line}", end="")
