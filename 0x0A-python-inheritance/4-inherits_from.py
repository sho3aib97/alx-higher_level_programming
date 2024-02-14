#!/usr/bin/pytho3
''' check if subclass and not type '''

def inherits_from(obj, a_class):
    ''' function check inheritance without the type '''
    return isinstance(obj, a_class) and type(obj) != a_class
