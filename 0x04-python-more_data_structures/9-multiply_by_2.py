#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    for key in a_dictionary:
        a_dictionary[key] = a_dictionary[key] * 2
    return a_dictionary
