from collections import Counter

def solution(participant, completion):
    part = Counter(participant)
    comp = Counter(completion)
    
    for runner in part:
        if part[runner] != comp[runner]:
            return runner

print(solution(["leo", "kiki", "eden"], 	["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
#print(solution())