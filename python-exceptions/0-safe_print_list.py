#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    pel = 0
    for el in range(x):
        try:
            print("{:d}".format(my_list[el]), end="")
            pel += 1
        except IndexError:
            break
    print()
    return pel
