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
배열의 모양은 다양한 명령으로 변경할 수 있다. 다음 세가지 명령은 모두 수정된 배열을 반환하지만 원래 배열은 변경하지 않는다. 
```python 
import numpy as np

rg = np.random.default_rng(1)		# 기본 난수 생성기의 인스턴스 생성 
a = np.floor(10 * rg.random((3, 4)))

print(a.ravel())		# returns the array, flattened
# array([3., 7., 3., 4., 1., 4., 2., 2., 7., 2., 4., 9.])
print(a.reshape(6, 2))	# returns the array with a modified shape
# array([[3., 7.],
#       [3., 4.],
#       [1., 4.],
#       [2., 2.],
#       [7., 2.],
#       [4., 9.]])
print(a.T)				# returns the array, transposed 
# array([[3., 1., 7.],
#       [7., 4., 2.],
#       [3., 2., 4.],
#       [4., 2., 9.]])
print(a.T.shape)
# (4, 3)
print(a.shape)
# (3, 4)
```
ravel에서 생성된 배열의 요소 순서는 일반적으로 "C 스타일" 이다. 즉, 가장 오른쪽 인덱스가 "가장 빠르게 변경" 되므로 a[0, 0]뒤의 요소는 a[0, 1]이다. 배열이 다른 모양으로 변형되면 배열은 다시 "C 스타일"로 처리된다. numpy는 일반적으로 이 순서로 저장된 배열을 생성하므로 ravel은 일반적으로 인수를 복사할 필요가 없지만 배열이 다른 배열의 조각을 가져오거나 비정상적인 옵션으로 생성된 경우 복사해야 할 수도 있다. ravel 및 reshape 함수는 선택적 인수를 사용하여 가장 왼쪽 인덱스가 가장 빠르게 변경되는 FORTRAN 스타일 배열을 사용하도록 지시할 수도 있다. reshape함수는 수정된 모양으로 인수를 반환하는 반면 ndarray.resize 메소드는 배열 자체를 수정한다. 
```python 
print(a) 
# array([[3., 7., 3., 4.],
#       [1., 4., 2., 2.],
#       [7., 2., 4., 9.]])
a.resize((2, 6))
print(a)
# array([[3., 7., 3., 4., 1., 4.],
#       [2., 2., 7., 2., 4., 9.]])
```
크기 조정 작업에서 차원이 -1로 지정되면 다른 차원이 자동으로 계산됩니다. 
```python
print(a.reshape(3, -1))
# array([[3., 7., 3., 4.],
#       [1., 4., 2., 2.],
#       [7., 2., 4., 9.]])
```
> <strong> 더 많은 참조</strong>
>> [ndarray.shape](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape), [reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape), [resize](https://numpy.org/doc/stable/reference/generated/numpy.resize.html#numpy.resize), [ravel](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel)

## <strong> 서로다른 배열 합치기 </strong>
여러 배열을 서로 다른 축을 따라 함께 쌓을 수 있다. 
```python 
import numpy as np 

rg = np.random.default_rng(1)		# 기본 난수 생성기의 인스턴스 생성 
a = np.floor(10 * rg.random((2, 2)))
print(a) 
# array([[9., 7.],
#       [5., 2.]]) 
b = np.floor(10 * rg.random((2, 2)))
print(b)
# array([[1., 9.],
#       [5., 1.]])
np.vstack((a, b))
# array([[9., 7.],
#       [5., 2.],
#       [1., 9.],
#       [5., 1.]])
np.hstack((a, b))
# array([[9., 7., 1., 9.],
#       [5., 2., 5., 1.]])
```
column_stack 함수는 1D 배열을 2D 배열에 열로 쌓습니다. 2D 배열의 경우에만 hstack과 동일하다. 
```python
from numpy import newaxis 
import numpy as np 
print(np.column_stack((a, b)))		# with 2d arrays 
# array([[9., 7., 1., 9.],
#       [5., 2., 5., 1.]])
a = np.array([4., 2.])
b = np.array([3., 8.])
print(np.column_stack((a, b)))		# returns a 2d array
# array([[4., 3.],
#       [2., 8.]])
np.hstack((a, b))					# the result is different 
# array([4., 2., 3., 8.])
print(a[:, newaxis])				# view `a` as a 2d column vector 
# array([[4.],
#       [2.]])
print(np.column_stack((a[:, newaxis], b[:, newaxis])))
# array([[4., 3.],
#       [2., 8.]])
print(np.hstack((a[:, newaxis], b[:, newaxis])))	# the result is the same 
# array([[4., 3.],
#        [2., 8.]])
```
row_stack 함수는 모든 입력 배열에 대한 vstack과 동일하다. 실제로 row_stack은 vstack의 별칭이다. 
```python 
print(np.column_stack is np.hstack)
# False 
print(np.row_stack is np.vstack)
# True 
```
일반적으로 2차원 이상의 배열의 경우 hstack은 두 번째 축을 따라 스택하고 vstack은 첫번째 축을 따라 스택하며 연결은 연결이 발생해야 하는 축의 번호를 제공하는 선택적 인수를 허용한다.

메모 
복잡한 경우 r_ 및 c_는 한 축을 따라 숫자를 쌓아 배열을 만드는 데 유용하다. 범위 리터럴을 사용할 수 있다. 
```python 
np.r_[1:4, 0, 4]
# array([1, 2, 3, 4])
```
배열을 인수로 사용하는 경우 r_ 및 c_는 기본 동작에서 vstack 및 hstack과 유사하지만 연결할 축의 번호를 제공하는 선택적 인수를 허용한다. 
> <string>더 많은 부분 참조 </strong>
>> [hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack), [vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack), [column_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack), [concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate), [c_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_), [r_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_) 


## <strong>하나의 배열을 여러 개의 작은 배열로 분할 </strong>
hsplit을 사용하면 반환할 동일한 모양의 배열 수를 지정하거나 분할이 발생해야 하는 열을 지정하여 수평 축을 따라 배열을 분할할 수 있다. 
```python
import numpy as np

rg = np.random.default_rng(1)		# 기본 난수 생성기의 인스턴스 생성 
a = np.floor(10 * rg.random((2, 12)))
print(a) 
# array([[6., 7., 6., 9., 0., 5., 4., 0., 6., 8., 5., 2.],
       [8., 5., 5., 7., 1., 8., 6., 7., 1., 8., 1., 0.]])
print(np.hsplit(a, 3))
# [array([[6., 7., 6., 9.],
#       [8., 5., 5., 7.]]), array([[0., 5., 4., 0.],
#       [1., 8., 6., 7.]]), array([[6., 8., 5., 2.],
#       [1., 8., 1., 0.]])]
print(np.hsplit(a, (3, 4)))
# [array([[6., 7., 6.],
#       [8., 5., 5.]]), array([[9.],
#       [7.]]), array([[0., 5., 4., 0., 6., 8., 5., 2.],
#       [1., 8., 6., 7., 1., 8., 1., 0.]])]
```
vsplit은 세로 축을 따라 분할하고 array_split을 사용하면 분할할 축을 지정할 수 있다. 
