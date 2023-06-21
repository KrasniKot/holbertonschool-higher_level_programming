#!/usr/bin/python3
"""Contains lookup()"""

def lookup(obj):
    """Return a list of valid atributes of obj"""
    return dir(obj)