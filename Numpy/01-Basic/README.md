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

## <strong> 예제</strong>
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

## <strong> 배열 생성</strong>
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
> <strong>다음과 같은 함수를 찾아보면 좋다. </strong>
>> [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array), [zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros), [zeros_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like), [ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones), [ones_like](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like), [empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty), [empty_like](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#numpy.empty_like), [arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange), [linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace), numpy.random.Generator.rand, numpy.random.Generator.randn, [fromfunction](https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html#numpy.fromfunction), [fromfile](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile)

## <strong>배열 출력하기</strong>
배열을 인쇄할 때 nupy는 중첩목록과 유사한 방식으로 배열을 표시하지만 레이아웃은 다음과 같다. 
* 마지막 축은 왼쪽에서 오른쪽으로 인쇄되고, 
* 마지막에서 두 번째는 위에서 아래로 인쇄되고, 
* 나머지 부분도 위에서 아래로 인쇄되며 각 슬라이스는 빈 줄로 다음 슬라이스와 구분된다. 


그런 다음 1차원 배열은 행으로, 2차원 행렬과 3차원 행렬 list 로 인쇄된다. 
```python 
import numpy as np 

a = np.arange(6)					# 1D array 
print(a)
# [0 1 2 3 4 5]

b = np.arange(12).reshape(4, 3)		# 2D array
print(b)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

c = np.arange(24).reshape(2, 3, 4)	# 3D array 
print(c)
#	[[[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
#
# [[12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]]

```
reshape에 대한 자세한 내용은 아래의 내용을 참조한다. 
배열이 너무 커서 인쇄할 수 없는 경우 numpy는 자동으로 배열의 중앙 부분을 건너뛰고 모서리만 인쇄한다. 
```python
import numpy as np

print(np.arange(10000))
# [   0    1    2 ... 9997 9998 9999]
print(np.arange(10000).reshape(100, 100))
#[[   0    1    2 ...   97   98   99]
# [ 100  101  102 ...  197  198  199]
# [ 200  201  202 ...  297  298  299]
# ...
# [9700 9701 9702 ... 9797 9798 9799]
# [9800 9801 9802 ... 9897 9898 9899]
# [9900 9901 9902 ... 9997 9998 9999]]

```
이 동작을 비활성화하고 numpy가 전체 배열을 인쇄하도록 하려면 `set_printoptions`를 사용하여 인쇄 옵션을 변경 할 수 있다. 
```python
import numpy as np 

np.set_printoptions(threshold=sys.maxsize)
# sys module should be imported 
```


## <strong> Basic Operations </strong>
배열의 산술 연산자는 요소별로 적용된다. 새 배열이 생성되고 결과로 채워진다. 
```python
import numpy as np
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(b) 
# array([0, 1, 2, 3])
c = a - b 
print(c)
# array([20, 29, 38, 47])
print(b**2)
# array([0, 1, 4, 9])
print(10 * np.sin(a))
# array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
print(a < 35)
# array([ True,  True, False, False])
```
많은 행렬 언어와 달리 곱 연산자 *는 numpy 배열에서 요소별로 작동한다. 행렬 곱은 @연산자(python >= 3.5) 또는 점 함수 또는 메서드를 사용하여 수행할 수 있다. 

```python 
import numpy as np 

a = np.array([[1, 1],
				[0, 1]])
b = np.array([[2, 0], 
				[3, 4]])
print(a * b)	# elementwise product 
# array([[2, 0],
#       [0, 4]])
print(a @ b) 	# matrix product 
# array([[5, 4],
#       [3, 4]])
print(a.dot(b))	# another matrix product 
# array([[5, 4],
#       [3, 4]])
```
+= 및 *= 와 같은 일부 작업은 새 배열을 생성하는 대신 기존 배열을 수정하는 역활을 한다. 
```python
import numpy as np

rg = np.random.default_rng(1)		# 기본 난수 생성기의 인스턴스 생성 
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
a *= 3
print(a) 
# array([[3, 3, 3],
#       [3, 3, 3]])
b += a
print(b)
# array([[3.51182162, 3.9504637 , 3.14415961],
#       [3.94864945, 3.31183145, 3.42332645]])
a += b	# b is not automatically converted to integer type 
#Trackback (most recent call last):
#	...
#numpy.core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int64') with casting rule 'same_kind'

```
다른 유형의 배열로 작업할 때 결과 배열의 유형은 더 일반적이거나 정확한 배열에 해당한다. (업캐스팅으로 알려진 동작)
```python 
import numpy as np 

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print(b.dtype.name)
# 'float64'
c = a + b 
print(c)
# array([1.        , 2.57079633, 4.14159265])
print(c.dtype.name)
# 'float64' 
d = np.exp(c * 1j)
print(d)
# array([ 0.54030231+0.84147098j, -0.84147098+0.54030231j,
#       -0.54030231-0.84147098j])
print(d.dtype.name)
# 'complex128'

```
배열에 있는 모든 요소의 합을 계산하는 것과 같은 많은 단항 연산은 ndarray 클래스의 메소드로 구현된다. 
```python 
import numpy as np

rg = np.random.default_rng(1)		# 기본 난수 생성기의 인스턴스 생성 
a = rg.random((2, 3))
print(a) 
# array([[0.82770259, 0.40919914, 0.54959369],
#       [0.02755911, 0.75351311, 0.53814331]])
print(a.sum())
# 3.1057109529998157
print(a.min())
# 0.027559113243068367
print(a.max())
# 0.8277025938204418
```
기본적으로 이러한 작업은 배열의 모양에 관계없이 마치 숫자 목록인 것처럼 배열에 적용됩니다. 그러나 axis 매개변수를 지정하면 배열의 지정된 축을 따라 작업을 적용할 수 있다. 
```python 
import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
# array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])
print(a.sum(axis=0))			# sum of each column 
# array([12, 15, 18, 21])
print(a.min(axis=1))
# array([0, 4, 8])
print(a.cumsum(axis=1)) 		# cumulative sum along each row 
# array([[ 0,  1,  3,  6],
#       [ 4,  9, 15, 22],
#       [ 8, 17, 27, 38]])
```
## <strong>Universal Functions</strong>
numpy는 sin, cos, exp와 같은 친숙한 수학 함수를 제공한다. numpy에서는 이것을 "범용 함수"(ufunc)라고 한다. numpy 내에서 이러한 함수는 배열에서 요소별로 작동하여 배열을 출력으로 생성한다. 
```python
import numpy as np

a = np.arange(3)
print(a) 
# array([0, 1, 2])
print(np.exp(a))
# array([1.        , 2.71828183, 7.3890561 ])
print(np.sqrt(a))
# array([0.        , 1.        , 1.41421356])
b = np.array([2., -1., 4.])
print(np.add(a, b))
# array([2., 0., 6.])

```
> <strong>보다 많은 함수는 아래 내용을 참조할 것.</strong>
>> [all](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all), [any](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any), [apply_along_axis](https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html#numpy.apply_along_axis), [argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax), [argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin), [argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort), [average](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average), [bincount](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html#numpy.bincount), [ceil](https://numpy.org/doc/stable/reference/generated/numpy.ceil.html#numpy.ceil), [clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip), [conj](https://numpy.org/doc/stable/reference/generated/numpy.conj.html#numpy.conj), [corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef), [cov](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov), [cross](https://numpy.org/doc/stable/reference/generated/numpy.cross.html#numpy.cross), [cumprod](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy.cumprod), [cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum), [diff](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff), [dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot), [floor](https://numpy.org/doc/stable/reference/generated/numpy.floor.html#numpy.floor), [inner](https://numpy.org/doc/stable/reference/generated/numpy.inner.html#numpy.inner), [invert](https://numpy.org/doc/stable/reference/generated/numpy.invert.html#numpy.invert), [lexsort](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort), [max](https://docs.python.org/dev/library/functions.html#max), [maximum](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html#numpy.maximum), [mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean), [median](https://numpy.org/doc/stable/reference/generated/numpy.median.html#numpy.median), [min](https://docs.python.org/dev/library/functions.html#min), [minimum](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy.minimum), [nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero), [outer](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer), [prod](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod), [re](https://docs.python.org/dev/library/re.html#module-re), [round](https://docs.python.org/dev/library/functions.html#round), [sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort), [std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std), [sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum), [trace](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace), [transpose](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose), [var](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var), [vdot](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy.vdot), [vectorize](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#numpy.vectorize), [where](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where)
## <strong>인덱스, 슬라이싱 과 반복자 (Indexing, Slicing, Iterating)

1차원 배열은 list 및 기타 python 시퀀스와 마찬가지로 인덱싱, 슬라이스 및 반복될수 있다. 
```python
import numpy as np 

a = np.arange(10)**3
print(a)
# array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
print(a[2:5])
# array([ 8, 27, 64])
a[:6:2] = 1000
print(a)
# array([1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729])
print(a[::-1]) 	# reversed a 
# array([ 729,  512,  343,  216,  125, 1000,   27, 1000,    1, 1000])
for i in a:
	print(i**(1 / 3.))
#...
#9.999999999999998
#1.0
#9.999999999999998
#3.0
#9.999999999999998
#4.999999999999999
#5.999999999999999
#6.999999999999999
#7.999999999999999
#8.999999999999998
```
다차원 배열은 축당 하나의 인덱스를 가질 수 있습니다. 이러한 인덱스는 쉼표로 구분된 튜플에 제공된다. 
```python
import numpy as np

def f(x, y):
	return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int)
print(b)
# array([[ 0,  1,  2,  3],
#       [10, 11, 12, 13],
#       [20, 21, 22, 23],
#       [30, 31, 32, 33],
#       [40, 41, 42, 43]])
print(b[2, 3])
# 23 
print(b[0:5, 1]) 	# each row in the second column of b 
# array([ 1, 11, 21, 31, 41])
print(b[:, 1])		# equivalent to the previous example 
# array([ 1, 11, 21, 31, 41])
print(b[1:3, :])	# each column in the second and third row of b 
# array([[10, 11, 12, 13],
#       [20, 21, 22, 23]])

```
축 수보다 적은 이덱스가 제공되면 누락된 인덱스는 완전한 조각으로 간주됨. 
```python
import numpy as np

print(b[-1])		# the last row. Equivalent to b[-1, :]
# array([40, 41, 42, 43])
```
b[i]에서 대괄호 안의 표현식은 i로 처리되고 나머지 축을 나타내는데 필요한 만큼 :의 인스턴스가 뒤따른다. numpy에서는 점을 사용하여 이것을 b[i, ...]로 작성할 수도 있다. 
점(...)은 완전한 인덱싱 튜플을 생성하는데 필요한 만큼의 콜론을 나타낸다. 예를 들어, x 가 5개의 축이 있는 배열의 경우 

* x[1, 2, ...] 와 x[1, 2, :, :, :], 는 동일하다 
* x[..., 3] to x[:, :, :, :, 3] 
* x[4, ..., 5, :] to x[4, :, :, 5, :] 
```python 
import numpy as np

c = np.array([[[ 0, 1, 2], 	# a 3D array (two stacked 2D arrays)
				[ 10, 12, 13]],
				[[100, 101, 102],
				 [110, 112, 113]]])
print(c.shape)
# (2, 2, 3)
print(c[1, ...])		# same as c[1, :, :] or c[1]
# array([[100, 101, 102],
#       [110, 112, 113]])
print(c[..., 2])		# same as c[:, :, 2]
# array([[  2,  13],
#       [102, 113]])

```
다차원 배열에 대한 반복은 첫 번째 축에 대해 수행된다. 

```python
for row in b:
	print(row)

# [0 1 2 3]
# [10 11 12 13]
# [20 21 22 23]
# [30 31 32 33]
# [40 41 42 43]
```
그러나 배열의 각 요소에 대한 작업을 수행하려는 경우 배열의 모든 요소에 대한 반복자인 flat 속성을 사용할 수 있다. 

```python
import numpy as np

b = np.fromfunction(f, (5, 4), dtype=int)
print(b)

for element in b.flat:
	print(element)
...
#0
#1
#2
#3
#10
#11
#12
#13
#20
#21
#22
#23
#30
#31
#32
#33
#40
#41
#42
#43
```
> <strong> 더 참조하기</strong>
>> [Indexing](https://numpy.org/doc/stable/user/basics.indexing.html#basics-indexing), [Indexing](https://numpy.org/doc/stable/reference/arrays.indexing.html#arrays-indexing)(reference), [newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis), [ndenumerate](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate), [indices](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices)

