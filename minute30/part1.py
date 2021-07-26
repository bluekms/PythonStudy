# ==============================
# 자료형
# ==============================
a = 10
b = 10.1
c = "hello world"
d = -1
e = "kang"
f = "minseok"
g = 10 + 2j  # 복소수 complex
h = 0b1001
i = 0o1001
j = 0o1001
print(h)
print(type(g))
# print(dir(a))

# ==============================
# 배열
# ==============================
strValue = "01234567890123456789"
print("01: " + strValue[0])  # 인덱스
print("02: " + strValue[3:10])  # 인덱싱 n부터 m - 1까지
print("03: " + strValue[3:20:2])  # n부터 m - 1까지 2개씩 건너뛰면서
print("04: " + strValue[3:20:3])  # n부터 m - 1까지 3개씩 건너뛰면서
print("05: " + strValue[10:0:-1])  # n부터 m + 1까지 역순으로
print("06: " + strValue[10:-1:-1])  # err
print("07: " + strValue[:10:2])  # 처음부터 10까지 2건너뛰면서
print("08: " + strValue[::2])  # 처음부터 끝가지 2건너뛰면서
print("09: " + strValue[::-1])  # 처음부터 끝까지 역순으로
print("10: " + strValue[-1])  # 마지막 값 인덱스

# ==============================
# 문자열
# ==============================
print(type(c))
# print(dir(c))  # _가 없는 메서드는 public 메서드
print(c.upper())
print(c.lower())
print(c.count("l"))  # l의 숫자를 카운트
print(c.strip())  # 공백제거. lstrip(), rstrip()
print(c.split(" "))
print("!".join(c.split(" ")))  # 사이에 !를 넣어서 합쳐줌
print("제 이름은 {}입니다. 저는 {}년생 입니다.".format("강민석", 86))
print("제 이름은 {1}입니다. 저는 {0}년생 입니다.".format("강민석", 86))
year = 2021
month = 7
day = 25
print(year, month, day, end=" ")  # end옵션은 \n 대신 들어간다
print(year, month, day, sep="/")  # sep 옵션은 사이사이에 넣는다

# ==============================
# 형변환
# ==============================
a = 10
b = "10"
print(a + int(b))
print(str(a) + b)

# ==============================
# bool타입과 형변환
# ==============================
a = True
b = False
print(type(a))
# print(dir(a))
print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # False
print(bool(" "))  # True
print(bool(1))  # True
print(bool(-1))  # True 0 제외한 다른 숫자는 전부 True

# ==============================
# 산술연산
# ==============================
a = 3
b = 10
print(a + b)
print(a - b)
print(b / a)  # 3.3333 (float)
print(b // a)  # 3 (int)
print(b * a)
print(b ** a)  # 1000 (b의 3승)
print(b % a)

# ==============================
# 논리연산
# ==============================
a = True  # 1
b = False  # 0
print(a and b)  # * 둘중 하나가 0이면 0
print(a or b)  # + 둘중 하나가 1이면 1
print(not b)  # 반대

# ==============================
# bit연산
# ==============================
a = 40
b = 14
print(bin(a)[2:].zfill(8))  # 0010 1000
print(bin(b)[2:].zfill(8))  # 0000 1110
print(a & b)  # 0000 1000   8
print(a | b)  # 0010 1110   46
print(~b)
print(" " + bin(b))
print(bin(~b))
