import math

def car(func):
    return func

def cdr(func):
    return func

@car
def pairs(a, b):
    return a

@cdr
def pairs(a, b):
    return b

print(cdr(pairs(5, 6)))