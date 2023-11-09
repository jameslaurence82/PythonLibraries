import numpy as np

# The + or add() function of two equal-sized arrays perform element-wise additions
#  uses the + operator to add two 1-D arrays:

a = np.array([1, 2])
b = np.array([2, 3])

c = a + b
print(c)
print()

#NumPy add() function and + operator to add two 2D arrays example
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = a + b
print(c)

# Numpy subtract() function
# uses the - operator to find the difference between two 1-D arrays:
a = np.array([1, 2])
b = np.array([3, 4])

c = b - a
print(c)
print()
#  subtract() function to find the difference between two 1D arrays like this:
a = np.array([1, 2])
b = np.array([3, 4])

c = np.subtract(b, a)

print(c)
print()
# subtract() function to find the difference between two 2D arrays:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.subtract(b, a)
print(c)
print()

#  uses the * operator to get the products of two 1-D arrays:
a = np.array([1, 2])
b = np.array([3, 4])

c = a*b
print(c)

# multiply() function to get the product between two 1D arrays as follows:
a = np.array([1, 2])
b = np.array([3, 4])

c = np.multiply(a, b)
print(c)
print()
# uses the * operator to get the products of two 2D arrays:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = a*b
print(c)
print()

# uses the / operator to find the quotient of two 1-D arrays:
a = np.array([8, 6])
b = np.array([2, 3])

c = a/b
print(c)
print()

# divide() function to get the quotient of two 1D arrays as follows:
a = np.array([8, 6])
b = np.array([2, 3])

c = np.divide(a, b)
print(c)
print()
# uses the / operator to find the quotient of two 2D arrays:
a = np.array([[10, 8], [6, 4]])
b = np.array([[5, 2], [2, 1]])

c = a/b
print(c)
print()