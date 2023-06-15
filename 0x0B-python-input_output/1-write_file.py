#!/usr/bin/python3

'''
Define a function to write to a text file
'''


def write_file(filename="", text=""):
    '''
    Write a string to a text file

    Args:
    filename(string): the name (or pathname) of the file to open and write to
    text(string): the input string to be written to a file

    Returns:
    count(int): the number of characters actually written to filename
    '''
    with open(filename, mode='w', encoding='UTF8') as content:
        count = content.write(text)
        return count
