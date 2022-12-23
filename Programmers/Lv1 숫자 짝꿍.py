def solution(X, Y):
    answer = []
    dictX = {}
    dictY = {}
    for c in X: dictX[c] = dictX.get(c, 0) + 1
    for c in Y: dictY[c] = dictY.get(c, 0) + 1
    for c in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']:
        if c in dictX.keys() and c in dictY.keys():
            answer += c * min(dictX[c], dictY[c])
    if len(answer) == 0: return '-1'            
    if len(answer) == answer.count('0'): return '0'
    return ''.join(answer)

def solution5(X, Y):
    answer = ''
    charList = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
    dictX = {}
    dictY = {}
    for i in charList:
        dictX[i] = 0
        dictY[i] = 0
    for c in X: dictX[c] += 1
    for c in Y: dictY[c] += 1
    for i in charList:
        if dictX[i] > 0 and dictY[i] > 0:
            answer += i * min(dictX[i], dictY[i])
    if answer == '': return '-1'            
    if int(answer) == 0: return '0'
    return answer

def solution4(X, Y):
    answer = ''
    for i in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']:
        cntX = X.count(i)
        cntY = Y.count(i)
        if cntX > 0 and cntY > 0:
            answer += i * min(cntX, cntY)
    if answer == '': return '-1'            
    if int(answer) == 0: return '0'
    return answer

def solution3(X, Y):
    answer = ''
    dictX = {}
    dictY = {}
    for i in range(9, -1, -1):
        i = str(i)
        dictX[i] = 0
        dictY[i] = 0
    for c in X:
        dictX[c] += 1
    for c in Y:
        dictY[c] += 1
    for i in range(9, -1, -1):
        i = str(i)
        if dictX[i] > 0 and dictY[i] > 0:
            for n in range(min(dictX[i], dictY[i])):
                answer += i
    if answer == '': return '-1'            
    if int(answer) == 0: return '0'
    return answer

def solution2(X, Y):
    answer = ''
    X = list(X)
    Y = list(Y)
    for i in range(9, -1, -1):
        i = str(i)
        cntX = X.count(i)
        cntY = Y.count(i)
        if cntX > 0 and cntY > 0:
            for c in range(min(cntX, cntY)):
                answer += i
    
    if answer == '': return '-1'            
    if int(answer) == 0: return '0'
    return answer

#print(solution("100", "2345"))
#print(solution("100", "203045"))
#print(solution("100", "123450"))
#print(solution("12321", "42531"))
print(solution("5525", "1255"))