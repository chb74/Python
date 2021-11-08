
import numpy as np
 
rg = np.random.default_rng(1)

a = np.floor(10 * rg.random((2, 2)))

print("A")
print(a)

b = np.floor(10 * rg.random((2, 2)))
print("B")
print(b)

c = np.vstack((a, b))
print("vstack a and b")
print(c)

d = np.hstack((a, b))
print("hstack a and b")
print(d)
