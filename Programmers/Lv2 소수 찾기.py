import itertools

def solution(numbers):
    answer = 0
    nPr = []
    valueArray = []
    for i in range(1, len(numbers) + 1):
        nPr.extend(list(itertools.permutations(list(numbers), i)))
        
    for arr in nPr:
        val = int(''.join(arr))
        if (val in valueArray) == False:
            valueArray.append(val)
    print(valueArray)
    
    for value in valueArray:
        if isPrime(value):
            answer += 1
            
    return answer

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False  
    return True

#print(solution("17"))       # 3
#print(solution("011"))      # 2
print(solution("011"))