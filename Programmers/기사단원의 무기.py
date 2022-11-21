def solution(number, limit, power):
    divisors = []
    for i in range(1, number + 1):
        divisors.append(len(GetDivisor(i)))
    
    answer = 0
    for i in divisors:
        if i > limit:
            answer += power
        else:
            answer += i
    return answer

def GetDivisor(n):
    front = []
    back = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            front.append(i)
            if i != n // i:
                back.append(n // i)
    return front + back[::-1]