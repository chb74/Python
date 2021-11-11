# Matplotlib 가이드  

* [Matplotlib 설치 가이드](#matplotlib-install-guide)
* [사용자 가이드](#matplotlib-user-guide)

## <a name="matplotlib-install-guide">Matplotlib 설치 가이드 </a>
Matplotlib 릴리스는 PyPI에서 MacOS, Windows 및 리눅스용 휠 패키지로 사용할 수 있다. Numpy, Pandas 처럼 pip 로 설치하면 된다. 

```bash
python -m pip install -U pip 
python -m pip install -U matplotlib 

# At MacBook 
pip install matplotlib 

```
이 명령으로 소스에서 Matplotlib가 컴파일되고 컴파일에 문제가 있는 경우 --prefer-binary를 추가하여 OS 및 파이썬용으로 미리 컴파일된 휠이 있는 최신 버전의 Matplotlib를 선택할 수 있다. 

### Conda Packages 
```bash 
conda install matplotlib 
```

### Linux Package Manager
* Debian / Ubuntu : sudo apt-get install python3-matplotlib 
* Fedora : sudo dnf install python3-matplotlib 
* Red Hat : sudo yum install python3-matplotlib 
* Arch : sudo pacman -S python-matplotlib 

### 소스로 설치하기 
[소스는 여기](https://matplotlib.org/stable/users/installing_source.html#install-from-source)

### 개발중인 소스설치 
[소스는 여기](https://matplotlib.org/stable/devel/development_setup.html#installing-for-devs)


## <a name=matplotlib-user-guide>사용자 가이드</a>
이 튜토리얼에서는 Matplotlib 를 시작하는데 도움이 되는 몇가지 기본 사용 패턴과 모범 사례를 다룬다. 
```python 
import numpy as np
import matplolib.pyplot as plt 
```

### 간단한 예제 
matplotlib는 그림(예: 창, 주피터 위젯 등)에 데이터를 그래피로 표시하며, 각 그림에는 하나 이상의 축이 포함될 수 있다. (즉, 점이 xy 좌표 또는 극좌표의 세타-r로 지정될 수 있는 영역). 플롯 또는 3D 플롯의 xyz등). 축이 있는 그림을 만드는 가장 간단한 방법은 `pyplot.subplots`를 사용하는 것이다. 그런 다음 Axes.plot를 사용하여 축에 일부 데이터를 그릴 수 있다. 

```python
fig, ax = plt.subplots()            # 단일 좌표축을 포함하는 Figure를 생성
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) # 좌표축에 일부 데이터를 플로팅 한다. 

plt.show()
```
결과는 ![AX 그래프](ax.png)

다른 많은 플로팅 라이브러리나 언어에서는 좌표축을 명시적으로 생성할 필요가 없다. 예를 들어, matlab에서는 다음을 수행할 수 있다. 
```python
plot([1, 2, 3, 4], [1, 4, 2, 3])        % MATLAB plot 
```
원하는 그래프를 얻을수가 있다. 

실제로 matplotlib에서 동일한 작업을 수행할 수 있다. 각 축 그래프 방법에 대해 matplotlib.pyplot 모듈에는 "현재" 축에서 해당 플롯을 수행하는 해당 함수가 있다. 아직 존재하지 않습니다. 따라서 이전 예제는 다음과 같이 더 짧게 작성할 수 있다. 

```python
plt.plot([1 ,2 ,3, 4], [1, 4, 2, 3])        # Matplotlib plot. 
```
결과는 위와 같음 

### 그림의 일부 
matplotlib 그림의 구성 요소를 자세히 살펴보자. 

![Matplotlib](matplotlib.png)

**그림(Figure)**
전체 그림은 위와같으며, 그림은 모든 하위 축, '특수' 아티스트(제목, 그림 범례등) 및 캔버스를 추적한다. (캔버스에 대해 너무 걱정할 필요없다 실제로 그리기를 수행하여 플롯을 가져오는 개체이기 때문에 중요하지만 사용자에게는 거의 보이지 않는다.) Figure에는 여러 개의 축이 포함될 수 있지만 일반적으로 적어도 하나는 있다. 

새 그림을 만드는 가장 쉬운 방법은 pyplot을 사용하는 것이다. 
```python 
fig = plt.figure()                  # 축이 없는 빈 그림이다. 
fig, ax = plt.subplots()            # 축이 하나인 도형 
fig, axs = plt.subplots(2, 2)       # 축의 2x2 그리드가 있는 그림 
```
Figure와 함께 좌표축을 만드는 것이 편리하지만 나중에 좌표축을 추가하여 더 복잡한 좌표축 레이아웃을 허용할 수도 있다. 

**중심선(Axes)**
이것들은 숫자 라인과 같은 객체이다. 그들은 그래프 한계를 설정하고 눈금(축의 표시)과 눈금 레이블(눈금에 레이블을 지정하는 문자열) 을 생성한다. 눈금의 위치는 Locator 개체에 의해 결정되고 눈금 레이블 문자열은 포맷터에 의해 형식이 지정된다. 올바른 로케이터와 포맷터를 조합하면 눈금 위치와 레이블을 매우 세밀하게 제어할 수 있다. 

**아티스트(Artist)**
기본적으로 Figure에서 볼 수 있는 모든 것은 아티스트이다. (Figure, Axes 및 Axis 개체 포함). 여기에는 Text 개체, Line2D개체, 컬렉션 개체, Patch 개체 등이 포함된다. 그림이 렌더링되면 모든 아티스트가 캔버스에 그려진다. 대부분의 아티스트는 축에 묶여 있다. 이러한 아티스트는 여러축에서 공유하거나 한 축에서 다른 축으로 이동할 수 없다. 

### 플로팅 함수에 대한 입력 유형
모든 플로팅 함수는 numpy.array 또는 numpy.ma.masked_array를 입력으로 예상한다. pandas 데이터 개체 및 numpy.matrix와 같은 배열과 유사한 클래스는 의도한 대로 작동하거나 작동하지 않을 수 있다. 플로팅하기 전에 이를 numpy.array객체로 변환하는 것이 가장 좋습니다. 

예를 들어 pandas.DataFrame을 변환하려면, 
```python
a = pandas.DataFrame(np.random.rand(4, 5), columns = list('abcde))
a_asarray = a.values 
```
