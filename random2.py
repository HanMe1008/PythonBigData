# 중간범위 X
import numpy as np

# 0~1 사이의 random number 발생
np.random.seed(7)       # 시드가 같으면 난수가 변하지 않는다
print(np.random.randint(0, 10, (2, 3)))
