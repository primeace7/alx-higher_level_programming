#!/usr/bin/python3

'''
list_division: divide 2 lists, element by element


Args:
    my_list_1: the list of dividends

    my_list_2: the list of divisors

    list_length: the length of the list to return

Return:
    A list of quotients of length list_length

'''


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print('division by 0')
            result.append(0)
        except TypeError:
            print('wrong type')
            result.append(0)
        except IndexError:
            print('out of range')
            result.append(0)
    return result
