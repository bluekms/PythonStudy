from collections import Counter

a = [1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 8]
c = Counter(a)
print(c)

for i in c:
    print(i)
    print("---")

for i in c.elements():
    print(i)
    print("---")

# 쓰기 편함
for i, j in c.items():
    print(i, j)

# print(c.keys())
# print(c.values())
# print(c.items())

# tuple의 list로 반환
print(c.most_common())

s = "hello, world"
sc = Counter(s)
print(sc)

# 요소를 뒤에 추가한것과 같은 결과
# hello, worldhello
sc.update("hello")
print(sc)

# h가 -1이 됨
# sc.subtract(Counter("hello"))
sc.subtract("hello")
sc.subtract("hello")
sc.subtract("hello")
print(sc)

# one가 100개인 것으로 출력
d = {"one": 100, "two": 200, "three": 200}
s = Counter(d)
print(s)

# dict에서 쓸 때는 의미에 주의
d = {"one": "100", "two": "200", "three": "200"}
s = Counter(d)
print(s)
