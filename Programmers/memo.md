# numpy

# Where

# 정규식
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

Lv1 신규 아이디 추천.py

# Counter
* Lv1 완주하지 못한 선수


# 소수 찾기
```
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False  
    return True
```