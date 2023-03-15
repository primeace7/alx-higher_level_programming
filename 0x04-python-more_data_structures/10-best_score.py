#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(list(a_dictionary)) == 0:
        return None
    largest_key = ''
    largest_val = -999999

    for key, value in a_dictionary.items():
        if value > largest_val:
            largest_val = value
            largest_key = key
    return largest_key
