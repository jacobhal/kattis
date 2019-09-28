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

# This solution is slightly more effcient than the naive solution

def split_weight(items):
    nr_of_items = items.pop(0) # Remove nr of items from list
    total_weight = sum(items)
    equal_weight = total_weight/2
    # Results array to append to
    equal_weight_result = 0
    closest_lower_weight = 0

    # Define an inner function so we can fill the results array
    def sub_sum(arr, target, partial = []):
        s = sum(partial)

        #print("Array: ", arr)
        #print(f"Partial array: {partial}, partial sum: {s}\n")

        # Base case: Append our sum to results array if it is equal to target
        nonlocal equal_weight_result
        if s == target:
            equal_weight_result = s
            return
        # Update the closest minimum weight
        nonlocal closest_lower_weight # Fetch variable from outer scope
        if s < target and s > closest_lower_weight:
            closest_lower_weight = s
        # Base case: If we have already surpassed the number we want, stop
        if s >= target:
            return

        # Main loop
        for i in range(len(arr)):
            # Assign the current item and then the rest of the array to separate variables
            item = arr[i]
            remaining = arr[i+1:]
            # Do a recursive call with the remaining array as the new array and build our partial array one item at a time
            sub_sum(remaining, target, partial + [item])

    # Call sub_sum to fill results
    sub_sum(items, equal_weight)
    # Check if t
    if equal_weight_result != 0:
        return [equal_weight_result, equal_weight_result]
    return [total_weight - closest_lower_weight, closest_lower_weight]

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
