#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return 0

    uniq = set(my_list)
    total = 0

    for i in uniq:
        total += i
    return total
