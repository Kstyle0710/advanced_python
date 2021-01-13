'''
Closure : 외부에서 호출된 함수의 변수값, 상태 등을 복사후 저장
   -> 후에 접근 가능 (후에 이어서 볼 수 있게 하는 책깔피 같은 기능)
'''
## 전 수업에서 class로 구현한 Averager를 closure로 구현해보기

def closure_ex1():
    series = []  # free variable (클로저 영억)
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager    # 함수를 결과로 반환

avg_closure1 = closure_ex1()  # 이렇게 함수를 한번 실행해서 변수에 담고 변수에 담긴 상태에서 계산값을 줄 수 있다.

print(avg_closure1(10))
print(avg_closure1(20))
print(avg_closure1(50))
print("-"*10)

# function inspection
print(dir(avg_closure1))
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars)
print(dir(avg_closure1.__closure__))
print(avg_closure1.__closure__[0].cell_contents)

## 잘못된 클로저 사용의 예

def closure_ex2():
    # free variable
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10))   # 에러 발생

## 다시 정상 작동하게 수정해보기
def closure_ex3():
    # free variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total    # 상기 에러 함수에서 여기 추가
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()
print(avg_closure3(10))   # 정상 출력
print(avg_closure3(45))
print(avg_closure3(25))

