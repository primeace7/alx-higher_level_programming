#!/usr/bin/python3

'''
safe_print_list_integers(my_list=[], x=0) - print the first
x elements of a list that are integers

Args:
    my_list: the list to print from

    x: the number of elements to print from my_list
'''


def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            j += 1

        except IndexError:
            raise
        except Exception:
            continue
    if j != 0:
        print()
    return j
