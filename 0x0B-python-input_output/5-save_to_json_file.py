#!/usr/bin/python3

'''
Define a function to serialize an object to JSON
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    serialize an object input into a JSON file

    Args:
    my_obj(object): the python object to serialize
    filename(string): the name (or pathname) of the JSON file to create
    '''
    with open(filename, mode='a', encoding='UTF8') as file_out:
        json.dump(my_obj, file_out)
