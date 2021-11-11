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

**그림(Figure)**<br>
전체 그림은 위와같으며, 그림은 모든 하위 축, '특수' 아티스트(제목, 그림 범례등) 및 캔버스를 추적한다. (캔버스에 대해 너무 걱정할 필요없다 실제로 그리기를 수행하여 플롯을 가져오는 개체이기 때문에 중요하지만 사용자에게는 거의 보이지 않는다.) Figure에는 여러 개의 축이 포함될 수 있지만 일반적으로 적어도 하나는 있다. 

새 그림을 만드는 가장 쉬운 방법은 pyplot을 사용하는 것이다. 
```python 
fig = plt.figure()                  # 축이 없는 빈 그림이다. 
fig, ax = plt.subplots()            # 축이 하나인 도형 
fig, axs = plt.subplots(2, 2)       # 축의 2x2 그리드가 있는 그림 
```
Figure와 함께 좌표축을 만드는 것이 편리하지만 나중에 좌표축을 추가하여 더 복잡한 좌표축 레이아웃을 허용할 수도 있다. 

**중심선(Axes)**<br>
이것들은 숫자 라인과 같은 객체이다. 그들은 그래프 한계를 설정하고 눈금(축의 표시)과 눈금 레이블(눈금에 레이블을 지정하는 문자열) 을 생성한다. 눈금의 위치는 Locator 개체에 의해 결정되고 눈금 레이블 문자열은 포맷터에 의해 형식이 지정된다. 올바른 로케이터와 포맷터를 조합하면 눈금 위치와 레이블을 매우 세밀하게 제어할 수 있다. 

**아티스트(Artist)**<br>
기본적으로 Figure에서 볼 수 있는 모든 것은 아티스트이다. (Figure, Axes 및 Axis 개체 포함). 여기에는 Text 개체, Line2D개체, 컬렉션 개체, Patch 개체 등이 포함된다. 그림이 렌더링되면 모든 아티스트가 캔버스에 그려진다. 대부분의 아티스트는 축에 묶여 있다. 이러한 아티스트는 여러축에서 공유하거나 한 축에서 다른 축으로 이동할 수 없다. 

### 플로팅 함수에 대한 입력 유형
모든 플로팅 함수는 numpy.array 또는 numpy.ma.masked_array를 입력으로 예상한다. pandas 데이터 개체 및 numpy.matrix와 같은 배열과 유사한 클래스는 의도한 대로 작동하거나 작동하지 않을 수 있다. 플로팅하기 전에 이를 numpy.array객체로 변환하는 것이 가장 좋습니다. 

예를 들어 pandas.DataFrame을 변환하려면, 
```python
a = pandas.DataFrame(np.random.rand(4, 5), columns = list('abcde'))
a_asarray = a.values 
```

numpy.matrix를 변환하려면 

```python
b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)
```

### 객체 지향 인터페이스와 pyplot 인터페이스
위에서 언급했듯이 Matplotlib를 사용하는 기본적으로 두가지 방법이 있다. 
* 명시적으로 그림과 축을 만들고 이에 대한 메서드를 호출한다. (객체지향 스타일: OO방법 -> OO : Object Oriented)
* pyplot을 사용하여 그림과 축을 자동으로 생성 및 관리하고 플리팅에 pyplot 기능을 사용하는 방법

OO 스타일 
```python
x = np.linspace(0, 2, 100)

# OO 스타일에서도 '.pyplot.Figure'를 사용하여 그림을 그린다. 
fig, ax = plt.subplots()                    # Figure와 좌표축을 생성
ax.plot(x, x, label='linear')               # 좌표축에 일부 데이터를 플로팅 한다. 
ax.plot(x, x**2, label='quardratic')        # 좌표축에 더 많은 데이터를 플로팅 한다. 
ax.plot(x, x**3, label='cubic')             # 그리고 계속 
ax.set_xlabel('x label')                    # 좌표축에 x 레이블을 추가한다. 
ax.set_ylabel('y label')                    # 좌표축에 y 레이블을 추가한다. 
ax.set_title('Simple Plot')                 # 좌표축에 타이틀을 추가한다. 
ax.legend()                                 # Add a Legend. (범례를 추가한다.)
plt.show()

```

or pyplot-style 
```python
x = np.linspace(0, 2, 100)

plt.plot(x, x, label="linear")              # (암시적) 축에 일부 데이터를 플로팅 한다. 
plt.plot(x, x**2, label="quadratic")        # etc 
plt.plot(x, x**3, label="cubic")
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()
```

또한 GUI 응용 프로그램에 matplotlib를 포함하는 경우 그림 생성 시에도 pyplot을 완전히 삭제하는 세 번째 접근 방식이 있습니다. (Embedding Matplotlib in graphical user interfaces](https://matplotlib.org/stable/gallery/index.html#user-interfaces))

matplotlib 의 문서와 예제는 OO와 pyplot 접근 방식(동일하게 강력함) 을 모두 사용하며 둘중 하나를 자유롭게 사용해야 한다. (그러나 둘 중 하나를 선택하여 혼합하는 대신 고수하는 것이 좋다.) 일반적으로 pyplot을 대화형 플로팅(예: 주피터 노트북) 으로 제한하고 비 대화형 플로팅 (더 큰 프로젝트의 일부로 재사용되는 함수 및 스크립트)에 OO스타일을 선호하는 것이 좋다. 

> **노트**
>> 이전 예제에서는 from pylab import *를 통해 소위 pylab 인터페이스를 대신 사용한 예제를 찾을 수 있다. 이 * import는 pyplot와 numpy에서 모두 가져오기 때문에 다음을 수행할 수 있다. 
>> ```python
>> x = linspace(0, 2, 100)
>> plot(x, x, label='linear')
>> ```
>> 더욱 MATLAB과 유사한 스타일을 제공한다. 이 접근 방식은 현재 권장되지 않으며 더 이상 사용되지 않는다. 야생에서 여전히 만날 수 있기 때문에 여기에서만 언급된다. 

일반적으로 동일한 플롯을 반복해서 만들지만 데이터 세트가 다르기 때문에 플롯을 수행하기 위해 특수 기능을 작성해야 한다. 권장되는 함수 서명은 다음과 같다. 

```python 
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes 
        The axes to draw to 
    data1 : array 
        The x data 
    
    data2 : array
        The y data 

    param_dict : dict 
        Dictionary of kwargs to pass to ax.plot 

    Returns 
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out
```

다음과 같이 사용가능하다. 
```python
data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})
```

또는 2개의 하위 플롯을 갖고 싶다면 
```python
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
```

이러한 간단한 예의 경우 이 스타일은 과도하게 보이지만 그래프가 약간 더 복잡해지면 효과가 있다. 

### 백엔드 (Backends)
#### 백엔드가 뭐냐 ?
웹사이트와 메일링 리스트에 있는 많은 문서는 "백엔드"를 언급하며 많은 신규 사용자가 이 용어를 혼동한다. matplotlib는 다양한 사용 사례와 출력 형식을 대상으로 한다. 어떤 사람들은 파이썬 쉘에서 대화식으로 matplotlib를 사용하고 명령을 입력할 때 플로팅 창이 팝업된다. 어떤 사람들은 주피터 노트북을 실행하고 빠른 데이터 분석을 위해 인라인 플롯을 그린다. 다른 사람들은 matplotlib 를 PyQt 또는 PyGObject와 같은 그래픽 사용자 인터페이스에 포함하여 풍부한 응용 프로그램을 빌드한다. 어떤 사람들은 배치 스크립트에서 matplotlib를 사용하여 수치 시뮬레이션에서 포스트스크립트 이미지를 생성하고 다른 사람들은 웹 애플리케이션 서버를 실행하여 그래프를 동적으로 제공한다. 

이러한 모든 사용사례를 지원하기 위해 matplotlib는 다양한 출력을 대상으로 할 수 있으며 이러한 각 기능을 백엔드라고 한다. "프론트엔드"는 사용자가 직면하는 코드, 즉 플로팅 코드인 반면, "백엔드"는 그림을 만들기 위해 뒤에서 모든 힘든 작업을 수행한다. 백엔드에는 두가지 유형이 있다. 사용자 인터페이스 백엔드 (PyQt/PySide, PyGObject, Tkinter, wxPython 또는 macOS/Cocoa에서 사용); "대화형 백엔드"라고도 함) 및 이미지 파일을 만들기 위한 하드카피 백엔드(PNG, SVG, PDF, PS; "비대화형 백엔드"라고도 함)

#### 백엔드 선택하기 
백엔드를 구성하는 세가지 방법이 있다. 

* matplotlibrc 파일의 [rcParams["backend"]](https://matplotlib.org/stable/tutorials/introductory/customizing.html?highlight=backend#a-sample-matplotlibrc-file) 매개변수 
* [MPLBACKEND](https://matplotlib.org/stable/faq/environment_variables_faq.html#envvar-MPLBACKEND) 환경 변수
* 함수 [matplotlib.use()](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use)
 
 더 자세한 설명은 아래에... 

 이러한 구성이 여러 개 있는 경우 목록의 마지막 구성이 우선한다. 예를 들어 matplotlib.use()를 호출하면 matplotlibrc의 설정이 무시된다. 

 백엔드가 명시적으로 설정되지 않는 경우 matplotlib는 시스템에서 사용 가능한 항목과 GUI 이벤트 루프가 이미 실행 중인지 여부에 따라 사용 가능한 백엔드를 자동으로 감지한다. 리눅스에서 환경 변수 DISPLAY가 설정되지 않은 경우 "이벤트 루프"는 "헤드리스"로 식별되어 비대화형 백엔드(agg)로 폴백된다. 다른 모든 경우에는 대화형 백엔드가 선호된다. (일반적으로 최소한 tkagg를 사용할 수 있다.)

구성 방법에 대한 자세한 설명은 다음과 같습니다. 

  * matplotlibrc 파일에서 rcParams["backend"] 설정 : 
    ```bash 
    backend : qt5agg            #  안티그레인(agg) 렌더링과 함께 pyqt5 사용 
    ```
