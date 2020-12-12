'''
병행성(Concurrency)
Iterator, Generator

파이썬에서 반복 가능한 타입
: collections, text, list, dict, set, tuple, unpacking, *args...
'''

t = 'ABCDEFGHIJKLMNOP'
print(dir(t))   #__iter__ 속성이 있다.  (초보스러운 확인 방법)

# for c in t:
    # print(c)  # 반복 가능한 이유는 내부적으로 iter라는 함수가 호출되었다.

w = iter(t)    # iter는 반복함수
print(next(w))  # next는 하나씩 순차적으로 불러오는 함수
print(next(w))
print(next(w))

## 반복형 확인
print(hasattr(t, '__iter__'))   # has attribute의 약식 확인 함수

print("-"*30)

## next를 활용한 구현
class WordSplitter():
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")

    def __next__(self):
        print("Called __next__")
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stop Interation')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit({})'.format(self._text)

wi = WordSplitter("Hello My World and Hope you to enjoy")
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print("-"*30)

## Generator를 활용한 방법

class WordSplitGenerator():
    def __init__(self, text):
        self._text = text.split(" ")

    def __iter__(self):
        for word in self._text:
            yield word   ## 중요한 부분
        return

        def __repr__(self):
            return 'WordSplitGenerator({})'.format(self._text)

wg = WordSplitGenerator("Hello My World and Hope you to enjoy")
wt = iter(wg)

print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))


