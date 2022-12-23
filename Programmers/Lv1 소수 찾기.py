def solution(n):
    answer = 1
    for i in range(3, n + 1):
        if IsPrimeNumber(i):
            answer += 1
    return answer

def IsPrimeNumber(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(solution(1000000))