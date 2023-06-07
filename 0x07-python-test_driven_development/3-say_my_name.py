#!/usr/bin/python3

'''
this module implements a name-printing function
'''


def say_my_name(first_name, last_name=""):
    '''
    Print out a person's name

    Args:
    first_name(string): first name
    last_name(string, optional): last name

    Returns: nothing

    Raises:
    TypeError: if first_name or last_name, or both, aren't strings
    '''
    if first_name is None or type(first_name) != str:
        raise TypeError('first_name must be a string')
    if last_name is None or type(last_name) != str:
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}'.strip())
