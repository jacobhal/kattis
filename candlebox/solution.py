#!/bin/python3

import math
import os
import random
import re
import sys

"""
This assignment is called the candlebox problem. We have two persons A and B who start putting
candles in boxes at the ages of 4 and 3 respectively. It turns out that person B has put
candles in the wrong box over the years and the task is to find out how many candles we have
to remove from box A.
The first number is the difference in age between the two and the other two are
the number of candles in box A and B respectively.
Input example: 2
               26
               8 
"""

def candles_to_remove(D, R, T):
    rita_age = 4
    theo_age = 3

    # Define arrays with years where no candles were put into boxes
    theo = [0] * 100
    rita = [0] * 100
    # Fill the arrays with the sum series where indices correspond to the years of Theo and Rita
    # Rita: [0, 0, 0, 0, 4, 9, 15, 22...], Theo: [0, 0, 0, 3, 7, 12, 18...]
    for i in range(len(theo)):
        if i >= rita_age:
            rita[i] = rita[i-1] + i
        if i >= theo_age:
            theo[i] = theo[i-1] + i

    for i in range(D, len(theo)):
        # If we find ages for Theo and Rita with the specified age difference that matches the sum of candles we are done
        # We return the total amount of candles in Rita's box subtracted by the correct amount of candles at her age
        if (theo[i-D] + rita[i] == R + T):
            return R - rita[i]

D = int(input()) # Age difference between Theo and Rita, 1 <= D <= 20
R = int(input()) # Number of candles in Rita's box,  4 <= R < 1000
T = int(input()) # Number of candles in Theo’s box, 0 <= T < 1000

res = candles_to_remove(D, R, T)

print(res)
