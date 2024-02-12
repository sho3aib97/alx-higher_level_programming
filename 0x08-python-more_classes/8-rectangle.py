#!/usr/bin/python3
'''
Rectangle class with height and width
'''

class Rectangle:
    ''' Rectangle class with w, h properties '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        ''' Constructing the class '''
        self.height = height
        self.width = width

        Rectangle.number_of_instances += 1

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

    def __str__(self):
        ''' Redefining __str__ '''
        string = ""
        if self.__height != 0 and self.__width != 0:
            string += '\n'.join(str(self.print_symbol) * self.__width for h in range(self.__height))
        return string
    
    def __repr__(self):
        ''' Redefining __repr__ '''
        return "Rectangle(" + str(self.__width) + ', ' + str(self.__height) + ')'

    def __del__(self):
        ''' Redefining __del__'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' Static method to compare obj '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
