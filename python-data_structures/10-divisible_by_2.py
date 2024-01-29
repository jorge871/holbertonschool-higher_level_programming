#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_list_t = list(my_list)
    for t in range(len(my_list)):
        my_list_t[t] = (False if my_list[t] % 2 != 0 else True)
    return my_list_t
