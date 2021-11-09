# <strong>Shape Manipulation</strong>

## 배열의 모양 변경 
배열은 각 축을 따라 요소의 수로 지정된 모양을 갖습니다. 
```python
import numpy as np

a = np.floor(10 * rg.random((3, 4)))

print(a)
# array([[3., 7., 3., 4.],
#       [1., 4., 2., 2.],
#       [7., 2., 4., 9.]])
print(a.shape)
# (3, 4)
```

