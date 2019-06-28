"""
Given an array, get the number of N in the subset of the array
example:
array = [2,4,6,10]
N = 16
[6, 10], [2, 4, 10] would be the outputs
"""

import numpy as np


arr = [2, 4, 5, 10]
givenN = 16


def getSubset(arr, givenN):
    arr = sorted(arr)
    elem = []
    i = 0
    j = 0
    maxLenght = len(arr) - 1
    while i != maxLenght:
        if arr[i] < givenN:
            getHighest = max(arr)

            if getHighest + arr[i] == givenN:
                elem.append(getHighest)
                elem.append(arr[i])

            if arr[i] + arr[j] == givenN:
                elem.append(arr[j])
                elem.append(arr[i])
            else:
                j+=1

            try:
                if arr[i] + arr[j] + getHighest == givenN:
                    elem.append(getHighest)
                    elem.append(arr[i])
                    elem.append(arr[j])
                else:
                    j+=1
            except:
                pass
        i+=1
    return elem

aa = getSubset(arr, givenN)
print(aa)

