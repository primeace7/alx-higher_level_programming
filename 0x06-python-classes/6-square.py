#!/usr/bin/python3
'''
    This module defines a class, Square, as in, the plane shape
    from mathematics
'''


class Square:
    '''
    A class defining a square plane shape
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        initialize the square properties

        Args:
            size (int, optional): the dimension of the square
        '''
        self.size = size
        self.position = position

    @property
    def position(self):
        '''
        Getter and setter for the privagte position attribute

        Args:
        value(tuple, for setter): a tuple representing the coordinates
           begining of the square's printing

        Returns:
        tuple(for getter): the value of the square's position

        Raises:
        TypeError: when position isn't a 2-element tuple of integers
        '''
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int\
           or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

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

    def my_print(self):
        '''
        print a physical representation of the square using #s
        '''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[1] <= 1:
                    for i in range(self.__position[0]):
                        print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
