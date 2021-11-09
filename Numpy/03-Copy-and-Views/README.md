# <strong>복사와 뷰</strong>
배열을 조작하고 조작할 때 데이터가 새로운 배열에 복사되는 경우가 있고 그렇지 않은 경우가 있다. 이것은 종종 초보자에게 혼란의 원인이다. 세가지 경우가 있단다 

## <strong>복사 아님 </strong>
단순 할당은 개체 또는 해당 데이터의 복사본을 만들지 않는다. 

```python 
import numpy as np 

a = np.array([[0, 1, 2, 3],
			[4, 5, 6, 7],
			[8, 9, 10, 11]])
b = a						# no new object is created 
print(b is a)				# a and b are two names for the same ndarray object 
# True 
```
Python은 변경 가능한 객체를 참조로 전달하므로 함수 호출은 복사본을 만들지 않는다. 
```python
def f(x):
	print(id(x))

print(id(a))			# id is a unique identifier of an object 
# 148293216  # may vary
f(a)
# 148293216  # may vary
```
## <strong> 뷰와 얕은 복사</strong>
다른 배열 개체는 동일한 데이터를 공유할 수 있다. view  메소드는 동일한 데이터를 보는 새로운 배열 객체를 생성한다. 
```python
import numpy as np

c = a.view()
print(c is a)		
# False 
print(c.base is a)		# c is a view of the data owned by a
# True 
print(c.flags.owndata)
# False 
c = c.reshape((2, 6))	# a's shape doesn't change 
print(a.shape)
# (3, 4)
print(a)
# array([[   0,    1,    2,    3],
#       [1234,    5,    6,    7],
#       [   8,    9,   10,   11]])
```
배열을 슬라이싱하면 배열의 뷰가 반환됨. 
```python 
s = a[:, 1:3]
s[:] = 10				# s[:] is a view of s. Note the difference between s = 10 and s[:] = 10
print(a)
# array([[   0,   10,   10,    3],
#       [1234,   10,   10,    7],
#       [   8,   10,   10,   11]])
```
## <strong>깊은 복사</strong>
복사 방법은 배열과 해당 데이터의 전체 복사본을 만듭니다. 
```python
d = a.copy()		# a new array object with new data is created 
print(d is a)
# False 
print(d.base is a)	# d doesn't share anything with a 
# False 
d[0, 0] = 9999
print(a)
# array([[   0,   10,   10,    3],
#       [1234,   10,   10,    7],
#       [   8,   10,   10,   11]])
```
원본 배열이 더 이상 필요하지 않은 경우 슬라이싱 후에 copy를 호출해야 하는 경우가 있습니다. 예를 들어, a가 거대한 중간 결과이고 최종 결과 b가 슬라이싱을 사용하여 b를 구성할 때 깊은 복사를 만들어야 하는 작은 부분만 포함한다고 가정한다. 
```python
a = np.arange(int(1e8))
b = a[:100].copy()
del a 					# the memory of ``a`` can be released. 
```
b = a[:100]이 대신 사용되면 a는 b에 의해 참조되며 del a가 실행되더라도 메모리에 유지된다. 

## <strong> 함수와 메소드 개요</strong>
다음은 범주별로 정렬된 몇 가지 유용한 numpy 함수 및 메서드 이름 목록이다. 전체 목록은 루틴을 참조.

#### 배열 생성 (Array Creation)
> [arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange), [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array), [copy](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy), [empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty), [empty_like](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#numpy.empty_like), [eye](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye), [fromfile](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile), [fromfunction](https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html#numpy.fromfunction), [identity](https://numpy.org/doc/stable/reference/generated/numpy.identity.html#numpy.identity), [linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace), [logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace), [mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid), [ogrid](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid), [ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones), [ones_like](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like), [r_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_), [zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros), [zeros_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like)

#### 변환 (Conversions)
> [ndarray.astype](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype), [atleast_1d](https://numpy.org/doc/stable/reference/generated/numpy.atleast_1d.html#numpy.atleast_1d), [atleast_2d](https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html#numpy.atleast_2d), [atleast_3d](https://numpy.org/doc/stable/reference/generated/numpy.atleast_3d.html#numpy.atleast_3d), [mat](https://numpy.org/doc/stable/reference/generated/numpy.mat.html#numpy.mat)

#### 조작 (Manipulations)
> [array_split](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#numpy.array_split), [column_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack), [concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate), [diagonal](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal), [dsplit](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html#numpy.dsplit), [dstack](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#numpy.dstack), [hsplit](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html#numpy.hsplit), [hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack), [ndarray.item](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.item.html#numpy.ndarray.item), [newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis), [ravel](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel), [repeat](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat), [reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape), [resize](https://numpy.org/doc/stable/reference/generated/numpy.resize.html#numpy.resize), [squeeze](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy.squeeze), [swapaxes](https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html#numpy.swapaxes), [take](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take), [transpose](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose), [vsplit](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#numpy.vsplit), [vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack)

#### 질의 (Questions)
> [all](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all), [any](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any), [nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero), [where](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where)

#### 순서 (Ordering)
> [argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax), [argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin), [argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort), [max](https://docs.python.org/dev/library/functions.html#max), [min](https://docs.python.org/dev/library/functions.html#min), [ptp](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp), [searchsorted](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted), [sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort)

#### 오퍼레이션 (Operations)
> [choose](https://numpy.org/doc/stable/reference/generated/numpy.choose.html#numpy.choose), [compress](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#numpy.compress), [cumprod](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy.cumprod), [cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum), [inner](https://numpy.org/doc/stable/reference/generated/numpy.inner.html#numpy.inner), [ndarray.fill](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.fill.html#numpy.ndarray.fill), [imag](https://numpy.org/doc/stable/reference/generated/numpy.imag.html#numpy.imag), [prod](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod), [put](https://numpy.org/doc/stable/reference/generated/numpy.put.html#numpy.put), [putmask](https://numpy.org/doc/stable/reference/generated/numpy.putmask.html#numpy.putmask), [real](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real), [sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum)

#### 기본 통계 (Basic Statistics)
> [cov](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov), [mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean), [std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std), [var](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var)

#### 기본 선형 대수학 (Basic Linear Algebra)
> [cross](https://numpy.org/doc/stable/reference/generated/numpy.cross.html#numpy.cross), [dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot), [outer](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer), [linalg.svd](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd), [vdot](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy.vdot)

