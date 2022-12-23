def solution(n):
    answer = []
    for c in list(str(n))[::-1]:
        answer.append(int(c))
    return answer

print(solution(12345))