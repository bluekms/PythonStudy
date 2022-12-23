def solution(t, p):
    answer = 0
    nP = int(p)
    for i in range(0, len(t) - (len(p) - 1)):
        last = min(i + len(p), len(t))
        value = int(t[i:last])
        if value <= nP:
            answer += 1
    return answer

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))