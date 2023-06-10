#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        bina = a / b
    except ZeroDivisionError:
        bina = None
    finally:
        print("Inside result: {}".format(bina))
        return bina
