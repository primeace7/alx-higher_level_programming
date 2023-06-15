#!/usr/bin/python3

'''
Define a function that deserialises a JSON file
'''

import json


def load_from_json_file(filename):
    '''
    deserialise a JSON file and return the corresponding python object

    Args:
    filename(string): the name (or pathname) of the file to deserialise

    Returns: the corresponding python object
    '''
    with open(filename, mode='r', encoding='UTF8') as new:
        return json.load(new)
