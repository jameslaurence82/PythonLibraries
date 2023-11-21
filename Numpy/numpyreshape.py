import numpy as np

# reshape() function to change a 1-D array with 4 elements to a 2-D array:
a = np.arange(1, 5)
print(a)

b = np.reshape(a, (2, 2))
print(b)

"""
a = np.arange(1, 5)
print(a)
b = np.reshape(a, (2, 3)) # this gives a value error. not enough elements
print(b)
# ValueError: cannot reshape array of size 4 into shape (2,3)
"""
print()
# Numpy reshape() returns a view
a = np.arange(1, 5)
b = np.reshape(a, (2, 2))

# change the element [0,0]
b[0, 0] = 0

print(b)
print(a)