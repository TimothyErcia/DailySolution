"""
This question was asked by Zillow.
You are given a 2-d matrix where each cell represents number of coins in that cell. 
Assuming we start at matrix[0][0], and can only move right or down, 
find the maximum number of coins you can collect by the bottom right corner.
For example, in this matrix
0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""
import math as math
import numpy as np

np_matrix = np.array([
    [0,3,1,1], 
    [2,0,0,4], 
    [1,5,3,1]])
i = 0
j = 0

varSum = 0

start = np_matrix[0][0]
down = np_matrix[i+1][j]
right = np_matrix[i][j+1]

maxNum = np_matrix.shape
def rootAdd(valueI, valueJ):
    start = np_matrix[valueI][valueJ]
    down = np_matrix[valueI+1][valueJ]
    right = np_matrix[valueI][valueJ+1]

#end = np_matrix[2][3]
print(maxNum1)
    

