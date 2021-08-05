# ==============================
# list
#   append : 리스트 끝에 포인터 1개 추가
#   extend : 리스트 끝에 모든 원소 추가
#   copy : 깊은 복사
#   count : 해당 원소 수 반환
#   index : 리스트 값의 index 반환 (없으면 throw)
#   insert(a, b) : a위치에 b원소 삽입
#   pop : 지정한 위치의 원소를 꺼냄 (삭제됨)
#   remove : 원소 삭제 (처음 발견된것 하나)
# ==============================
x = [1, 2, 3, 4]
x.append([3, 4])
x.extend([3, 4])
y = x.copy()
x.count(3)
x.index(2)
x.insert(2, 999)
x.remove(2)


# ==============================
# format
# ==============================
format(1000000, ",")
format(1000000, "e")
format(100000, "x")  # 186a0 (str)
hex(100000)  # 0x186a0 (str)
format(100000, "0>20,.4f")  # 0으로 체움, 우측정렬, 총20자, 콤마, 소숫점4자리
format(100000, "9<20,.4f")  # 9로 체움, 좌측정렬, 20자, 콤마, 소숫점4자리
format(100000, "7=20,.4f")  # 7로 체움, 중앙정렬, 20자, 콤마, 소숫점4자리
format(100000, "7^20,.4f")  # 상동


# ==============================
# filter : 함수가 True를 반환하는 요소를 출력
# map : 함수의 결과를 출력
# ==============================
def foo(value):
    if value % 2 == 0:
        return True
    else:
        return False


list(filter(foo, range(20)))
list(map(foo, range(20)))
list(filter(lambda x: 2 % 2 == 0, range(20)))
list(map(lambda x: x ** 2, range(20)))


# ==============================
# zip
#   가장 짧은 요소를 기준으로 튜플의 리스트를 반환
# ==============================
list(zip(["a", "b", "c", "d"], [1, 2, 3, 4], [10, 20, 30, 40], "ABC"))
set(zip(["a", "a", "c", "d"], [1, 2, 3, 4], [10, 20, 30, 40], "ABCD"))
set(zip(["a", "a", "c", "d"], [1, 1, 3, 4], [10, 10, 30, 40], "AACD"))


# ==============================
# min, max
# ==============================
x = {8: 1, 3: 9, -2: 1, 10: -1}
res = max(x)  # key가 가장 큰 요소의 key를 출력 (10)
res = max(x, key=lambda k: x[k])  # value가 가장 큰 요소의 key를 출력 (3)
x[res]  # value가 가장 큰 요소의 value를 출력


# ==============================
# sort : 리스트의 원본을 직접 정렬
# sorted : 정렬된 리스트를 반환
# lambda를 사용해 dictionary 정렬 가능
# ==============================
x = [1, 3, 2, 5]
x.sort()
sorted(x)

test1 = ["abc", "def", "hello world", "hello", "python"]
sorted(test1, key=len, reverse=True)
# ['hello world', 'python', 'hello', 'abc', 'def']
# 길이순, 역방향 정렬

test2 = "Life is too short, You need python".split()
sorted(test2, key=str.lower)
# ['is', 'Life', 'need', 'python', 'short,', 'too', 'You']
# 대소문자 구별 없이 알파벳으로 정렬

test3 = list(zip("anvfe", [1, 2, 5, 4, 3]))
sorted(test3, key=lambda x: x[1])
# [('a', 1), ('n', 2), ('e', 3), ('f', 4), ('v', 5)]
# x[1]은 list
# list의 순서로 정렬된 내용을 반환

sorted(test3, key=lambda x: x[0])
# [('a', 1), ('e', 3), ('f', 4), ('n', 2), ('v', 5)]
# x[0]은 str
# 문자열의 순서대로 정렬된 내용을 반환

# ==============================
# in, not in
# ==============================
5 in [1, 2, 3, 4, 5]  # True
5 not in [1, 2, 3, 4, 5]  # False


# ==============================
# reverse : 리스트 원본을 직접 뒤집음
# reversed : 뒤집힌 리스트를 반환
# ==============================
x.reverse()
reversed(x)


# ==============================
# queue
# ==============================
l = []
l.append(10)
l.append(20)
l.append(30)
l.pop(0)


import queue

q = queue.Queue()
q.put(10)
q.put(20)
q.put(30)
q.get()


class ListQueue:
    def __init__(self):
        self.queue = []

    def push(self, n):
        return self.queue.append(n)

    def pop(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)

    def printq(self):
        print(self.queue)

    def empty(self):
        if len(self.queue) == 0:
            return True
        return False


q = ListQueue()
q.push(10)
q.push(20)
q.push(30)
q.pop()


# ==============================
# stack
# ==============================
l = []
l.append(10)
l.append(20)
l.append(30)
l.pop()


class ListStack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        return self.stack.append(n)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def prints(self):
        print(self.stack)

    def empty(self):
        if len(self.stack) == 0:
            return True
        return False


s = ListStack()
s.push(10)
s.push(20)
s.push(30)
s.pop()

d = {"one": "하나", "two": "둘"}
d.keys()  # 키의 리스트
d.values()  # 값의 리스트
d.items()  # 튜플의 리스트


# ==============================
# set p.30
# ==============================
s = {3, 1, 1, 2, 2, 4, 5}
s.add(7)
s.discard(7)
1 in s
