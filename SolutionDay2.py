"""
Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

import math

array = [1, 2, 3, 4, 5]
max_len = len(array)
number = math.factorial(max_len)
mlist = []
i = 0
while i != max_len:
    j = int(number * (1 / array[i]))
    i+=1
    mlist.append(j)
print(mlist)
