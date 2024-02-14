#!/usr/bin/python3
''' function that determines the membership of an obj in a class '''

def is_same_class(obj, a_class):
    '''' check for memebership '''
    return type(obj) == a_class
