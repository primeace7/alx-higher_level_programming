#!/usr/bin/python3

'''
define a function that determines if an object is an instance of a class, or an
instance of the class' derivative
'''


def is_kind_of_class(obj, a_class):
    '''
    determine if an object is an instance of a class, or an instance
     of its derivative

    Args:
    obj(object): an object to check
    a_class(class): a class to check if obj is an instnace or
        derivative of

    Returns(bool):
    True: if obj is an instance of a_class, or an instance of
        a_class' derivatives
    False: if obj isn't an instance of a_class, or an instance of its
        derivatives
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
