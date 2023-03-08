#!/usr/bin/python3
for i in range(0, 26):
    if i % 2 == 0:
        out = chr(ord('z') - i)
    else:
        out = chr(ord('z') - i - 32)
    print('{}'.format(out), end='')
