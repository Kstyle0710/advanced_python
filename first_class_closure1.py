'''클로저 기초'''

## 파이썬의 변수 범위(Scope)

print("### ex1")
def func_v1(a):
    print(a)
    print(b)

# func_v1(10) # 에러 발생

print("### ex2")
b = 20  # global
def func_v2(a):
    print(a)
    print(b)
func_v2(10) # 정상 출력

print("### ex3")
c = 30
def func_v3(a):
    print(a)
    # print(c)
    c = 40
# func_v3(10) # 에러 발생

print("### ex4")
c = 30
def func_v4(a):
    c = 40
    print(a)
    print(c)

func_v4(10) # 정상 출력 (c=40)

print("### ex5")### ex5
c = 30
def func_v5(a):
    c = 40
    print(a)
    print(c)

print('>>', c)   # global에 있는 30이 출력
func_v5(10) # 정상 출력 (c=40)

print("### ex6")
c = 30
def func_v6(a):
    global c
    print(a)
    print(c)
    c = 40

print("### ex6")  # global에 있는 30이 출력
func_v6(10) # 정상 출력 (c=40)
print('>>>', c)  # 함수 실행후 c 값은 40

print("-"*20)
## Closure 사용 이유
'''
서버 프로그램의 가장 중요 이슈 -> 동시성 제어 -> 제한된 메모리에 여러 자원이 접근 -> 교착 상태
메모리를 공유하지 않고 메시지의 전달의 형태로 처리
클로저는 공유하되 변경되지 않음 (immutable, read only)
클로저는 불변 자료구조 및 멀티스레드 프로그래밍에 강점
'''

## 클래스로 예시 만들기
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, args):
        self._series.append(args)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

## 인스턴스 생성
averager_cls = Averager()
# print(dir(averager_cls))

# 누적
print(averager_cls(10))
print(averager_cls(30))  # 클래스 안에서 계산 결과를 series 리스트에 기억하면서 연속 계산을 실시함



