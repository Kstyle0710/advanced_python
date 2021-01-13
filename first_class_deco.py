'''
데코레이터의 장점
1. 중복 제거, 코드 간설, 공통함수 작성
2. 로깅, 프레임워크, 유효성 체크 -> 공통 기능
3. 장신구처럼 여기저기 조합해서 사용하기 좋다.

단점
1. 가독성이 떨어질 수 있다.
2. 특정 기능에 한정된 함수는 단일 함수로 작성이 더 낫다.
3. 디버깅 불편
'''



## 데코레이터 미사용시
import time

def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[{}] {}({}) -> {}'.format(et, name, arg_str, result))
        return result
    return perf_clocked

def time_func(second):
    time.sleep(second)

def sum_func(*nums):
    return sum(nums)

## 데코레이터 미사용

none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print("-"*10, 'Called None Decorator -> time_func')
print()
none_deco1(1.5)

print("-"*10, 'Called None Decorator -> sum_func')
none_deco2(100, 200, 300, 400, 500, 600)


## 데코레이터 사용시
@perf_clock
def time_func(second):
    time.sleep(second)
@perf_clock
def sum_func(*nums):
    return sum(nums)


none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print("-"*10, 'Called Decorator -> time_func')
time_func(1.5)

print("-"*10, 'Called Decorator -> sum_func')
sum_func(100, 200, 300, 400, 500, 600)

