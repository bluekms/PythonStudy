# 반복문 : Bottom-up. 작은 문제에서 출발
# 재귀함수 : top-down. 큰 문제에서 출발. 종료조건 필수!

x = 0
n = 100

# 반복문
for i in range(1, n + 1):
    x += i

# 시그마공식
x = n * (n + 1) // 2

# 재귀함수
def foo(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n + foo(n - 1)

def console():
    if input('## ') == 'exit':
        return
    if input('## ') == 'hi':
        print('hello world')
    console()

# 2진수 변환 반복문
def mybin(x: int) -> str:
    result = '';
    while True:
        if x % 2 == 0:
            result += '0'
        else:
            result += '1'
        x //= 2
        if x == 1:
            result += '1'
            return result[::-1]

# 2진수 변환 재귀함수
def mybin2(x: int) -> str:
    if x < 2:
        return str(x)
    else:
        return str(mybin2(x // 2)) + str(x % 2)

# 피보나치 반복문
def myfibo(first: int, next: int, count: int):
    print(first)
    for i in range(count):
        print(next)
        first, next = next, first + next

# 피보나치 재귀함수
def myfibo2(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return myfibo2(n - 1) + myfibo2(n - 2)

# sum 반복문
from typing import List
def mysum(arr: List[int]):
    sum = 0
    for i in arr:
        sum += i
    print(sum)

# sum 재귀함수
def mysum2(arr: List[int]) -> int:
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + mysum2(arr[1:])

# pow 반복문
def mypow(n: int, e: int) -> int:
    result = 1
    for i in range(e):
        result *= n
    return result

# pow 재귀함수
def mypow2(n: int, e: int) -> int:
    if e == 1:
        return n
    else:
        return n * mypow2(n, e - 1)

# 최대공약수 유클리드 호제법
# ref: https://wikidocs.net/21759

def comma(s: str) -> str:
    if len(s) < 3:
        return s
    else:
        # s[len(s) - 3:] 전체 길이의 3칸 앞부터 끝까지 (:)
        # ',' 앞에다 , 추가
        # comma(s[:len(s) - 3]) 재귀함수 호출로 저음부터 len(s) - 3 까지
        return comma(s[:len(s) - 3]) + ',' + s[len(s) - 3:]

print(comma('10000000'))