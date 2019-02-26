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
