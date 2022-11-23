def Split(arr, n):
    for i in range(0, len(arr), n):
        yield arr[i:i + n]

def solution(k, m, score):
    list.sort(score, reverse=True)
    boxes = Split(score, m)
    answer = 0
    for i in boxes:
        if len(i) < m:
            break
        answer += min(i) * m
    return answer

#print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))