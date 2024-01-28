#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    all_args = 0
    for x in range(1, len(argv)):
        all_args = all_args + int(argv[x])
    print(f"{all_args:d}")
