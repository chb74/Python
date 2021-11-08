import numpy as np

# universal function - ufunc -> sin, cos, exp 

a = np.arange(3) # [0, 1, 2]

b = np.exp(a)
print(b)        # array([1.        , 2.71828183, 7.3890561 ])
print(np.sqrt(b))   # array([0.        , 1.        , 1.41421356])

c = np.array([2., -1., 4.])
print(np.add(c, a)) # array([2., 0., 6.])
