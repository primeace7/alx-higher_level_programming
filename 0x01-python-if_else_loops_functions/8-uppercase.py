#!/usr/bin/python3
def uppercase(str):
    copy = []
    if str == '':
        print()
        return
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            copy.append(chr(ord(i) - 32))
        else:
            copy.append(i)
    for i in range(len(copy)):
        if i == len(copy) - 1:
            use = '\n'
        else:
            use = ''
        print('{}'.format(copy[i]), end=use)
