#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    for key in sorted(a_dictionary):
        print(key, ': ', a_dictionary[key], sep='')
