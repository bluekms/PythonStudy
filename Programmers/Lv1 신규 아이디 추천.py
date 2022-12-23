def solution(new_id):
    new_id = new_id.lower()
    new_id = RemoveSpecialChar(new_id)
    new_id = RemoveDots(new_id)
    if new_id == '': new_id = 'a'
    if len(new_id) >= 16: new_id = new_id[0:15]
    if len(new_id) > 0 and new_id[len(new_id) - 1] == '.': new_id = new_id[0:len(new_id)-1]
    while len(new_id) <= 2:
        new_id += new_id[len(new_id) - 1]
    return new_id

def RemoveSpecialChar(id):
    specialCharList = "~!@#$%^&*()=+[{]}:?,<>/"
    for c in specialCharList:
        id = id.replace(c, '')
    return id

def RemoveDots(id):
    arr = []
    for i in range(0, len(id)):
        if i == 0:
            arr.append(id[i])
        else:
            if id[i] == '.':
                if arr[len(arr) - 1] != '.':
                    arr.append(id[i])
            else:
                arr.append(id[i])
            
    if len(arr) > 0 and arr[0] == '.':
        arr.pop(0)
        
    if len(arr) > 0 and arr[len(arr) - 1] == '.':
        arr.pop()
        
    return "".join(arr)

#print(solution("...!@BaT#*..y.abcdefghijklm"))  # "bat.y.abcdefghi"
#print(solution("z-+.^."))                       # "z--"
#print(solution("=.="))                          # "aaa"
#print(solution("123_.def"))                     # "123_.def"
print(solution("abcdefghijklmn.p"))             # "abcdefghijklmn"
#print(solution())


"""
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
    
https://velog.io/@ash3767/python-%EC%A0%95%EA%B7%9C%EC%8B%9D

import re
re.sub(타겟, 변환, 문자열)
^           시작
$           종료
[문자열]    이것들
[^문자열]   나머지들
|           or
?           없거나 하나
+           하나 이상
*           없거나 하나 이상
패턴{n}     패턴이 n번 \d{3}
패턴{n,m}   패턴이 n~5개 \d{3,5}
\d          숫자
\w          문자
\s          화이트 스페이스 [\t\n\r\f]
.           \n을 제외한 모든 문자 .{3} 3글자
"""