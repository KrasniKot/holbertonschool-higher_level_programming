#!/usr/bin/python3

import sys
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    operators = ["+", "-", "*", "/"]
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i in range(len(operators))