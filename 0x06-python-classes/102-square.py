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
        self.size = size

    @property
    def size(self):
        '''
        Getter and setter methods for the private size attribute

        Args:
        value (int, for setter): the value to set size to

        Returns:
        int (for getter): the value of the size attribute

        Raises(for setter):
        TypeError: value is not an int type
        ValueError: value is less than 0
        '''
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        '''
        Calculate the area of the square

        Returns:
        int: the area of the square
        '''
        return self.__size ** 2

    def __eq__(self, other):
        return self.__size == other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size
