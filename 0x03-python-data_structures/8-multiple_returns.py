#!/usr/bin/python3
def multiple_returns(sentence):
    string_len = len(sentence)
    new_tuple = ()
    new_tuple += string_len,
    if string_len == 0:
        new_tuple += None,
    else:
        new_tuple += sentence[0],
    return new_tuple
