#!/usr/bin/python3
def uppercase(str):
    for upc in str:
        if ord(upc) in range(97, 123):
            upc = chr(ord(upc) - 32)
        print("{}".format(upc), end='')
    print("")
