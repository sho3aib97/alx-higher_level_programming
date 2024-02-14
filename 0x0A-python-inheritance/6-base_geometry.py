#!/usr/bin/python3
''' writing empty class '''

class BaseGeometry:
    ''' base class for geometric shapes '''

    def area(self):
        raise Exception('area() is not implemented')
