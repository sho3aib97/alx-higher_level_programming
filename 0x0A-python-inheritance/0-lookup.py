#!/usr/bin/python3
''' list  the attr and methods of an obj '''

def lookup(obj):
    ''' lookup function to list obj attr and method
    Args:
        obj (object): the object to list its attrs.

    Returns:
        list: list of methods and attributes
    '''
    return dir(obj)
