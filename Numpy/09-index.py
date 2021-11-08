import numpy as np

a = np.arange(10)**3    # array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])

print(a[2])    # 8
print(a[2:5])   # array([ 8, 27, 64])
print(a[:6:2] = 1000
print(a)    # array([1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729])
print(a[::-1])  # reversed a : array([ 729,  512,  343,  216,  125, 1000,   27, 1000,    1, 1000])

for i in a:
    print(i**(1 / 3.))


