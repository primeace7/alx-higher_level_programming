#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    for i in range(len(my_list)):
        out = my_list[len(my_list) - 1 - i]
        print("{:d}".format(out))
