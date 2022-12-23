def solution(id_list, report, k):
    reportDict = {}
    banCountDict = {}
    mailCountDict = {}
    
    for id in id_list:
        reportDict[id] = []
        banCountDict[id] = 0
        mailCountDict[id] = 0
        
    for ids in report:
        idArray = ids.split()
        if (idArray[1] in reportDict[idArray[0]]) == False:
            reportDict[idArray[0]].append(idArray[1])
            banCountDict[idArray[1]] += 1
    
    for id in id_list:
        if banCountDict[id] >= k:
            for reportId in reportDict.keys():
                    if id in reportDict[reportId]:
                        mailCountDict[reportId] += 1
    
    answer = []
    for id in id_list:
        answer.append(mailCountDict[id])
        
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))