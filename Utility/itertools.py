# 알고리즘 통계에서 많이 사용
# izip, imap, islice, ifilter -> 성능향상

import re  # 정규표현식
import math
import numpy
import pandas
import collections
import functools
import itertools

# count
for c, s in zip(itertools.count(0, 0.5), "abc"):
    print(f"{c}, {s}")

# cycle
for c, s in zip(itertools.cycle(range(3)), "abcdef"):
    print(f"{c}, {s}")

print(pow(2, 3))
# 8

print(list(map(pow, range(10), [2, 2, 2, 2])))
print(list(map(pow, range(10), itertools.repeat(2))))
# 2의 승수

print(list(itertools.repeat("abc", 3)))
# ['abc', 'abc', 'abc']

# groupby
# g를 그냥 출력하면 itertools._grouper의 주소값만 나옴
print([k for k, g in itertools.groupby("AAAABBBCCDAABBB")])
print([list(g) for k, g in itertools.groupby("AAAABBBCCDAABBB")])

expenditure = [
    ("호준", 1000000),
    ("호중", 100000),
    ("길동", 300000),
    ("호준", 100000),
    ("길동", 10000),
    ("길동", 10000),
]

# 정렬되어 있지 않으면 묶이지 않는다
expenditure = sorted(expenditure, key=lambda x: x[0])
print(list(itertools.groupby(expenditure)))

# 지출액 더하기
for name, total in itertools.groupby(expenditure, lambda x: x[0]):
    print(f"{name} : {[i for i in total]}")

for name, total in itertools.groupby(expenditure, lambda x: x[0]):
    print(f"{name} : {sum([i[1] for i in total])}")

# dropwhile
# 조건이 false인 것부터 순회 (반, takewhile)
print(list(filter(lambda x: x <= 5, range(10))))
print(list(itertools.takewhile(lambda x: x <= 5, range(10))))
print(list(itertools.dropwhile(lambda x: x <= 5, range(10))))

# tee
# 한번만 참조된다
a, b = itertools.tee(range(10), 2)
print(list(a))
print(list(b))
print(list(a))
print(list(b))

# zip_longest
print(list(zip("ABCD", "xy")))
print(itertools.zip_longest("ABCD", "xy", fillvalue="-"))

# 순열과 조합
print(list(itertools.product("ABC", repeat=2)))
print(list(itertools.permutations("ABC", 2)))
print(list(itertools.combinations("ABC", 2)))
print(list(itertools.combinations_with_replacement("ABC", 2)))
