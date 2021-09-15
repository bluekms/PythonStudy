from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(11, y=22)
print(p.x + p.y)
print(p[0] + p[1])

# unpacking
i, j = p
print(i + j)

p.count(200)  # 해당 아이템의 수 반환
p.index(100)  # 해당 아이템의 인덱스 반환
p._replace(x=1000)  # 새 namedtuple 생성
p._asdict()  # {'x': 11, 'y': 22}
p._fields  # ('x', 'y')

기술명세 = namedtuple("기술", ["기술이름", "자격증", "연차"])
강민석 = 기술명세("파이썬", "정보처리기사", 8)
print(강민석)
