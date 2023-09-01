#!/usr/bin/python3

'''
implement a function that find the peak from a set of numbers
'''

def find_peak(list_of_integers):
    '''
    find the peak from a list of numbers
    '''

    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        for i in range(len(list_of_integers)):
            if i == 0 and list_of_integers[i] >= list_of_integers[1]:
                return list_of_integers[i]
            elif i == len(list_of_integers) - 1 and list_of_integers[i] >=\
                 list_of_integers[-2]:
                return list_of_integers[i]
            else:
                continue

            if list_of_integers[i] >= list_of_integers[i - 1] and\
               list_of_integers[i] >= list_of_integers[i + 1]:
                return list_of_integers[i]

        return None

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
