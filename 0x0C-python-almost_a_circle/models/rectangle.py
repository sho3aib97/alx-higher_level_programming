#!/usr/bin/python3
''' 
creating Rectangle class, inherets form Base
'''
from models.base import Base

class Rectangle(Base):
    ''' class of Rectangle inherets from Base class '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' instantation of class attrs '''
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def check_value(self, attrName: str, value: object, comparison=True):
        ''' chechs value '''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(attrName))

        if comparison:
            if value <= 0:
                raise ValueError('{} must be > 0'.format(attrName))
            else:
                if value < 0:
                    raise ValueError('{} must be >= 0'.format(attrName))

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @width.setter
    def width(self, width: int):
        ''' width setter '''
        check_value('width', width)
        self.__width = width

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @height.setter
    def height(self, height: int):
        ''' height setter '''
        check_value('height', height)
        self.__height = height


    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @x.setter
    def x(self, x: int):
        ''' x setter '''
        check_value('x', x, False)
        self.__x = x

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @y.setter
    def y(self, y: int):
        ''' y setter '''
        check_value('y', y, False)
        self.__y = y

