
import numpy as np 

print(np.arange(10000))

print(np.arange(10000).reshape(100, 100))

# 이 동작을 비활성화하고 NumPy가 전체 배열을 인쇄하도록 하려면 set_printoptions를 사용하여 인쇄 옵션을 변경할 수 있습니다. 
np.set_printoptions(threshold = sys.maxsize)

