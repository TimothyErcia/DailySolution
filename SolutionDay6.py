"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, 
since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
"""
import math as math
import numpy as np

def getNonAdjacentValue(value):
    number1 = 0
    number2 = 0

    for position in range(len(value)):
        if position % 2 == 0:
            number1 = number1 + value[position]
        else:
            number2 = number2 + value[position]
    if number1 > number2:
        return number1
    elif number1 == number2:
        maxNum = arr2[len(value) - 1]
        minNum = arr2[0]
        number1 = maxNum + minNum
        return number1
    else:
        return number2 

val = getNonAdjacentValue(arr)
print(val)
