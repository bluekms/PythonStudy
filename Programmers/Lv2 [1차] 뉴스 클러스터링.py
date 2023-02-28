import re
import math

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1s = []
    str2s = []
    
    for i in range(0, len(str1)):
        if re.search("([a-z][a-z])", str1[i:i+2]):
            str1s.append(str1[i:i+2])
    
    for i in range(0, len(str2)):
        if re.search("([a-z][a-z])", str2[i:i+2]):
            str2s.append(str2[i:i+2])

    inter = []
    union = []
    
    if len(str1s) != len(set(str1s)) or len(str2s) != len(set(str2s)):
        strL = []
        strS = []
        if len(str1s) >= len(str2s):
            strL = str1s
            strS = str2s
        else:
            strL = str2s
            strS = str1s
        
        while len(strS) > 0:
            str = strS.pop(0)
            if str in strL:
                strL.pop(strL.index(str))
                inter.append(str)
            union.append(str)
        union = union + strL
    else:
        inter = set(str1s) & set(str2s)
        union = set(str1s) | set(str2s)    

    if len(union) == 0:
        return 1 * 65536
    else:
        return math.floor(len(inter) / len(union) * 65536)

#print(solution("FRANCE", "french"))
#print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
#print(solution("E=M*C^2", "e=m*c^2"))
#print(solution())

"""
aa1+aa2

aa
a1
1+
aa
a2

aa
aa

AAAA12
aaaa12

aa
aa
aa

A = {1, 1, 2, 2, 3}
B = {1, 2, 2, 4, 5}

1
A = {1, 2, 2, 3}
B = {1, 2, 2, 4, 5}
I = {1, }
U = {1, }

A ∩ B = {1, 2, 2}
A ∪ B = {1, 1, 2, 2, 3, 4, 5}
"""