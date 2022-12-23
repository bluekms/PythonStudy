leftNums = [1,4,7,10]
rightNums = [3,6,9,12]

def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for i in numbers:
        if i in leftNums:
            answer += 'L'
            left = i
        elif i in rightNums:
            answer += 'R'
            right = i
        else:
            lDistance = GetDistance(left, i)
            rDistance = GetDistance(right, i)
            if lDistance < rDistance:
                answer += 'L'
                left = i
            elif lDistance > rDistance:
                answer += 'R'
                right = i
            else:
                if hand == "left":
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    right = i
    return answer

def GetDistance(src, dst):
    distance = 0
    if src in leftNums:
        distance += 1
        src += 1
    elif src in rightNums:
        distance += 1
        src -= 1
    if src == 0:
        src = 11
    if dst == 0:
        dst = 11
    return int(abs(dst - src) / 3) + distance

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")) # LRLLLRLLRRL
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))  # LRLLRRLLLRR
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))    # LLRLLRLLRL
#print(solution())

"""
 1  2  3
 4  5  6
 7  8  9
10 11 12
"""