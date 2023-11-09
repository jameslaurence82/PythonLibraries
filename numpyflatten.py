# ndarray.flatten(order='C')
# The order parameter specifies the order of elements of an array 
# in the returned array. It accepts one of the following values:

# ‘C’ means to flatten array elements into row-major order (C-style).
# ‘F’ means to flatten array elements into column-major order (Fortran-style).
# ‘A’ – means to flatten array elements in column-major order if a is Fortran contiguous in memory or row-major otherwise.
# ‘K’ means to flatten array elements in order of the elements laid out in memory.
# By default, the order is ‘C’ which flattens the array elements into row-major

import numpy as np

# flatten() method to return a 1-D array from a 2-D array:
a = np.array([[1, 2], [3, 4]])
b = a.flatten()
print(b)

# b is a copy, not a view of the array a. If you change elements in array b, 
# the elements in array a are not changed.
a = np.array([[1, 2], [3, 4]])
b = a.flatten()

# change element at index 0
b[0] = 0
print(b)

# display the array a
print(a)
print()

# Using numpy flatten() method to flatten an array using column-major order
a = np.array([[1, 2], [3, 4]])
b = a.flatten(order='F')

print(b)
print()