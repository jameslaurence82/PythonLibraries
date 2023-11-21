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

a = np.arange(1, 5)
result = np.prod(a)

print(a)
print(f'result={result}')

result = np.prod([
    [1, 2],
    [3, 4]
],axis = 1)
print("axis 1")
print(f'result={result}')

result = np.prod([
    [1, 2],
    [3, 4]
],axis = 0)
print("axis 0")
print(f'result={result}')

# Selecting numbers to include in the product
# nan avoids not a number elements
a = np.array([np.nan, 3, 4])
result = np.prod(a, where=[False, True, True])
print(result)

result = np.prod(np.arange(1,34))
print(result)

"""
Minimum and Maximum
"""
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(f"arry a is:\n {a}")
min = np.amin(a)
print(min)
max = np.amax(a)
print(max)