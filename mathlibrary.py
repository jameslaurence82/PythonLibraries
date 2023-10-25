# import math
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
variance = np.var(a)
print("prints the variance of the array")
print(variance)

print()
print("using numpy library for square root of variance of array")
stdev = np.sqrt(variance)
print(stdev)

print("using std() from numpy to find standard deviation of array")
std = np.std(a)
print(std)

# using the axis function is the correct way
variance = np.var(a, axis = 1)
print("prints the variance of the array")
print(variance)

print()
print("using numpy library for square root of variance of array")
stdev = np.sqrt(variance)
print(stdev)

print("using std() from numpy library to find standard deviation of array")
std = np.std(a, axis = 1)
print(std)
