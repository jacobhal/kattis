#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

"""
This assignment is a variation of the knapsack problem.
We want to fill two backpacks with equal weight if possible, otherwise
come as close as possible and let one of the backpacks carry the rest.
Instead of having both values and weights as in the knapsack problem, we are
dealing with only weights in this case.
The input consists of a first number that represents the number of items, and 
the rest are the weights of each item.
Input example: 3 320 430 100
If the user inputs a single 0, terminate.
"""

# This naive solution goes through all possible combinations of sums with O(n^2) complexity

def split_weight(items):
    nr_of_items = items.pop(0) # Remove nr of items from list
    total_weight = sum(items)
    res = find_closest_weight(items, total_weight/2)
    return res

def find_closest_weight(arr, target):
    lowest_weight = 0
    for i in range(len(arr)+1):
        for subset in itertools.combinations(arr, i):
            s = sum(subset)
            if s == target:
                return [s, s]
            if s < target and s > lowest_weight:
                lowest_weight = s
    return [target*2 - lowest_weight, lowest_weight]

while True:
    val = input()
    # Loop until user inputs a single 0
    if val == "0":
        break

    # If there is no 0, we assume that we have an array of 5 decimal numbers, where the last one is the p-value
    # Convert the line read into an array by removing trailing whitespaces and then splitting the string on any whitespace
    arr = list(map(int, val.rstrip().split())) # Use map to convert the values to floats
    res = split_weight(arr)
    print(f'{int(res[0])} {int(res[1])}')
