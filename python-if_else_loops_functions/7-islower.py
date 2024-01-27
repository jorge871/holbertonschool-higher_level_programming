#!/usr/bin/python3
def islower(c):
    low = ord(c)
    if low in range(97, 123):
        return True
    else:
        return False
