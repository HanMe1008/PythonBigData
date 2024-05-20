import numpy as np

# 넘파이 랜덤 추출 모듈 : np.random 함수 정리
# rand, random : 0~1 사이 균일 분포 추출 함수
# np.random.rand() : 값 1개가 추출
# np.random.rand(D) : 해당 dimension을 가진 넘파이 array가 생성
# ex) np.random.rand(5, 3)
# np.random.random 함수 : 원하는 차원의 형태를 튜플 자료형
# ex) np.random.random((5,3))

data = np.random.randint(1000, size=50)
print(data)

print(max(data),
      np.argmax(data),
      sep = '\n')

print('최대값= ', format(max(data)),
      '최대값 위치= ', format(np.argmax(data)),
      sep = '\n')