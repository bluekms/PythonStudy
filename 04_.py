# 다리가 아픈 동물들이 순서대로 들어온다
# 무척추, 척추, 어류, 양서류, 파충류, 조류, 포유류
# 같은 종은 무릎 앉기 (1초)
# 회복되면 빠진다
# 아무도 없다면, 1분이 걸린다
# 자리가 꽉 차 있는데 다른 종이 들어올 경우, 가장 오랫동안 같은 종이 한 번도 들어오지 않은 종이 빠지면서 1분이 걸린다
# 동물이 다음 순으로 들어올 경우 전체 수행시간을 구하라
# LRU 자리가 없을 경우 가장 오랫동안 사용되지 않은 자리를 반환

# false 라면 0번째에 넣는다
# hit 라면 pop(0)를 해서 뒤에 넣는다 알고리즘이 쉬워진다
# 초만 필요하다면 굳이 변수를 두개 쓸 필요는 없다

from typing import List


def solution(동물: List[str], 자리: int) -> str:
    의자: List[str] = [] * 자리
    answer = 0

    for i in 동물:
        if len(의자) < 3:
            if i in 의자:
                히트된페이지 = 의자.pop(의자.index(i))
                의자.append(히트된페이지)
                answer += 1
            else:
                의자.append(i)
                answer += 60
        else:
            if i in 의자:
                히트된페이지 = 의자.pop(의자.index(i))
                의자.append(히트된페이지)
                answer += 1
            else:
                의자.pop(0)
                의자.append(i)
                answer += 60

    return f"{answer // 60}분 {answer % 60}초"


동물 = ["척추동물", "어류", "척추동물", "무척추동물", "파충류", "척추동물", "어류", "파충류"]

print(solution(동물, 3))
