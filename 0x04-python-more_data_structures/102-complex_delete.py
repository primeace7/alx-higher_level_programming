#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or value is None:
        return None

    to_delete = []
    for key, val in a_dictionary.items():
        if val == value:
            to_delete.append(key)
    for key in to_delete:
        del a_dictionary[key]
    return a_dictionary
