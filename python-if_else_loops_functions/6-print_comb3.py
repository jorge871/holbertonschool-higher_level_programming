#!/usr/bin/python3
for x in range(10):
    for t in range(10):
        if x < t:
            print("{:d}{:d}".format(x, t), end='')
            if x < 8:
                print(",", end=' ')
            else:
                print("")
