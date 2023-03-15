#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return my_list
    result = [replace if i == search else i for i in my_list]
    return result
