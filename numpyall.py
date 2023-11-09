import numpy as np


# The following example uses the all() 
# function to test whether all numbers in an array are non-zero:
result = np.all([0, 1, 2, 3])
print(result)

# The result is False because the array has zero at index 0.
result = np.all(np.array([-1, 2, 3]))
print(result)

# The following example uses the all() function to test if 
# all elements of a multidimensional array evaluate to True:
a = np.array([[0, 1], [2, 3]])
result = np.all(a, axis=0)
print(result)


# Also, you can evaluate elements along an axis by passing
# the axis argument like this:
a = np.array([
    [0, 1],
    [2, 3]]
)
result = np.all(a, axis=0)
print(result)

# And axis-1:
a = np.array([
    [0, 1],
    [2, 3]
])
result = np.all(a, axis=1)
print(result)