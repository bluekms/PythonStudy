# import
* from typing import Dict, List, Tuple
* import json
* import datetime
* import numpy as np
    * np.rot90(array, 반시계방향_횟수)
    * np.array(ARRAY) 사칙연산 가능 (+-*/, @ 행렬의 곱)

<br>
<br>
<br>

# 연산자
** : 
거듭제곱

// : 
나누기 후 소숫점 버림
<br>
<br>
<br>

# 날짜
import datetime
* curr = datetime.datetime.today()
* curr.year
* curr.month
* curr.day
* curr.hour
* curr.minute
* curr.second
* curr.microsecond
```
시간 = 1
분 = 1
print(f{시간:0>2}:{분:0>2})
01:01
```
```
import datetime
today = datetime.datetime.now()
print(f'today:%Y-%m-%d-%A')
```
<br>
<br>
<br>

# 함수
ord() : 
문자 -> 숫자 ordinal value

chr() : 
숫자 -> 문자 character

strip() :
문자열 공백 제거

map(f, e) :
지정된 함수로 e를 처리

zip (a, b) :
튜플로 묶어준다

json.dumps(JSON, ensure_ascii=False) :
json -> 문자열

json.loads(JSONSTR) : 
문자열 -> json

array.index(N) : 
배열에 인덱스로 접근 array[N] 안됨

bin(n), oct(n), hex(n) :
진수 구하기

format(n, ',') :
3자리마다 쉼표 추가
<br>
<br>
<br>
# 컨테이너 관련 함수

str[2:] :
2번째부터 끝까지

str[::-1] :
역순으로

len(arr) :
배열 길이를 구한다

remove :
O(N)

del :
O(1)

list.append(item) : 
뒤에 item 추가

list.pop(N) : 
N번 요소를 꺼냄
<br>
<br>

## 배열의 숫자를 영어로 바꾸기
```
for i in array

chr(i) for i in array

''.join([chr(i) for i in array])

# str(num)은 캐스팅
```

## 임의 배열 초기화
```
arr = [[0 for i in range(col)] for i in range(row)]
arr = [[[0, 0] for i in range(col)] for j in range(row)]
```

## f string
```
print(f'{"kms":<10}')       # KMS
print(f'{"kms":>10}')       #        KSM
print(f'{"kms":~^10}')      # ~~~kms~~~~
print(f"{3.141592:0.2f}")   # 3.1
print(f"{3.141592:0.2}")    # 3.14
```
<br>
<br>
<br>
# collections
https://docs.python.org/3.11/library/collections.html

## namedtuple
명명된 필드를 가지는 튜플클래스 생성

## deque
양 끝에서 추가와 삭제

## ChainMap
여러개의 컨테이너를 묶을 수 있음

## Counter
구성요소의 수를 셈

## OrderedDict
순서있는 Dict

## defaultdict
키가 없을 때 기본값

## UserDict
Dict를 만드는 부모클래스

## UserList
List를 만드는 부모클래스

## UserString
String을 만드는 부모클래스

<br>
<br>
<br>
# 정적 타입 선언
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=passion053&logNo=221070020739