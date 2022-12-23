def solution(n):
    answer = 0
    for c in list(str(n)):
        answer += int(c)
    return answer

print(solution(123))