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
