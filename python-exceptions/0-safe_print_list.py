#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    my_function = 0
    for p in range(0, x):
        try:
            print(my_list[p], end='')
            my_function += 1
        except Exception:
            break
    print()
    return my_function
