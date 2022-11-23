words = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    answer = 0
    for b in babbling:
        if Check(b, ""):
            answer += 1
    return answer

def Check(b, before):
    if b == "":
        return True
    for w in words:
        if w == before:
            continue
        else:
            if b[0:len(w)] == w:
                return Check(b[len(w):len(b)], w)
    return False

def solution2(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa", "wooyemawooye"]))

print(solution2(["wooyemawooye"]))