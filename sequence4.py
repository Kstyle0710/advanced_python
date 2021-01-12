'''Immutable Dict 생성, 지능형 Set 등'''

## Immutable Dict

from types import MappingProxyType

d = {'key1' : 'value1'}   # 수정되면 안되는 중요한 딕셔너리라면...

# read Only
d_frozen = MappingProxyType(d)
print(d, id(d))
print(d_frozen, id(d_frozen))

## 수정 가능
d['key2'] = 'val2'
print(d, id(d))

## 수정 불가
# d_frozen['key2'] = 'val2'
# print(d_frozen, id(d_frozen))  # 수정 불가하여 에러 발생

## Set
s1 ={'Apple', 'Orange', 'Apple', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Kiwi'])
s3 = {3}
s4 = set()   # not {}
s5 = frozenset(s1)   # Read Only 처리

s1.add('Melon')
print(s1)

# 추가 불가
# s5.add("Melon")
# print(s5)

## 선언 최적화
## 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis
print("-"*10)
print(dis('{10}'))   # 3단계로 실행
print("-"*10)
print(dis('set([10])'))   # 5단계로 실행

# 지능형 집합
print("-"*10)

print({chr(i) for i in range(0, 256)})

from unicodedata import name
print({name(chr(i), '') for i in range(0, 256)})











