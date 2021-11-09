# <strong> 기본의 이해 </strong>
Numpy의 주요 객체는 동종 다차원 배열이다. 이것은 음이 아닌 정수의 튜플에 의해 인덱싱된 모두 같은 유형의 요소(보통은 숫자이다.) 의 테이블이다. Numpy에서는 차원을 축이라고 한다. 

예를들어, 3D공간 [1, 2, 1]에서 점의 좌표는 하나의 축을 가진다. 이축에는 3개의 요소가 있으므로 길이가 3이라고 한다. 아래 그림의 예에서 배열에는 2개의 축이 있다. 첫번째 축의 길이는 2이고 두 번째 축의 길이는 3이다. 

```python
[[1., 0., 0.], 
 [0., 1., 2.]]
```
Numpy의 배열 클래스는 ndarray라고 한다. 별치 배열로도 알려져 있다. numpy.array는 1차원 배열만 처리하고 더 적은 기능을 제공하는 표준 Python 라이브러리 클래스 array.array와 동일하지 않다. ndarray객체의 더 중요한 속성은 다음과 같다. 

* ndarray.ndim
배열의 축(차원) 수 

* ndarray.shape 
배열의 차원. 이것은 각 차원에서 배열의 크기를 나타내는 정수의 튜플이다. n개의 행과 m개의 열이 있는 행렬의 경우 모양은 (n, m)이다. 따라서 모양 튜플의 길이는 축의 수 ndim이다. 

* ndarray.size 
배열의 총 요수 수이다. 이것은 모양 요소의 곱과 같다. (2, 3) => 6 

* ndarray.dtype 
배열의 요수 유형을 설명하는 개체이다. 표준 POython 유형을 사용하여 dtype을 만들거나 지정할 수 있다. 또한 Numpy는 자체 유형을 제공한다. numpy.int32, numpy.int16 및 nupy.float64 

* ndarray.itemsize 
배열의 각 요소의 크기 (바이트)이다. 예를 들어 float64유형의 요소 배열의 항목 크기는 8(=64/8)인 반면 complex32 유형 중 하나는 항목 크기가 4(32/8)이다. ndarray.dtype.itemsize와 동일하다. 

* ndarray.data 
배열의 실제 요소를 포함하는 버퍼. 일반적으로 인덱싱 기능을 사용하여 배열의 요소에 액세스하기 때문에 이 속성을 사용할 필요가 없다. 

### <strong> 예제</strong>
```python
import numpy as np
a = np.arange(15).reshape(3, 5)

print(a)
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]]
 
print(a.shape) 
# (3, 5) 

print(a.ndim)
# 2 -- 2 Dimension 

print(a.dtype.name)
# int64 

print(a.itemsize)
# 8 

print(a.size)
# 15 

print(type(a))
# <class 'numpy.ndarray'>

b = np.array([6, 7, 8])
print(b) 
# array([6, 7, 8])

print(type(b))
# <class 'numpy.ndarray'> 

```

### <strong> 배열 생성</strong>
배열을 만드는 방법에는 여러 가지가 있다. 

예를들어, 배열 함수를 사용하여 일반 Python list 또는 튜플에서 배열을 만들 수 있다. 결과 배열의 유형은 시퀀스의 요소 유형에서 추론된다. 
```python
import numpy as np
a = np.array([2, 3, 4])
print(a)
# array([2, 3, 4]) - just print [2, 3, 4]

print(a.dtype)
# dtype('int64')

b = np.array([1.2, 3.5, 5.2])
print(b.dtype)
# float64 
```
시퀀스 오류는 단일 시퀀스를 인수로 제공하는 대신 여러 인수로 배열을 호출하는 것으로 구성된다. 아래 코드를 보라 
```python
import numpy as np 
a = np.array(1, 2, 3, 4) # -- WRONG 
Trackback (most recent call last):
	...
TypeError: array() takes from 1 to 2 positional arguments but 4 were given
a = np.array([1, 2, 3, 4]) # -- RIGHT !!!
```
배열은 시퀀스의 시퀀스를 2차원 배열로, 시퀀스의 시퀀스의 시퀀스는 3차원 배열로 변환한다. 
```python 
import numpy as np 

b = np.array([(1.5, 2, 3), (4, 5, 6)]) 
print(b)
# array([[1.5, 2. , 3. ],
#       [4. , 5. , 6. ]])
```
배열의 유형은 생성시 명시적으로 지정할 수도 있습니다. 

```python 
import numpy as np 

c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c) 
# array([[1.+0.j, 2.+0.j],
#       [3.+0.j, 4.+0.j]])
```
배열의 요소는 원래 알려지지 않았지만 크기는 알려져 있다. 따라서 Numpy는 초기 자리 표시자 콘텐츠로 배열을 생성하는 여러기능을 제공한다. 이는 배열을 확장해야 하는 필요성과 값비싼 작업을 최소화 한다. 
함수 zeros는 0으로 가득 찬 배열을 만들고, 함수 ones는 1로 가득찬 배열을 만들고, empty 함수는 초기 내용이 무작위이고 메모리 상태에 따라 달라지는 배열을 만든다. 기본적으로 생성된 배열의 dtype는 float64이지만 키워드 인수 dtype을 통해 지정할 수 있다. 

```python 
import numpy as np 

a = np.zeros((3, 4)) 
print(a)
# array([[0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.]])

b = np.ones((2, 3, 4), dtype=np.int16)
# array([[[1, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1]],

#       [[1, 1, 1, 1],
#       [1, 1, 1, 1],
#        [1, 1, 1, 1]]], dtype=int16)
c = np.empty((2, 3))
# array([[3.73603959e-262, 6.02658058e-154, 6.55490914e-260],  # may vary
       [5.30498948e-313, 3.14673309e-307, 1.00000000e+000]])
```
숫자 시퀀스를 생성하기 위해서 numpy는 파이썬 내장 범위와 유사 하지만 배열을 반환하는 arange 함수를 제공한다. 
```python 
import numpy as np

a = np.arange(10, 30, 5)
print(a) 
# array([10, 15, 20, 25])
b = np.arange(0, 2, 0.3)	# it accepts float arguments 
print(b) 
# array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])

```
범위가 부동소수점 인수와 함께 사용되는 경우 유한 부동 소수점 정밀도로 인해 일반적으로 획득한 요소 수를 예측할 수 없다. 이러한 이유로 일반적으로 단계 대신 원하는 요소 수를 인수로 받는 `linspace` 함수를 사용하는 것도 좋다. 

```python
from numpy import pi 
a = np.linspace(0, 2, 9)		# 9 numbers from 0 to 2 
print(a) 
# array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])
x = np.linspace(0, 2 * pi, 100)	# useful to evaluate function at lots of points 
f = np.sin(x) 

```
> 다음과 같은 함수를 찾아보면 좋다. 
>> array, zeros, zeros_like, ones, ones_like, empty, empty_like, arange, linspace, numpy.random.Generator.rand, numpy.random.Generator.randn, fromfunction, fromfile
