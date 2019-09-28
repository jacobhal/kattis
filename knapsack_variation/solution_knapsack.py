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

# This solution is the most efficient with O(Wn) complexity, W being the target weight and n being number of items

def split_weight(items):
    nr_of_items = items.pop(0) # Remove nr of items from list
    total_weight = sum(items)
    res = knapsack_solution(items, total_weight/2)
    return res

# https://www.quora.com/Whats-an-intuitive-explanation-for-the-0-1-knapsack-problem-in-data-structures-and-algorithms
def knapsack_solution(items, capacity):
    n = len(items)
    W = int(capacity) # Weight capacity
    # Rows: Items, Cols: Capacity, K(n, W)
    K = [[0 for w in range(W + 1)] for i in range(n)]

    # Iterate over rows
    for i in range(1, n):
        # Iterate over capacities
        for w in range(1, W + 1):
            # Get the weight of the current item row
            wi = items[i]
            print(wi)
            # If the current item weight is lower than the current capacity column it can be used
            if wi <= w:
                # Item i can be part of the solution
                # K[i - 1][w - wi] + wi = previous row, offset index for column by subtracting current weight. Add current weight.
                # K[i - 1][w] = copy the value straight above this one, previous row but same capacity column
                K[i][w] = max([K[i - 1][w - wi] + wi, K[i - 1][w]])
            else:
                # Item i cannot be part of the solution, so set it to the previous item
                K[i][w] = K[i - 1][w]
            print(K[i][w])

    return [capacity*2 - K[n - 1][W], K[n - 1][W]]


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
