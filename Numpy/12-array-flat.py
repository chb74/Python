
import numpy as np

a = np.arange(20).reshape(5, 4)


for element in a.flat:
    print(element)
