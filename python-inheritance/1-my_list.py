#!/usr/bin/python3
"""Created class 'MyList' that inherits from list"""


class Mylist(list):
    """define class Mylist"""
    def print_sorted(self):
        """prints the list in ascending order"""
        new_list = self.copy()
        new_list.sort()
        print(new_list)
