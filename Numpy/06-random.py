import numpy as np 

rg = np.random.default_rng(1)
a = rg.random((2, 3))

print(a) 
print(a.sum())
print(a.min())
print(a.max())
