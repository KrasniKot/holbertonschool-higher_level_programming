#!/usr/bin/python3
def no_c(my_string):
    strcpy = ""
    for i in my_string:
        if i != "C" and i != "c":
            strcpy += i
    return strcpy
