# 시험 준비물 : 노트북
# 문제수 : 4    (10점 - 2문제, 40점 - 2문제(+날개문제))
# 7주차 강의자료는 시험에 안나오지만 중요
# 해양환경데이터정보학은 손코딩? 시험
# reshape
# concatenate
# 40점 : 10점 * 4
# 6장을 잘할줄알아야함
# 행렬의 행 or 열 자유롭게 변환 (행&열 변환) - 40점
# Lms 과제란에 올리기
# 공개 시간 11:00, 제출 시간 12:00

import numpy as np
import csv

f = open('data.csv', 'r', encoding='UTF-8-sig')
rd = csv.reader(f)

for i in rd:
    print(i)
    print(type(i))
f.close()

