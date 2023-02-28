def solution(priorities, location):
    answer = 0
    
    while True:
    
        maxValue = max(priorities)
        firstValue = priorities.pop(0)
        
        if maxValue == firstValue:
            answer += 1
            if location == 0:
                break
            else:
                location = location - 1
        else:
            priorities.append(firstValue)
            if location == 0:
                location = len(priorities) - 1
            else:
                location = location - 1
                
    return answer
  

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))