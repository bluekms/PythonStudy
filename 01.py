# ord() : 문자 -> 숫자 ordinal value
# chr() : 숫자 -> 문자 character
# map(f, e) : 지정된 함수로 e를 처리
# zip (a, b) : 튜플로 묶어준다

text = ['   + -- + - + -   ',
'   + --- + - +   ',
'   + -- + - + -   ',
'   + - + - + - +   ']

# 2진수
for i in text:
    print(int(i.strip().replace(' ', '').replace('+', "1").replace('-', '0'), 2))

I = []
for i in text:
    I.append(chr(int(i.strip().replace(' ', '').replace('+', "1").replace('-', '0'), 2)))
print(''.join(I))

# 한줄로
''.join([chr(int(i.strip().replace(' ', '').replace('+', "1").replace('-', '0'), 2)) for i in text])

# 짝수만
for i in range(10):
    if i % 2 == 0:
        print(i)

# 짝수만 한줄로
print([i for i in range(10) if i % 2 == 0])

# 구구단 한줄로
print([f'{i} X {j} = {i*j}' for i in range(2, 10) for j in range(1, 10)])

# 자릿수 맞추기
print('111'.zfill(10))

# 함수를 사용한 풀이
s = [i.strip().replace(' ', '').replace('+', "1").replace('-', '0') for i in text]
print(s)

# 람다 사용
print(''.join(list(map(lambda x : chr(int(x, 2)), s))))

# 함수 사용
def f(x):
    return chr(int(x, 2))

print(''.join(list(map(f, s))))