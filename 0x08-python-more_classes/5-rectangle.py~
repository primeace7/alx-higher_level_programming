#!/usr/bin/python3

'''
A rectangle class module
'''


class Rectangle():
    '''
    A rectangle class

    Args:
    width(int): rectangle width
    height(int): rectangle height

    Attributes:
    width(int): rectangle width
    height(int): rectangle height
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Getter and setter methods for private width attribute

        Getter returns the width, setter modifies the value of width

        Args(for setter):
        value(int): the value to set width to

        Raises(for setter):
        TypeError: if width isn't an integer
        ValueError: if width < 0
        '''

        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        '''
        Getter and setter methods for private height attribute

        Getter returns the height, setter modifies the value of height

        Args(for setter):
        value(int): the value to set height to

        Raises(for setter):
        TypeError: if height isn't an integer
        ValueError: if height < 0
        '''

        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        '''
        calculate the rectangle area

        Returns(int): the area of a rectangle instance
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        '''
        calculate the rectangle perimeter

        Returns(int): the perimeter of a rectangle instance
        '''
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        draw_rect = ''
        for i in range(self.__height):
            for j in range(self.__width):
                draw_rect += '#'
            if i != self.__height - 1:
                draw_rect += '\n'
        return draw_rect

    def __repr__(self):
        return 'Rectangle(' + str(self.__width) + ', ' +\
            str(self.__height) + ')'
