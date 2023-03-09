#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    arglist_len = len(argv)

    sum = 0
    for i in range(1, arglist_len):
        sum += int(argv[i])
    print(sum)
