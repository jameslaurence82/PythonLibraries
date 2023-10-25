import numpy

# https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true
# You are given two integer arrays,  and  of dimensions X.
# Your task is to perform the following operations:
# Add (a + b)
# Subtract (a - b)
# Multiply (a * b)
# Integer Division (a / b) <<-- floor_divide
# Mod (a % b)
# Power (a ** b)
# m is the 

# creation of two 1 dimensional arrays
n,m = input().strip().split()
a = numpy.array(input().strip().split(" "))
b = numpy.array(input().strip().split(" "))
    


# processing arrays
print(numpy.add(a,b, axis = 0)) # adding arrays
print(numpy.subtract(a,b)) # subtracting arrays
print(numpy.multiply(a,b)) # multiplying arrays
print(numpy.floor_divide(a,b)) # floor division of arrays
print(numpy.mod(a,b)) # modulus division of arrays
print(numpy.power(a,b)) # power to arrays