#!/usr/bin/python3
def fizzbuzz():
    for fzbz in range(1, 101):
        if fzbz % 3 == 0:
            print("Fizz", end=' ')
        if fzbz % 5 == 0:
            print("Buzz", end=' ')
        if fzbz % 3 != 0 and fzbz % 5 != 0:
            print(fzbz, end=' ')
    print("", end=' ')
