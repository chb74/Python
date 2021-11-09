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