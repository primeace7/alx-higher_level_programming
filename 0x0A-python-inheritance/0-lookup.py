#!/usr/bin/python3

'''
define a function that returns all the names (functions, variables, attributes)
defined in a particular object'''

def lookup(obj):
    '''
    return list of names defined in an object

    Args:
    obj(object type): the object whose defined names should be returned

    Returns:
    list: a list of the defined names in obj
    '''

    return dir(obj)
