s1 = [1, 2, 3, 4, 5]
s2 = [2, 1, 2, 3, 2, 4, 2, 5]
s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    scores = {1:0, 2:0, 3:0}
    for i in range(0, len(answers)):
        if s1[i%len(s1)] == answers[i]:
            scores[1] += 1
        if s2[i%len(s2)] == answers[i]:
            scores[2] += 1
        if s3[i%len(s3)] == answers[i]:
            scores[3] += 1
    
    list = sorted(scores.items(), key = lambda item: item[1], reverse = True)
    max = 0
    answer = [] 
    for pair in list:
        if max == 0:
            max = pair[1]
            answer.append(pair[0])
        else:
            if max == pair[1]:
                answer.append(pair[0])
    return answer

print(solution([3, 3, 2, 1, 5])) #[3]
print(solution([5, 5, 4, 2, 3])) #[1,2,3]