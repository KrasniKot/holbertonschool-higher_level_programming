#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    return sum(a * b for a, b in my_list)/sum(c[1] for c in my_list)
