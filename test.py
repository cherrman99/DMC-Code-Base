#this is to test if numpy works
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print (arr)

#this is some basic math
print (2+2)
print (4*8)

#find area of circle with given radius
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str (r) + " is: " + str(pi * r**2))

#finding max and min numbers of sequence
def max_min(data):
    l = data[0]
    s = data[0]
    for num in data:
        if num> l:
            l = num
        elif num< s:
            S = num
    return l, S

print(max_min([0, 20, 30, -20, 50, 2000]))