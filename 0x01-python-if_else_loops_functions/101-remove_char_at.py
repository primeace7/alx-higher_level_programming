#!/usr/bin/python3
def remove_char_at(string, n):
    copy = string
    string = ''
    for i in range(len(copy)):
        if i == n:
            continue
        string += copy[i]
    return string
