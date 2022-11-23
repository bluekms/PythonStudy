import math

def solution(a, b, n):
    answer = 0
    while n > b:
        quotient = math.floor(n / a)
        if quotient == 0:
            return answer
        remain = n % a
        answer += quotient * b
        n = quotient * b + remain
    return answer

#print(solution(2,1,20))
#print(solution(3,1,20))
print(solution(3,2,20))

#000 000 000 000 000 000 00
#000 000 000 000 00
#000 000 000 0
#000 000 0
#000 00
#000 0
#000
#00