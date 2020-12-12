'''
파이썬 데이터 모델
Magic Method(Special Method)는 클래스 안에 정의할 수 있는 특별한(built-in) 메소드를 의미
'''

# 기본형 - 모든 데이터 타입은 "class"이다.
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

# 매직 매소드 사용
n = 10
print(n +100)
print(n.__add__(100))
print(n.__bool__())
print()
print(n*1000)
print(n.__mul__(1000))

print()
print()

# 클래스 예제1
class Fruit():
    def __init__(self, name, price):
        self._name = name
        self._price =price

    def __str__(self):
        return 'Fruit Info : {} / {}'.format(self._name, self._price)

    def __add__(self, x):
        return self._price + x._price

    def __sub__(self, other):
        return self._price - other._price

# 인스턴스 생성
s1 = Fruit('Orange', 1000)
s2 = Fruit('Apple', 700)
s3 = Fruit('Banana', 500)

print(s1)
print(s2)
print(Fruit.__add__(s1, s2))
print(s1 + s2)
print(s1 - s2)














