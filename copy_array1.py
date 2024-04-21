# 중간범위 X
import numpy as np

# Numpy 배열 객체 복사
array1 = np.arange(0, 10)
array2 = array1
array2[0] = 99
print(array1)
print()

array3 = np.arange(0, 10)
array4 = array1.copy()
array4[0] = 99
print(array3)