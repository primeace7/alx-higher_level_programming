#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            if i == len(str) - 1:
                use = '\n'
            else:
                use = ''
            print('{}'.format(chr(ord(str[i]) - 32)), end=use)
        else:
            if i == len(str) - 1:
                use = '\n'
            else:
                use = ''
            print('{}'.format(str[i]), end=use)
