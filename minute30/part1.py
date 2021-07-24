a = 10
b = 10.1
c = 'hello world'
d = -1
e = 'kang'
f = 'minseok'
g = 10 + 2j         #복소수 complex
h = 0b1001
i = 0o1001
j = 0o1001
print(h)
print(type(g))
# print(dir(a))

strValue = '01234567890123456789'
print('01: ' + strValue[0])          # 인덱스
print('02: ' + strValue[3:10])       # 인덱싱 n부터 m - 1까지
print('03: ' + strValue[3:20:2])     # n부터 m - 1까지 2개씩 건너뛰면서
print('04: ' + strValue[3:20:3])     # n부터 m - 1까지 3개씩 건너뛰면서
print('05: ' + strValue[10:0:-1])    # n부터 m까지 역순으로 마지막 원소 포함 안함