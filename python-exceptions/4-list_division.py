#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    p = []
    for b in range(list_length):
        try:
            a = my_list_1[b] / my_list_2[b]
        except TypeError:
            print("wrong type")
            a = 0
        except ZeroDivisionError:
            print("division by 0")
            a = 0
        except IndexError:
            print("out of range")
            a = 0
        finally:
            p.append(a)
    return p
