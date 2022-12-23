def solution(dartResult):
    pointList = []
    numIndex = 0
    currIndex = 0
    
    for c in dartResult:
        pointIndex = len(pointList)
        if c.isdigit() == False:
            if c == 'S':
                num = int(dartResult[numIndex:currIndex])
                pointList.append(num)
                numIndex = currIndex + 1
            elif c == 'D':
                num = int(dartResult[numIndex:currIndex])
                pointList.append(num * num)
                numIndex = currIndex + 1
            elif c == 'T':
                num = int(dartResult[numIndex:currIndex])
                pointList.append(num * num * num)
                numIndex = currIndex + 1
            elif c == '*':
                if pointIndex == 1:
                    pointList[0] *= 2
                else:
                    pointList[pointIndex - 1] *= 2
                    pointList[pointIndex - 2] *= 2
                numIndex = currIndex + 1
            elif c == '#':
                pointList[pointIndex - 1] *= -1
                numIndex = currIndex + 1
        currIndex += 1
                    
    return sum(pointList)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))