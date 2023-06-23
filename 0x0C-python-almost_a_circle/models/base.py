#!/usr/bin/python3

'''
Definition of some plane shapes
'''
import json
import csv


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
        '''
        Convert a list of dicitonaries to JSON

        Args:
        list_dictionaries(list): list of dicionaries to convert to json string

        Returns:
        (str): the json-string-equivalent of @list_dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        write a list of object dictionaries to a json file

        Args:
        list_objs(list): a list of objects, each object is represented as
            a dictionary.
        '''
        with open(f'{cls.__name__}.json', mode='w', encoding='UTF8') as j_file:
            if list_objs is None:
                json_string = cls.to_json_string([])
            else:
                list_of_dicts = []
                for obj in list_objs:
                    list_of_dicts.append(obj.to_dictionary())
                json_string = cls.to_json_string(list_of_dicts)

            j_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''
        deserialize a json string to its equivalent python object

        Args:
        json_string(str): a json string to be deserialized

        Returns:
        (obj): the python equivalent of json_string
            or an empty list if json_string is empty
        '''
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        create a class instance from an object dictionary

        Args:
        dictionary(:obj: dict): a class instance represented as a dictionary

        Returns:
        (:obj:): an instance of the calling class, cls, created from the
            contents of the input dictionary
        '''

        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''
        create a list of class instances from a json file

        Returns:
        (list): a list of instances of the calling class created from a
            json string with the name <cls>.json
        '''

        try:
            with open(f'{cls.__name__}.json', mode='r', encoding='UTF8') as\
                 json_file:
                obj_dict_list = (json_file.read()).replace('\n', '')
                obj_dict_list = cls.from_json_string(obj_dict_list)
                return [cls.create(**instance) for instance in obj_dict_list]
        except FileNotFoundError:
            print(f'File {cls.__name__}.json not found.')
            return []
        except Exception:
            raise

    @classmethod
    def save_to_file_csv(cls, list_objs):

        if cls.__name__ == 'Rectangle':
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            fieldnames = ['id', 'size', 'x', 'y']

        with open(f'{cls.__name__}.csv', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if list_objs is not None:
                writer.writeheader()
                for instance in list_objs:
                    writer.writerow(instance.to_dictionary())
            else:
                writer.writerow(dict())

    @classmethod
    def load_from_file_csv(cls):
        try:
            with open(f'{cls.__name__}.csv', 'r', newline='') as csfile:
                reader = csv.DictReader(csfile)
                return_list = []
                for instance in reader:
                    for key, val in instance.items():
                        instance[key] = int(val)
                    return_list.append(cls.create(**instance))
                return return_list
        except FileNotFoundError:
            print(f'File {cls.__name__}.csv not found.')
            return []
        except Exception:
            raise
