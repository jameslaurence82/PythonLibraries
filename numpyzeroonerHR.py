"""
https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true
You are given the shape of the array in the form of space-separated integers, 
each integer representing the size of different dimensions, your task is to 
print an array of the given shape and integer type using the tools numpy.zeros 
and numpy.ones.
Input Format
A single line containing the space-separated integers.
Constraints
1 <= each integer <= 3
"""

# pseudo code
# user input of array shape as integer
# shape input function to create zero 
# shape input function to create one

import numpy as np

def zeros(arr):
    arr1 = np.zeros(arr)
    print(arr1)
    # return arr1

def ones(arr):
    arr2 = np.ones(arr)
    print(arr2)
    # return arr2

arr = input().strip().split(' ')
new_arr = np.array(arr, dtype = int)
print(new_arr)
print(type(new_arr))

print(zeros(new_arr), ones(new_arr))

