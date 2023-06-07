#!/usr/bin/python3

'''
this module contains a square-printing function
'''


def print_square(size):
    '''
    Print a physical representation of a square with #s

    Args:
    size(int): the dimension of the square to print

    Returns: nothing

    Raises:
    TypeError: if size isn't an integer
    ValueError: if size is < 0
    '''
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    if size == 0:
        print()
        return

    for i in range(size):
        for i in range(size):
            print('#', end='')
        print()
