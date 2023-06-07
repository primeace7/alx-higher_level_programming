#!/usr/bin/python3

'''
this module contains a text indentation function
'''


def text_indentation(text):
    '''
    Indent input text with newlines

    Args:
    text(str): the text string to indent

    Returns: nothing

    Raises:
    TypeError: if text is not a string
    '''
    if type(text) != str or text is None:
        raise TypeError('text must be a string')

    line = ''
    for letter in text:
        line += letter
        if letter in ['.', '?', ':']:
            print(line.strip())
            print()
            line = ''
    if line != '':
        print(line.strip(), end='')
