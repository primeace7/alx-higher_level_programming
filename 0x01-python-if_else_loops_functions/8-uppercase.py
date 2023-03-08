#!/usr/bin/python3
def uppercase(str):
    if str == '':
        str = '\n'
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            if i == str[-1]:
                use = '\n'
            else:
                use = ''
            print('{}'.format(chr(ord(i) - 32)), end=use)
        else:
            if i == str[-1] and str != '\n':
                use = '\n'
            else:
                use = ''
            print('{}'.format(i), end=use)
