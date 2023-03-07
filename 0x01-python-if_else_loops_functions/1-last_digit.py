#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
leading_digits = int(number/10)
last_digit = number - (leading_digits * 10)
print(f'Last digit of {number} is {last_digit} and ', end='')
if last_digit == 0:
    print(f'is 0')
elif last_digit > 5:
    print(f'is greater than 5')
elif last_digit < 6 and last_digit != 0:
    print(f'is less than 6 and not 0')
