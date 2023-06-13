#!/usr/bin/python3

'''
define a derived list class from list
'''


class MyList(list):
    '''
    a class derived from python's standard list class
    '''

    def print_sorted(self):
        '''
        print a the list sorted in ascending order
        '''
        print(sorted(self))
