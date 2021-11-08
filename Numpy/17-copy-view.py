import numpy as np

a = np.array([[0, 1, 2, 3], 
                [4, 5, 6, 7],
                [8, 9, 10, 11]])


def f(x):
    print(id(x))


b = a           # no new object is created 
print(b is a)   # a and b are two names for the same ndarray object 

print(f(a))
print(f(b))

