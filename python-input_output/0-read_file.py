#!/usr/bin/python3
"""Contains the function read_file()"""


def read_file(filename=""):
    """Reads a file and prints it to the stdout"""
    with open("my_file_0.txt", encoding="UTF8") as fil:
        print(fil.read(), end="")
