#!/usr/bin/python3
import dis
def testing():
    from test2 import sub, add
    add()
    sub()

print(dis.dis(testing))
