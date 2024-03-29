from itertools import combinations

def solution(number):
    answer = 0
    per = combinations(number, 3)
    for p in per:
        if sum(p) == 0:
            answer += 1
    return answer

print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))