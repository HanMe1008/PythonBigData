import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# 배열 합치기
array3 = np.concatenate([array1, array2])

print(array3.shape)
print(array3)

