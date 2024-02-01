#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())
    for p in keys:
        print("{}:".format(p), a_dictionary[p])
