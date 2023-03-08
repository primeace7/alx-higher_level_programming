#!/usr/bin/python3
import dis
def print_last_digit(number):
    if number < 0:
        number *= -1
    last_digit = number % 10
    print(f'{last_digit}', end='')
    return last_digit

analysis = dis.get_instructions(print_last_digit)
for item in analysis:
    print(item)
