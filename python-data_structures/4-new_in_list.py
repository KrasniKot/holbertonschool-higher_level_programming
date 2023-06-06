#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > 0 and my_list[idx]:
        cpylist = my_list.copy()
        cpylist[idx] = element
        return cpylist
    return my_list
