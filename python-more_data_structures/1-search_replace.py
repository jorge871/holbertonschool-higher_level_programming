#!/usr/bin/python3
def search_replace(my_list, search, repleace):
    new_list = list(my_list)
    for i in range (len(new_list)):
        if new_list[i] == search:
            new_list[i] = repleace
    return new_list