#!/usr/bin/python3
'''
This module is an implementation of an add function
'''


def add_integer(a, b=98):
    '''
    Add two integers and return the result

    Args:
    a (int): the addend
    b (int, optional): the augend

    Return:
    int: the sum of a and b

    Raises:
    TypeError: a or b or both aren't integers
    '''
    if a is None or (type(a) not in [int, float]):
        raise TypeError('a must be an integer')
    elif b is None or (type(b) not in [int, float]):
        raise TypeError('b must be an integer')

    if a + 1 == a:
        raise TypeError('a must be an integer')
    elif b + 1 == b:
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return a + b
