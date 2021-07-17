# pip install numpy
import numpy as np

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

결과 = np.rot90(두번째밭, 1) + np.array(첫번째밭)

[str(i) for i in 결과[0]]
''.join([str(i) for i in 결과[0]])

int(''.join([str(i) for i in 결과[0]]), 8)

for j in range(0, 5):
    value = int(''.join([str(i) for i in 결과[j]]), 8)
    if j == 0:
        print(value)
    else:
        print(chr(value))