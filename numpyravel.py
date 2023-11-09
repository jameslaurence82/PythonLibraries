# The ravel() function accepts an array and returns a 1-D array 
# containing the elements of the input array:

# numpy.ravel(a, order='C')

import numpy as np

#uses the ravel() function to flatten a 2-D array:
a = np.array([[1, 2], [3, 4]])
b = np.ravel(a)

print(b)
print()

# ravel() function vs. flatten() method
# flatten() method creates a copy of an input array 
# while the ravel() function creates a view of the array
a = np.array([[1, 2], [3, 4]])
b = np.ravel(a)

# change element at index 0
b[0] = 0

# show both b & a array
print(b)
print(a)
print()

