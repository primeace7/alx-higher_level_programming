#!/usr/bin/python3

'''
define a module to read a file
'''


def read_file(filename=""):
    '''
    open and print the content of a file

    Args:
    filename(string): the pathname(or filename) of the file to be opened
    '''
    with open(filename, mode='r', encoding='UTF8') as text:
        print(text.read())
