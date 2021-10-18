from collections import defaultdict

# 키가 호출되면 기본값이 들어있음
d = defaultdict(str)
d["one"] = "1"
d["two"] = "2"
d["three"]
print(d)

# 특히 리스트의 경우 여러개의 중복값을 저장하기 위한 용도로 사용
cource = [
    ("인스타그램클론", 1123),
    ("정규표현식", 23),
    ("MBTI페이지만들기", 1313),
    ("python부트캠프", 312),
    ("눈떠보니코딩테스트전날", 1623),
]

d = defaultdict(list)
for study, studentCount in cource:
    if studentCount < 100:
        d["10"].append(study)
    elif studentCount < 1000:
        d["100"].append(study)
    elif studentCount < 10000:
        d["1000"].append(study)

print(d)
