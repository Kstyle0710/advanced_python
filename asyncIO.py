# pip install asyncio
# pip install beautifulsoup4

'''
AsuncIO : 비동기 I/O Coroutine 작업을 쉽게 할 수 있도록 만들어 놓은 라이브러리

Blocking I/O : 호출된 함수가 자신의 작업이 완료될 때까지 제어권을 가지고 있음. 타 함수는 대기
NonBlocking I/O : 호출된 함수(서브루틴)가 return후 호출한 함수(메인루틴)에 제어권 전달 -> 타 함수는 일 지속
'''

import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
from bs4 import BeautifulSoup

## 실행 시작 시간
start = timeit.default_timer()

## 서비스 방향이 비슷한 사이트로 실습 권장 : 게시판성 커뮤니티
urls = ['http://daum.net', 'https://naver.com', 'https://tistory.com']


async def fetch(url, executor):
    # 스레드 이름 호출
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url)
    # 실행
    res = await loop.run_in_executor(executor, urlopen, url) # urlopen이 block함수이기때문에 여기서 nonblock으로 변경

    # parsing 해주기
    soup = BeautifulSoup(res.read(), 'html.parser')

    # 전체 페이지 소스 확인
    # print(soup.prettify())

    result_data = soup.title

    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)

    # 결과 반환
    return result_data #res.read()[0:10]

async def main():
    # 스레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather 에서 실행
    futures =[
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # 결과 취함
    rst = await asyncio.gather(*futures)   # *는 unpacking 의미

    print()
    print('Result : ', rst)


if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer()-start
    # 총 실행시간
    print('Total Running Time : ', duration)























