#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers = 0
    for b in range(0, x):
        try:
            print("{:d}".format(my_list[b]), end="")
            integers += 1
        except (ValueError, TypeError):
            pass
    print()
    return integers
