import numpy as np
# The following example uses the any() function to test whether
# any number in an array are non-zero:
result = np.any([0, 1, 2, 3])
print(result)

#The result is True because the array of three non-zero numbers.
result = np.any(np.array([0, 0]))
print(result)

# he any() function to test if any elements of a multidimensional 
# array evaluate to True:
a = np.array([[0, 1], [2, 3]])
result = np.any(a)
print(result)

# And axis-1:
a = np.array([
    [0, 0],
    [0, 1]
])
result = np.any(a, axis=1)
print(result)