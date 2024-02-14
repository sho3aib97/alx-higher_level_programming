#!/usr/bin/python3
''' writing empty class '''

class BaseGeometry:
    ''' base class for geometric shapes '''

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' evaluate value '''

        if isinstance(value, int):
            raise TypeError('{} must be an integer'. format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
