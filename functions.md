# import
* import json
* import datetime
<br>
<br>
<br>

# 연산자
## **
거듭제곱

## //
나누기 후 소숫점 버림
<br>
<br>
<br>

# 날짜
* 오늘시간 = datetime.datetime.today()
* print(오늘시간.year)
* print(오늘시간.month)
* print(오늘시간.day)
* print(오늘시간.hour)
* print(오늘시간.minute)
* print(오늘시간.second)
* print(오늘시간.microsecond)
```
시간 = 1
분 = 1
print(f{시간:0>2}:{분:0>2})
01:01
```
<br>
<br>
<br>

# 함수
## ord()
문자 -> 숫자 ordinal value

## chr()
숫자 -> 문자 character

## strip()
문자열 공백 제거

## map(f, e)
지정된 함수로 e를 처리

## zip (a, b)
튜플로 묶어준다

## len(arr)
배열 길이를 구한다

## remove
O(N)

## del
O(1)

## json.dumps(JSON, ensure_ascii=False)
json -> 문자열

## json.loads(JSONSTR)
문자열 -> json

## array.index(N)
배열에 인덱스로 접근 array[N] 안됨
<br>
<br>
<br>