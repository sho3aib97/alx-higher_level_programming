#!/usr/bin/python3
''' check for instance and subclass '''

def is_kind_of_class(obj, a_class):
    ''' function check obj class and it's superclass '''
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
