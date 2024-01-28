#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print(f"{argc - 1} argument:\n{1}: {argv[1]}")
    else:
        print(f"{argc - 1} arguments:")
        for e in range(1, argc):
            print(f"{e}: {argv[e]}")
