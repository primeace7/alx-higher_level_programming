#!/usr/bin/python3

'''
implement a Rectangle class from BaseGeometry class
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    define a Rectangle shape object

    Params:
    width(int): the width of the rectangle
    height(int): the height of the rectangle

    Args:
    width(int): the width of the rectangle
    height(int): the height of the rectangle
    '''

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator('width', self.__width)
        self.integer_validator('height', self.__height)
