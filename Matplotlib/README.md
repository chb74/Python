# Matplotlib 가이드  

## Matplotlib 설치 가이드 
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


## 사용자 가이드 
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