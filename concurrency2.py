'''
Generator 실습
Yield 실습
Itertools 실습
'''

# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행

## Generator Ex1 : 제너레이터 함수를 만들고 만들어진 함수를 다시 iter, next 함수로 실행

def generator_ex1():
    print('Start')
    yield 'A Point'    # A Point만 return 해주고 "기억하고" 멈춘다.
    print('Continue')
    yield 'B Point'
    print('End')

temp = iter(generator_ex1())
# print(temp)
# print(next(temp))
# print(next(temp))


# for v in generator_ex1():
#     print(v)

## Generator Ex2
# temp2 = [x * 3 for x in generator_ex1()]     # dtype : class 'list'
# temp3 = (x * 3 for x in generator_ex1())     # dtype : class 'generator'

# print(type(temp2))
# print(temp2)
# print(type(temp3))
# print(temp3)

## Generator Ex3 (중요 함수)
### count, takewhile, filterfalse, accumulate, chain, product, groupby...

### 무한대로 숫자를 만들어보고 싶다면..
import itertools
# gen1 = itertools.count(1, 2.5)    # (시작수, 증가단위) 끝없이 증가한다.
# print(dir(gen1))
# print(hasattr(gen1, '__next__'))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))

### 조건 (필터)
# print("-"*30)
#
# gen2 = itertools.takewhile(lambda x : x < 1000, itertools.count(1, 2.5))
# print(gen2)
# for v in gen2:
#     print(v)
#
# print("-"*30)

# 필터의 반대
# gen3 = itertools.filterfalse(lambda x : x < 3, [1, 2, 3, 4, 5])  # 역필터이므로 3 4, 5가 저장
# for i in gen3:
#     print(i)

# print("-"*30)

# 누적 합계
# gen4 = itertools.accumulate([x for x in range(1, 10)])
# for i in gen4:
#     print(i)
#
# print("-"*30)

# 연결 1 (두개의 리스트를 하나로 합치기)
# gen5 = itertools.chain('ABCDE', range(1, 11, 2))
# print(gen5)
# print(list(gen5))    # list로 형변환후 출력

# print("-"*30)

# 연결 2
# gen6 = itertools.chain(enumerate('ABCDE'))
# print(gen6)
# print(list(gen6))
# ls = list(gen6)
# print(hasattr(ls, '__iter__'))
# print(type(ls))
# print(len(ls))
#
# for x in ls:
#     print(x)

# print("-"*30)

# 개별1 (개별로 튜플로 반환)
# gen7 = itertools.product('ABCDE')
# print(list(gen7))

# print("-"*30)

# 연산(경우의 수)
# gen8 = itertools.product('ABCDE', repeat=2)
# print(list(gen8))

# print("-"*30)

# 그룹화
# gen9 = itertools.groupby('AAABBBCCCDEEE')
# print(list(gen9))    # 가독성이 안좋다. for로 까보자
# print("-"*10)
# for chr, group in gen9:  ## 위의 print(list(gen9))를 주석처리 해야 한다.
#     print(chr)
#     print(list(group))
























