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
        '''
        raise Exception('area() is not implemented')
