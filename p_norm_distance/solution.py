#!/bin/python3

import math
import os
import random
import re
import sys

"""
This assignment is to print out the p_norm distance between two points for a given p-value.
Input: x1 y1 x2 y2 p
If the user inputs 0, terminate.
"""

def p_norm(arr):
    p = arr[4]
    firstTerm = math.pow(abs((arr[0] - arr[2])), p)
    secondTerm = math.pow(abs((arr[1] - arr[3])), p)
    res = math.pow((firstTerm + secondTerm), 1/p)
    return res


while True:
    val = input()
    # Loop until user inputs a single 0
    if val == "0":
        break

    # If there is no 0, we assume that we have an array of 5 decimal numbers, where the last one is the p-value
    # Convert the line read into an array by removing trailing whitespaces and then splitting the string on any whitespace
    arr = list(map(float, val.rstrip().split())) # Use map to convert the values to floats
    res = p_norm(arr)
    print(res)
