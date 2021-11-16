# 기본 사용방법

Ref : https://wikidocs.net/92071

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

```python

```