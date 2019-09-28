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

# Helpful links for the knapsack problem are below
# https://www.quora.com/Whats-an-intuitive-explanation-for-the-0-1-knapsack-problem-in-data-structures-and-algorithms
# https://medium.com/@fabianterh/how-to-solve-the-knapsack-problem-with-dynamic-programming-eb88c706d3cf
def knapsack_solution(items, capacity):
    """
    The Knapsack solution idea is to use dynamic programming (solving sub-problems) by createing
    a 2-dimensional array to keep track of the maximum weight that can be obtained with a combination of items.
    A row number i represents the set of all items from rows 1->i. For instance, values in row
    4 assumes that we are only using item 1, 2, 3 and 4.
    A column number w represents the weight capacity of our knapsack, so values in column 8 assumes that our
    knapsack can hold 8 weight units.
    All in all, an entry K[i][w] represents the maximum weight that can be obtained with items 1, 2, 3,..., i in a
    knapsack with w weight units.

    Concrete example with capacity = 10, n = 4, weights = {5, 4, 6, 3}, values = {10, 40, 30, 50}
    (In our case we store the weights directly instead of values but the principle is the same)
                0   1   2   3   4   5   6   7   8   9   10
    0 Items     0   0   0   0   0   0   0   0   0   0   0
    Item 1      0   0   0   0   0   10  10  10  10  10  10
    Item 2      0   0   0   0   40  40  40  40  40  50  50
    Item 3      0
    Item 4      0

    At row 3 (item 2), and column 5 (knapsack capacity of 4), we can choose to either include item 2
    (which weighs 4 units) or not. If we choose not to include it, the maximum value we can obtain is the
    same as if we only have item 1 to choose from (which is found in the row above, i.e. 0).
    If we want to include item 2, the maximum value we can obtain with item 2 is the value of item 2 (40) + the maximum value
    we can obtain with the remaining capacity (which is 0, because the knapsack is completely full already).

    At row 3 (item 2), and column 10 (knapsack capacity of 9), again, we can choose to either include item 2 or not.
    If we choose not to, the maximum value we can obtain is the same as that in the row above at the same column, i.e. 10
    (by including only item 1, which has a value of 10).
    If we include item 2, we have a remaining knapsack capacity of 9 - 4 = 5. We can find out the maximum value that can
    be obtained with a capacity of 5 by looking at the row above, at column 5.
    Thus, the maximum value we can obtain by including item 2 is 40 (the value of item 2) + 10 = 50.
    We pick the larger of 50 vs 10, and so the maximum value we can obtain with items 1 and 2, with a knapsack capacity of 9, is 50.

    """
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
            # If the current item weight is lower than the current capacity column, item i can be part of the solution
            if wi <= w:
                # K[i - 1][w - wi] + wi = The weight we can obtain by including the current item
                # K[i - 1][w] = The weight we can obtain by not including the current item, copy the value straight above this one, previous row but same capacity column
                K[i][w] = max([K[i - 1][w - wi] + wi, K[i - 1][w]])
            # Item i cannot be part of the solution
            else:
                # Set the maximum weight with the current item included to the maximum weight that we can obtain without it
                K[i][w] = K[i - 1][w]

    # Return the last cell in the matrix (the maximum weight)
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
