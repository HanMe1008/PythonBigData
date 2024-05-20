"""
l =([1, 2, 3],
    [4, 5, 6],
    [7, 8, 9])

import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array(([1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]))

C = np.array(l)

print(A)
print()
print(B)
print()
print(C)

D = np.array([ [[1,2,3,4], [1,2,3,4], [1,2,3,4]],
               [[1,2,3,4], [1,2,3,4], [1,2,3,4]],
               [[1,2,3,4], [1,2,3,4], [1,2,3,4]],
               [[1,2,3,4], [1,2,3,4], [1,2,3,4]] ])

print(D)
print(D.ndim)
print(D.shape)
print()

array1 = np.array([1, 2, 3, 4])
print(array1)
print()
array1 = array1.reshape(2, 2)
print(array1)
"""
"""
import numpy as np

a = np.array(range(1, 16, 1)).reshape(3, 5)
b = np.array(range(-1, -6, -1)).reshape(1, 5)

A = np.concatenate((a, b), axis = 0)
print(A)
print()

idx_row = [2, 3, 0]
idx_col = [2, 1, 3]

what_i_want = A[idx_row, idx_col]
print(what_i_want)


for i in range(-99, 0, 1):
    print(i, end = " ")
print()

for i in range(-1, -100, -1):
    print(i, end = " ")
"""

"""
fact = 1
for i in range(1, 50+1):
    fact *= i
print(fact)
"""
"""
for i in range(2, 10):
    for j in range(1, 10):
        print("{}*{} = {:2d}".format(i, j, i*j), end = " ")

print()

for i in range(8):
    print(' ' * (7 - i), '#')
"""
"""
for i in range(1, 5+1):
    print(' ' * (5 - i), '+' * (2 * i - 1))
"""
"""
sosus = []
for i in range(2, 100+1):
    is_sosu = True
    for j in range(2, i):
        if i % j == 0:
            is_sosu = False

    if is_sosu == True:
        sosus.append(i)

print(sosus)    
"""
"""
def get_sum(a, b):
    result = a + b + c
    return result

c = 5
X = get_sum(2, 3)
print(X)
"""
"""
pi = 3.14
radius = 10
def circle_area_circum(radius):
    area = radius**2 * pi
    circum = 2 * pi * radius
    return area, circum

area, circum = circle_area_circum(radius)
print("반지름이 {}인 원의 면적은 {:.1f}, 원의 둘레는 {:.1f}".format(radius, area, circum))
"""
"""
def multiples(n, m):
    tup=()
    for i in range(1, m+1):
        tup = tup + (i*n, )
    return tup

r1, r2, r3, r4 = multiples(3, 4)
print(r1, r2, r3, r4)

r1, r2, r3, r4, r5 = multiples(2, 5)
print(r1, r2, r3, r4, r5)
"""
"""
def sum_nums(*numbers):
    total = 0
    for n in numbers:
        total += n
    mean = total / len(numbers)
    return print("{} 개의 인자 {}\n합계 : {} , 평균 : {:.1f}".format(len(numbers), numbers, total, mean))

sum_nums(10, 20, 30)
print()
sum_nums(10, 20, 30, 40, 50)
"""
"""
def min_nums(*numbers):
    return print("최소값은 {}".format(min(numbers)))
min_nums(20, 40, 50, 10)
"""
"""
name = input("당신의 이름을 입력해주세요 : ")
age = input('나이를 입력해주세요. : ')
job = input('직업을 입력해주세요. : ')
region = input('사는 곳을 입력해 주세요. : ')
print("당신의 이름은 {}, 나이는 {}살, 직업은 {}, 사는 곳은 {}입니다.".format(name, age, job, region))
print()
print("당신의 이름은", name, ", 나이는", age, "살, 직업은", job, ", 사는 곳은", region, "입니다.")
"""
"""
s = 'My favorite thing is monsters.'
t = s.replace('monsters', 'cartoons')
print(t)

s = '_'.join('ABCD')
print(s)
"""
"""
even_list = list(range(2, 10+1, 2))
print(even_list)

string = list('ABC')
print(string)
"""
"""
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print(nations)
nations.append('Nepal')
print(nations)

if 'Japan' in nations:
    print("Japan 는(은) 국가 목록에 있습니다.")
else:
    print("Japan 는(은) 국가 목록에 없습니다.")

if 'Russia' in nations:
    print("Russia 는(은) 국가 목록에 있습니다.")
else:
    print("Russia 는(은) 국가 목록에 없습니다.")
"""
"""
a = [1, 2, 3]
b = [10, 20, 30]
a.append(b)
print(a)

a = [1, 2, 3]
b = [10, 20, 30]
a.extend(b)
print(a)
"""
"""
nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nlist.insert(0, 0)
print(nlist)

nlist.reverse()
print("마지막 원소 = {}".format(nlist.pop()))
print(nlist)
"""

# print([1, 2, 3] * int(input("반복할 정소를 입력하시오 : ")))
"""
s_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(s_list[:5])
print(s_list[5:11])
print(s_list[11:15])
print(s_list[2:11:2])
print(s_list[10:5:-1])
print(s_list[10:1:-2])
"""
"""
capital_dic = {'Korea' : 'Seoul', 'China' : 'Beijing', 'USA' : 'Washington DC'}
print(capital_dic['Korea'])
"""
"""
fruits_dic = {'apple' : 5000, 'banana' : 4000, 'grape' : 5300, 'melon' : 6500}
for fruit in fruits_dic:
    print("{0}의 가격은 {1}입니다.".format(fruit, fruits_dic[fruit]))
"""
"""
class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.korean_quiz = korean_quiz
        self.math_quiz = math_quiz
        self.science_quiz = science_quiz
        
    
    def __str__(self):
        return print("이름: {}, 학번: {}\n국어성적: {}, 수학성적: {}, 과학성적: {}\n합계: {}, 평균:{}".format(self.name,self.student_id,self.korean_quiz,self.math_quiz,self.science_quiz,self.total_score,self.avg_score)
        
 
    
    def get_name(self):
        return self.name
    def get_student_id(self):
        return self.student_id
    def get_korean_quiz(self):
        return self.korean_quiz
    def get_math_quiz(self):   
        return self.math_quiz
    def get_science_quiz(self):
        return self.science_quiz
    def get_total_score(self):
        self.total_score = self.korean_quiz + self.math_quiz + self.science_quiz
        return self.total_score
    def get_avg_score(self):
        self.avg_score = self.total_score / 3
        return self.avg_score
                     
    def set_korean_quiz(self, value):
        self.korean_quiz = value
    def set_math_quiz(self,value):
        self.math_quiz = value
    def set_science_quiz(self, value):
        self.science_quiz = value
    
    



name = input("학생의 이름을 입력하세요: ")
student_id = int(input("학생의 학번을 입력하세요: "))

student = Student(name, student_id)

korean_quiz = int(input("학생의 국어성적을 입력하세요: "))
math_quiz = int(input("학생의 수학성적을 입력하세요: "))
science_quiz = int(input("학생의 과학성적을 입력하세요: "))
student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)
student.get_total_score()
student.get_avg_score()
                     
print(student)
"""
"""
import numpy as np
A = np.array([2, 3, 3, 2])
B = A.reshape(2, 2)
print(B)
print(np.linalg.inv(B))
"""






