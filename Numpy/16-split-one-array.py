
import numpy as np

rg = np.random.default_rng(1)

a = np.floor(10 * rg.random((2, 12)))

print("a vector")
print(a)

Stacking together different arrays
print(np.hsplit(a, 3))
