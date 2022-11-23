import random

def solution(ingredient):
    s = []
    answer = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1,2,3,1]:
            answer += 1
            for i in range(4):
                s.pop()
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
print(solution([1,1,1,2,3,1,2,3,1,2,3,1,2,3,1]))

arr = []
for i in range(0, 1000000):
    arr.append(random.randint(1,3))
    
print(solution(arr))