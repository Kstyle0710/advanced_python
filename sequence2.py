## Tuple advanced
### unpacking

print(divmod(100, 9))
t = (100, 9)
print(divmod(*t))    # 튜플 앞에 별표 하나는 튜플 언팩킹  (참고로 딕셔너리 언팩킹은 별 두개)
print(*(divmod(100, 9)))

print("-"*5)

a, b = divmod(100, 9)
print(a)
print(b)

print("-"*5)

x, y, *rest = range(10)
print(x)
print(y)
print(rest)

print("-"*5)

x, y, *rest = range(2)
print(x)
print(y)
print(rest)

print("-"*5)

x, y, *rest = 1, 2, 3, 4, 5
print(x)
print(y)
print(rest)

print("-"*5)

## Mutable(가변형) vs, Immutable(불변형)

l = (15, 20, 25)
m = [15, 20, 25]
print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2
print(l, id(l))
print(m, id(m))  # 이 경우의 리스트는 id 값이 새로 할당된다.

print("-"*5)
l *= 2
m *= 2
print(l, id(l))
print(m, id(m))  # 이 경우의 리스트는 id 값이 종전과 동일하다.

print("-"*5)
## sort vs. sorted
## reverse, key=len, key=str.lower, key=func....

## sorted : 정렬 후 새로운 객체를 반환 (원본이 수정되지 않는다.)
f_list = ['orange', 'apple', 'banaba', 'lemon', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))   # 오름차순의 역순(내림차순)
print('sorted - ', sorted(f_list, key=len))   # 길이순 정렬
print('sorted - ', sorted(f_list, key = lambda x : x[-1]))  # 맨 마지막 글자를 기준을 정렬

print(f_list) # 원본은 안바뀐다.

print("-"*5)

## sort : 정렬후 객체 직접 변경 (원본이 수정된다.)
print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)  # 실행할 때마다 원본이 바뀐다.
print(f_list)   # 원본도 바뀌었다.





