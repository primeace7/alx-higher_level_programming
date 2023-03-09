#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arglist_len = len(sys.argv) - 1

    if arglist_len == 0:
        arg = f'{arglist_len} arguments.'
    elif arglist_len == 1:
        arg = f'{arglist_len} argument:'
    else:
        arg = f'{arglist_len} arguments:'

    print(f'{arg}')
    if arglist_len > 0:
        for i in range(1, arglist_len + 1):
            print(f'{i}: {sys.argv[i]}')
