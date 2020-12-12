'''
Magic Method(Special Method) 심화
'''

# 클래스 예제2 (수학벡터 관련 커스터마이징된 클래스를 만들어보자)
class Vector(object):
    def __init__(self, *args):
        '''
        Create a vector, example : v = vector(5, 10)
        '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''return the vector information'''
        return 'Vector(%r, %r)' %(self._x, self._y)

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        return Vector(self._x * other._x, self._y * other._y)

    def __bool__(self):
        return bool(max(self._x, self._y))

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# doc 출력
print(Vector.__repr__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(v1 * v2)
print(bool(v3))
















