import numpy as np

a = np.array([2, 3, 4])
b = np.array((1.2, 3.5, 5.2))
c = np.array([(1.5, 2, 3), (4, 5, 6)])
d = np.array([[1, 2], [3, 4]], dtype=complex)

print(a)
print(a.dtype)

e = np.zeros((3, 4))
f = np.ones((2, 3, 4), dtype=np.int16)
g = np.empty((2, 3)) 

print(e)
print(f)
print(g)

h = np.arange(10, 30, 5)
i = np.arange(0, 2, 0.3)

from numpy import pi 

j = np.linspace(0, 2, 9)    # 9 numbers from 0 to 2 
k = np.linspace(0, 2 * pi, 100) 
l = np.sin(x)
