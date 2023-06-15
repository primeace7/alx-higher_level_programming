#!/usr/bin/python3

'''
Define a function that appends text to a file
'''


def append_write(filename="", text=""):
    '''
    Append a string to the end of a text file

    Args:
    filename(string): the name of the file to append to
    text(string): the string to append to the file

    Returns:
    count(int): the number of charactters written to the file
    '''
    with open(filename, mode='a', encoding='UTF8') as content:
        count = content.write(text)
        return count
