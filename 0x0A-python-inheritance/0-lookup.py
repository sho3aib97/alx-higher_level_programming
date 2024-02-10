#!/usr/bin/python3
""" return the attr and methods of an obj """

def lookup(obj):
""" lookup function
Args:
    obj (object): the object to list its attrs
Returns:
    list: list of methods and attributes
"""
    return dir(obj)
