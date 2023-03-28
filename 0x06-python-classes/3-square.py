#!/usr/bin/python3
'''
    This module defines a class, Square, as in, the plane shape
    from mathematics
'''


class Square:
    '''
    A class defining a square plane shape
    '''
    def __init__(self, size=0):
        '''
        initialize the square properties

        Args:
            size (int, optional): the dimension of the square
        '''
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''
        Calculate the area of the square

        Returns:
        int: the area of the square
        '''
        return self.__size ** 2
