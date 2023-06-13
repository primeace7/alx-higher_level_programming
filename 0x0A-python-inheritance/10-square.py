#!/usr/bin/python3

'''
implementation of a square class based on Rectangle class
'''

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    '''
    implementation of Square shape class

    Params:
    size: the dimension of the square

    Args:
    size: the dimension of the square
    '''

    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
