첫번째밭 = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
]

두번째밭 = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 3],
    [0, 0, 0, 0, 4],
    [0, 2, 0, 0, 2],
    [4, 5, 0, 2, 0],
]

# [[None, None, None, None, None],
#  [None, None, None, None, None],
#  [None, None, None, None, None],
#  [None, None, None, None, None],
#  [None, None, None, None, None]]
# x = [[None] * 5] * 5
# print(x)

# 주의) 배열 요소의 주소값이 같다
# [[1000, None, None, None, None],
#  [1000, None, None, None, None],
#  [1000, None, None, None, None],
#  [1000, None, None, None, None],
#  [1000, None, None, None, None]]
# x[0][0] = 1000
# print(x)

# 90도 뒤집기
## 0, 4 -> 0, 0
## 1, 4 -> 0, 1
## 2, 4 -> 0, 2
## 3, 4 -> 0, 3
## 4, 4 -> 0, 4

## 0, 3 -> 1, 0
## 1, 3 -> 1, 1
## 2, 3 -> 1, 2
## 3, 3 -> 1, 3
## 4, 3 -> 1, 4

## 0, 2 -> 2, 0
## 1, 2 -> 2, 1
## 2, 2 -> 2, 2
## 3, 2 -> 2, 3
## 4, 2 -> 2, 4

## 0, 1 -> 3, 0
## 1, 1 -> 3, 1
## 2, 1 -> 3, 2
## 3, 1 -> 3, 3
## 4, 1 -> 3, 4

## 0, 0 -> 4, 0
## 1, 0 -> 4, 1
## 2, 0 -> 4, 2
## 3, 0 -> 4, 3
## 4, 0 -> 4, 4

sample = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

for i in range(len(두번째밭)):
    for j in range(len(두번째밭[0])):
        sample[i][j] = 두번째밭[j][len(두번째밭) - 1 - i]

print(sample)

for i in range(len(두번째밭)):
    for j in range(len(두번째밭[0])):
        sample[i][j] += 첫번째밭[i][j]