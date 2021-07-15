# 큰 값 순회 깊이 우선 탐색
# 작은 값 순회 깊이 우선 탐색

graph = {
    100: set([67, 66]),
    67: set([100, 82, 63]),
    66: set([100, 73, 69]),
    82: set([67, 61, 79]),
    63: set([67]),
    73: set([66]),
    69: set([66, 65, 81]),
    61: set([82]),
    79: set([82, 87, 77]),
    65: set([69, 84, 99]),
    81: set([69]),
    87: set([79, 31, 78]),
    77: set([79]),
    84: set([65]),
    99: set([65]),
    31: set([87]),
    78: set([87]),
}


def 깊이우선탐색(graph, start):
    방문 = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in 방문:
            방문.append(n)
            차집합 = graph[n] - set(방문)
            stack += 차집합
            # print(f"visited: {방문}")
            # print(f"stack: {stack}")

    return 방문


def 작은값깊이우선탐색(graph, start):
    방문 = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in 방문:
            방문.append(n)
            차집합 = graph[n] - set(방문)
            if len(차집합) == 0:
                방문 += stack
                break
            stack.append(min(차집합))
            # print(f"visited: {방문}")
            # print(f"stack: {stack}")

    return 방문


def 큰값깊이우선탐색(graph, start):
    방문 = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in 방문:
            방문.append(n)
            차집합 = graph[n] - set(방문)
            if len(차집합) == 0:
                방문 += stack
                break
            stack.append(max(차집합))
            # print(f"visited: {방문}")
            # print(f"stack: {stack}")

    return 방문


print([chr(i) for i in 작은값깊이우선탐색(graph, 100)])
print([chr(i) for i in 큰값깊이우선탐색(graph, 100)])