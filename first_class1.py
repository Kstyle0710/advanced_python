'''
일급함수
파이썬 함수의 특징
1. 런타임 초기화
2. 변수 할당 가능
3. 함수 인수 전달 가능
4. 함수 결과 반환 가능
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
# 함수 인수 전달 및 함수로 결과 반환  -> 고위 함수 (high-order function)
# map, filter, reduce 함수

print([var_func(i) for i in range(1, 6) if i % 2])

print(list(filter(lambda x : x % 2, range(1, 6))))
print(list(map(var_func, filter(lambda x : x % 2, range(1, 6)))))
print("-"*10)

# reduce
print(sum(range(1, 11)))

from functools import reduce
from operator import add
print(reduce(add, range(1, 11)))
print("-"*10)

# 익명 함수 (lambda)
print(reduce(lambda x, t : x + t, range(1, 11)))
print("-"*10)

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
print(callable(str), callable(list), callable(var_func), callable(A), callable(50))
# 50은 상수라서 __call__ attribute 가 없다.


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








