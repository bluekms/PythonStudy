import numpy

# numpy where 사용법 https://pinkwink.kr/1236

def solution(N, stages):
    failureRate = {}
    stages = numpy.array(stages)
    for s in range(1, N + 1):
        curr = len(numpy.where(stages == s)[0])
        total = len(numpy.where(stages >= s)[0])
        if total > 0:
            failureRate.update({s : curr / total})
        else:
            failureRate.update({s:0})
    answer = dict(sorted(failureRate.items(), reverse=True, key=lambda item: item[1]))
    return list(answer.keys())

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))