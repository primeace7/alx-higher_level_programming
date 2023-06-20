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

    @classmethod
    def save_to_file(cls, list_objs):
        with open(f'{cls.__name__}.json', mode='a', encoding='UTF8') as json_file:
            if list_objs is None:
                json_string = cls.to_json_string([])
            else:
                list_of_dicts = []
                for obj in list_objs:
                    list_of_dicts.append(obj.to_dictionary())
                json_string = cls.to_json_string(list_of_dicts)

            json_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        kwargs = dictionary

        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1, 1, 1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1, 1, 1, 1)

        dummy_instance.update(**kwargs)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        instances_list = []

        try:
            with open(f'{cls.__name__}.json', mode='r', encoding='UTF8') as json_file:
                instance_dict_list = (json_file.read()).replace('\n', '')
                instance_dict_list = cls.from_json_string(instance_dict_list)
                print(instance_dict_list)
                for instance in instance_dict_list:
                    instances_list.append(cls.create(**instance))
            return instances_list
        except FileNotFoundError:
            return instances_list
        except Exception:
            raise
