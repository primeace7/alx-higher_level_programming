#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    if my_list is None:
        return None
    total = 0
    weights = 0

    for tup in my_list:
        total += (tup[0] * tup[1])
        weights += tup[1]
    return total / weights
