#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    new_list.sort()
    result = 0
    uniq = 0
    for i in new_list:
        if i != uniq:
            result += i
            uniq = i
    return result
