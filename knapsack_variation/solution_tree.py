#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

"""
This tree solution is NOT finished.
"""

class Node:
    # Tree node: left and right child + data which can be any object
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # First, check whether we have a root node
        if self.data:
            # If there is a root node and the node we want to add is less than the root, enter left tree
            if data < self.data:
                # Recursively go through the tree and insert
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # If there is a root node and the node we want to add is larger than the root, enter right tree
            elif data > self.data:
                # Recursively go through the tree and insert
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def sum_tree_old(n, current_sum, target):
    if n is not None:
        print("Node value: ", n.data)
    print("Current sum: ", current_sum[0])
    print("Target sum: ", target)
    # Base case:
    if (n == None):
        current_sum[0] = 0
        return False

    sum_left, sum_right = [0], [0]
    x = sum_tree(n.left, sum_left, target)
    y = sum_tree(n.right, sum_right, target)
    current_sum[0] = (sum_left[0] +
                  sum_right[0] + n.data)
    return ((x or y) or (current_sum[0] == target))

def sum_tree(n, current_sum, target):
    if n == None:
        if current_sum > target and current_sum < target*2:
            ans = current_sum
        return 0

    left = sum_tree(n.left, target)
    right = sum_tree(n.right, target)

    result = (sum_left[0] + sum_right[0] + n.data)
    if result == target:
        return result

def split_weight(items):
    nr_of_items = items.pop(0) # Remove nr of items from list
    total_weight = sum(items)
    equal_weight = total_weight/2
    items.sort()
    print(items)
    # Choose root node
    root_index = int(len(items)/2)
    root = Node(items[root_index])
    prefix = items[0:root_index]
    suffix = items[root_index+1:]
    rest = prefix + suffix
    # Add all the rest of the nodes to the tree
    for val in rest:
        root.insert(val)

    ans = 0
    current_sum = 0
    print(sum_tree(root, equal_weight))
    print(ans)

    return [0, 0]

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
