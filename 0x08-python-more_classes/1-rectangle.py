#!/usr/bin/python3
'''
Rectangle class with height and width
'''

class Rectangle:
    ''' rectangle class with w, h properties '''
    def __init__(self, width=0, height=0):
        ''' constructing the class '''
        self.height = height
        self.width = width 
    @property
    def width(self):
        ''' defining width property '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' defining width setter '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        ''' defining height property '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' defining height setter '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
