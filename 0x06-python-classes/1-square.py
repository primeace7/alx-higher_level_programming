#!/usr/bin/python3
'''
    This module defines a class, Square, as in, the plane shape
    from mathematics
'''


class Square:
    '''
    A class defining a square plane shape
    '''
    def __init__(self, size):
        '''
        Args:
            size (int, optional): the dimension of the square
        '''

        self.__size = size
