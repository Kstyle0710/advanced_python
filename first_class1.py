'''
일급함수    함수형 프로그램을 만드는 기초
파이썬 함수의 특징
1. 런타임 초기화 (실행시점에)
2. (함수를) 변수로 할당 가능
3. 함수를 인수로 전달 가능
4. 함수를 결과로 반환 가능
'''

# 5! 함수로 만들기

def factorial(n):
    ''' Factorial Function -> n : int'''
    if n == 1:
        return 1
    return n*factorial(n-1)

class A:
    pass

print(factorial(5))
print(type(factorial), type(A))
print(dir(factorial))
print(factorial.__code__)

# 변수에 할당
var_func = factorial
print(var_func)
print(var_func(5))
print(list(map(var_func, range(1, 11))))
print("-"*10)

# 함수 인수 전달 및 함수로 결과 반환  -> 고위 함수 (higher-order function)
# map, filter, reduce 함수

print([var_func(i) for i in range(1, 6) if i % 2])
print("-"*5)

print(list(filter(lambda x : x % 2, range(1, 6))))   # 필터는 함수 조건이 참인 경우의 대입값만 반환
print(list(map(lambda x : x % 2, range(1, 6))))      # 맵은 그냥 순서대로 대입값들을 함수에 대입후 함수 계산값을 전부 반환
print("-"*5)

print(list(map(var_func, filter(lambda x : x % 2, range(1, 6)))))
print("-reduce -"*10)

# reduce   감소시키면서 누적한다.
print(sum(range(1, 11)))  # 1부터 10까지의 합

from functools import reduce
from operator import add
print(reduce(add, range(1, 11)))  # 후단의 리스트 대입값들을 순차로 앞단의 함수에 대입하면서 누적값을 계산


print("-lambda-"*10)

# 익명 함수 (lambda)
print(reduce(lambda x, t : x + t, range(1, 11)))
print("-"*10)


print("-Callable-"*10)
# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
print(callable(str), callable(list), callable(var_func), callable(A), callable(50))
# 50은 상수라서 __call__ attribute 가 없다.

print("-partial-"*10)
# partial 사용법 : 인수 고정 -> 콜백 함수에 사용
from operator import mul
from functools import partial

five = partial(mul, 5)
print(five(5))

six = partial(five, 6)
print(six())

# 5의 배수 구하기
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))








