import numpy as np

# Create numpy array
tc = np.array([25.5, 28.1, 30.6])
# To convert these temperatures from celsius to Kelvin, you use the following:
tk =  tc * 9 / 5 + 32
print(tk)

#  the calculation is much simpler than the following Python code:
tk1 = [c*9/5 + 32 for c in tc]
print(tk1)

# One Dimensional Array
a = np.array([1, 2, 3])
print(type(a)) # Print Data Type of array <- class 'numpy.ndarray'
print("One Dimenional")
print(a) # prints array values
print(a.ndim) # get the number of dimensions of ndarray
print(a.dtype) # get the datatype ndarray


b = np.array([1, 2, 3], dtype=np.float64)

print(b)
print(a.dtype)

# Two dimensional Array

c = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)
print("Two Dimenional")
print(c)
print(c.ndim) # get the number of dimensions of ndarray

# Three dimensional Array

d = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ],
    ]
)
print("Three Dimenional")
print(d)
print(d.ndim) # get the number of dimensions of ndarray

print("Getting Shape of Array")
print("Shape property returns a tuple")
print(a.shape)
print(b.shape)
print(c.shape)
print(d.shape)

# NumPy zeros()
print()
print("NumPy zeros()")
# create a numpy array of a given shape whose elements are filled with zeros

e = np.zeros((2, 3))
print(e)
print(e.dtype)

# NumPy Ones()
print("NumPy Ones()")
f = np.ones((2, 3, 2))
print(f)
print(f.dtype)

print()
# NumPy arange()
# numpy.arange(start, stop, step, dtype=None, *, like=None) <- formatting
print("NumPy arange()")
g = np.arange(1, 10, 2) # integers used so datatype will be int32

print(g)
print(g.dtype)

h = np.arange(1.0, 10.0, 2) # float used so datatype will be float63

print(h)
print(h.dtype)

print()
# numpy linspace()
print("NumPy linspace()")
j = np.linspace(1, 2, 5)
print("NumPy linspace() endpoint = True as default")
print(j)

k = np.linspace(1, 2, 5, endpoint=False)
print("NumPy linspace() endpoint = False as default")
print(k)

print()
# NumPy Array Indexing
print("NumPy Array Indexing")
l = np.arange(0, 5)
print(l)
print("Prints specific index numbers")
print(l[0]) # prints index 0
print(l[1]) # prints index 1
print(l[-1]) # prints last index
print(l[-2]) # prints second last index

print()
# NumPy array indexing on 2-D arrays
print("NumPy array indexing on 2-D arrays")
a1 = np.array([
    [1, 2, 3], # this is index 0
    [4, 5, 6] # this is index 1
])

print(a1.shape)

print(a1[0])  # [1 2 3]
print(a1[1])  # [4 5 6]

print(a1[0, 0])  # 1
print(a1[1, 0])  # 4
print(a1[0, 2])  # 3
print(a1[1, 2])  # 6
print(a1[0, -1])  # 3
print(a1[1, -1])  # 6

print()
# NumPy array indexing on 3-D arrays\
print("NumPy array indexing on 3-D arrays")

b1 = np.array([
    [[1, 2], [3, 4], [5, 6]],
    [[5, 6], [7, 8], [9, 10]],
])

print(b1.shape)
a = np.array([
    [[1, 2], [3, 4], [5, 6]],
    [[5, 6], [7, 8], [9, 10]],
])

print(a[0, 0, 1]) 

print()
# Numpy Array Slicing
print("Numpy Array Slicing")
# Numpy array slicing on one-dimensional arrays [m:n]
# [m:n:1]
# select every two elements, you can use the following slice: [m:n:2]

# Slicing Expression	    Meaning
# a[m:n]	                Select elements with an index starting at m and ending at n-1.
# a[:] or a[0:-1]	        Select all elements in a given axis
# a[:n]	                    Select elements starting with index 0 and up to element with index n-1
# a[m:]	                    Select elements starting with index m and up to the last element
# a[m:-1]	                Select elements starting with index m and up to the last element
# a[m:n:k]              	Select elements with index m through n (exclusive), with an increment k
# a[::-1]	                Select all elements in reverse order

print()
a2 = np.arange(0, 10)

print("Output")
print('a2=', a2)
print('a2[2:5]=', a2[2:5])
print('a2[:]=', a2[:])
print('a2[0:-1]=', a2[0:-1])
print('a2[0:6]=', a2[0:6])
print('a2[7:]=', a2[7:])
print('a2[5:-1]=', a2[5:-1])
print('a2[0:5:2]=', a2[0:5:2])
print('a2[::-1]=', a2[::-1])


a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Numpy array slicing on multidimensional arrays
prinbt("Numpy array slicing on multidimensional arrays")
print(a[0:2, :])

b2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(b2[1:, 1:])