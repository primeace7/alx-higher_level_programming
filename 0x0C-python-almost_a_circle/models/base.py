#!/usr/bin/python3

'''
Definition of some plane shapes
'''
import json


class Base():
    '''
    Define a plane shape class

    Params:
    id(int): the instance id
    nb_objects(int): the number of instances of this class in existence

    Args:
    id(int): the instance id
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)
