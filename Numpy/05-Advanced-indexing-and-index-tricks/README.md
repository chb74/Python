# <strong> Advanced indexing and index tricks</strong>
Numpy는 일반 파이썬 시퀀스보다 더 많은 인덱싱 기능을 제공합니다. 정수 및 슬라이스로 인덱싱하는 것 외에도 이전에 보았듯이 배열은 정수 배열 및 부울 배열로 인덱싱할 수 있다. 

## <strong> Indexing with Arrays of Indices </strong>

```python 
import numpy as np

a = np.arange(12)**2 			# the first 12 square numbers 
i = np.array(1, 1, 3, 8, 5]) 	# an array of indices 
print(a[i])						# the elements of `a` at the positions `i`
# array([ 1,  1,  9, 64, 25])
j = np.array([[3, 4], [9, 7]])	# a bidimensional array of indices 
print(a[j])						# the same shape as `j`
# array([[ 9, 16],
#       [81, 49]])
```
