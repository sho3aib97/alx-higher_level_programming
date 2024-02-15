#!/usr/bin/python3
'''
Creating my first base class
'''

class Base:
    ''' base class to check other classes for repetitiveness '''

    __nb_objects = 0
    def __init__(self, id=None):
        ''' instantiation of the base class '''

        if id != None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
