import math

def solution(food):
    answer = []
    for i in range(1, len(food)):
        for j in range(0, math.floor(food[i]/2)):
            answer.append(i)
    food2 = answer[::-1]
    answer.append(0)
    for i in food2:
        answer.append(i)    
    return ''.join(str(e) for e in answer)

print(solution([1,3,4,6]))