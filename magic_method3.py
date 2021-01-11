'''
Magic Method(Special Method) 심화3
객체 -> 파이썬의 데이터를 추상화
모든 객체 -> id,     type -> value
named tuple
'''

# 일반적인 튜플 연습 (피타코라스 정리)
pt1 = (1, 5)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
print(l_leng1)

# 네임드 튜플 사용
from collections import namedtuple

# declare named tuples
Point = namedtuple('Point', 'x, y')

pt3 = Point(1, 5)
pt4 = Point(2.5, 1.5)

print(pt3)
print(pt4)
print(pt3[0], pt4[0])
print(pt3.x, pt4.x)

l_leng2 = sqrt((pt3.x-pt4.x)**2 + (pt3.y-pt4.y)**2)
print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point1', ['x', 'y'])
Point2 = namedtuple('Point2', 'x, y')
Point3 = namedtuple('Point3', 'x y x class', rename=True)
print(Point1)
print(Point2)
print(Point3)

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(10, 20, 30, 40)

# 출력
print(p1)
print(p2)
print(p3)

# Dict to Unpacking
temp_dict = {'x':75, 'y':55}
p5 = Point2(**temp_dict)   # 딕셔너리 쌍별**은 언패킹.. 튜플은 홑별*
print(p5)

# unpacking
a, b = p2
print(a, b)

# named tuple method
## list ==> named tuple
temp_list = [52, 38]
p4 = Point1._make(temp_list)  #_make() 리스트를 네임드튜플에 맞게 언팩킹 (위에 딕셔너리 언팩킹은 쌍별이었다.)
print(p4)

## _fields : 필드 네임 확인 (키 값 조회시 활용)
print(p1._fields)

## _asdict : 네임드튜플을 Orderred Dict으로 반환
print(p1._asdict())

# Named Tuple 실 사용 실습
## 반 20명, 4개의 반 (A, B, C, D)

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 생성
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)

for s in students:
    print(s)

