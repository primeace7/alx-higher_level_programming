#!/usr/bin/python3

'''
Define a function to deserialize a json object
'''

import json


def from_json_string(my_str):
    '''
    deserialize a json object and return the python equivalent

    Args:
    my_str(object): the json object to deserialize

    Returns:
    text(object): the python equivalent of my_str
    '''
    text = json.loads(my_str)
    return text
