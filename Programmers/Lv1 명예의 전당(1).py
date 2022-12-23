def solution(k, score):
    answer = []
    rankingScore = []
    for s in score:
        if len(rankingScore) < k:
            rankingScore.append(s)
            answer.append(min(rankingScore))
        else:
            rankingScore.append(s)
            rankingScore.remove(min(rankingScore))
            answer.append(min(rankingScore))
    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))