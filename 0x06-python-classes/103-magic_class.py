#!/usr/bin/python3
'''
create a circle class
'''
import dis
import math


class MagicClass:
    '''define a class that represents a circle'''
    def __init__(self, radius=0):
        '''
        Args:
        radius(int or float, optional): the circle's radius

        Raises:
        TypeError: if radius is not int or float
        '''
        if type(radius) == int or type(radius) == float:
            self.__radius = radius
        else:
            raise TypeError('radius must be a number')

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return self.__radius * math.pi * 2
