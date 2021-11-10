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

## <strong>선택 (Selection) </strong>
> **참고**
>> 선택 및 설정을 위한 표준 Python/Numpy 표현식은 직관적이고 대화식 작업에 유용하지만 프로덕션 코드의 경우 최적화된 pandas 데이터 액세스 방법인 .at, .iat, .loc 및 iloc을 권장한다. 

[인덱싱 및 데이터 선택](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing) 및 [MultiIndex / 고급 인덱싱](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced)

### <strong>구하기 (Getting)</strong>
df.A와 동일한 시리즈를 생성하는 단일 열 선택 

```python 
print(df["A"])
# 2013-01-01    0.469112
# 2013-01-02    1.212112
# 2013-01-03   -0.861849
# 2013-01-04    0.721555
# 2013-01-05   -0.424972
# 2013-01-06   -0.673690
# Freq: D, Name: A, dtype: float64
```

행을 슬라이스하는 []를 통해 선택한다. 
```python
print(df[0:3])
#                    A         B         C         D
# 2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
# 2013-01-02  1.212112 -0.173215  0.119209 -1.044236
# 2013-01-03 -0.861849 -2.104569 -0.494929  1.071804

print(df["20130102":"20130104"])
#                    A         B         C         D
# 2013-01-02  1.212112 -0.173215  0.119209 -1.044236
# 2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
# 2013-01-04  0.721555 -0.706771 -1.039575  0.271860
```
### <strong> 라벨로 선택하기 (Selection by label) </strong>
>참조
>> [보다 더 많은 정보](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-label)

레이블을 사용하여 횡단면 가져오기
```python
print(df.loc[dates[0]])
# A    0.469112
# B   -0.282863
# C   -1.509059
# D   -1.135632
# Name: 2013-01-01 00:00:00, dtype: float64
```

레이블로 다중 축을 선택하기 
```python
print(df.loc[:, ["A", "B"]])
#                    A         B
# 2013-01-01  0.469112 -0.282863
# 2013-01-02  1.212112 -0.173215
# 2013-01-03 -0.861849 -2.104569
# 2013-01-04  0.721555 -0.706771
# 2013-01-05 -0.424972  0.567020
# 2013-01-06 -0.673690  0.113648
```

레이블 슬라이싱을 표시하면 두 끝점이 모두 포함됨. 
```python
print(df.loc["20130102":"20130104", ["A", "B"]])
#                    A         B
# 2013-01-02  1.212112 -0.173215
# 2013-01-03 -0.861849 -2.104569
# 2013-01-04  0.721555 -0.706771
```

반환개체의 크기 축소
```python
print(df.loc["20130102", ["A", "B"]])
# A    1.212112
# B   -0.173215
# Name: 2013-01-02 00:00:00, dtype: float64
```
스칼라 값을 얻으려면 
```python
print(df.loc[date[0], "A"])
# 0.4691122999071863
```

스칼라에 빠르게 액세스하려면 (이전 방법과 동일하다.)
```python
print(df.at[dates[0], "A"])
# 0.4691122999071863
```

### **위치로 선택하기 (Selection by position)**
보다 더 자세한 사항은 [여기](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-integer)

전달된 정수의 위치를 통해서 선택하기 
```python 
print(df.iloc[3])
# A    0.721555
# B   -0.706771
# C   -1.039575
# D    0.271860
# Name: 2013-01-04 00:00:00, dtype: float64
```

Numpy/Python과 유사하게 작동하는 정수 조각
```python
print(df.iloc[3:5, 0:2])
#                    A         B
# 2013-01-04  0.721555 -0.706771
# 2013-01-05 -0.424972  0.567020
```

Numpy/Python 스타일과 유사한 정수 위치 목록으로 선택하기 
```python 
print(df.iloc[[1, 2, 4], [0, 2]])
#                    A         C
# 2013-01-02  1.212112  0.119209
# 2013-01-03 -0.861849 -0.494929
# 2013-01-05 -0.424972  0.276232
```

행을 명시적으로 슬라이싱하는 경우 
```python
print(df.iloc[1:3, :])
#                    A         B         C         D
# 2013-01-02  1.212112 -0.173215  0.119209 -1.044236
# 2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
```

행을 명시적으로 슬라이싱하는 경우: 
```python 
print(df.iloc[:, 1:3])
#                    B         C
# 2013-01-01 -0.282863 -1.509059
# 2013-01-02 -0.173215  0.119209
# 2013-01-03 -2.104569 -0.494929
# 2013-01-04 -0.706771 -1.039575
# 2013-01-05  0.567020  0.276232
# 2013-01-06  0.113648 -1.478427
```

명시적으로 값을 얻으려면
```python 
print(df.iloc[1, 1])
# -0.17321464905330858
```

스칼라에 빠르게 액세스하려면 (이전 방법과 동일)
```python
print(df.iat[1, 1])
# -0.17321464905330858
```

### **부울 인덱싱 (Boolean Indexing)**
단일 열의 값을 사용하여 데이터 선택 

```python 
print(df[df["A"] > 0])
#                    A         B         C         D
# 2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
# 2013-01-02  1.212112 -0.173215  0.119209 -1.044236
# 2013-01-04  0.721555 -0.706771 -1.039575  0.271860
```

부울 조건이 충족되는 DataFrame에서 값을 선택하기 
```python
print(df[df > 0])
#                    A         B         C         D
# 2013-01-01  0.469112       NaN       NaN       NaN
# 2013-01-02  1.212112       NaN  0.119209       NaN
# 2013-01-03       NaN       NaN       NaN  1.071804
# 2013-01-04  0.721555       NaN       NaN  0.271860
# 2013-01-05       NaN  0.567020  0.276232       NaN
# 2013-01-06       NaN  0.113648       NaN  0.524988
```

필터링을 위해 isin() 메서드 사용
```python 
df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
print(df2)
#                    A         B         C         D      E
# 2013-01-01  0.469112 -0.282863 -1.509059 -1.135632    one
# 2013-01-02  1.212112 -0.173215  0.119209 -1.044236    one
# 2013-01-03 -0.861849 -2.104569 -0.494929  1.071804    two
# 2013-01-04  0.721555 -0.706771 -1.039575  0.271860  three
# 2013-01-05 -0.424972  0.567020  0.276232 -1.087401   four
# 2013-01-06 -0.673690  0.113648 -1.478427  0.524988  three
```
```python 
print(df2[df2["E"].isin(["two", "four"])])
#                    A         B         C         D     E
# 2013-01-03 -0.861849 -2.104569 -0.494929  1.071804   two
# 2013-01-05 -0.424972  0.567020  0.276232 -1.087401  four
```

### **설정하기 (Setting)**
새 열을 설정하면 인덱스별로 데이터가 자동으로 정렬된다. 

```python 
s1 = pd.Series([1, 2, 3, 4, 5, 6], index = pd.date_range("20130102", periods = 6))

print(s1)
# 2013-01-02    1
# 2013-01-03    2
# 2013-01-04    3
# 2013-01-05    4
# 2013-01-06    5
# 2013-01-07    6
# Freq: D, dtype: int64
df["F"]  = s1
```

라벨로 값을 설정하고 
```python 
df.at[dates[0], "A"] = 0 
```

위치에 값을 설정하고 
```python
df.iat[0, 1] = 0
```

Numpy 배열로 할당하여 설정: 
```python
df.loc[:, "D"] = np.array([5] * len(df))
```

이전 설정 작업의 결과
```python
print(df)
#                    A         B         C  D    F
# 2013-01-01  0.000000  0.000000 -1.509059  5  NaN
# 2013-01-02  1.212112 -0.173215  0.119209  5  1.0
# 2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0
# 2013-01-04  0.721555 -0.706771 -1.039575  5  3.0
# 2013-01-05 -0.424972  0.567020  0.276232  5  4.0
# 2013-01-06 -0.673690  0.113648 -1.478427  5  5.0
```

설정이 있는 where 작업하기 
```python
df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)
#                    A         B         C  D    F
# 2013-01-01  0.000000  0.000000 -1.509059 -5  NaN
# 2013-01-02 -1.212112 -0.173215 -0.119209 -5 -1.0
# 2013-01-03 -0.861849 -2.104569 -0.494929 -5 -2.0
# 2013-01-04 -0.721555 -0.706771 -1.039575 -5 -3.0
# 2013-01-05 -0.424972 -0.567020 -0.276232 -5 -4.0
# 2013-01-06 -0.673690 -0.113648 -1.478427 -5 -5.0
```

## <strong> 데이터 누락 (Missing Data) </strong>
pandas 는 주로 np.nan값을 사용하여 누락된 데이터를 나타낸다. 기본적으로 계산에 포함되지 않는다. [누락된 데이터 섹션 참조](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data)

재인덱싱을 사용하면 지정된 축의 인덱스를 변경/추가/삭제할 수 있다. 그러면 데이터 복사본이 반환됨. 

```python 
df1 = df.reindex(index = dates[0:4], columns = list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1

print(df1)
#                    A         B         C  D    F    E
# 2013-01-01  0.000000  0.000000 -1.509059  5  NaN  1.0
# 2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
# 2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0  NaN
# 2013-01-04  0.721555 -0.706771 -1.039575  5  3.0  NaN
```

누락된 데이터가 있는 행을 삭제한다. 
```python
print(df1.dropna(how = "any"))
#                    A         B         C  D    F    E
# 2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
```

누락된 데이터로 채우기 
```python
print(df1.fillna(value = 5))
#                    A         B         C  D    F    E
# 2013-01-01  0.000000  0.000000 -1.509059  5  5.0  1.0
# 2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
# 2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0  5.0
# 2013-01-04  0.721555 -0.706771 -1.039575  5  3.0  5.0
```

값이 nan인 부울 마스크를 얻으려면 
```python
print(pd.isna(df1))
#                 A      B      C      D      F      E
# 2013-01-01  False  False  False  False   True  False
# 2013-01-02  False  False  False  False  False  False
# 2013-01-03  False  False  False  False  False   True
# 2013-01-04  False  False  False  False  False   True
```


## <strong> 운영?? (Operations) </strong>
[Binary Ops의 기본 섹션](https://pandas.pydata.org/docs/user_guide/basics.html#basics-binop)

### **Stats**
일반적으로 작업은 누락된 데이터를 제외한다. 

기술 통계 수행 
```python 
print(df.mean())
# A   -0.004474
# B   -0.383981
# C   -0.687758
# D    5.000000
# F    3.000000
# dtype: float64
```

다른 축에서 동일한 작업하기 
```python
print(df.mean(1))
# 2013-01-01    0.872735
# 2013-01-02    1.431621
# 2013-01-03    0.707731
# 2013-01-04    1.395042
# 2013-01-05    1.883656
# 2013-01-06    1.592306
# Freq: D, dtype: float64
```

차원이 다르고 정렬이 필요한 개체로 작업을 한다.또한 pandas는 지정된 차원을 따라 자동으로 브로드캐스트를 한다. 
```python
s = pd.Series([1, 3, 5, np.nan, 6, 8], index = dates).shift(2)
print(s)
# 2013-01-01    NaN
# 2013-01-02    NaN
# 2013-01-03    1.0
# 2013-01-04    3.0
# 2013-01-05    5.0
# 2013-01-06    NaN
# Freq: D, dtype: float64

print(df.sub(s, axis = "index"))
#                    A         B         C    D    F
# 2013-01-01       NaN       NaN       NaN  NaN  NaN
# 2013-01-02       NaN       NaN       NaN  NaN  NaN
# 2013-01-03 -1.861849 -3.104569 -1.494929  4.0  1.0
# 2013-01-04 -2.278445 -3.706771 -4.039575  2.0  0.0
# 2013-01-05 -5.424972 -4.432980 -4.723768  0.0 -1.0
# 2013-01-06       NaN       NaN       NaN  NaN  NaN
```

### **적용하기 (Apply)**
데이터에 함수 적용하기 
```python
print(df.apply(np.cumsum))
#                    A         B         C   D     F
# 2013-01-01  0.000000  0.000000 -1.509059   5   NaN
# 2013-01-02  1.212112 -0.173215 -1.389850  10   1.0
# 2013-01-03  0.350263 -2.277784 -1.884779  15   3.0
# 2013-01-04  1.071818 -2.984555 -2.924354  20   6.0
# 2013-01-05  0.646846 -2.417535 -2.648122  25  10.0
# 2013-01-06 -0.026844 -2.303886 -4.126549  30  15.0

print(df.apply(lambda x: x.max() - x.min()))
# A    2.073961
# B    2.671590
# C    1.785291
# D    0.000000
# F    4.000000
# dtype: float64
```

### **히스토그래밍**
보다 자세한 내용은 [여기](https://pandas.pydata.org/docs/user_guide/basics.html#basics-discretization)

```python 
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
# 0    4
# 1    2
# 2    1
# 3    2
# 4    6
# 5    4
# 6    4
# 7    6
# 8    4
# 9    4
# dtype: int64
print(s.value_counts())
# 4    5
# 2    2
# 6    2
# 1    1
# dtype: int64
```

### **스트링 메소드(String Methods)**
Series에는 아래 코드 조각과 같이 배열의 각 요소에서 쉽게 작동할 수 있도록 하는 str 속성에 일련의 문자열 처리 방법이 장착되어 있다. str의 패턴 일치는 일반적으로 기본적으로 [정규식](https://docs.python.org/3/library/re.html)을 사용한다. (어떤 경우에는 항상 정규식을 사용). [벡터화된 문자열 메서드](https://pandas.pydata.org/docs/user_guide/text.html#text-string-methods)에서 자세히 알아보자 
```python
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])

print(s.str.lower())
# 0       a
# 1       b
# 2       c
# 3    aaba
# 4    baca
# 5     NaN
# 6    caba
# 7     dog
# 8     cat
# dtype: object

```

## **병합 (Merge)**

### **연결 (Concat)** 
pandas는 조인/병합 유형 작업의 경우 인덱스 및 관계 대수 기능에 대한 다양한 종류의 설정 논리를 사용하여 Series 및 DataFrame 개체를 쉽게 결합할 수 있는 다양한 기능을 제공한다. 

[병합 섹션 참조](https://pandas.pydata.org/docs/user_guide/merging.html#merging)

Concat()을 사용하여 pandas 객체 연결하기 
```python
df = pd.DataFrame(np.random.randn(10, 4))
print(df)
#           0         1         2         3
# 0 -0.548702  1.467327 -1.015962 -0.483075
# 1  1.637550 -1.217659 -0.291519 -1.745505
# 2 -0.263952  0.991460 -0.919069  0.266046
# 3 -0.709661  1.669052  1.037882 -1.705775
# 4 -0.919854 -0.042379  1.247642 -0.009920
# 5  0.290213  0.495767  0.362949  1.548106
# 6 -1.131345 -0.089329  0.337863 -0.945867
# 7 -0.932132  1.956030  0.017587 -0.016692
# 8 -0.575247  0.254161 -1.143704  0.215897
# 9  1.193555 -0.077118 -0.408530 -0.862495

# break it into pieces 
pieces = [df[:3], df[3:7], df[7:]]

print(pd.concat(pieces))
#           0         1         2         3
# 0 -0.548702  1.467327 -1.015962 -0.483075
# 1  1.637550 -1.217659 -0.291519 -1.745505
# 2 -0.263952  0.991460 -0.919069  0.266046
# 3 -0.709661  1.669052  1.037882 -1.705775
# 4 -0.919854 -0.042379  1.247642 -0.009920
# 5  0.290213  0.495767  0.362949  1.548106
# 6 -1.131345 -0.089329  0.337863 -0.945867
# 7 -0.932132  1.956030  0.017587 -0.016692
# 8 -0.575247  0.254161 -1.143704  0.215897
# 9  1.193555 -0.077118 -0.408530 -0.862495

```
> **노트**    
>> [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)에 열을 추가하는 것은 비교적 빠르다. 그러나 행을 추가하려면 복사본이 필요하고 비용이 많이 들 수 있다. 반복적으로 레코드를 추가하여 [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)을 작성하는 대신 미리 작성된 레코드 목목을 [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)생성자에게 전달하는 것이 좋다. 자세한 내용은 [데이터프레임에 추가](https://pandas.pydata.org/docs/user_guide/merging.html#merging-concatenation)를 참조


### **조인(Join)**
SQL 스타일이 병합됨. [데이터베이스 스타일 결합 섹션 참조](https://pandas.pydata.org/docs/user_guide/merging.html#merging-join)

```python
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataRame({"key": ["foo", "foo"], "rval": [4, 5]})

print(left)
#    key  lval
# 0  foo     1
# 1  foo     2

print(right)
#    key  rval
# 0  foo     4
# 1  foo     5

print(pd.merge(left, right, on = "key"))
#    key  lval  rval
# 0  foo     1     4
# 1  foo     1     5
# 2  foo     2     4
# 3  foo     2     5
```

제공할 수 있는 또 다른 예는 다음과 같다. 
```python 
left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})

print(left)
#    key  lval
# 0  foo     1
# 1  bar     2

print(right)
#    key  rval
# 0  foo     4
# 1  bar     5

print(pd.merge(left, right, on="key"))
#    key  lval  rval
# 0  foo     1     4
# 1  bar     2     5
```

## **그룹화(Grouping)**
"그룹화 기준"은 다음 단계 중 하나 이상을 포함하는 프로세스를 나타낸다. 
> * 분할 (Splitting) : 일부 기준에 따라 데이터를 그룹으로 분할 
> * 적용 (Applying) : 각 그룹에 독립적으로 기능 적용 
> * 결합 (Combining) : 결과를 데이터 구조로 결합





