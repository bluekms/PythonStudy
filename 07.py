cross = [[[3, 0, 1, 1, 8],
		  [5, 0, 4, 5, 4],
		  [1, 5, 0, 5, 1],
		  [1, 2, 1, 0, 1],
		  [0, 2, 5, 1, 1]],
		 [[1, 2, 0, 3, 3],
		  [1, 2, 0, 2, 4],
		  [1, 2, 0, 2, 4],
		  [4, 2, 0, 0, 1],
		  [8, 4, 1, 1, 0]]]

c = cross[0] + cross[1]
# print(cross_[0])
# print(cross_[0][4])

# for i in range(len(cross_)):
# 	for j in range(4, -1, -1):
# 		print(i, j, cross_[i][j])

c_ = [[3, 0, 1, 1, 8],
	 [5, 0, 4, 5, 4],
	 [1, 5, 0, 5, 1],
	 [1, 2, 1, 0, 1],
	 [8, 2, 5, 1, 1]]

가중치누적값 = [[0 for i in range(len(c[0]))] for j in range(len(c))]
좌표저장 = [[[0, 0] for i in range(len(c[0]))] for j in range(len(c))]

for i in range(len(c)):
    for j in range(4, -1, -1):
        if i == 0 and j == 4:
            가중치누적값[0][4] = c[0][4]
            좌표저장[i][j] = [99, 99]
        elif i == 0:
            가중치누적값[i][j] = 가중치누적값[i][j + 1] + c[i][j]
            좌표저장[i][j] = [i, j + 1]
        elif j == 4:
            가중치누적값[i][j] = 가중치누적값[i - 1][j] + c[i][j]
            좌표저장[i][j] = [i - 1, j]
        else:
            # 가중치누적값[i][j] = min(가중치누적값[i][j - 1], 가중치누적값[i - 1][j]) + c[i][j]
            if 가중치누적값[i][j + 1] > 가중치누적값[i - 1][j]:
                가중치누적값[i][j] = 가중치누적값[i - 1][j] + c[i][j]
                좌표저장[i][j] = [i - 1, j]
            else:
                가중치누적값[i][j] = 가중치누적값[i][j + 1] + c[i][j]
                좌표저장[i][j] = [i, j + 1]

# print(c, 가중치누적값)
print(좌표저장)