# ==============================
# 지능형 리스트 (압축된 리스트)
# ==============================
l = [i for i in range(10)]
# print(l)

# for i in range(2, 10):
#     for j in range(1, 10):
#         print("{} X {} = {}".format(i, j, i * j))

gugudan = [
    # 출력물
    # for문
    # 안쪽 for문
    "{} X {} = {}".format(i, j, i * j)
    for i in range(2, 10)
    for j in range(1, 10)
]
# print(gugudan)

# ==============================
# 다중인자 리스트 순회 (언패킹)
# ==============================
l = [(1, 10), (2, 20), (3, 30), (4, 40)]
print(l[2][1])  # 30
for i, j in l:
    print(i, j)

# ==============================
# enumerate
#   넘버링
#   순위
# ==============================
print(list(enumerate(range(100, 1000, 100), 1)))
for i in enumerate(range(100, 1000, 100), 1):
    print(i)

# ==============================
# pass 유사 TODO
# ==============================
for i in range(10):
    pass
    print("hello world")
