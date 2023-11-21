import numpy as np

# sort() function to sort numbers in a 1-D array:
a = np.array([2, 3, 1])
b = np.sort(a)
print(b)

print()
# sort() function to sort an array from low to high and use a slice
a = np.array([2, 3, 1])
b = np.sort(a)[::-1]
print(b)

print()
# sort() function to sort a 2-D array:
a = np.array([
    [2, 3, 1],
    [5, 6, 4]
])

b = np.sort(a)
print(b)
print()

# sort() function to sort elements on axis 0:
a = np.array([
    [5, 3, 4],
    [2, 6, 1]
])

b = np.sort(a, axis=0)
print(b)
print()

#  sort elements of the array on axis 1:
a = np.array([
    [5, 3, 4],
    [2, 6, 1]
])

b = np.sort(a, axis=1)
print(b)
print()

# sort() function to sort a structured array example
dtype = [('name', 'S10'),
        ('year_of_services', float),
        ('salary', float)]

employees = [
    ('Alice', 1.5, 12500),
    ('Bob', 1, 15500),
    ('Jane', 1, 11000)
]

payroll = np.array(employees, dtype=dtype)

result = np.sort(
    payroll,
    order=['year_of_services', 'salary']
)

print(result)
print("the b is because of the S10 in dataype)")

# ort() function to sort a structured array example
dtype = [('name', 'U10'),
        ('year_of_services', float),
        ('salary', float)]

employees = [
    ('Alice', 1.5, 12500),
    ('Bob', 1, 15500),
    ('Jane', 1, 11000)
]

payroll = np.array(employees, dtype=dtype)

result = np.sort(
    payroll,
    order=['year_of_services', 'salary']
)
print()
print(result)
print("the b is gone because of the U10 in dataype)")

print("changing the sort order to be by name")
dtype = [('name', 'U10'),
        ('year_of_services', float),
        ('salary', float)]

employees = [
    ('Alice', 1.5, 12500),
    ('Bob', 2, 15500),
    ('Bob', 1, 15500),
    ('Jane', 1, 11000)
]

payroll = np.array(employees, dtype=dtype)

result = np.sort(
    payroll,
    order=['name', 'year_of_services', 'salary']
)
print("sorts by by criteria, if identical, then second criteria is sorted")
print(result)
print("the b is gone because of the U10 in dataype)")