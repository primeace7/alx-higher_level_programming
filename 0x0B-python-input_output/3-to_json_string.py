#!/usr/bin/python3

'''
Define a function to return a string in JSON
'''
import json

def to_json_string(my_obj):
    '''
    serialize a text as JSON

    Args:
    my_obj(object): the object to serialize

    Returns:
    json_text: the JSON representatio n of obj
    '''
    return (json.dumps(my_obj))
