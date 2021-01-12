'''
시퀀스 형태
- 컨테이너 : 서로다른 자료형 포함 가능 (list, tuple, collection.deque)
- 플랫(Flat) : 한개이 자료형만 포함 (str, bytes, bytearray, array.array)

- 가변형 : list, array..array, bitearray, deque, memoryview
- 불별형 : tuple, str, bytes

리스트 및 튜플 고급 학습
'''

# 일반 반복문 형태
chars = '+_)(*&^%$#@'   # Flat의 str(불변형)  중간에 뭘 밀어넣거나 바꿀 수 없다.
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))   # ord는 문자의 유니코드 출력 함수
print(code_list1)

## # 지능형 리스트 (lists Comprehension)
code_list2 = [ord(s) for s in chars]
print(code_list2)

## comprehending list + map + filter  ########################
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

code_list4 = list(filter(lambda x : x >40, map(ord, chars)))
print(code_list4)

###
# Generator 생성 (한번에 한개의 항목을 생성.. 메모리에 로드한다.)
import array    # array는 flat형(하나의 자료형)이면서 가변형이다.

### 종전의 방식
tuple_g = [ord(s) for s in chars]
print(tuple_g)

### generator 사용 방식  (bracket를 parenthesis로 변경)
tuple_g = (ord(s) for s in chars)   # 리스트 항목중 첫번째인 43을 반환할 준비만 하고 있는 상태
print(tuple_g)
print(type(tuple_g))
print(next(tuple_g))   # next를 통해 단계적인 호출이 가능
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

array_g = array.array('I', (ord(s) for s in chars))
print(array_g)
print(type(array_g))
print(array_g.tolist())

### 리스트 주의 사항 (깊은 복사, 얕은 복사) ##################
mark1 = [['~']*3 for _ in range(4)]
print(mark1)
print(type(mark1))

mark2 = [['~']*3]*4
print(mark2)
print(type(mark2))   # 타입 자체는 똑같은 리스트이다.

## 값을 수정해본다면...
mark1[0][1]='x'
mark2[0][1]='x'

print(mark1)
print(mark2)  # 그러나 모든 소속 리스트의 1위치 값이 변경되었다.

## 증명
print([id(s) for s in mark1])
print([id(s) for s in mark2])   # 4개의 아이디가 모두 같다.

