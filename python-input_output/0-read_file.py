#!/usr/bin/python3
"""Contains the function read_file()"""


def read_file(filename=""):
    with open("my_file_0.txt", encoding = "UTF8") as file:
        print(file.read(), end="")
