'''
futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
지연시간 (BLOCK) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
'''

'''
concurrent.futures
  1) 멀티스레딩/멀티프로세싱 API 통일 -> 사용하기 쉬움
  2) 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> promise 개념
'''
'''
GIL (global interpreter lock)
 두개 이상의 스레드가 동시에 실행될 때 하나의 자원을 동시에 액세스하는 경우 -> 문제 방지하기 위해 
 GIL  실행, 리소스 전체에 락이 걸린다. -> context switch (문맥교환) 
 
 GIL 우회 : 멀티프로세싱 사용, Cpython 사용
'''

## 2가지 패턴 실습
### concurrent.futures 사용법1 : map (본 파일 작성 부분)
### concurrent.futures 사용법2

import os
import time
from concurrent import futures

WORK_LIST = [10000, 100000, 1000000, 10000000]   # 여기 워크리스트에 함수 등 다른 것을 담아서 동시성 작업 응용 가능

# 동시성 함계 계산 메인 함수 - 누적 합계 함수(제너레이터)
## 개별 함수 정의
def sum_generator(n):
    return sum(n for n in range(1, n+1))

## 메인함수 정의
def main():
    # worker count
    worker = min(10, len(WORK_LIST))
    # 시작 시간
    st_time = time.time()
    # 결과건수
    # ProcessPoolExcutor
    with futures.ThreadPoolExecutor() as excutor:
        result = excutor.map(sum_generator, WORK_LIST)
        ## map 함수는 work 대상중에 한시간 짜리가 있으면 한시간 기다렸다가 모두의 결과를 반환 (그래서 다음 수업의 wait 개념 필요)
    # 종료후 걸린 시간
    ed_time = time.time()-st_time
    # 출력포맷
    msg = '\n Result -> {} Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(list(result), ed_time))

## 실행
if __name__ == '__main__':
    main()

















