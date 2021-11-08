
from numpy import newaxis 
import numpy as np


rg = np.random.default_rng(1)
a = np.floor(10 * rg.random((2, 2)))
b = np.floor(10 * rg.random((2, 2)))

c = np.column_stack((a, b))

print("column stack a and b")
print(c)

a = np.array([4., 2.])
b = np.array([3., 8.])
c = np.column_stack((a, b)) # returns a 2D array 
print("new column stack")
print(c)
d = np.hstack((a, b))
print("hstack a and b")
print(d)

print("view `a` as a 2D column vector")
print(a[:, newaxis]) 
print("column_stack")
print(np.column_stack((a[:, newaxis], b[:, newaxis])))

print("hstack")
print(np.hstack((a[:, newaxis], b[:, newaxis])))

print("np.column_stack is np.hstack")
print(np.column_stack is np.hstack)

print("np.row_stack is np.vstack")
print(np.row_stack is np.vstack)
