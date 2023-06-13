#!/usr/bin/python3

'''
define a function that determines if an object is an instance
   of a class, or an instance of a class that derives from the
   specified class
'''


def inherits_from(obj, a_class):
    '''
    determine if an object is an instance of a class, or an instance of a class
        that derives from the specified class

    Args:
    obj(object): the object to check
    a_class: the class to check

    Returns(bool):
    True: if obj is an instance of a_class, or an instance of a derivative of
        a_class
    False: if obj isn't an instance of a_class or an instance of a
        derivative of a_class
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
