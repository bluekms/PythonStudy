def solution(n, lost, reserve):
    
    for i in range(1, n + 1):
        isLost = i in lost
        isReserve = i in reserve
        if isReserve == True and isLost == True:
            lost.remove(i)
            reserve.remove(i)
            
    answer = 0
    for i in range(1, n + 1):
        isLost = i in lost
        isReserve = i in reserve
        if isReserve == False and isLost == False:
            answer += 1
        elif isReserve == True and isLost == False:
            answer += 1
            if i - 1 in lost:
                answer += 1
                lost.remove(i - 1)
            elif i + 1 in lost:
                lost.remove(i + 1)
    return answer

print(solution(5, [2, 4], [1, 3, 5]))   # 5
print(solution(5, [2, 4], [3]))         # 4
print(solution(3, [3], [1]))            # 2
print(solution(4, [2,3], [3,4]))        # 3
print(solution(5, [4,2], [3,5]))        # 5
print(solution(6, [3,4,5], [3,4,6]))    # 5