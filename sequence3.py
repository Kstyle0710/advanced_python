'''
hashtable
Dict 생성 고급 예제
Setdefault 사용법
'''

## hashtable (key에 value를 저장하는 구조 + 키 값의 연산 결과에 따라 직접 접근이 가능한 구조)

## Dict 구조
# print(__builtins__.__dict__)

## hash 값 확인

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2))   # 에러 발생- 리스트는 mutable이라 hash 값이 없다

## Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print(new_dict2)



