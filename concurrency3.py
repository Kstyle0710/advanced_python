'''
병행성(Concurrency) - 코루틴(Coroutine)
코루틴 : 싱글 스레드에서 스택을 기반으로 동작하는 비동기 작업
코루틴 제어를 위해 Yield 키워드 사용 : 상태 저장 및 양방향 전송
yiedl <--> send를 통해 양방향 통신 가능
'''

## 코루틴 Ex1

def coroutine1():
    print('>>> coroutine started')
    i = yield
    print('>>> coroutine recieved : {}'.format(i))

# 제너레이터 선언
cr1 = coroutine1()
# print(cr1, type(cr1))

# yield 지점까지 서브루틴 수행
# next(cr1)
# next(cr1)
# 기본 전달 값은 None

# 지정 값 전송
# cr1.send(100)    ## 메인루틴과 서브루틴이 send를 통해 서로의 상태값 교환 가능

# 잘못된 사용 yield까지 next 없이 바로 send 수행시는?
cr2 = coroutine1()
# cr2.send(100)  ## 에러 발생


## 코루틴 Ex2 (상태값을 알 수 있다.)
'''
GEN_CREATED : 처음 대기 상태
GEN_RUNNING : 실행 상태
GEN_SUSPENDED : Yield 대기 상태 (중요 - send 사용 가능 상태)
GEN_CLOSED : 실행 완료 상태
'''

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x   ## 서브루틴의 x를 메인루틴의 y로 전달
    print('>>> coroutine recieved1 : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received2 : {}'.format(z))

# cr3 = coroutine2(10)
# print(next(cr3))   # 한줄 한줄 실행해 볼 것!!!
# cr3.send(100)
# cr3.send(100)

## 상태값 호출해보기
cr3 = coroutine2(10)

from inspect import getgeneratorstate

# print(getgeneratorstate(cr3))
# print(next(cr3))
# print(cr3.send(100))
# print(getgeneratorstate(cr3))
# cr3.send(100)
# print(cr3.send(100))
#
# print()
# print()


'''
python ^3.5 에서 def -> async, yield -> await로 변경 사용 가능 (StopIteration도 자동처리)
'''
## 중첩 코루틴 처리

def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 3):
        yield y

t1 = generator1()
# next는 4번까지 가능
# print(next(t1))  # A
# print(next(t1))  # B
# print(next(t1))  # 1
# print(next(t1))  # 2

## 더 간단히 표현

def generator2():
    yield from 'AB'
    yield from range(1, 3)

t3 = generator2()
# print(next(t3))
# print(next(t3))
# print(next(t3))
# print(next(t3))









