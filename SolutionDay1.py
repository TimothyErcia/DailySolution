"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

import math
import itertools

def IsEqualtoK(k, array):
    i = 0
    max_len = len(array) - 1
    while i != max_len:
        try:
            permu = list(itertools.permutations(array, 2))
            mSum = sum(permu[i])
            if mSum == k:
                print("true " + str(permu[i]))
            else:
                print("false " + str(permu[i]))
            i = i + 1
        except:
            print("Hello Error") 
            break

IsEqualtoK(17, [10, 5, 3, 7])
