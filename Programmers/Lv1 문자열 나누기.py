def solution(s):
    i = GetSplitIndex(s)
    answer = 1
    while i > 0:
        s = s[i + 1:len(s)]
        if len(s) == 0:
            break
        i = GetSplitIndex(s)
        answer += 1
    return answer

def GetSplitIndex(s):
    x = s[0]
    dict = {x:0, "ANOTHER": 0}
    i = 0
    for i in range(len(s)):
        c = s[i]
        if c == x:
            dict[x] += 1
        else:
            dict["ANOTHER"] += 1
        if dict[x] == dict["ANOTHER"]:
            return i
    return i

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))

"""
a
ab

r
ra

c
ca

d
da

b
br

a
"""