#!/usr/bin/python3
'''
a definition of a geometric shape's class
'''

class BaseGeometry():
    '''
    a geometric shape definition
    '''
    def area(self):
        '''
        calculate the area of a shape

        Raises:
        Exception: if area calculation isn't defined
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        verify if that value >= 0

        Args:
        name(string): the name of the data 'value'
        value(int): the value to be verified

        Raises:
        TypeError: value isn't an int
        ValueError: value is <= 0
        '''
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
