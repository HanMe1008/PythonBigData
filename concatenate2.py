import numpy as np

array1 = np.arange(4).reshape(1, 4)
array2 = np.arange(8).reshape(2, 4)

print(array1)
print(array2)

# 행을 추가하기 위해선 axis=0
# 열을 추가하기 위해선 axis=1
array3 = np.concatenate([array1, array2], axis=0)
print(array3)