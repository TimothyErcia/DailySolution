"""
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
"""
import math


def isPositive(array = None):
    max_len = len(array)
    counter = 1
    i = 0
    while i != max_len:
        if array[i] == counter and array[i] > 0:
            counter += 1
            i += 1

        elif array[i] != counter and array[i] > 0 and counter not in array:
            print(counter)
            break

        else:
            i += 1
            counter += 1

isPositive(array = [-1, 1, 0, 3])
