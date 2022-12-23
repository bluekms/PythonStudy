import itertools

# 순열은 타임오버
def solution2(numbers):
    nPr = list(itertools.permutations(numbers, len(numbers)))
    numbers = []
    for array in nPr:
        numbers.append(int("".join(list(map(str, array)))))
    return str(max(numbers))

# 원소가 0부터 1000이니까 4자리로 늘려서 내림차순 정렬한 뒤 붙여준다
def solution(numbers):
    answer = ''
    sum_ = 0
    tmp = []
    for number in numbers:
        c = (str(number) * 4)[:4]
        length = len(str(number))
        tmp.append((c, length))
    tmp.sort(reverse=True)
    for (c, length) in tmp:
        sum_ += int(c)
        if sum_ == 0:
            return '0'
        answer += c[:length]
    return answer

#print(solution([6, 10, 2]))     # 6210
#print(solution([3, 30, 34, 5, 9])) # 9534330
print(solution([1, 11, 110])) # 111110