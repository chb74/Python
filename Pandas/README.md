## <strong>Pandas </strong>
Pandas 는 Python 모듈이고 라이브러리이다. 데이터 구조 및 데이터 분석 도구를 제공하는 오픈소스이다. 

## <strong> 10분만에 Pandas 마스터 하기</strong>
이것은 주료 신규 사용자를 대상으로 하는 Pandas에 대한 짧은 소개이다.
더 자세한 사항은 [여기서](https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook) 볼수 있다.

보통은 아래처럼 라이브러리를 임포트 해준다. 
```python 

import numpy as np 
import pandas as pd 

```

## <strong> 객체 생성 (Object creation) </strong>

[링크](https://pandas.pydata.org/docs/user_guide/dsintro.html#dsintro)를 참조하라. 

값 목록을 전달하여 시리즈 생성, pandas가 기본 정수 인덱스 생성: 
```python
s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s) 
# 0    1.0
#1    3.0
#2    5.0
#3    NaN
#4    6.0
#5    8.0
#dtype: float64
```

날짜/시간 인덱스와 레이블이 지정된 열이 있는 Numpy 배열을 전달하여 DataFrame 만들기 
```python
dates = pd.date_range("20130101", periods = 6)
print(dates)
# DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#               '2013-01-05', '2013-01-06'],
#              dtype='datetime64[ns]', freq='D')
df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns = list("ABCD"))

print(df)
#                    A         B         C         D
#2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
#2013-01-02  1.212112 -0.173215  0.119209 -1.044236
#2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
#2013-01-04  0.721555 -0.706771 -1.039575  0.271860
#2013-01-05 -0.424972  0.567020  0.276232 -1.087401
#2013-01-06 -0.673690  0.113648 -1.478427  0.524988
```

Json 형태의 Dictionary 를 전달하여 DataFrame 만들기 
```python

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index = list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)
#      A          B    C  D      E    F
#0  1.0 2013-01-02  1.0  3   test  foo
#1  1.0 2013-01-02  1.0  3  train  foo
#2  1.0 2013-01-02  1.0  3   test  foo
#3  1.0 2013-01-02  1.0  3  train  foo
```
결과는 DataFrame의 열에는 다른 dtype 이 있다. 다음과 같이 

```python
print(df2.dtypes)
# A           float64
# B    datetime64[ns]
# C           float32
# D             int32
# E          category
# F            object
# dtype: object
```
## <strong> 데이터 보기 (Viewing Data) </strong>
여기도 [참고](https://pandas.pydata.org/docs/user_guide/basics.html#basics)할것.

프레임의 상단 및 하단 행을 보는 방법은 다음과 같다. 

```python
print(df.head())
#                    A         B         C         D
# 2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
# 2013-01-02  1.212112 -0.173215  0.119209 -1.044236
# 2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
# 2013-01-04  0.721555 -0.706771 -1.039575  0.271860
# 2013-01-05 -0.424972  0.567020  0.276232 -1.087401

print(df.tail(3))
#                    A         B         C         D
# 2013-01-04  0.721555 -0.706771 -1.039575  0.271860
# 2013-01-05 -0.424972  0.567020  0.276232 -1.087401
# 2013-01-06 -0.673690  0.113648 -1.478427  0.524988

```
열(index)과 행(column) 보여주기 
```python

print(df.index)
# DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#               '2013-01-05', '2013-01-06'],
#              dtype='datetime64[ns]', freq='D')
print(df.columns)
# Index(['A', 'B', 'C', 'D'], dtype='object')
DataFrame.to_numpy()는 기본 데이터의 numpy 표현을 제공한다. DataFrame에 다른 데이터 유형이 있는 열이 있는 경우 이는 비용이 많이 드는 작업이 될수 있다. 이는 pandas와 numpy 간의 근보ㅗㄴ적인 차이점으로 귀결된다. numpy 배열에는 전체 배열에 대해 하나의 dtype이 있는 반면 pandas DataFrame에는 열당 하나의 dtype이 있습니다. DataFrame.to_numpy()를 호출하면 pandas는 DataFrame의 모든 dtype을 보유할 수 있는 numpy dtype을 찾습니다. 이것은 결국 모든 값을 파이썬 객체로 캐스팅해야 하는 객체가 될수 있다. 

모든 부동 소수점 값의 DataFrame인 df의 경우 DataFrame.to_numpy()는 빠르고 데이터 복사가 필요하지 않는다. 

```python
print(df.to_numpy())
# array([[ 0.4691, -0.2829, -1.5091, -1.1356],
#       [ 1.2121, -0.1732,  0.1192, -1.0442],
#       [-0.8618, -2.1046, -0.4949,  1.0718],
#       [ 0.7216, -0.7068, -1.0396,  0.2719],
#       [-0.425 ,  0.567 ,  0.2762, -1.0874],
#       [-0.6737,  0.1136, -1.4784,  0.525 ]])
```
df2의 경우 여러 dtype이 있는 DataFrame인 DataFrame.to_numpy()는 상대적으로 비싸다. 

```python 
print(df2.to_numpy())
# array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']],
      dtype=object)
```
> <strong> Note</strong>
> [DataFrame.to_numpy()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy) 는 출력에 인덱스 또는 열 레이블을 포함하지 않는다. 

describe()는 데이터의 빠른 통계 요약을 보여준다. 
```python 
print(df.describe())
#             A         B         C         D
#count  6.000000  6.000000  6.000000  6.000000
#mean   0.073711 -0.431125 -0.687758 -0.233103
#std    0.843157  0.922818  0.779887  0.973118
#min   -0.861849 -2.104569 -1.509059 -1.135632
#25%   -0.611510 -0.600794 -1.368714 -1.076610
#50%    0.022070 -0.228039 -0.767252 -0.386188
#75%    0.658444  0.041933 -0.034326  0.461706
#max    1.212112  0.567020  0.276232  1.071804
```

데이터 전치하기 
```python 
print(df.T)
#    2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
#A    0.469112    1.212112   -0.861849    0.721555   -0.424972   -0.673690
#B   -0.282863   -0.173215   -2.104569   -0.706771    0.567020    0.113648
#C   -1.509059    0.119209   -0.494929   -1.039575    0.276232   -1.478427
#D   -1.135632   -1.044236    1.071804    0.271860   -1.087401    0.524988
```

축을 기준으로 정렬하기 
```python
print(df.sort_index(axis = 1, ascending = False))
# 2013-01-01 -1.135632 -1.509059 -0.282863  0.469112
# 2013-01-02 -1.044236  0.119209 -0.173215  1.212112
# 2013-01-03  1.071804 -0.494929 -2.104569 -0.861849
# 2013-01-04  0.271860 -1.039575 -0.706771  0.721555
# 2013-01-05 -1.087401  0.276232  0.567020 -0.424972
# 2013-01-06  0.524988 -1.478427  0.113648 -0.673690
```

값을 기준으로 정렬하기 
```python
print(df.sort_values(by="B"))
#                    A         B         C         D
# 2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
# 2013-01-04  0.721555 -0.706771 -1.039575  0.271860
# 2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
# 2013-01-02  1.212112 -0.173215  0.119209 -1.044236
# 2013-01-06 -0.673690  0.113648 -1.478427  0.524988
# 2013-01-05 -0.424972  0.567020  0.276232 -1.087401
```

## <strong> 선택 (Selection) </strong>
> <strong>참고</strong>
> 선택 및 설정을 위한 표준 Python/Numpy 표현식은 직관적이고 대화식 작업에 유용하지만 프로덕션 코드의 경우 최적화된 pandas 데이터 액세스 방법인 .at, .iat, .loc 및 iloc을 권장한다. 









