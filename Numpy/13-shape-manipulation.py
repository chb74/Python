
import numpy as np

rg = np.random.default_rng(1)

a = np.floor(10 * rg.random((3, 4)))
print(a)
print(a.shape)

print("Flatted")
print(a.ravel())    # returns the array, flattened

print("Transposed")
print(a.T)          # returns the aray, transposed 
print(a.T.shape)


print("Resized")
a.resize((2, 6))
print(a)
print(a.shape)

print("Reshape")
a.reshape((3, -1))
print(a)
