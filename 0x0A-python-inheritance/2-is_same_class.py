#!/usr/bin/python3

'''
define a function that determines if an object is an instance of a class
'''


def is_same_class(obj, a_class):
    '''
    determine if an object is an instance of a class

    Args:
    obj(object): the object whos instance status is to be checked
    a_class(class): the class to check for the instance of obj

    Returns(bool):
    True: if obj is an instance of a_class
    False: if obj isn't an instance of a_class
    '''
    if type(obj) == a_class:
        return True
    else:
        return False
