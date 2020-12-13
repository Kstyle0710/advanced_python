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
### concurrent.futures 사용법1  : map
### concurrent.futures 사용법2  : wait , as_completed (본 파일 작성 부분)

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

WORK_LIST = [100000, 1000000, 10000000, 100000000]  # 여기 워크리스트에 함수 등 다른 것을 담아서 동시성 작업 응용 가능


# 동시성 함계 계산 메인 함수 - 누적 합계 함수(제너레이터)
## 개별 함수 정의
def sum_generator(n):
    return sum(n for n in range(1, n + 1))

## 메인함수 정의
def main():
    # worker count
    worker = min(10, len(WORK_LIST))
    # 시작 시간
    st_time = time.time()
    # futures를 받는 변수 선언
    futures_list = []
    # 결과건수
    # ProcessPoolExecutor  or ThreadPoolExecutor
    with ProcessPoolExecutor() as excutor:
        for work in WORK_LIST:
            # not 실행 but Future만 반환
            future = excutor.submit(sum_generator, work)
            # 스케쥴링
            futures_list.append(future)
            # 스케쥴링 확인
            print('Scheduled for {} : {}'.format(work, future))
            print()

        # ## Wait 결과 출력
        # result = wait(futures_list, timeout=5)  ### 기다리는 시간 지정 가능
        # # 성공 출력
        # print('Completed Task : ' + str(result.done))
        # # 실패 출력
        # print('Failure Tast : ' + str(result.not_done))
        # # 결과값 출력
        # print([future.result() for future in result.done])

        ## as_completed 결과 출력
        for future in as_completed(futures_list):   ## 먼저 처리되는게 먼저 결과로 반환된다.
            result = future.result()
            done = future.done()
            cancelled = future.cancelled()

            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))


    # 종료후 걸린 시간
    ed_time = time.time() - st_time
    # 출력포맷
    msg = '\n Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(ed_time))

## 실행
if __name__ == '__main__':
    main()

















