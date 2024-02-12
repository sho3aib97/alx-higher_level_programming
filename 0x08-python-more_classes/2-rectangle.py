#!/usr/bin/python3
'''
Rectangle class with height and width
'''

class Rectangle:
    ''' Rectangle class with w, h properties '''
    def __init__(self, width=0, height=0):
        ''' Constructing the class '''
        self.height = height
        self.width = width
    @property
    def width(self):
        ''' Defining width property '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Defining width setter '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        ''' Defining height property '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Defining height setter '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
       ''' Calculating area '''
       return self.__width * self.__height

    def perimeter(self):
       ''' Calculating perimeter '''
       if self.__width == 0 or self.__height == 0:
           return 0
       return 2 * (self.__width + self.__height)
