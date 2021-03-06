import json
돌의내구도 = [1, 2, 1, 4]
독 = [{
    "이름": "루비독",
    "나이": "95년생",
    "점프력": "3",
    "몸무게": "4",
}, {
    "이름": "피치독",
    "나이": "95년생",
    "점프력": "3",
    "몸무게": "3",
}, {
    "이름": "씨-독",
    "나이": "72년생",
    "점프력": "2",
    "몸무게": "1",
}, {
    "이름": "코볼독",
    "나이": "59년생",
    "점프력": "1",
    "몸무게": "1",
},
]


def 징검다리를건너라(돌의내구도, 독):
    answer = [i['이름'] for i in 독]
    return answer


print(징검다리를건너라(돌의내구도.copy(), 독.copy()))


def 징검다리를건너라(돌의내구도, 독):
    answer = [i['이름'] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도) - 1:
            독의위치 += int(i['점프력'])
            돌의내구도[독의위치 - 1] -= int(i['몸무게'])
            if 돌의내구도[독의위치-1] < 0:
                answer[answer.index(i['이름'])] = 'fail'
                break
    return [i for i in answer if i != 'fail']


print(징검다리를건너라(돌의내구도.copy(), 독.copy()))


# remove O(N)
# del O(1)
def 징검다리를건너라(돌의내구도, 독):
    answer = [i['이름'] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도) - 1:
            독의위치 += int(i['점프력'])
            돌의내구도[독의위치 - 1] -= int(i['몸무게'])
            if 돌의내구도[독의위치-1] < 0:
                del answer[answer.index(i['이름'])]
                break
    return answer


print(징검다리를건너라(돌의내구도.copy(), 독.copy()))


돌의내구도 = [5, 3, 4, 1, 3, 8, 3]


def 징검다리를건너라(돌의내구도, 독):
    answer = [i['이름'] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도) - 1:
            독의위치 += int(i['점프력'])
            돌의내구도[독의위치 - 1] -= int(i['몸무게'])
            if 돌의내구도[독의위치-1] < 0:
                del answer[answer.index(i['이름'])]
                break
    return answer


print(징검다리를건너라(돌의내구도.copy(), 독.copy()))


JSON독 = json.dumps(독, ensure_ascii=False)
print(JSON독[:10])

JSON독 = json.loads(JSON독)
print(JSON독[0])
print(독[0])
