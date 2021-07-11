# 9:00 25
# 9:10 15
# 9:20 15
# 9:30 15
# 9:40 15
# 9:50 15
# 1시간마다 100명
# 9시 ~ 21시 전
# 1일마다 12시간 1200명 수송

waiting = 14000605
# waiting = 1200202
# waiting = 1
daysPerMonth = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]
manPerHour = [25, 15, 15, 15, 15, 15]


def solution(n: int):
    remain = n
    year = 0
    month = 0
    day = 0
    hour = 0
    minute = 0

    # 년
    totalDaysPerYear = 0
    for i in daysPerMonth:
        totalDaysPerYear += i

    year = n // (totalDaysPerYear * 100 * 12)
    remain = n % (totalDaysPerYear * 100 * 12)

    # 월
    for i in daysPerMonth:
        if remain < (i * 100 * 12):
            month = daysPerMonth.index(i)
            break
        remain -= i * 100 * 12

    # 일
    for i in range(0, daysPerMonth[month]):
        day += 1
        if remain < (100 * 12):
            break
        remain -= 100 * 12

    # 시
    for i in range(9, 21):
        if remain < 100:
            hour = i
            break
        remain -= 100

    for i in manPerHour:
        if remain < i:
            minute = manPerHour.index(i) * 10
            break
        remain -= i

    if minute * 2 > 60:
        hour += 1
        minute -= 60

    return f"{year + 2020}년 {month + 1}월 {day}일 {hour}시 {minute}분 출발"


print(solution(waiting))
