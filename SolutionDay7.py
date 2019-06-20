"""
This problem was asked by LinkedIn.
Given a string, return whether it represents a number. Here are the different kinds of numbers:
•	"10", a positive integer
•	"-10", a negative integer
•	"10.1", a positive real number
•	"-10.1", a negative real number
•	"1e5", a number in scientific notation
And here are examples of non-numbers:
•	"a"
•	"x 1"
•	"a -2"
•	"-"

"""

import math as math
import numpy as np

def Isreal(value):
    if value.isalpha:
        return "non-number"
    elif value.isalnum:
        return "non-number"
    elif value.isnumeric:
        try:
            if int(value) > 0:
                return "positive integer"
            else:
                return "negative integer"
        except:
            if value.isdecimal:
                if float(value) > 0 and float(value).real:
                    return "positive real number"
                else:
                    return "negative real number" 
    
var = Isreal("10")
print(var)    
