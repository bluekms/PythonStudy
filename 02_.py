stones = [5, 3, 4, 1, 3, 8, 3]
dogs = [{
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


def run(stones, dogs):
    answer = []
    for dog in dogs:
        current = 0
        while True:
            current += int(dog['점프력'])
            if(len(stones) < current):
                answer.append(dog['이름'])
                break
            stones[current - 1] -= int(dog['몸무게'])
            if stones[current - 1] < 0:
                break
    return answer


print(run(stones, dogs))
