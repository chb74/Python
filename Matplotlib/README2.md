# 기본 사용방법

Ref Original URL : https://wikidocs.net/92071

plt.plot([1, 2, 3, 4]) 와 같이 입력하면 x 축 값은 자동으로 만들어 냅니다. 즉, 다음과 같이 만들어집니다. 

`plt.plot([0, 1, 2, 3], [1, 2, 3, 4])`

```python
import matplotlib.pyplot as plt 

# plt가 입력값을 y 값으로 알아서 가정한다. 
plt.plot([1, 2, 3, 4])
plt.show() 
```

```python 
import matplotlib.pyplot as plt 

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()
```

### 스타일 지정하기 

x,y  값 인자에 대해 선의 색상과 형태를 지정하는 포맷 문자열(Format String)을 세번째 인자에 입력할 수 있다. 포맷 문자열 'ro'는 빨간색('red')의 원형 ('o') 마커를 의미한다. 또한 예를 들어 'b-'는 파란색 ('blue')의 실선('-')을 의미함. matplotlib.pyplot 모듈의 axis() 함수를 이용해서 축의 범위 [xmin, xmax, ymin, ymax] 를 지정 
```python 
import matplotlib.pyplot as plt 

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```

### 여러개의 그래프 그리기 
matplotlib에서는 일반적으로 Numpy 배열을 이용하게 됨. Numpy 사용하지 않더라도 모든 스퀀스는 내부적으로 Numpy 배열로 변환됨. 

`plt.plot(X, Y1, 'r--', X, Y2, 'bs', X, Y3, 'g^')`

```python
import matplotlib.pyplot as plt 
import numpy as np 

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```
결과는 ![Multi-Graph](./multigraph.png){: width="100" height="80"}


### 숫자 입력하기 
matplotlib.pyplot 모듈의 plot()은 선(Line) 또는 마커(Marker) 그래프 그리기에 사용되는 함수이다. plot() 함수에 y값을 리스트 형태로 입력하면 위 그림과 같은 꺽은선 그래프가 그려짐. 

```python 
import matplotlib.pyplot as plt 

# 좌표는 y축으로 인식 
plt.plot([2, 3, 5, 10])
plt.show()
```

### x, y 값 입력하기 

```python 
import matplotlib.pyplot as plt 

plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.show() 
```
plot() 함수에 두개의 리스트를 입력하면 순서대로 x, y값들로 인식해서 점 `(1, 2), (2, 3), (3, 5), (4, 10)`를 잇는 꺽은선 그래프가 나타남 

### 레이블이 있는 데이터 사용하기 
파이썬 딕셔너리와 같이 레이블이 있는 데이터를 그래프로 나타낼수 있다. plot() 함수에 데이터의 레이블 (딕셔너리의 키)을 입력해주고, data 파라미터에 딕셔너리를 지정해줌. 
```python 
import matplotlib.pyplot as plt 

data_dict = {'data_x': [1, 2, 3, 4, 5], 'data_y': [2, 3, 5, 10, 8]}
plt.plot('data_x', 'data_y', data=data_dict)
plt.show()
```

### Matplotlib 축 레이블 설정하기 
matplotlib.pyplot 모듈의 xlabel(), ylabel() 함수를 사용하면 그래프의 x, y축에 대한 레이블을 표시할 수 있다. 이 페이지에서는 xlabel(), ylabel() 함수를 사용해서 그래프의 축에 레이블을 표시하는 방법은 
```python 
import matplotlib.pyplot as plt 

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.show() 
```

