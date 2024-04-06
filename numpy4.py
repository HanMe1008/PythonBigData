import numpy as np
A = np.array([[10, 20, 30], [40, 50, 60]])
print(A.shape)
print(A)

B = np.array([1,2,3])
C = np.array([4,5,6])
# vector B, C 출력
print("B ==", B, ", C ==", C)

# vector A, B의 형상(shape) 출력
print("B.shape ==", B.shape, ", C.shape ==", C.shape)

# vector A, B의 차원 출력
print("B.ndim ==", B.ndim, ", C.ndim ==", C.ndim)

# 
l=([1,2,3],
   [4,5,6],
   [7,8,9])
import numpy as np
A = np.array(l)
print(A)
print(A.ndim)
print(A.shape)

# 0~9까지 random하게 초기화 
import numpy as np
array1 = np.random.randint(0, 10, (3, 3))
print(array1)

# 평균 : 0, 표준편차 : 1인 표준 정규를 띄는 배열
import numpy as np
array2 = np.random.normal(0, 1, (3,3))
print(array2)

# 행 변환
# 1. vector를 matrix(행렬)로 변환
import numpy as np

array1 = np.array([1, 2, 3, 4])
array2 = array1.reshape((2,2))

print(array2)

# 2. matrix를 다른 형상의 matrix로 변환
import numpy as np

A = np.arange(15)
print(A)

A = np.arange(15).reshape(3, 5)
print(A)

A = np.arange(30).reshape(2, 3, 5)
print(A)
print(A[0][1][3])