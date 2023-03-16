#!/usr/bin/python3
'''
In this solution, counting starts from the back so previous refers to the
letter after current. For example in the roman_string XLVI, during the first
iteration through the string, current will be I, and previous will be I.
During the second iteration through the string, current will be V and previous
will be I.

Counting starts from the back because, unlike ini the normal decimal system,
the roman numerals have no place value. The total value of the number doesn't
neccessarily increase as you encounter more significant letters.
'''


def roman_to_int(roman_string):
    if (type(roman_string) is not str) or (roman_string is None):
        return 0

    numerals = dict(V=(5, 1), X=(10, 2), L=(50, 3), C=(100, 4),
                    D=(500, 5), M=(1000, 6))
    numerals['I'] = (1, 0)
    total = 0

    for i in range(len(roman_string)):
        current = numerals[roman_string[-1 - i]]
        previous = numerals[roman_string[-i]]

        if i == 0:
            total += current[0]
        else:
            if current[1] < previous[1]:
                total -= current[0]
            else:
                total += current[0]

    return total
