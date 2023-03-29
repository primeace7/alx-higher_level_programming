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
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
