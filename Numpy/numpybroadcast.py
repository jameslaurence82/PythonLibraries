# broadcasting is a set of rules for applying arithmetic 
# operations on arrays of DIFFERENT SHAPES

import numpy as np

# you can use the + operator to add a number to an array
a = np.array([1, 2, 3])
b = a + 1 # sets the same arraty shape
c = a + [1,1,1]
print(b)
print(c)
print()

# you can add a 1D array to a 2D array using broadcasting like this:
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.array([10, 20, 30])
c = a + b
print(c)
print()

"""
##############NumPy broadcasting rules###############
NumPy defines a set of rules for broadcasting:

Rule 1: if two arrays have different dimensions, it pads ones on the left side of the shape of the array that has fewer dimensions.
Rule 2: if two dimensions of arrays do not match in any dimension, the array with a shape equal to one in that dimension is stretched (or broadcast) to match the shape of another array.
Rule 3: if any dimension of two arrays is not equal and neither is equal to one, NumPy raises an error.
"""

# example adds a 2-D array to a 1D array:
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.ones(3)
print(b)
c = a + b
print(c)
print()

#ample illustrates the case where NumPy broadcasts both arrays:
a = np.array([
    [1],
    [2],
    [3],
])
print(f"a shape: ", a.shape)

b = np.array([1, 2, 3])
print(f"b shape: ", b.shape)

c = a + b
print(c)
print(f"c shape: ", c.shape)
print()

# Example adds two arrays that are not compatible:
# a = np.array([
#     [1, 2],
#     [3, 4],
#     [5, 6],
# ])
# print(f"a shape: ", a.shape)

# b = np.array([1, 2, 3])
# print(f"b shape: ", b.shape)

# c = a + b
# ValueError: operands could not be broadcast together with shapes (3,2) (3,)



