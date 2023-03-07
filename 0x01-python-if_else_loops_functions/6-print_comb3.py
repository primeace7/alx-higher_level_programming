#!/usr/bin/python3
i = 0
j = i + 1

while i < 9:
    while j < 10:
        if (i == 8) and (j == 9):
            print('{}{}'.format(i, j), end='\n', sep='')
            j += 1
        else:
            print('{}{}'.format(i, j), end=', ', sep='')
            j += 1
    i += 1
    j = i + 1
