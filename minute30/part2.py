# ==============================
# list [ ]
#   임의접근 가능 [N]
#   값 변경 가능
# ==============================
l = [100, 200, 300, 400]
print(l)
print(type(l))
# print(dir(l))

l[2] = 1000
l.append(300)  # 마지막에 원소 추가
l.count(300)  # 300인 원소의 수를 반환
l.extend([100, 200, 300])  # AddRange
l.index(300)  # 먼저 찾아진 값의 인덱스 반환
l.insert(3, 1000)
l.pop()  # 마지막 값을 꺼냄
l.pop(2)  # 해당 index의 값을 꺼냄
l.remove(100)  # 처음 나오는 100을 삭제
l.reverse()  # 뒤집는다
l.sort()  # 해당 list를 뒤집는다

# ==============================
# tuple ( )
#   임의접근 가능 [N]
#   값(포인터) 변경 불가능
# ==============================
t = (100, 200, 300)
print(t)
print(type(t))
# print(dir(t))

# t[1] = 1000   # err 변경 불가능
l = [10, 20]
t = (l, 200, 300)
l[0] = 10000
t[0][1] = 999

# ==============================
# set { }
#   임의 접근 불가능
#   중복을 허용하지 않음
# ==============================
s = {100, 200, 300, 300, 300}
print(s)
print(type(s))
# print(dir(s))

s.add(500)
set("aabbcccddefggg")  # 캐스팅 시 중복제거가 됨
ss = {1, 2, 3}
s.union(ss)  # 합집합

# ==============================
# dictionary {key:value}
#   임의 접근 불가능
#   키 중복을 허용하지 않음
# ==============================
d = {"one": 10, "two": 20}
print(d)
print(type(d))
# print(dir(d))

d["one"]
# print(d["onee"])  # err
d.keys()
d.values()
d.items()  # list[ ] 안에 tuple( )로 반환
list(d.items())[0][1]  # list로 캐스팅 하여 임의접근

jeju = {"banana": 5000, "orange": 2000}
seoul = jeju.copy()  # 딮카피
jeju["orange"] = 10000
print(seoul)
