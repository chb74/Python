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

