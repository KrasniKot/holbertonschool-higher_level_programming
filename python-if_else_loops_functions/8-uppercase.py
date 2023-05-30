#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in range(0, len(str)):
        if ord(str[i]) < 123 and ord(str[i]) > 96:
            new += chr(ord(str[i]) - 32)
        else:
            new += str[i]
    print("{}".format(new))
