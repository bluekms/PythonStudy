def solution(board, moves):
    result = []
    for i in moves:
        index = i - 1
        for row in range(0, len(board[0])):
            if board[row][index] > 0:
                result.append(board[row][index])
                board[row][index] = 0
                break
    print(result)
    answer = 0
    while True:
        if TryRemove(result):
            answer += 2
        else:
            break
    return answer

def TryRemove(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            arr.pop(i - 1)
            arr.pop(i - 1)
            return True
    return False

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

"""
[0,0,0,0,0]
[0,0,1,0,3]
[0,2,5,0,1]
[4,2,4,4,2]
[3,5,1,3,1]

1: 4
[0,0,0,0,0]
[0,0,1,0,3]
[0,2,5,0,1]
[0,2,4,4,2]
[3,5,1,3,1]
"""