def solution(s):
    dict = {}
    answer = []
    for i in range(0, len(s)):
        if s[i] in dict:
            distance = i - dict[s[i]]
            answer.append(distance)
            dict[s[i]] = i
        else:
            dict.update({s[i] : i})
            answer.append(-1)
    return answer

print(solution("banana"))
print(solution("foobar"))