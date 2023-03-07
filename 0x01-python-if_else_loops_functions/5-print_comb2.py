#!/usr/bin/python3
for i in range(0, 100):
    first_digit = int(i / 10)
    last_digit = i - (first_digit * 100)
    if i != 99:
        print('{:02d}'.format(i), end=', ')
    elif i == 99:
        print('{:02d}'.format(i))
