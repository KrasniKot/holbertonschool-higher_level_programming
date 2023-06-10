#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    flist = []
    for idx in range(list_length):
        idxrlt = 0
        try:
            idxrlt = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            flist.append(idxrlt)
    return flist
