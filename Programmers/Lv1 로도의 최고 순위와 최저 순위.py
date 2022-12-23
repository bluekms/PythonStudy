def solution(lottos, win_nums):
    count = 0
    zero = 0
    for i in lottos:
        if i == 0:
            zero += 1
        elif i in win_nums:
            count += 1
    maxValue = min(6 - (count + zero) + 1, 6)
    minValue = min(6 - count + 1, 6)
    answer = [maxValue, minValue]
    return answer

print(solution([1,2,3,4,5,6], [7,8,9,10,11,12]))
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))

# 등수: 6 - 맞은 갯수 + 1