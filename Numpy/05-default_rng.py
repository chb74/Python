import numpy as np

rg = np.random.default_rng(1)   # create instance of default random number generator 
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))

a *= 3
print(a)

b += a
print(b)

c = np.ones(3, dtype=np.int32)
d = np.linspace(0, pi, 3)

e = c + d
print(c)

f = np.exp(e * 1j)
print(f)

g = rg.random((2, 3))
print(g)
print(g.sum())
print(g.min())
print(g.max())
