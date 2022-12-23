import itertools

def solution(nums):
    answer = 0
    cr = list(itertools.combinations(nums, 3))
    for arr in cr:
        if IsPrime(sum(arr)):  
            answer += 1
    return answer

def IsPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  
    return True

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))